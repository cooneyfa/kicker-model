#!/usr/bin/env python3
"""Fetch NFL spreads/totals (median across books) from The Odds API,
filter to a given event-id list, save compact game-lines file.

GitHub version: set THE_ODDS_API_KEY in your environment with your own
The Odds API key. The internal version used a private credential helper;
this public copy changes only auth plumbing and the output path.
"""
import json, os, sys, urllib.parse, urllib.request
from statistics import median

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def main():
    ids = sys.argv[1].split(",") if len(sys.argv) > 1 else []
    out_name = sys.argv[2] if len(sys.argv) > 2 else "game-lines-week8.json"
    key = os.environ.get("THE_ODDS_API_KEY")
    if not key:
        raise SystemExit("Set THE_ODDS_API_KEY in your environment first.")
    params = {"regions": "us", "markets": "h2h,spreads,totals", "oddsFormat": "american",
              "bookmakers": "draftkings,fanduel,betmgm,caesars,bet365,betrivers",
              "apiKey": key}
    base = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(base, headers={"User-Agent": "kicker-model/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        quota = (resp.headers.get("x-requests-remaining"), resp.headers.get("x-requests-used"))
        payload = json.load(resp)
    out = {}
    for ev in payload:
        if ids and ev["id"] not in ids:
            continue
        totals, spreads = [], {}
        for bm in ev.get("bookmakers", []):
            for m in bm.get("markets", []):
                if m["key"] == "totals":
                    totals += [o["point"] for o in m["outcomes"] if o.get("point") is not None]
                if m["key"] == "spreads":
                    for o in m["outcomes"]:
                        spreads.setdefault(o["name"], []).append(o["point"])
        if not totals:
            continue
        out[ev["id"]] = {"away": ev["away_team"], "home": ev["home_team"],
                         "commence_time": ev["commence_time"],
                         "total": median(totals),
                         "spreads": {t: median(v) for t, v in spreads.items()}}
        print(ev["away_team"], "@", ev["home_team"], "total", median(totals), "spreads", out[ev["id"]]["spreads"])
    os.makedirs(BASE, exist_ok=True)
    with open(os.path.join(BASE, out_name), "w") as f:
        json.dump(out, f, indent=1)
    print("saved", out_name, "events:", len(out))
    print("API quota: %s remaining (used %s)" % quota)

if __name__ == "__main__":
    main()
