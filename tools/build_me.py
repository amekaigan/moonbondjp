#!/usr/bin/env python3
"""「自分用の鑑定」ページ（public/me/index.html）を作る。

- 表の部分（宿のデータ・日付の計算・色柄）は /full/index.html から抜き出して使う（二重に書かない）
- 宿ごとの文章は tools/me_content.py から入れる
- 文章を足したら、このファイルを実行して、できた2つのファイルを一緒に保存する
    python3 tools/build_me.py
  できるもの: public/me/index.html（購入者だけが開く鑑定書）、public/me-ready.json（購入できる宿の一覧）
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from me_content import ME  # noqa: E402
from me_lucky import LUCKY  # noqa: E402

full = (ROOT / 'public/full/index.html').read_text(encoding='utf-8')
lines = full.split('\n')


def grab_var(name):
    for i, l in enumerate(lines):
        if l.startswith('var %s = ' % name) or l.startswith('var %s=' % name):
            if l.rstrip().endswith(';') and (l.count('[') == l.count(']') and l.count('{') == l.count('}')):
                return l
            out = [l]
            for j in range(i + 1, len(lines)):
                out.append(lines[j])
                if lines[j] in ('];', '};'):
                    return '\n'.join(out)
    raise SystemExit('見つかりません: var ' + name)


def grab_func(name):
    for i, l in enumerate(lines):
        if l.startswith('function %s(' % name):
            out, depth = [], 0
            for j in range(i, len(lines)):
                out.append(lines[j])
                depth += lines[j].count('{') - lines[j].count('}')
                if depth == 0:
                    return '\n'.join(out)
    raise SystemExit('見つかりません: function ' + name)


style = re.search(r'<style>(.*?)</style>', full, re.S).group(1)
core = re.search(r'<script id="core">(.*?)</script>', full, re.S).group(1)
tables = '\n'.join(grab_var(n) for n in ['MONTH_NAMES', 'M', 'PAT', 'REL', 'YOMI', 'MJ', 'PATJ', 'RELJ', 'ROLE', 'SIDE', 'CHARS'])
funcs = '\n'.join(grab_func(n) for n in ['$', 'esc', 'nm', 'dateText', 'todayJST', 'fillDate', 'readDate', 'charSlug'])

extra_css = """
.cover-art{display:block;width:calc(100% + 40px);margin:-22px -20px 4px;height:auto;aspect-ratio:5/4;object-fit:cover;border-radius:18px 18px 0 0}
.cover-for,.cover-names{padding-right:0}
.swatches{display:flex;flex-wrap:wrap;gap:10px}
.sw-i{display:flex;align-items:center;gap:8px;font-size:17.5px;font-weight:700}
.sw-i i{width:26px;height:26px;border-radius:50%;display:inline-block;box-shadow:inset 0 0 0 1px rgba(29,27,39,.2)}
.pkey{background:var(--paper-2);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:8px}
.pkey-h{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.pkey-h b{font-family:var(--display);font-size:20px}
.pkey-h span{font-size:16.5px;color:var(--ink-2)}
.pkey p{font-size:17.5px;line-height:1.8}
.mrow{display:flex;flex-wrap:wrap;gap:8px}
.mp{display:flex;flex-direction:column;align-items:center;gap:3px;width:68px;text-align:center}
.mp img{width:68px;height:54px;object-fit:cover;object-position:left top;border-radius:10px;display:block}
.mp b{width:68px;height:54px;border-radius:10px;background:var(--paper);display:grid;place-items:center;font-family:var(--display);font-size:26px}
.mp small{font-size:14.5px;font-weight:700;line-height:1.25}
.grp{font-family:var(--display);font-size:20px;margin-top:8px}
.mon{display:flex;flex-direction:column;gap:6px}
.mo{display:flex;flex-direction:column;gap:6px;border-radius:10px;padding:10px 12px;background:var(--paper-2)}
.mo.now{background:#fbf3d9;box-shadow:0 0 0 2px var(--kin)}
.mo-l{font-size:16.5px;font-weight:700;line-height:1.4}
.mo-l small{display:inline;margin-left:8px;color:var(--ink-2);font-weight:500}
.mo-t{font-size:17.5px;line-height:1.75;display:flex;flex-direction:column;align-items:flex-start;gap:4px}
.pk{display:flex;flex-direction:column;gap:3px;font-size:17.5px;line-height:1.7}
.pk b{font-family:var(--body);font-weight:700;font-size:17.5px}
.pk span{font-size:17px;color:var(--ink-2)}
.pick .pk+.pk{margin-top:8px}
.tag{display:inline-flex;align-items:center;gap:6px;font-size:15.5px;font-weight:800;border-radius:999px;padding:1px 9px;margin-right:6px;color:#fff6ea}
.t-good{background:#2f7d5b}.t-calm{background:#6C848D}.t-care{background:var(--shu)}
.calm{display:flex;flex-direction:column;gap:6px}
.cal-m{font-family:var(--display);font-size:20px;font-weight:700;margin-top:4px}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:4px}
.cal-w{text-align:center;font-size:15.5px;font-weight:700;color:var(--ink-2);padding-bottom:2px}
.cal-w.sun{color:var(--shu)}
.cd{border-radius:10px;padding:7px 0 6px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:2px;line-height:1}
.cd b{font-size:20px;font-weight:700;font-variant-numeric:tabular-nums}
.cd i{font-style:normal;font-size:16.5px;font-weight:800;line-height:1}
.cd.t-good{background:#cfe8d8;color:#17513a}
.cd.t-calm{background:#e6e9eb;color:#46555c}
.cd.t-care{background:#f6d3c8;color:#9c2f16}
.cd.today{box-shadow:0 0 0 3px var(--ink)}
.cd.blank{visibility:hidden}
.cal-key{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:16.5px;color:var(--ink-2)}
.cal-key span{display:inline-flex;align-items:center;gap:6px}
.cal-key i{font-style:normal;font-weight:800;width:26px;height:26px;border-radius:8px;display:inline-grid;place-items:center;font-size:15.5px}
.cal-key .k-good{background:#cfe8d8;color:#17513a}.cal-key .k-calm{background:#e6e9eb;color:#46555c}.cal-key .k-care{background:#f6d3c8;color:#9c2f16}
.yr{border-radius:12px;padding:14px;background:var(--paper-2);display:flex;flex-direction:column;gap:6px}
.yr.now{background:#fbf3d9;box-shadow:0 0 0 2px var(--kin)}
.yr-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-weight:700;font-size:16px}
.yr-s{font-family:var(--display);font-size:22px;font-weight:700;line-height:1.3}
.yr-s small{font-family:var(--body);font-size:15px;font-weight:500;color:var(--ink-2);margin-left:6px}
.ys{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
.yc{border-radius:10px;padding:8px 2px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:3px;line-height:1.25}
.yc small{font-size:13.5px;font-weight:700}
.yc b{font-size:15.5px}
.yc i{font-style:normal;font-size:16px;font-weight:800}
.yc.t-good{background:#cfe8d8;color:#17513a}.yc.t-calm{background:#e6e9eb;color:#46555c}.yc.t-care{background:#f6d3c8;color:#9c2f16}
.yc.now{box-shadow:0 0 0 3px var(--ink)}
.luck{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.lk{background:var(--paper-2);border-radius:14px;padding:14px 12px;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.lk-i{height:44px;display:grid;place-items:center;font-size:34px;line-height:1}
.lk-i .dot{width:40px;height:40px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(29,27,39,.2)}
.lk-i .num{font-family:var(--display);font-weight:800;font-size:38px}
.lk-i svg{width:42px;height:42px}
.lk small{font-size:15.5px;color:var(--ink-2);font-weight:700}
.lk b{font-size:18.5px;line-height:1.35}
.picks{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
.pick{border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:6px}
.pick.good{background:#e5f1ea}.pick.care{background:#f8e6df}
.pick ul{display:flex;flex-direction:column;gap:6px;font-size:17.5px}
.pick li{display:flex;gap:8px;align-items:baseline}
.pick li b{font-family:var(--display);min-width:5.6em}
.soon{background:var(--night-2);border:1px solid var(--hair);border-radius:18px;padding:22px 20px;text-align:center;color:var(--mist)}
"""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Moonbond · Your Reading</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;700;800&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap" rel="stylesheet">
<style>
/* 自分用の鑑定（tools/build_me.py で作る。直接は書き換えない） */__STYLE__
</style>
<script id="core">__CORE__</script>
<script src="/analytics.js" defer></script>
</head>
<body>
<header class="wrap top">
  <div class="brand"><span class="brand-moon" aria-hidden="true"></span><span class="brand-name">Moonbond</span><span class="brand-jp" lang="ja">月の縁</span></div>
  <div class="lang" role="group" aria-label="Language"><button type="button" id="langEn" aria-pressed="true">EN</button><button type="button" id="langJa" aria-pressed="false" lang="ja">日本語</button></div>
</header>
<main class="wrap">
  <section class="intro">
    <div class="intro-head">
      <div><h1 id="tH1"></h1><p class="intro-sub" id="tSub"></p></div>
      <img src="/full/art/moon.webp" alt="" width="330" height="328">
    </div>
    <form id="birthForm" novalidate>
      <fieldset><legend id="tYou"></legend>
        <div class="date-row">
          <label for="bMonth"><span class="lm"></span><select id="bMonth"></select></label>
          <label for="bDay"><span class="ld"></span><select id="bDay"></select></label>
          <label for="bYear"><span class="ly"></span><select id="bYear"></select></label>
        </div>
      </fieldset>
      <button class="btn" type="submit" id="tGo"></button>
      <p class="err" id="err" role="alert"></p>
    </form>
  </section>
  <div id="reading" hidden></div>
</main>
<script>
var lang = 'en';
var ME = __ME__;
var LUCKY = __LUCKY__;
__TABLES__
__FUNCS__
function L(en, ja){ return lang === 'ja' ? ja : en; }
var mine = null;
var TRAITS = [['Drive','行動力'],['Heart','情'],['Mind','知性'],['Calm','落ち着き']];
var CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#d4472a"/><path d="M7.5 12.5l3 3 6-6.5" fill="none" stroke="#fff6ea" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
var SPARK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.2 6.6 6.8 2.4-6.8 2.4L12 20.5l-2.2-6.6L3 11.5l6.8-2.4z" fill="#d6b05a"/></svg>';
function pbar(p, label){ return '<span class="pbar" role="img" aria-label="' + label + ' ' + p + '%"><i style="width:' + p + '%"></i></span><span class="pct">' + p + '<small>%</small></span>'; }
function chapter(n, title, body){
  return '<section class="ch"><div class="ch-head"><span class="ch-num" aria-hidden="true">' + n + '</span><div><p class="ch-label">' + L('Chapter ' + n, '第' + n + '章') + '</p><h2>' + esc(title) + '</h2></div></div>' + body + '</section>';
}
function pr(x){ return '<p>' + esc(L(x[0], x[1])) + '</p>'; }
function room(name, x){ return '<div class="room"><span class="room-name">' + esc(name) + '</span><p>' + esc(L(x[0], x[1])) + '</p></div>'; }

/* 十一の関係ごとの一言（その月・その日の宿が、あなたの宿から見て何にあたるか） */
var TONE = {
  ei:['Luck runs with you. A good time to start things.','運が味方する時。物事を始めるのに向いています。'],
  shin:['Warm and supported. Good for people and agreements.','あたたかく支えられる時。人との話し合いや約束ごとに向いています。'],
  yu:['Easy and light. Meet people, talk, enjoy yourself.','気楽で軽やかな時。会って話して、楽しむのに向いています。'],
  sei:['Effort pays off. Push your project forward.','努力が実りやすい時。取り組んでいる課題を前に進めて。'],
  an:['Calm and settled. Your usual pace works well.','穏やかで落ち着く時。いつものペースがよく合います。'],
  mei:['A mirror time. Look at yourself and reset.','自分を見つめ直す時。気持ちを整えるのに向いています。'],
  tai:['Quiet and protective. Look after what you already have.','守りの時。今あるものを大切にしましょう。'],
  go:['Old threads come back. Finish things before you start anything new.','過去の縁や宿題が戻りやすい時。新しいことより、片づけを先に。'],
  sui:['Energy dips. Rest, and do not give more than you have.','力が落ちやすい時。しっかり休んで、尽くしすぎないで。'],
  kai:['Plans may shake. Put big decisions off.','予定が揺れやすい時。大きな決断は先送りに。'],
  ki:['Unpredictable. Be careful with new bets.','思わぬことが起きやすい時。新しい賭けは慎重に。']
};
var TG = {ei:'good',shin:'good',yu:'good',sei:'good',an:'calm',mei:'calm',tai:'calm',go:'care',sui:'care',kai:'care',ki:'care'};
var TGN = {good:['Favorable','追い風'],calm:['Steady','安定'],care:['Go gently','慎重に']};
function tagOf(key){ var g = TG[key]; return '<span class="tag t-' + g + '">' + L(TGN[g][0], TGN[g][1]) + '</span>'; }
var LMON = ['Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan'];
var DOW = [['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],['日','月','火','水','木','金','土']];

function relName(key){ return lang === 'ja' ? RELJ[key][1] : REL[key][2]; }
function relMark(key){ return REL[key][0]; }

function nextDays(n){
  var t = todayJST(), base = dayNum(t.y, t.m, t.d), out = [];
  for (var i = 0; i < n; i++){
    var dt = new Date((base + i) * 86400000), y = dt.getUTCFullYear(), m = dt.getUTCMonth() + 1, d = dt.getUTCDate(), s = shukuOf(y, m, d);
    if (!s) continue;
    out.push({m:m, d:d, w:dt.getUTCDay(), key:relOf(mine.idx, s.idx).key});
  }
  return out;
}
function dayLabel(x){ return L(x.m + '/' + x.d + ' ' + DOW[0][x.w], x.m + '月' + x.d + '日（' + DOW[1][x.w] + '）'); }

function mp(i){
  var s = charSlug(i), v = CHARS[s];
  var im = v ? '<img src="/art/chars/' + s + '-s.webp?v=' + v + '" alt="" width="68" height="54">' : '<b lang="ja">' + M[i][0] + '</b>';
  return '<div class="mp">' + im + '<small>' + esc(lang === 'ja' ? M[i][0] + '宿' : M[i][2]) + '</small></div>';
}
function pkey(key){
  var list = [];
  for (var b = 0; b < 27; b++){ if (b !== mine.idx && relOf(mine.idx, b).key === key) list.push(b); }
  if (!list.length) return '';
  return '<div class="pkey"><div class="pkey-h"><b>' + esc(L(ROLE[key][0], ROLE[key][1])) + '</b><span>' + esc(L(REL[key][0] + ' ' + REL[key][1] + ' · ' + REL[key][2], RELJ[key][0] + '（' + RELJ[key][1] + '）')) + '</span></div>' +
    '<p>' + esc(L(SIDE[key].a[0], SIDE[key].a[1])) + '</p><div class="mrow">' + list.map(mp).join('') + '</div></div>';
}

function render(){
  if (!mine) return;
  var a = mine.idx, m = M[a], j = MJ[a], slug = charSlug(a), D = ME[slug], h = '';
  var big = CHARS[slug] ? '<img class="cover-art" src="/art/chars/' + slug + '.webp?v=' + CHARS[slug] + '" alt="" width="1200" height="960">' : '';
  h += '<section class="cover">' + big +
    '<p class="cover-for">' + L('A reading for you', 'あなたのための鑑定') + '</p>' +
    '<p class="cover-names">' + L(m[2] + ' Mansion', m[0] + '宿（' + YOMI[a] + '）') + '</p>' +
    '<p class="cover-for">' + dateText(mine) + '</p>' +
    '<p class="cover-bond">' + esc(L(m[3], j[0])) + '</p>' +
    '<p class="cover-sub">' + esc(L(m[4], j[1])) + '</p></section>';
  if (!D){
    h += '<section class="soon"><p>' + L('Your personal reading for this mansion is still being written. Please check back soon.', 'この宿の「自分用の鑑定」は、いま書いているところです。もうしばらくお待ちください。') + '</p></section>';
    $('reading').innerHTML = h; $('reading').hidden = false; return;
  }
  /* 1 */
  var tr = m[11], kw = lang === 'ja' ? j[2] : m[5];
  var li = function(x){ return '<li><b>' + esc(L(x[0], x[1])) + '</b><br>' + esc(L(x[2], x[3])) + '</li>'; };
  h += chapter(1, L('The real you', '本当のあなた'),
    '<ul class="chips" style="display:flex;flex-wrap:wrap;gap:6px">' + kw.map(function(x){ return '<li class="chip" style="background:var(--paper-2)">' + esc(x) + '</li>'; }).join('') + '</ul>' +
    D.core.map(pr).join('') +
    '<div class="meter">' + tr.map(function(v, i){ var lb = L(TRAITS[i][0], TRAITS[i][1]); return '<div class="meter-row"><span>' + lb + '</span>' + pbar([0, 34, 50, 66, 80, 92][v], lb) + '</div>'; }).join('') + '</div>' +
    '<div class="pros"><div class="pro good"><div class="pro-h"><span class="pro-ic" aria-hidden="true">＋</span>' + L('Your strengths', 'あなたの強み') + '</div><ul>' + D.strengths.map(li).join('') + '</ul></div>' +
    '<div class="pro care"><div class="pro-h"><span class="pro-ic" aria-hidden="true">！</span>' + L('Your blind spots', 'つまずきやすいところ') + '</div><ul>' + D.blind.map(li).join('') + '</ul></div></div>');
  /* 2 */
  h += chapter(2, L('How you love', '恋愛のしかた'),
    '<div class="rooms">' + room(L('Who moves you', '惹かれる人'), D.love.attract) + room(L('Your pattern', 'くり返しやすいパターン'), D.love.pattern) + '</div>' +
    '<div class="try"><span class="mini">' + L('Try this month', '今月やってみること') + '</span><p>' + esc(L(D.love.try[0], D.love.try[1])) + '</p></div>');
  /* 3 */
  h += chapter(3, L('Work and money', '仕事とお金'),
    '<ul class="dots">' + D.work.fit.map(function(x){ return '<li>' + CHECK + '<span>' + esc(L(x[0], x[1])) + '</span></li>'; }).join('') + '</ul>' +
    '<div class="rooms">' + room(L('How you work best', '力が出る環境'), D.work.style) + room(L('How money comes to you', 'お金との付き合い方'), D.work.money) + '</div>' +
    '<div class="gift">' + SPARK + '<div><span class="mini">' + L('Keep in mind', '覚えておくこと') + '</span><p>' + esc(L(D.work.caution[0], D.work.caution[1])) + '</p></div></div>');
  /* 4 */
  h += chapter(4, L('The people around you', 'まわりの人との相性'),
    '<p>' + L('Shukuyō sorts the other 26 mansions into kinds of bond with yours. Here is who lifts you, who is easy company, and who needs gentler handling.', '宿曜では、ほかの26の宿が、あなたの宿から見てどんな関係にあたるかが決まっています。運をくれる人、一緒にいて楽な人、ていねいに付き合いたい人を並べました。') + '</p>' +
    '<h3 class="grp">' + L('Lift you up', 'あなたを引き上げてくれる人') + '</h3>' + pkey('ei') + pkey('shin') +
    '<h3 class="grp">' + L('Easy to be with', '一緒にいて楽な人') + '</h3>' + pkey('yu') + pkey('an') +
    '<h3 class="grp">' + L('Help you grow', '成長させてくれる人') + '</h3>' + pkey('sei') +
    '<h3 class="grp">' + L('Old ties', '前世からの縁といわれる人') + '</h3>' + pkey('go') + pkey('tai') +
    '<h3 class="grp">' + L('Handle with care', 'ていねいに付き合いたい人') + '</h3>' + pkey('sui') + pkey('kai') + pkey('ki') +
    '<div class="rooms">' + room(L('What drains you', '消耗するもの'), D.drain) + room(L('What restores you', '回復するもの'), D.recharge) + '</div>');
  /* 5 */
  var t = todayJST(), lu = lunarOf(dayNum(t.y, t.m, t.d)), cur = lu ? lu.m : 0, months = '';
  for (var mi = 1; mi <= 12; mi++){
    var key = relOf(a, FIRST[mi]).key;
    months += '<div class="mo' + (mi === cur ? ' now' : '') + '"><div class="mo-l">' + L('Lunar month ' + mi, '旧暦' + mi + '月') + '<small>' + L('around ' + LMON[mi - 1], 'おおよそ' + (((mi + 0) % 12) + 1) + '月') + (mi === cur ? L(' · now', '・いま') : '') + '</small></div>' +
      '<div class="mo-t">' + tagOf(key) + esc(L(TONE[key][0], TONE[key][1])) + '</div></div>';
  }
  /* 九曜（くよう）：数え年を9で割った余りで、その年の星が決まる。寺社の九曜早見表（数え年1=羅睺、2=土曜、3=水曜、4=金曜、5=日曜、6=火曜、7=計都、8=月曜、9=木曜）に合わせてある */
  var MK = {good:'◎', calm:'○', care:'▲'};
  var KUYO = [
    ['木曜星', 'Jupiter', 'good', 'A year when sprouts come up. Almost anything you start is said to go well. Stay alert, and do not get careless.', '芽が出る年。何を始めても吉とされます。ただし油断は禁物です。'],
    ['羅睺星', 'Rahu (the eclipse)', 'care', 'A slow year when things do not go as planned. Protect what you have and hold off on big new starts.', '思うように進みにくい年。新しいことを急がず、いまあるものを守る一年に。'],
    ['土曜星', 'Saturn', 'calm', 'The year after a hard patch, when things begin to open. Good for preparing. Start the real thing a little later.', '苦しい時期のあとに、運が開きはじめる年。準備には向いています。本格的な開始は少し先に。'],
    ['水曜星', 'Mercury', 'calm', 'A year when people above you and acquaintances lift you up. Stay modest even when things go well.', '目上の人や知人に引き立てられやすい年。調子がよくても、控えめに。'],
    ['金曜星', 'Venus', 'calm', 'Steady effort pays off. Good for buying, selling, and steady work. Pay attention to detail.', 'コツコツ進めると成果が出る年。お金の整理や、地道な仕事に向いています。細かいところまで目を配って。'],
    ['日曜星', 'Sun', 'good', 'A tailwind year. Things tend to go smoothly. Do not get proud, and avoid extravagance.', '追い風の年。物事が順調に運びやすい時です。おごらず、ぜいたくは控えめに。'],
    ['火曜星', 'Mars', 'care', 'A year to be careful with haste, quarrels and fire or theft. Avoid forcing things and wait for the year to turn.', 'あせり、争いごと、火の元や盗難に気をつけたい年。無理をせず、年が変わるのを待つ気持ちで。'],
    ['計都星', 'Ketu (the comet)', 'care', 'A year of hesitation and mix-ups. Avoid hasty decisions and borrowing money, and talk things over with someone you trust.', '迷いや行き違いが出やすい年。軽はずみな決断やお金の借り入れは避けて、信頼できる人に相談を。'],
    ['月曜星', 'Moon', 'good', 'A year when happy things tend to come in threes. Find a good adviser and think things through.', 'うれしいことが重なりやすい年。よい相談相手を持って、じっくり考えて進むと運が味方します。']
  ];
  var TL = {good:['Tailwind', '追い風'], calm:['Steady', '安定'], care:['Go gently', '慎重に']};
  var yearHtml = '';
  if (mine.y){
    var yh = '', ys = '';
    for (var yi = 0; yi < 5; yi++){
      var yy = t.y + yi, age = yy - mine.y + 1, K9 = KUYO[age % 9];
      ys += '<span class="yc t-' + K9[2] + (yi === 0 ? ' now' : '') + '"><small>' + L(String(yy), yy + '年') + '</small><i aria-hidden="true">' + MK[K9[2]] + '</i><b>' + esc(L(K9[1].replace(/ \(.*\)/, ''), K9[0])) + '</b></span>';
      if (yi < 2) yh += '<div class="yr' + (yi === 0 ? ' now' : '') + '"><div class="yr-h"><span class="tag t-' + K9[2] + '">' + L(TL[K9[2]][0], TL[K9[2]][1]) + '</span>' + L(yi === 0 ? 'This year, ' + yy : 'Next year, ' + yy, yi === 0 ? '今年（' + yy + '年）' : '来年（' + yy + '年）') + '</div><div class="yr-s">' + esc(L(K9[1], K9[0])) + '<small>' + L('age ' + age + ' by the old count', '数え年' + age + '歳') + '</small></div><p>' + esc(L(K9[3], K9[4])) + '</p></div>';
    }
    yearHtml = '<h3 class="grp">' + L('Your star for each year', '年ごとの運気（九曜）') + '</h3>' +
      '<p>' + L('Shukuyō also reads a nine-year cycle of stars, called Kuyō. Your star changes every year, and follows your age counted the old Japanese way (you are one at birth, and add a year each New Year).', '宿曜には、九曜（くよう）という、9年でひとめぐりする星の見方もあります。星は毎年変わり、昔ながらの数え年（生まれた年が1歳、お正月ごとに1つ増える）で決まります。') + '</p>' +
      yh + '<div class="ys">' + ys + '</div>';
  }
  var days = nextDays(30), dh = '', good = [], care = [], MK = {good:'◎', calm:'○', care:'▲'}, t0 = todayJST(), curM = 0;
  var GO = ['ei','shin','yu','sei'], CO = ['kai','ki','go','sui'];
  days.forEach(function(x){
    if (x.m !== curM){
      if (curM) dh += '</div>';
      curM = x.m;
      dh += '<h4 class="cal-m">' + L(MONTH_NAMES[x.m - 1], x.m + '月') + '</h4><div class="cal">';
      for (var wi = 0; wi < 7; wi++) dh += '<span class="cal-w' + (wi === 0 ? ' sun' : '') + '">' + DOW[lang === 'ja' ? 1 : 0][wi] + '</span>';
      for (var bi = 0; bi < x.w; bi++) dh += '<span class="cd blank"></span>';
    }
    dh += '<span class="cd t-' + TG[x.key] + (x.m === t0.m && x.d === t0.d ? ' today' : '') + '" aria-label="' + esc(dayLabel(x)) + '"><b>' + x.d + '</b><i aria-hidden="true">' + MK[TG[x.key]] + '</i></span>';
    if (GO.indexOf(x.key) >= 0) good.push(x); if (CO.indexOf(x.key) >= 0) care.push(x);
  });
  good.sort(function(p, q){ return GO.indexOf(p.key) - GO.indexOf(q.key); });
  care.sort(function(p, q){ return CO.indexOf(p.key) - CO.indexOf(q.key); });
  var pickList = function(arr, order, cls, ttl){
    var rows = '';
    order.forEach(function(k){
      var ds = arr.filter(function(x){ return x.key === k; }).slice(0, 4);
      if (ds.length) rows += '<div class="pk"><b>' + esc(L(TONE[k][0], TONE[k][1])) + '</b><span>' + ds.map(dayLabel).join(L(', ', '、')) + '</span></div>';
    });
    return '<div class="pick ' + cls + '"><span class="mini">' + ttl + '</span>' + (rows || '<p>' + L('None in the next 30 days.', 'この30日間にはありません。') + '</p>') + '</div>';
  };
  h += chapter(5, L('Your luck, year by year', '運気の流れ'),
    '<p>' + L('In Shukuyō, each lunar month and each day belongs to one of the 27 mansions. How that mansion relates to yours sets the tone. This is the traditional method, worked out for your mansion.', '宿曜では、旧暦の月も毎日も、27の宿のどれかにあたります。その宿があなたの宿から見て何にあたるかで、その時の流れが決まります。伝統的な読み方を、あなたの宿に合わせて計算しました。') + '</p>' +
    yearHtml +
    '<h3 class="grp">' + L('The 12 lunar months', '旧暦12か月') + '</h3>' +
    '<p>' + L('This part is the same every year. It is the pattern of your mansion, month by month.', 'この部分は、毎年同じです。あなたの宿の、月ごとのめぐりの傾向です。') + '</p><div class="mon">' + months + '</div>' +
    '<h3 class="grp">' + L('The next 30 days', 'これからの30日') + '</h3>' +
    '<div class="cal-key"><span><i class="k-good">◎</i>' + L('Favorable', '追い風') + '</span><span><i class="k-calm">○</i>' + L('Steady', '安定') + '</span><span><i class="k-care">▲</i>' + L('Go gently', '慎重に') + '</span><span>' + L('Black frame: today', '黒い枠：今日') + '</span></div>' +
    '<div class="calm">' + dh + '</div></div>' +
    '<div class="picks">' + pickList(good, GO, 'good', L('Best days to move', '動くのによい日')) + pickList(care, CO, 'care', L('Days to go gently', '慎重に過ごしたい日')) + '</div>');
  /* 6 */
  var c1 = m[8], c2 = m[9], pat = PAT[m[10]], patJ = PATJ[m[10]], K = LUCKY[a];
  var compass = '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="none" stroke="#1d1b27" stroke-opacity=".25" stroke-width="2"/><g transform="rotate(' + K[4] + ' 24 24)"><path d="M24 7 L31 26 L24 22 L17 26 Z" fill="#d4472a"/><path d="M24 41 L31 26 L24 22 L17 26 Z" fill="#1d1b27" fill-opacity=".25"/></g></svg>';
  var lk = function(icon, label, text){ return '<div class="lk"><span class="lk-i">' + icon + '</span><small>' + label + '</small><b>' + esc(text) + '</b></div>'; };
  var luckHtml = '<div class="luck">' +
    lk('<span class="dot" style="background:' + K[0] + '"></span>', L('Lucky color', 'ラッキーカラー'), L(K[1], K[2])) +
    lk('<span class="num">' + K[3] + '</span>', L('Lucky number', 'ラッキーナンバー'), L('Number ' + K[3], K[3] + '番')) +
    lk(compass, L('Lucky direction', 'ラッキー方角'), L(K[5], K[6])) +
    lk(K[9], L('Lucky item', 'ラッキーアイテム'), L(K[7], K[8])) +
    lk(K[12], L('Lucky food', 'ラッキーフード'), L(K[10], K[11])) +
    lk(K[15], L('Lucky place', 'ラッキースポット'), L(K[13], K[14])) + '</div>';
  h += chapter(6, L('Small things that bring luck', '運を呼ぶヒント'),
    '<h3 class="grp">' + L('Your lucky picks', 'あなたのラッキー') + '</h3>' + luckHtml +
    '<h3 class="grp">' + L('Your kimono and obi colors', 'きものと帯の色') + '</h3>' +
    '<div class="swatches"><span class="sw-i"><i style="background:' + c1[2] + '"></i>' + esc(L(c1[0], c1[1])) + '</span><span class="sw-i"><i style="background:' + c2[2] + '"></i>' + esc(L(c2[0], c2[1])) + '</span></div>' +
    '<p>' + L('Your kimono and obi colors, in Japan\'s traditional color names. Wear them, or carry them in something small. Pattern: ' + pat[0] + ' (' + pat[2] + ').', 'あなたの宿に合わせた、きものと帯の色です。身につけても、小物で持ち歩いても。柄は' + pat[1] + '（' + patJ + '）。') + '</p>' +
    '<div class="try"><span class="mini">' + L('This week', '今週のひとこと') + '</span><p>' + esc(L(D.week[0], D.week[1])) + '</p></div>');
  h += '<section class="closing"><img src="/full/art/moon.webp" alt="" width="330" height="328"><p class="for">' + L('For you', 'あなたへ') + '</p><p class="line">' + esc(L(D.close[0], D.close[1])) + '</p>' +
    '<p class="fine">' + L('A reading for reflection and fun. It describes tendencies drawn from the Shukuyō tradition and promises no outcome. The kimono colors are our own styling idea.', '楽しみと振り返りのための読み物です。宿曜の伝統にもとづく傾向をお伝えするもので、結果を約束するものではありません。きものの色は当サイトの提案です。') + '</p></section>';
  $('reading').innerHTML = h; $('reading').hidden = false;
}
function applyLang(){
  document.documentElement.lang = lang;
  $('langEn').setAttribute('aria-pressed', String(lang === 'en')); $('langJa').setAttribute('aria-pressed', String(lang === 'ja'));
  document.title = L('Moonbond · Your Reading', '宿曜 くわしい鑑定（あなた編）');
  $('tH1').textContent = L('Your personal reading', 'あなた編のくわしい鑑定');
  $('tSub').textContent = L('Six chapters, written for your mansion.', '全6章。あなたの宿に合わせた鑑定です。');
  $('tYou').textContent = L('Your birthday', 'あなたの誕生日');
  $('tGo').textContent = L('Show the reading', '鑑定を表示する');
  var set = function(c, t){ var e = document.querySelectorAll('.' + c); for (var i = 0; i < e.length; i++) e[i].textContent = t; };
  set('lm', L('Month', '月')); set('ld', L('Day', '日')); set('ly', L('Year', '年'));
  var os = $('bMonth').options; for (var i = 0; i < os.length; i++) os[i].textContent = L(MONTH_NAMES[i], (i + 1) + '月');
  render();
}
function init(){
  try { var s = localStorage.getItem('tsukiyado-lang'); if (s === 'ja' || s === 'en') lang = s; } catch (e) {}
  fillDate('b', 1995, 11, 14);
  $('langEn').addEventListener('click', function(){ lang = 'en'; try { localStorage.setItem('tsukiyado-lang', 'en'); } catch (e) {} applyLang(); });
  $('langJa').addEventListener('click', function(){ lang = 'ja'; try { localStorage.setItem('tsukiyado-lang', 'ja'); } catch (e) {} applyLang(); });
  $('birthForm').addEventListener('submit', function(e){
    e.preventDefault();
    var A = readDate('b');
    if (A.err){ $('err').textContent = A.err; return; }
    $('err').textContent = ''; mine = A; render();
    $('reading').scrollIntoView({behavior: (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) ? 'auto' : 'smooth', block:'start'});
  });
  applyLang();
  /* 購入後のリンク: ?a=YYYY-MM-DD&lang=en|ja&k=… */
  try {
    var q = new URLSearchParams(location.search), pa = /^(\d{4})-(\d{1,2})-(\d{1,2})$/.exec(q.get('a') || '');
    if (q.get('lang') === 'ja' || q.get('lang') === 'en') { lang = q.get('lang'); applyLang(); }
    if (pa) {
      $('bYear').value = +pa[1]; $('bMonth').value = +pa[2]; $('bDay').value = +pa[3];
      var A = readDate('b');
      if (!A.err) { mine = A; render(); } else $('err').textContent = A.err;
      if (q.get('k')) $('birthForm').style.display = 'none';
    }
  } catch (e) {}
}
init();
</script>
</body>
</html>
"""

out = (TEMPLATE
       .replace('__STYLE__', style + extra_css)
       .replace('__CORE__', core)
       .replace('__TABLES__', tables)
       .replace('__FUNCS__', funcs)
       .replace('__ME__', json.dumps(ME, ensure_ascii=False, separators=(',', ':')))
       .replace('__LUCKY__', json.dumps(LUCKY, ensure_ascii=False, separators=(',', ':'))))
(ROOT / 'public/me').mkdir(exist_ok=True)
(ROOT / 'public/me/index.html').write_text(out, encoding='utf-8')
(ROOT / 'public/me-ready.json').write_text(json.dumps(sorted(ME.keys()), ensure_ascii=False) + '\n', encoding='utf-8')
print('作成: public/me/index.html（', len(ME), '宿ぶん）')

# 見本ページも一緒に作り直す
import subprocess
subprocess.run([sys.executable, str(ROOT / 'tools/build_samples.py')], check=True)
