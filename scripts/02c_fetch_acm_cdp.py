#!/usr/bin/env python3
"""Bulk-fetch ACM-only PDFs via the CDP Chrome instance (Cloudflare-aware).

Usage: 02c_fetch_acm_cdp.py <papers.jsonl> <pdf_dir> <manual_dir>

Flow per paper: direct in-page fetch. On 403 (Cloudflare suspicion):
  - back off 45s, probe again
  - after 3 consecutive blocked papers: print a HUMAN-ACTION banner and poll
    every 20s (up to 15 min) — the user clicks "Verify you are human" once in
    the CDP Chrome window; a successful probe resumes the batch.
Pacing 3.5-5s between successful fetches. Appends {id,status,bytes,why} to
<manual_dir>/manifest_cdp.jsonl; a paper needs 2 recorded fails to be skipped
on a rerun.
"""
import base64, json, os, random, sys, time
import websocket  # noqa: E402

papers_f, pdf_dir, manual_dir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(manual_dir, exist_ok=True)
manifest_f = os.path.join(manual_dir, "manifest_cdp.jsonl")

JS_T = """
(async (doi) => {
  const r = await fetch("https://dl.acm.org/doi/pdf/" + doi, {credentials: "include"});
  if (!r.ok) return "HTTPERR " + r.status;
  const b = new Uint8Array(await r.arrayBuffer());
  if (String.fromCharCode(...b.subarray(0, 5)) !== "%PDF-") return "NOTPDF";
  let s = "";
  const CH = 0x8000;
  for (let i = 0; i < b.length; i += CH)
    s += String.fromCharCode.apply(null, b.subarray(i, i + CH));
  return "B64 " + btoa(s);
})
"""


def targets():
    import urllib.request
    return json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list", timeout=5))


def dl_tab():
    for t in targets():
        if t.get("type") == "page" and "dl.acm.org" in t.get("url", ""):
            return t
    return None


def fetch_one(doi):
    """Returns (status, blob|None): ok / blocked / other-reason."""
    tab = dl_tab()
    if not tab:
        return "no-tab", None
    try:
        ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=90)
    except Exception as e:
        return f"ws-error:{type(e).__name__}", None
    try:
        expr = f"({JS_T})({json.dumps(doi)})"
        ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate",
                            "params": {"expression": expr, "returnByValue": True,
                                       "awaitPromise": True}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == 1:
                r = msg.get("result", {}).get("result", {})
                v = r.get("value") if isinstance(r, dict) else None
                if isinstance(v, str) and v.startswith("B64 "):
                    import base64 as b64
                    blob = b64.b64decode(v[4:])
                    return "ok" if blob[:5] == b"%PDF-" else "bad-magic", blob
                if isinstance(v, str) and v.startswith("HTTPERR"):
                    return "blocked" if "403" in v else v, None
                return f"eval:{json.dumps(r)[:60]}", None
    finally:
        ws.close()


def wait_for_clearance(probe_doi):
    """Back off, then wait for a human click if Cloudflare stays suspicious."""
    for phase, (delay, tries, banner) in enumerate(
            [(45, 2, False), (20, 45, True)]):
        if banner:
            print("\n" + "!" * 70, flush=True)
            print("!! HUMAN ACTION NEEDED: click 'Verify you are human' ONCE in the",
                  flush=True)
            print("!! second Chrome window (the dl.acm.org one). Waiting...", flush=True)
            print("!" * 70, flush=True)
        for i in range(tries):
            time.sleep(delay)
            st, _ = fetch_one(probe_doi)
            if st == "ok":
                print(f"[cdp] clearance regained (phase {phase}, try {i + 1})", flush=True)
                return True
            if st != "blocked":
                return False  # different error, don't loop
    return False


have = set()
for d in (pdf_dir, manual_dir):
    for f in os.listdir(d):
        if f.endswith(".pdf"):
            have.add(f[:-4])

fails = {}
if os.path.exists(manifest_f):
    for line in open(manifest_f):
        try:
            r = json.loads(line)
            if r.get("status") != "ok":
                fails[r["id"]] = fails.get(r["id"], 0) + 1
        except Exception:
            pass

todo = []
for line in open(papers_f):
    p = json.loads(line)
    pid, doi = p["id"], p.get("doi", "")
    if pid in have or not doi or fails.get(pid, 0) >= 2:
        continue
    todo.append((pid, doi))

print(f"[cdp] todo={len(todo)}", flush=True)
stats = {"ok": 0, "fail": 0}
consecutive_blocked = 0
mf = open(manifest_f, "a")
for i, (pid, doi) in enumerate(todo):
    st, blob = fetch_one(doi)
    if st == "blocked":
        consecutive_blocked += 1
        if wait_for_clearance(doi):
            st, blob = fetch_one(doi)
        else:
            st = "gave-up-clearance"
    if st == "ok":
        consecutive_blocked = 0
        stats["ok"] += 1
        open(os.path.join(manual_dir, f"{pid}.pdf"), "wb").write(blob)
        rec = {"id": pid, "status": "ok", "bytes": len(blob)}
    else:
        stats["fail"] += 1
        rec = {"id": pid, "status": "fail", "why": st[:100]}
    mf.write(json.dumps(rec) + "\n")
    mf.flush()
    if (i + 1) % 10 == 0:
        print(f"[cdp] {i+1}/{len(todo)} {json.dumps(stats)} blocked-streak={consecutive_blocked}",
              flush=True)
    time.sleep(random.uniform(3.5, 5.0) if st == "ok" else 2.0)
mf.close()
print(f"[cdp] DONE {json.dumps(stats)}", flush=True)
