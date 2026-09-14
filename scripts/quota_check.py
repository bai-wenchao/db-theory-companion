#!/usr/bin/env python3
"""GLM coding-plan weekly-quota governor (user policy, 2026-09-13).

Rule: daily allowance = 100%/7 per day since the last weekly reset.
Cumulative bound = COMPLETED days since reset × 100/7 (%) — a partial
day does not count (floor, not ceil; user correction 2026-09-13).
Day 0 (reset day itself) gets the first day's allowance so the master
is not deadlocked right after reset.
STOP when weekly usage >= bound - 3  (3-point reserve: ~1% for
summarization + checkpoint by this master, ~2% spare because other
workers may share the same plan).

Usage: quota_check.py [--json]
Reads ANTHROPIC_AUTH_TOKEN from env or ~/.claude/settings.json.
Exit code: 0 = GO, 3 = STOP (threshold tripped), 1 = API unreachable.
"""
import json, math, os, sys, time, urllib.request

EP = "https://open.bigmodel.cn/api/monitor/usage/quota/limit"

# User freeze (2026-09-13 ~23:00): this master is the ONLY active session overnight;
# until 2026-09-14 15:00 local the bound must NOT grow past 2 completed days, i.e.
# usable = 100%/7*2 - 3 regardless of the clock crossing day 3.
FREEZE_UNTIL = time.mktime((2026, 9, 14, 15, 0, 0, 0, 0, -1))
FREEZE_DAYS = 2


def token():
    t = os.environ.get("ANTHROPIC_AUTH_TOKEN")
    if t:
        return t
    s = json.load(open(os.path.expanduser("~/.claude/settings.json")))
    return s.get("env", {}).get("ANTHROPIC_AUTH_TOKEN")


def fetch():
    req = urllib.request.Request(EP, headers={"Authorization": token(),
                                              "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def main():
    try:
        d = fetch()["data"]
    except Exception as e:
        print(f"QUOTA-ERROR {type(e).__name__}")
        sys.exit(1)
    week = next(x for x in d["limits"] if x["unit"] == 6)
    hour = next((x for x in d["limits"] if x["unit"] == 3), None)
    pct = week["percentage"]
    until_reset_s = week["nextResetTime"] / 1000 - time.time()
    elapsed_days = 7 - until_reset_s / 86400.0
    n_days = max(1, int(elapsed_days))  # completed days only (floor); day 0 -> 1
    if time.time() < FREEZE_UNTIL:
        n_days = min(n_days, FREEZE_DAYS)  # frozen cap until 9/14 15:00 (user directive)
    bound = n_days * 100.0 / 7.0
    threshold = bound - 3.0  # soft bound = hard bound - 3 (user policy: other workers share quota)
    verdict = "STOP" if pct >= threshold else "GO"
    out = {
        "verdict": verdict, "weekly_used_pct": pct, "days_since_reset": round(elapsed_days, 2),
        "n_days_charged": n_days, "bound_pct": round(bound, 2), "threshold_pct": round(threshold, 2),
        "headroom_pct": round(threshold - pct, 2), "level": d.get("level"),
        "weekly_remaining": week["remaining"], "weekly_quota": week["usage"],
        "window_used_pct": hour["percentage"] if hour else None,
        "reset_in_h": round(until_reset_s / 3600, 1),
    }
    if "--json" in sys.argv:
        print(json.dumps(out))
    else:
        print(f"[quota] weekly {pct}% used | day-bound {n_days}d = {bound:.1f}% "
              f"(stop at {threshold:.1f}%) | headroom {out['headroom_pct']:.1f}pt "
              f"| 5h-window {out['window_used_pct']}% | weekly reset in {out['reset_in_h']}h")
        print(f"[quota] verdict: {verdict}")
    sys.exit(3 if verdict == "STOP" else 0)


if __name__ == "__main__":
    main()
