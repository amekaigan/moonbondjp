#!/usr/bin/env python3
"""カップル完全版（/couple/）を作る。
二人用のくわしい鑑定（public/full/index.html）の8章を、そのまま土台にして、5つの章を足す。
  9 二人が出会った意味 / 10 一緒に暮らすときのコツ / 11 二人の九曜（今年・来年・5年分）
  12 この先12か月、二人によい日 / 13 記念の鑑定証（名前を入れて画像で保存）
文章は tools/couple_content.py。二人用ページ（full）を直したら、このスクリプトも実行する。
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from couple_content import MEET, LIVE, LIVE_HEADS  # noqa: E402

src = (ROOT / 'public/full/index.html').read_text(encoding='utf-8')


def rep(s, a, b, count=1):
    assert s.count(a) == count, ('見つかりません/数が違います', a[:70], s.count(a))
    return s.replace(a, b)


s = src
s = rep(s, 'src="art/', 'src="/full/art/', 4)
s = rep(s, '<title>Moonbond · Full Reading</title>', '<title>Moonbond · Complete Couple Reading</title>')
s = rep(s, "document.title = L('Shukuyō Full Reading', '宿曜 くわしい相性鑑定');", "document.title = L('Shukuyō Complete Couple Reading', '宿曜 カップル完全版');")
s = rep(s, "$('tH1').textContent = L('The full reading', 'くわしい相性鑑定');", "$('tH1').textContent = L('The complete couple reading', 'カップル完全版');")
s = rep(s, "$('tSub').textContent = L('All eight chapters, written for one exact pairing.', '全8章。二人の組み合わせに合わせた鑑定です。');",
        "$('tSub').textContent = L('Thirteen chapters, written for one exact pairing.', '全13章。二人の組み合わせに合わせた完全版です。');")
s = rep(s, "L('A reading for two', '二人のための鑑定')", "L('The complete reading for two', '二人のための完全版')")

extra_css = """
.cal-m{font-family:var(--display);font-size:18px;font-weight:700;margin-top:4px}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:4px}
.cal-w{text-align:center;font-size:14px;font-weight:700;color:var(--ink-2);padding-bottom:2px}
.cal-w.sun{color:var(--shu)}
.cd{border-radius:10px;padding:7px 0 6px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:2px;line-height:1}
.cd b{font-size:18px;font-weight:700;font-variant-numeric:tabular-nums}
.cd i{font-style:normal;font-size:15px;font-weight:800;line-height:1}
.cd.t-good{background:#cfe8d8;color:#17513a}
.cd.t-calm{background:#e6e9eb;color:#46555c}
.cd.t-care{background:#f6d3c8;color:#9c2f16}
.cd.today{box-shadow:0 0 0 3px var(--ink)}
.cd.blank{visibility:hidden}
.cal-key{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:15px;color:var(--ink-2)}
.cal-key span{display:inline-flex;align-items:center;gap:6px}
.cal-key i{font-style:normal;font-weight:800;width:26px;height:26px;border-radius:8px;display:inline-grid;place-items:center;font-size:14px}
.cal-key .k-good{background:#cfe8d8;color:#17513a}.cal-key .k-calm{background:#e6e9eb;color:#46555c}.cal-key .k-care{background:#f6d3c8;color:#9c2f16}
.calm{display:flex;flex-direction:column;gap:6px}
.tag{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:800;border-radius:999px;padding:1px 9px;margin-right:6px;color:#fff6ea}
.t-good{background:#2f7d5b}.t-calm{background:#6C848D}.t-care{background:var(--shu)}
.cd.t-good,.cd.t-calm,.cd.t-care,.yc.t-good,.yc.t-calm,.yc.t-care{margin-right:0}
.yr{border-radius:12px;padding:14px;background:var(--paper-2);display:flex;flex-direction:column;gap:6px}
.yr.now{background:#fbf3d9;box-shadow:0 0 0 2px var(--kin)}
.yr-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-weight:700;font-size:16px}
.yr-two{display:flex;flex-direction:column;gap:4px;font-size:16px}
.yr-two b{font-family:var(--display);font-size:18px}
.ys{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
.yc{border-radius:10px;padding:8px 2px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:3px;line-height:1.25}
.yc small{font-size:13.5px;font-weight:700}
.yc i{font-style:normal;font-size:16px;font-weight:800}
.yc.t-good{background:#cfe8d8;color:#17513a}.yc.t-calm{background:#e6e9eb;color:#46555c}.yc.t-care{background:#f6d3c8;color:#9c2f16}
.yc.now{box-shadow:0 0 0 3px var(--ink)}
.mb{background:var(--paper-2);border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.mb-h{font-family:var(--display);font-size:18px;font-weight:700}
.mb p{font-size:16px;line-height:1.7}
.mb .lbl{font-weight:800}
.mb .lbl.g{color:#17513a}.mb .lbl.c{color:#9c2f16}
.cert-form{display:flex;flex-direction:column;gap:10px;min-width:0;max-width:100%}
.cert-form label{display:flex;flex-direction:column;gap:4px;font-size:15.5px;font-weight:700;min-width:0;max-width:100%}
.cert-form input{font:inherit;font-size:17px;padding:12px 12px;border-radius:10px;border:1px solid rgba(29,27,39,.3);background:#fff;color:var(--ink);display:block;width:100%;min-width:0;max-width:100%;box-sizing:border-box;-webkit-appearance:none;appearance:none}
.cert-btn{width:100%;box-sizing:border-box}
html,body{overflow-x:clip}
.cert-btn{appearance:none;border:0;background:var(--shu);color:#fff6ea;font:inherit;font-size:17px;font-weight:700;border-radius:10px;padding:14px 18px;cursor:pointer}
.cert-out{display:flex;flex-direction:column;gap:10px;align-items:center}
.cert-out img{width:100%;max-width:420px;height:auto;border-radius:12px;box-shadow:0 4px 18px rgba(0,0,0,.25)}
.cert-dl{display:inline-block;background:var(--kin);color:var(--ink);font-weight:800;text-decoration:none;border-radius:999px;padding:12px 22px;font-size:16.5px}
"""
s = rep(s, '</style>\n<script id="core">', extra_css + '</style>\n<script id="core">')

data = json.dumps({'MEET': MEET, 'LIVE': LIVE, 'HEADS': LIVE_HEADS}, ensure_ascii=False, separators=(',', ':'))

new_chapters = r"""
  /* ===== ここから完全版の追加章 ===== */
  var CPL = __DATA__;
  var MK = {good:'◎', calm:'○', care:'▲'}, TG = {ei:'good',shin:'good',yu:'good',sei:'good',an:'calm',mei:'calm',tai:'calm',go:'care',sui:'care',kai:'care',ki:'care'};
  var TL = {good:['Tailwind', '追い風'], calm:['Steady', '安定'], care:['Go gently', '慎重に']};
  var tagT = function(t){ return '<span class="tag t-' + t + '">' + L(TL[t][0], TL[t][1]) + '</span>'; };
  var DOWN = [['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],['日','月','火','水','木','金','土']];
  var mt = CPL.MEET[k], lv = CPL.LIVE[k];
  /* 9 */
  h += chapter(9, L('Why you two met', '二人が出会った意味'),
    '<p>' + esc(L(mt.story[0], mt.story[1])) + '</p>' +
    '<h3 class="grp">' + L('Three things this bond gives you', 'この縁が二人にくれるもの') + '</h3>' +
    '<ul class="dots">' + mt.gifts.map(function(g){ return '<li>' + CHECK + '<span>' + esc(L(g[0], g[1])) + '</span></li>'; }).join('') + '</ul>');
  /* 10 */
  h += chapter(10, L('Living together: five habits that help', '一緒に暮らすときのコツ'),
    '<p>' + L('These are tuned to your kind of bond, for couples who share a home or plan to.', '二人の縁のかたちに合わせた、暮らしのコツです。いっしょに住んでいる人にも、これから住む人にも。') + '</p>' +
    '<div class="rooms">' + lv.map(function(t, i){ return '<div class="room"><span class="room-name">' + esc(L(CPL.HEADS[i][0], CPL.HEADS[i][1])) + '</span><p>' + esc(L(t[0], t[1])) + '</p></div>'; }).join('') + '</div>');
  /* 11 */
  var KY = [
    ['木曜星', 'Jupiter', 'good'], ['羅睺星', 'Rahu (eclipse)', 'care'], ['土曜星', 'Saturn', 'calm'], ['水曜星', 'Mercury', 'calm'], ['金曜星', 'Venus', 'calm'],
    ['日曜星', 'Sun', 'good'], ['火曜星', 'Mars', 'care'], ['計都星', 'Ketu (comet)', 'care'], ['月曜星', 'Moon', 'good']
  ];
  var YT = {
    gg: ['Both of you are in a tailwind year. A good time to begin something together, such as a move, a trip or a promise.', '二人とも追い風の年。引っ越しや旅行、約束ごとなど、二人で何かを始めるのに向いています。'],
    gc: ['One of you is in a tailwind and the other is steady. Let the one with the tailwind lead, and let the steady one set the pace.', '片方は追い風、もう片方は安定の年。追い風の人が先に動き、安定の人がペースを整えると、うまく運びます。'],
    gr: ['One of you has a tailwind and the other is in a careful year. Move at the careful one’s pace, and share the good luck.', '片方は追い風、もう片方は慎重な年。慎重な側のペースに合わせて、追い風の運を分け合いましょう。'],
    cc: ['Both of you are in a steady year. A calm stretch for building habits, and for ordinary good days together.', '二人とも安定の年。習慣づくりや、穏やかな日々を重ねるのに向いた時期です。'],
    cr: ['One of you is steady and the other is in a careful year. Let the steady one be the anchor, and avoid big decisions.', '片方は安定、もう片方は慎重な年。安定の人が支えて、大きな決断は避けましょう。'],
    rr: ['Both of you are in a careful year. Keep plans simple, look after each other, and let the year pass gently.', '二人とも慎重な年。予定は少なめに、お互いをいたわって、静かに過ごしましょう。']
  };
  var ORD = {good:0, calm:1, care:2};
  var tNow = todayJST(), yh = '', ys = '';
  if (mine.y && partner.y){
    for (var yi = 0; yi < 5; yi++){
      var yy = tNow.y + yi, ka = KY[(yy - mine.y + 1) % 9], kb = KY[(yy - partner.y + 1) % 9];
      ys += '<span class="yc t-' + (function(){ var v = {good:1, calm:0, care:-1}, z = v[ka[2]] + v[kb[2]]; return z >= 1 ? 'good' : z <= -1 ? 'care' : 'calm'; })() + (yi === 0 ? ' now' : '') + '"><small>' + L(String(yy), yy + '年') + '</small><i aria-hidden="true">' + MK[ka[2]] + ' ' + MK[kb[2]] + '</i></span>';
      if (yi < 2){
        var pair = [ka[2], kb[2]].sort(function(p, q){ return ORD[p] - ORD[q]; }), key = pair.map(function(x){ return {good:'g', calm:'c', care:'r'}[x]; }).join('');
        yh += '<div class="yr' + (yi === 0 ? ' now' : '') + '"><div class="yr-h">' + L(yi === 0 ? 'This year, ' + yy : 'Next year, ' + yy, yi === 0 ? '今年（' + yy + '年）' : '来年（' + yy + '年）') + '</div>' +
          '<div class="yr-two"><span>' + L('You', 'あなた') + '：<b>' + esc(L(ka[1], ka[0])) + '</b> ' + tagT(ka[2]) + '</span><span>' + L('Them', '相手') + '：<b>' + esc(L(kb[1], kb[0])) + '</b> ' + tagT(kb[2]) + '</span></div>' +
          '<p>' + esc(L(YT[key][0], YT[key][1])) + '</p></div>';
      }
    }
  }
  h += chapter(11, L('Your stars this year and next', '二人の九曜：今年と来年'),
    '<p>' + L('Kuyō is a nine-year cycle of stars. Each of you has your own star each year, counted by the old Japanese age. Here are the two of you side by side.', '九曜は、9年でひとめぐりする星の見方です。星は毎年、数え年で一人ひとりに決まります。二人の星を並べて読みました。') + '</p>' +
    yh +
    '<h3 class="grp">' + L('The next five years', 'これからの5年') + '</h3>' +
    '<div class="cal-key"><span>' + L('Left: you, right: them', '左：あなた　右：相手') + '</span><span><i class="k-good">◎</i>' + L('Tailwind', '追い風') + '</span><span><i class="k-calm">○</i>' + L('Steady', '安定') + '</span><span><i class="k-care">▲</i>' + L('Go gently', '慎重に') + '</span></div>' +
    '<div class="ys">' + ys + '</div>');
  /* 12 */
  var days12 = [], baseN = dayNum(tNow.y, tNow.m, tNow.d);
  for (var di2 = 0; di2 < 365; di2++){
    var dtt = new Date((baseN + di2) * 86400000), y2 = dtt.getUTCFullYear(), m2 = dtt.getUTCMonth() + 1, d2 = dtt.getUTCDate(), sk = shukuOf(y2, m2, d2);
    if (!sk) continue;
    var ta = TG[relOf(a, sk.idx).key], tb = TG[relOf(b, sk.idx).key], sc = (ta === 'good' ? 1 : ta === 'care' ? -1 : 0) + (tb === 'good' ? 1 : tb === 'care' ? -1 : 0);
    days12.push({y:y2, m:m2, d:d2, w:dtt.getUTCDay(), sc:sc, t:(ta === 'care' || tb === 'care') ? 'care' : sc >= 1 ? 'good' : 'calm'});
  }
  var cal = '', curM = 0, cnt = 0;
  days12.slice(0, 30).forEach(function(x){
    if (x.m !== curM){
      if (curM) cal += '</div>';
      curM = x.m;
      cal += '<h4 class="cal-m">' + L(MONTH_NAMES[x.m - 1], x.m + '月') + '</h4><div class="cal">';
      for (var wi = 0; wi < 7; wi++) cal += '<span class="cal-w' + (wi === 0 ? ' sun' : '') + '">' + DOWN[lang === 'ja' ? 1 : 0][wi] + '</span>';
      for (var bi = 0; bi < x.w; bi++) cal += '<span class="cd blank"></span>';
    }
    cal += '<span class="cd t-' + x.t + (x.m === tNow.m && x.d === tNow.d ? ' today' : '') + '"><b>' + x.d + '</b><i aria-hidden="true">' + MK[x.t] + '</i></span>';
  });
  var byM = {}, mOrder = [];
  days12.forEach(function(x){ var key = x.y * 100 + x.m; if (!byM[key]){ byM[key] = {y:x.y, m:x.m, best:[], rest:[]}; mOrder.push(key); } if (x.sc === 2) byM[key].best.push(x.d); else if (x.t === 'care') byM[key].rest.push(x.d); });
  var dl = function(arr, n){ return arr.slice(0, n).map(function(d){ return L(String(d), d + '日'); }).join(L(', ', '、')); };
  var monthsHtml = mOrder.map(function(key){
    var o = byM[key];
    return '<div class="mb"><span class="mb-h">' + L(MONTH_NAMES[o.m - 1] + ' ' + o.y, o.y + '年' + o.m + '月') + '</span>' +
      '<p><span class="lbl g">' + L('Best for two: ', '二人で動くのによい日：') + '</span>' + (o.best.length ? dl(o.best, 5) : L('none this month', 'この月はありません')) + '</p>' +
      '<p><span class="lbl c">' + L('One of you should go gently: ', 'どちらかが慎重に：') + '</span>' + (o.rest.length ? dl(o.rest, 4) : L('none this month', 'この月はありません')) + '</p></div>';
  }).join('');
  h += chapter(12, L('The next 12 months for the two of you', 'この先12か月、二人によい日'),
    '<p>' + L('Each day belongs to one of the 27 mansions. We checked every day for both of you. “Best for two” are days that are good for both of you at once. “Go gently” are days when at least one of you is better off not rushing.', '毎日は27の宿のどれかにあたります。その日が二人それぞれにとって何にあたるかを、毎日調べました。「二人で動くのによい日」は、二人ともに追い風の日。「どちらかが慎重に」は、片方でもあわてたくない日です。') + '</p>' +
    '<h3 class="grp">' + L('The next 30 days', 'これからの30日') + '</h3>' +
    '<div class="cal-key"><span><i class="k-good">◎</i>' + L('Good for both', '二人に追い風') + '</span><span><i class="k-calm">○</i>' + L('Steady', '安定') + '</span><span><i class="k-care">▲</i>' + L('One needs care', 'どちらかが慎重に') + '</span><span>' + L('Black frame: today', '黒い枠：今日') + '</span></div>' +
    '<div class="calm">' + cal + '</div></div>' +
    '<h3 class="grp">' + L('Month by month', '月ごとの日付') + '</h3>' + monthsHtml);
  /* 13 */
  h += chapter(13, L('Your certificate', '記念の鑑定証'),
    '<p>' + L('A keepsake with your two names, your mansions and your bond. Type your names and save it as a picture.', '二人の名前と宿、縁のかたちが入った、記念の鑑定証です。名前を入れて、画像として保存できます。') + '</p>' +
    '<div class="cert-form"><label>' + L('Your name', 'あなたの名前') + '<input type="text" id="certA" size="10" maxlength="20" autocomplete="off" value="' + esc(certNames.a) + '"></label>' +
    '<label>' + L('Their name', 'お相手の名前') + '<input type="text" id="certB" size="10" maxlength="20" autocomplete="off" value="' + esc(certNames.b) + '"></label>' +
    '<button class="cert-btn" type="button" id="certGo">' + L('Make the certificate', '鑑定証をつくる') + '</button></div><div class="cert-out" id="certOut"></div>');
  /* ===== 完全版の追加章ここまで ===== */
"""
new_chapters = new_chapters.replace('__DATA__', data)

# 鑑定証の描画（canvas）と、名前の保持
cert_js = r"""
var certNames = {a:'', b:''};
function certDraw(){
  var a = mine.idx, b = partner.idx, r = relOf(a, b), pr = PAIR[r.key], k = pr[1], W = 1080, H = 1500, c = document.createElement('canvas');
  c.width = W; c.height = H;
  var x = c.getContext('2d'), SER = '"Shippori Mincho","Hiragino Mincho ProN","Yu Mincho",Georgia,serif';
  var g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#1b3668'); g.addColorStop(1, '#0c1a3a'); x.fillStyle = g; x.fillRect(0, 0, W, H);
  x.strokeStyle = '#d6b05a'; x.lineWidth = 6; x.strokeRect(36, 36, W - 72, H - 72); x.lineWidth = 2; x.strokeRect(58, 58, W - 116, H - 116);
  var wrap = function(t, cx, y, maxW, lh, font, color){
    x.font = font; x.fillStyle = color; x.textAlign = 'center';
    var lines = [], parts = String(t).split('\n');
    parts.forEach(function(p){
      var cur = '', toks = lang === 'ja' ? p.split('') : p.split(' ');
      toks.forEach(function(w){ var tryS = lang === 'ja' ? cur + w : (cur ? cur + ' ' + w : w); if (x.measureText(tryS).width > maxW && cur){ lines.push(cur); cur = w; } else cur = tryS; });
      if (cur) lines.push(cur);
    });
    lines.forEach(function(l, i){ x.fillText(l, cx, y + i * lh); });
    return y + lines.length * lh;
  };
  var nA = certNames.a.trim() || L(M[a][2], M[a][0] + '宿'), nB = certNames.b.trim() || L(M[b][2], M[b][0] + '宿');
  var draw = function(img){
    if (img) x.drawImage(img, W / 2 - 80, 110, 160, 160);
    x.textBaseline = 'alphabetic';
    var y = wrap(L('Certificate of Bond', '縁の鑑定証'), W / 2, 350, 900, 80, '700 64px ' + SER, '#f6f0e1');
    x.fillStyle = '#d6b05a'; x.fillRect(W / 2 - 60, y - 40, 120, 4);
    y = wrap(L('This certifies the bond between', 'この二人の縁をここに記します'), W / 2, y + 30, 880, 50, '500 34px ' + SER, '#bcc8e2');
    y = wrap(nA, W / 2, y + 70, 900, 96, '800 84px ' + SER, '#f6f0e1');
    y = wrap('×', W / 2, y + 6, 900, 70, '500 56px ' + SER, '#d6b05a');
    y = wrap(nB, W / 2, y + 30, 900, 96, '800 84px ' + SER, '#f6f0e1');
    y = wrap(L(M[a][2] + ' × ' + M[b][2], M[a][0] + '宿 × ' + M[b][0] + '宿'), W / 2, y + 60, 900, 60, '500 44px ' + SER, '#d6b05a');
    var lab = L(pr[0], PAIRJ[r.key]);
    y = wrap(L(k + ' · ' + lab, k + '（' + PAIRYOMI[k] + '）· ' + lab), W / 2, y + 50, 900, 56, '700 38px ' + SER, '#f6f0e1');
    y = wrap(L(VERDICT[k][0], VERDICT[k][2]), W / 2, y + 60, 820, 62, '500 42px ' + SER, '#f6f0e1');
    var t = todayJST();
    wrap(L(MONTH_NAMES[t.m - 1] + ' ' + t.d + ', ' + t.y, t.y + '年' + t.m + '月' + t.d + '日'), W / 2, H - 170, 800, 44, '500 32px ' + SER, '#bcc8e2');
    wrap('Moonbond  ·  moonbondjp.win', W / 2, H - 115, 800, 44, '700 30px ' + SER, '#d6b05a');
    var out = $('certOut');
    c.toBlob(function(bl){
      var url = URL.createObjectURL(bl);
      out.innerHTML = '<img alt="' + L('Your certificate', '二人の鑑定証') + '" src="' + url + '"><a class="cert-dl" href="' + url + '" download="moonbond-certificate.png">' + L('Save the picture', '画像を保存する') + '</a>';
    }, 'image/png');
  };
  var im = new Image(); im.onload = function(){ draw(im); }; im.onerror = function(){ draw(null); }; im.src = '/full/art/moon.webp';
}
function certInit(){
  var go = $('certGo'); if (!go) return;
  go.addEventListener('click', function(){
    certNames.a = $('certA').value; certNames.b = $('certB').value;
    var run = function(){ certDraw(); };
    if (document.fonts && document.fonts.load){ Promise.all([document.fonts.load('700 40px "Shippori Mincho"'), document.fonts.load('500 40px "Shippori Mincho"')]).then(run, run); } else run();
  });
  ['certA', 'certB'].forEach(function(id){ $(id).addEventListener('input', function(){ certNames[id === 'certA' ? 'a' : 'b'] = this.value; }); });
}
"""

# 追加章は「閉じのカード」の直前に差し込む
marker = "  h += '<section class=\"closing\">"
s = rep(s, marker, new_chapters + marker)
s = rep(s, "  $('reading').innerHTML = h; $('reading').hidden = false;\n}\nfunction applyLang(){", "  $('reading').innerHTML = h; $('reading').hidden = false; certInit();\n}\n" + cert_js + "function applyLang(){")

out = ROOT / 'public/couple/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(s, encoding='utf-8')
print('作成: public/couple/index.html')

# 見本ページも一緒に作り直す
import subprocess
subprocess.run([sys.executable, str(ROOT / 'tools/build_samples.py')], check=True)
