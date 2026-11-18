/* Moonbond analytics (GA4). Set the measurement ID below, e.g. 'G-XXXXXXXXXX'. Empty = no tracking. */
(function () {
  var GA_ID = 'G-705EPJMDMC';
  if (!/^G-[A-Z0-9]+$/.test(GA_ID)) { window.mbTrack = function () {}; return; }
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  var s = document.createElement('script');
  s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);
  gtag('js', new Date());
  /* Never send the query string: /full/?a=..&b=.. carries birthdays. */
  gtag('config', GA_ID, { page_location: location.origin + location.pathname, page_referrer: document.referrer ? document.referrer.split('?')[0] : '' });
  var isFull = /^\/full\/?/.test(location.pathname);
  window.mbTrack = function (name, params) { try { gtag('event', name, params || {}); } catch (e) {} };
  function lang() { return document.documentElement.lang === 'ja' ? 'ja' : 'en'; }
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('button, a, .tile, [data-buy]');
    if (!t) return;
    if (t.hasAttribute('data-buy')) { mbTrack('buy_click', { plan: t.getAttribute('data-buy'), lang: lang() }); return; }
    if (t.id === 'compareBtn') { mbTrack('compare_click', { lang: lang() }); return; }
    if (t.id === 'langEn' || t.id === 'langJa') { mbTrack('lang_switch', { to: t.id === 'langJa' ? 'ja' : 'en' }); return; }
    if (t.classList.contains('hero-btn')) { mbTrack('hero_cta_click', { lang: lang() }); return; }
    if (t.id === 'copyBtn') { mbTrack('share_copy', { lang: lang() }); return; }
    if (t.classList.contains('tile')) { mbTrack('mansion_tile_click', { lang: lang() }); }
  }, true);
  document.addEventListener('submit', function (e) {
    if (e.target && e.target.id === 'birthForm') mbTrack(isFull ? 'full_diagnose' : 'diagnose', { lang: lang() });
  }, true);
  if (isFull) mbTrack('full_view', { lang: lang() });
})();
