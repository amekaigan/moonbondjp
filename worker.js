// Moonbond — PayPalの支払いをCloudflare側で確かめてから、くわしい鑑定（/full/）を開く
//
// Cloudflareの「設定 → 変数とシークレット」に入れるもの（値はチャットやリポジトリに書かない）
//   PAYPAL_CLIENT_ID : PayPalアプリ（Live）の Client ID   … 種類は「シークレット」（テキストだと公開のたびに消える）
//   PAYPAL_SECRET    : 同じアプリの Secret                … 種類は「シークレット」
// PAYPAL_SECRET が未設定のあいだは、今までどおり /full/ を誰でも開ける（支払いボタンは「準備中」のまま）

const PRICE = { value: "9.99", currency: "USD" };
const API = "https://api-m.paypal.com";
const DATE = /^(\d{4})-(\d{1,2})-(\d{1,2})$/;

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

function b64u(buf) {
  let s = "";
  for (const b of new Uint8Array(buf)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

// 二人の誕生日から「鑑定を開く鍵」を作る（PayPalのSecretを元にした署名なので、外からは作れない）
async function sign(env, a, b) {
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode("moonbond-full:" + env.PAYPAL_SECRET), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64u(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(a + "|" + b))).slice(0, 22);
}
function same(x, y) {
  if (typeof x !== "string" || x.length !== y.length) return false;
  let d = 0;
  for (let i = 0; i < x.length; i++) d |= x.charCodeAt(i) ^ y.charCodeAt(i);
  return d === 0;
}

function cleanDate(v) {
  const m = DATE.exec(String(v || ""));
  if (!m) return null;
  const y = +m[1], mo = +m[2], d = +m[3];
  const t = new Date(Date.UTC(y, mo - 1, d));
  if (y < 1900 || t.getUTCMonth() !== mo - 1) return null;
  return `${y}-${String(mo).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
}

async function token(env) {
  const r = await fetch(API + "/v1/oauth2/token", {
    method: "POST",
    headers: { authorization: "Basic " + btoa(env.PAYPAL_CLIENT_ID + ":" + env.PAYPAL_SECRET), "content-type": "application/x-www-form-urlencoded" },
    body: "grant_type=client_credentials",
  });
  const j = await r.json();
  if (!j.access_token) throw new Error("paypal-auth");
  return j.access_token;
}
async function pp(env, path, method = "GET", body) {
  const r = await fetch(API + path, {
    method,
    headers: { authorization: "Bearer " + (await token(env)), "content-type": "application/json", prefer: "return=representation" },
    body: body ? JSON.stringify(body) : undefined,
  });
  return { ok: r.ok, j: await r.json().catch(() => ({})) };
}

async function readingUrl(env, order) {
  const unit = order.purchase_units?.[0] || {};
  const cap = unit.payments?.captures?.[0];
  if (order.status !== "COMPLETED" || !cap || cap.status !== "COMPLETED") return null;
  if (cap.amount?.currency_code !== PRICE.currency || cap.amount?.value !== PRICE.value) return null;
  const [a, b, lang] = String(unit.custom_id || "").split("|");
  if (!cleanDate(a) || !cleanDate(b)) return null;
  const k = await sign(env, a, b);
  return `/full/?a=${a}&b=${b}&lang=${lang === "ja" ? "ja" : "en"}&k=${k}`;
}

async function api(request, env, path) {
  const ready = env.PAYPAL_CLIENT_ID && env.PAYPAL_SECRET;
  if (path === "/api/paypal/config") return json({ clientId: ready ? env.PAYPAL_CLIENT_ID : null, price: PRICE });
  if (!ready) return json({ error: "not-ready" }, 503);
  if (request.method !== "POST") return json({ error: "method" }, 405);
  const body = await request.json().catch(() => ({}));

  if (path === "/api/paypal/order") {
    const a = cleanDate(body.a), b = cleanDate(body.b), lang = body.lang === "ja" ? "ja" : "en";
    if (!a || !b) return json({ error: "dates" }, 400);
    const { ok, j } = await pp(env, "/v2/checkout/orders", "POST", {
      intent: "CAPTURE",
      purchase_units: [{
        description: "Moonbond full compatibility reading",
        custom_id: `${a}|${b}|${lang}`,
        amount: { currency_code: PRICE.currency, value: PRICE.value },
      }],
      payment_source: { paypal: { experience_context: { brand_name: "Moonbond", shipping_preference: "NO_SHIPPING", user_action: "PAY_NOW" } } },
    });
    if (!ok || !j.id) return json({ error: "order" }, 502);
    return json({ id: j.id });
  }

  if (path === "/api/paypal/capture") {
    const id = String(body.id || "");
    if (!/^[A-Z0-9]{5,40}$/.test(id)) return json({ error: "id" }, 400);
    let { j } = await pp(env, `/v2/checkout/orders/${id}/capture`, "POST", {});
    // 二重に押された・通信が切れた時は、注文をもう一度見て確かめる
    if (j.status !== "COMPLETED") j = (await pp(env, `/v2/checkout/orders/${id}`)).j;
    const url = await readingUrl(env, j);
    if (!url) return json({ error: "not-paid", status: j.status || j.name || "unknown" }, 402);
    return json({ url });
  }
  return json({ error: "not-found" }, 404);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    try {
      if (path.startsWith("/api/")) return await api(request, env, path);
      // 鑑定ページ本体だけを確かめる（/full/art/ の画像はそのまま出す）
      if ((path === "/full" || path === "/full/" || path === "/full/index.html") && env.PAYPAL_SECRET) {
        const a = cleanDate(url.searchParams.get("a")), b = cleanDate(url.searchParams.get("b"));
        const ok = a && b && same(url.searchParams.get("k"), await sign(env, a, b));
        if (!ok) return Response.redirect(url.origin + "/#editions", 302);
      }
    } catch (e) {
      return json({ error: "server" }, 500);
    }
    return env.ASSETS.fetch(request);
  },
};
