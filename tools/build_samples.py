#!/usr/bin/env python3
"""サンプルの鑑定書（購入前に誰でも見られる見本）を作る。
  /me/sample/   … あなた編（1995-11-14生まれ・星宿）
  /full/sample/ … 二人用（1995-11-14 と 1996-03-03）
本物の鑑定書（public/me/index.html、public/full/index.html）をそのまま写して、誕生日を固定する。
本物を作り直したら、このファイルも実行する（tools/build_me.py は最後に自動で実行する）。
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANNER = (
    '<div class="sample-bar"><p><span class="sb-en">This is a sample reading, made for the example birthdays shown. Yours is written for your own mansion.</span>'
    '<span class="sb-ja">これは見本の鑑定書です。例の誕生日で作っています。購入すると、あなたの宿に合わせた鑑定書になります。</span></p>'
    '<a href="/#editions"><span class="sb-en">Get my reading</span><span class="sb-ja">自分の鑑定を読む</span></a></div>'
)
CSS = (
    '<style>.sample-bar{margin:12px 0;padding:14px 16px;border-radius:14px;background:#fbf3d9;color:#1d1b27;display:flex;flex-direction:column;gap:10px;font-size:14.5px;line-height:1.6}'
    '.sample-bar a{align-self:flex-start;background:#d6b05a;color:#1d1b27;font-weight:800;text-decoration:none;border-radius:999px;padding:9px 18px}'
    'html[lang=ja] .sb-en{display:none}html:not([lang=ja]) .sb-ja{display:none}</style>'
)


def make(src, dst, query, fixes):
    s = (ROOT / src).read_text(encoding='utf-8')
    for a, b in fixes:
        assert s.count(a) == 1, (src, a, s.count(a))
        s = s.replace(a, b)
    s = s.replace('new URLSearchParams(location.search)', "new URLSearchParams('%s' + (location.search ? '&' + location.search.slice(1) : ''))" % query)
    assert "'%s'" % query in s
    assert s.count('<main class="wrap">') == 1
    s = s.replace('<main class="wrap">', '<main class="wrap">' + BANNER, 1).replace('</head>', CSS + '</head>', 1)
    if 'name="robots"' not in s:
        s = s.replace('<head>', '<head>\n<meta name="robots" content="noindex">', 1)
    out = ROOT / dst
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(s, encoding='utf-8')
    print('作成:', dst)


make('public/me/index.html', 'public/me/sample/index.html', 'a=1995-11-14',
     [("if (q.get('k')) $('birthForm').style.display = 'none';", "$('birthForm').style.display = 'none';")])
make('public/full/index.html', 'public/full/sample/index.html', 'a=1995-11-14&b=1996-03-03',
     [("q.get('k') && pa && pb", "pa && pb"), ('src="art/', 'src="/full/art/')] if False else
     [("q.get('k') && pa && pb", "pa && pb")])
# 画像の相対パス（art/…）を、サンプルの置き場所から読めるようにする
p = ROOT / 'public/full/sample/index.html'
t = p.read_text(encoding='utf-8')
t = t.replace('src="art/', 'src="/full/art/')
p.write_text(t, encoding='utf-8')
