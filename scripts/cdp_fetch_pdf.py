#!/usr/bin/env python3
"""Fetch an ACM PDF via the CDP Chrome instance (passes Cloudflare in-page).
Usage: cdp_fetch_pdf.py <doi> <out.pdf>
Requires the CDP Chrome running with a dl.acm.org tab (same-origin context)."""
import base64, json, sys, time, urllib.request
import websocket

HTTP = "http://127.0.0.1:9222"
JS = """
(async () => {
  const r = await fetch(URL, {credentials: "include"});
  if (!r.ok) return "HTTPERR " + r.status;
  const b = new Uint8Array(await r.arrayBuffer());
  const head = String.fromCharCode(...b.subarray(0, 5));
  if (head !== "%PDF-") return "NOTPDF " + head;
  let s = "";
  const CH = 0x8000;
  for (let i = 0; i < b.length; i += CH)
    s += String.fromCharCode.apply(null, b.subarray(i, i + CH));
  return "B64 " + btoa(s);
})()
"""


def targets():
    return json.load(urllib.request.urlopen(HTTP + "/json/list", timeout=5))


def dl_tab():
    for t in targets():
        if t.get("type") == "page" and "dl.acm.org" in t.get("url", ""):
            return t
    return None


def navigate(tab_url, url):
    # reuse a dl.acm.org tab by opening the URL there via /json/new in that context is
    # not possible; instead navigate existing tab through its ws
    for t in targets():
        if t.get("type") == "page" and "dl.acm.org" in t.get("url", ""):
            ws = websocket.create_connection(t["webSocketDebuggerUrl"], timeout=30)
            try:
                ws.send(json.dumps({"id": 1, "method": "Page.navigate",
                                    "params": {"url": url}}))
                ws.recv()
            finally:
                ws.close()
            time.sleep(3)
            return True
    return False


def eval_js(expr, timeout=60):
    tab = dl_tab()
    if not tab:
        return None, "no dl.acm.org tab"
    ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=timeout)
    try:
        ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate",
                            "params": {"expression": expr, "returnByValue": True,
                                       "awaitPromise": True}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == 1:
                r = msg.get("result", {}).get("result", {})
                return r.get("value"), r
    finally:
        ws.close()


def fetch_pdf(doi, out_path):
    expr = JS.replace("URL", json.dumps(f"https://dl.acm.org/doi/pdf/{doi}"))
    val, raw = eval_js(expr)
    if not isinstance(val, str):
        return f"eval-failed: {json.dumps(raw)[:200]}"
    if val.startswith("B64 "):
        blob = base64.b64decode(val[4:])
        if blob[:5] != b"%PDF-":
            return "bad-magic-after-decode"
        open(out_path, "wb").write(blob)
        return f"ok {len(blob)} bytes"
    # challenge/HTML: navigate to the paper page (refresh clearance), retry once
    if val.startswith(("NOTPDF", "HTTPERR")) or "Just a moment" in str(raw):
        navigate(None, f"https://dl.acm.org/doi/{doi}")
        time.sleep(5)
        val, raw = eval_js(expr)
        if isinstance(val, str) and val.startswith("B64 "):
            blob = base64.b64decode(val[4:])
            open(out_path, "wb").write(blob)
            return f"ok-after-retry {len(blob)} bytes"
        return f"still-blocked: {str(val)[:80]}"
    return f"unexpected: {str(val)[:80]}"


if __name__ == "__main__":
    print(fetch_pdf(sys.argv[1], sys.argv[2]))
