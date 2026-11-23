# 宿ページ（public/mansions/<slug>/index.html）に「結婚と家庭」「お金」「運を呼ぶ習慣」「よくある質問」を足す
# 何度実行しても同じ結果になる（<!--extra-start--> 〜 <!--extra-end--> を差し替える）
import json, re, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mansion_extra import EXTRA

ROOT = os.path.join(os.path.dirname(__file__), '..', 'public', 'mansions')
CSS = (".lucky{margin:0;padding-left:20px;list-style:disc;display:flex;flex-direction:column;gap:6px}\n"
       ".faq details{border-top:1px solid rgba(29,27,39,.14);padding:12px 0}\n"
       ".faq details:first-of-type{border-top:0}\n"
       ".faq summary{cursor:pointer;font-weight:700;list-style-position:outside}\n"
       ".faq details p{margin:8px 0 0}\n")

def esc(t): return html.escape(t, quote=False)

for slug, (marriage, money, luck) in EXTRA.items():
    p = os.path.join(ROOT, slug, 'index.html')
    s = open(p, encoding='utf-8').read()
    name = re.search(r'<h1>([^<]+?) <span lang="ja">([^<]+)</span></h1>', s)
    full, kj = name.group(1), name.group(2)            # "Net Mansion", "畢宿"
    short = full.replace(' Mansion', '')
    romaji = re.search(r'<p class="ey">Shukuyō moon sign · ([^<]+)</p>', s).group(1)
    sub = html.unescape(re.search(r'<p class="sub">([^<]+)</p>', s).group(1))
    arch, tag = sub.split('. ', 1)
    love = html.unescape(re.search(r'<h2>In love</h2><p>([^<]+)</p>', s).group(1))
    best = html.unescape(re.search(r'For ' + re.escape(short) + r', that means ([^<]+?)\.</p>', s).group(1))
    jobs = re.findall(r'<span class="chip">([^<]+)</span>', s[s.find('Often drawn to'):s.find('</section>', s.find('Often drawn to'))])
    jobs_t = ', '.join(jobs[:-1]) + ' and ' + jobs[-1]

    faq = [
        (f"What is the {full} in Shukuyō?",
         f"The {full} ({kj}, {romaji}) is one of the 27 lunar mansions of Shukuyō, Japan's moon astrology. Moonbond calls it {arch}: {tag}"),
        (f"What is the {full} like in love?", love),
        (f"Which mansions are the best match for {short}?",
         f"In Shukuyō the luckiest bond is Prosperity & Kinship. For {short}, that means {best}."),
        (f"What jobs suit the {full}?", f"{short} is often drawn to {jobs_t}. {money}"),
        (f"How do I know if I am a {full}?",
         "Your mansion comes from where the Moon stood on your birthday in the old Japanese lunar calendar. Enter your birthday in Moonbond's free reading to see yours in seconds."),
    ]
    block = (
        "<!--extra-start-->\n"
        f'<section class="card"><h2>Marriage and family</h2><p>{esc(marriage)}</p></section>\n\n'
        f'<section class="card"><h2>Money</h2><p>{esc(money)}</p></section>\n\n'
        f'<section class="card"><h2>Bringing in good luck</h2><p class="small">Small habits that suit the {esc(short)} temperament.</p>'
        '<ul class="lucky">' + ''.join(f'<li>{esc(x)}</li>' for x in luck) + '</ul></section>\n'
        "<!--extra-end-->"
    )
    faq_block = (
        "<!--faq-start-->\n"
        f'<section class="card faq"><h2>Questions about the {esc(full)}</h2>'
        + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)
        + "</section>\n<!--faq-end-->"
    )
    # 差し替え（2回目以降）または挿入
    if '<!--extra-start-->' in s:
        s = re.sub(r'<!--extra-start-->.*?<!--extra-end-->', lambda m: block, s, flags=re.S)
        s = re.sub(r'<!--faq-start-->.*?<!--faq-end-->', lambda m: faq_block, s, flags=re.S)
    else:
        i = s.find('<section class="card"><h2>As a friend</h2>'); i = s.find('</section>', i) + len('</section>')
        s = s[:i] + '\n\n' + block + s[i:]
        j = s.find('<section class="card"><h2>How do I find my mansion?</h2>')
        assert j > 0, slug
        s = s[:j] + faq_block + '\n\n' + s[j:]
        s = s.replace('</style>', CSS + '</style>', 1)
    # タイトルと説明文
    s = re.sub(r'<title>[^<]*</title>', f'<title>{esc(full)} ({kj}) in Shukuyō: Personality, Love, Marriage, Money &amp; Compatibility | Moonbond</title>', s)
    desc = f'{full} ({kj}), "{arch}" in Japanese moon astrology. {tag} See its personality, love and marriage, money, career, lucky habits and how it matches the other 26 mansions.'
    s = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2), s)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2), s)
    # 構造化データに FAQPage を足す
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, flags=re.S)
    data = json.loads(m.group(1))
    data['@graph'] = [g for g in data['@graph'] if g.get('@type') != 'FAQPage']
    data['@graph'].append({'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]})
    s = s[:m.start(1)] + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
    open(p, 'w', encoding='utf-8').write(s)
    print('ok', slug)
