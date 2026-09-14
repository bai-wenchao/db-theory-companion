#!/usr/bin/env python3
"""Evaluate JS in a dl.acm.org tab of the CDP Chrome instance.
Usage: cdp_eval.py "<js expression>" [--tab-url substring]
Prints the JSON-encoded result. Creates a new tab (--open URL) if requested."""
import json, sys, urllib.request
import websocket

HTTP = "http://127.0.0.1:9222"


def targets():
    return json.load(urllib.request.urlopen(HTTP + "/json/list", timeout=5))


def find_tab(sub):
    for t in targets():
        if t.get("type") == "page" and sub in t.get("url", ""):
            return t
    return None


def eval_in(tab, expr, await_promise=True):
    ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=30)
    try:
        ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate",
                            "params": {"expression": expr, "returnByValue": True,
                                       "awaitPromise": await_promise}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == 1:
                return msg
    finally:
        ws.close()


def main():
    expr = sys.argv[1]
    sub = "dl.acm.org"
    url = None
    args = sys.argv[2:]
    for i, a in enumerate(args):
        if a == "--tab-url":
            sub = args[i + 1]
        if a == "--open":
            url = args[i + 1]
    if url:
        urllib.request.urlopen(HTTP + "/json/new?" + url, timeout=10)
        import time
        time.sleep(4)
    tab = find_tab(sub)
    if not tab:
        print(json.dumps({"error": "no tab matching", "sub": sub}))
        sys.exit(1)
    r = eval_in(tab, expr)
    print(json.dumps(r.get("result", {}).get("result", r)))


if __name__ == "__main__":
    main()
