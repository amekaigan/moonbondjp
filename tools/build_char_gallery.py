#!/usr/bin/env python3
"""キャラクター設定の確認ページ（Claudeの公開ページ用）を /home/claude/chargal に作る。
各キャラに、ChatGPTへ渡す「設定シート」の指示文をコピーボタン付きで載せる。"""
import sys, html, re, shutil, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from char_profiles import CHARS, SHEET
OUT = pathlib.Path('/home/claude/chargal'); (OUT / 'img').mkdir(parents=True, exist_ok=True)
s = (ROOT / 'public/full/index.html').read_text(encoding='utf-8')
i = s.find('var M = ['); j = s.find('\n];', i)
M = [re.match(r"\['(.)','([^']*)','([^']*)','([^']*)'", l).groups() for l in s[i:j].split('\n')[1:]]
shutil.copy(ROOT / 'art-src/sheets/star-v3.png', OUT / 'img/kirara-sheet.png')
e = html.escape

STYLE = """【画風】2枚目の見本と同じにする
・色紙を切って貼った「貼り絵」。形のふちは、はさみで切ったようにくっきり
・髪は、紙の切れ端を数枚重ねた形。毛先はとがった切り口
・着物・帯・肌は、1色の紙でベタに。にじみ・ぼかし・濃淡なし
・柄は、別の色の紙を細く切って上から貼ったように
・紙の重なりに、ごく薄い影。和紙の繊維がうっすら見える質感
・ほおの赤みは、ほぼなし
・頭身は全員、2枚目の見本と同じ3.5頭身。年上の子も背を高くせず、大人っぽさは落ち着いた表情と仕草で出す
・背景はクリーム色の無地。文字やロゴは入れない。横長16:9"""

def prompt(c):
    age, face, poses = SHEET[c['slug']]
    t = '、'.join(x[1] for x in c['traits'])
    return (f"1枚目の絵の女の子「{c['name'][1]}」の、キャラクター設定シートを描いてください。2枚目（別の子の設定シート）を、画風と並べ方の見本にします。2枚目の子の顔や服はまねしないでください。\n\n"
            f"{STYLE}\n\n"
            f"【見た目】1枚目の絵とまったく同じにする\n・{c['look']}\n・相棒「{c['spirit'][1]}」：{c['spirit'][3]}。帯と同じ布でできていて、リボンの尾がある\n\n"
            f"【性格】{age}。{t}。口ぐせは「{c['line'][1]}」\n"
            f"【表情】{face}\n\n"
            f"【4つのポーズ】横に4人並べる。4人とも{c['spirit'][1]}がそばにいる\n" +
            '\n'.join(f"{'①②③④'[n]} {p}" for n, p in enumerate(poses)))

FIX_STAR = "とても良いです。一番右（④）だけ直してください。口を開けずに、口を閉じたまま口角だけ上げた、自信のある笑みにしてください。ほかの3人、画風、ポーズはそのままで。"

cards = ''
for k, c in enumerate(CHARS):
    shutil.copy(ROOT / f"public/art/chars/{c['slug']}-s.webp", OUT / f"img/{c['slug']}.webp")
    m = M[k]
    if c['slug'] == 'star':
        pr = FIX_STAR
        extra = '<p class="note">設定シートはほぼ完成。今のチャットで、これを送るだけです。</p><img class="sheet" src="img/kirara-sheet.png" alt="きららの設定シート">'
    else:
        pr = prompt(c); extra = ''
    cards += f'''<article class="c" id="{c['slug']}"><img src="img/{c['slug']}.webp" alt="{e(c['name'][1])}" loading="lazy">
<div class="b"><p class="sh"><span class="kj">{m[0]}</span>{m[0]}宿 · {e(m[2])}</p>
<h2>{e(c['name'][1])}<small>{e(c['name'][0])}</small></h2>
<ul class="t">{''.join(f'<li>{e(t[1])}</li>' for t in c['traits'])}</ul>
<p class="q">「{e(c['line'][1])}」<small>{e(c['line'][0])}</small></p>
<dl><dt>帯の精</dt><dd><b>{e(c['spirit'][1])}</b>（{e(c['spirit'][3])}）</dd><dt>好きなもの</dt><dd>{e(c['likes'][1])}</dd></dl>
{extra}<details><summary>ChatGPTへの指示文</summary><pre>{e(pr)}</pre><button type="button" class="cp">コピーする</button></details></div></article>'''

page = f'''<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Moonbond 27宿キャラクター設定（案）</title><style>
:root{{--night:#12264f;--paper:#f6f0e1;--ink:#1d1b27;--ink2:#5a566c;--kin:#d6b05a;--shu:#d4472a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--night);color:var(--paper);font-family:"Hiragino Sans","Noto Sans JP",sans-serif;font-size:17px;line-height:1.7}}
header{{max-width:1100px;margin:0 auto;padding:24px 16px 8px}}h1{{font-family:"Hiragino Mincho ProN","Noto Serif JP",serif;font-size:26px;margin:0 0 6px}}
header p{{margin:0 0 8px;color:#bcc8e2;font-size:16px}}header ol{{margin:0;padding-left:1.4em;color:#e7ecf6;font-size:16px}}
.g{{max-width:1100px;margin:0 auto;padding:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}}
.c{{background:var(--paper);color:var(--ink);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}
.c>img{{width:100%;aspect-ratio:5/4;object-fit:cover;display:block}}
.b{{padding:14px 16px 18px;display:flex;flex-direction:column;gap:8px}}
.sh{{margin:0;font-size:14.5px;color:var(--ink2);display:flex;align-items:center;gap:8px}}
.kj{{width:28px;height:28px;border-radius:50%;background:var(--night);color:var(--kin);display:inline-grid;place-items:center;font-weight:700;font-size:15px}}
h2{{margin:0;font-family:"Hiragino Mincho ProN","Noto Serif JP",serif;font-size:26px;display:flex;align-items:baseline;gap:10px}}
h2 small{{font-family:Georgia,serif;font-size:17px;color:var(--ink2);font-weight:400}}
.t{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}}.t li{{background:var(--night);color:var(--paper);border-radius:999px;padding:2px 12px;font-size:15px;font-weight:700}}
.q{{margin:0;background:#fbf3d9;border-radius:14px;padding:10px 12px;font-weight:700}}.q small{{display:block;font-weight:400;color:var(--ink2);font-size:14.5px}}
dl{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:15.5px}}dt{{color:var(--shu);font-weight:700}}dd{{margin:0}}
.note{{margin:0;font-weight:700;color:#17513a}}.sheet{{width:100%;border-radius:10px}}
details{{background:#ebe2cc;border-radius:12px;padding:10px 12px}}summary{{font-weight:700;cursor:pointer}}
pre{{white-space:pre-wrap;font-family:inherit;font-size:14.5px;line-height:1.6;margin:8px 0}}
.cp{{width:100%;border:0;border-radius:10px;background:var(--shu);color:#fff6ea;font:inherit;font-weight:700;padding:10px}}
</style></head><body><header><h1>27宿のキャラクター設定（案）</h1>
<p>各カードの「ChatGPTへの指示文」で、表情4種の設定シートを描いてもらえます。</p>
<ol><li>ChatGPTで新しいチャットを開く</li><li>1枚目にそのキャラの絵（moonbondjp.win/art/chars/〇〇.webp）、2枚目にきららの設定シートを添付</li><li>指示文をコピーして送る</li></ol></header>
<main class="g">{cards}</main>
<script>document.querySelectorAll('.cp').forEach(function(b){{b.addEventListener('click',function(){{var t=b.previousElementSibling.textContent;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{b.textContent='コピーしました'}},function(){{var r=document.createRange();r.selectNodeContents(b.previousElementSibling);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='選択しました。長押しでコピー'}});setTimeout(function(){{b.textContent='コピーする'}},2500);}});}});</script>
</body></html>'''
(OUT / 'index.html').write_text(page, encoding='utf-8')
print('ok')
