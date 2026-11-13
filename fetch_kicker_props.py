#!/usr/bin/env python3
"""
fetch_kicker_props.py -- Pull NFL kicker prop lines from The Odds API v4.

Markets: player_kicking_points, player_field_goals, player_pats (3 credits/event).
Alt ladders (DraftKings only) are pulled separately for screened candidates
with --alts EVENT_ID[,EVENT_ID...] (player_kicking_points_alternate +
player_field_goals_alternate, ~1 credit/market/event).

Usage:
    python3 fetch_kicker_props.py --week-events events.json   # ids+labels
    python3 fetch_kicker_props.py --events id1,id2
    python3 fetch_kicker_props.py --alts id1,id2

Snapshots land in data/odds-snapshots/. Stdlib only. Never crashes.
Auth (GitHub version): set THE_ODDS_API_KEY in your environment with your
own The Odds API key. The key is never printed or committed.
Note: the internal version of this file used a private credential helper;
this public copy is the only change, and only to auth plumbing — markets,
books, normalization, and output format are unchanged.
"""
import argparse, json, os, sys, urllib.parse, urllib.request
from datetime import datetime, timezone

SPORT = "americanfootball_nfl"
CORE = ["player_kicking_points", "player_field_goals", "player_pats"]
ALTS = ["player_kicking_points_alternate", "player_field_goals_alternate"]
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "odds-snapshots")


def api_key():
    key = os.environ.get("THE_ODDS_API_KEY")
    if not key:
        raise SystemExit("Set THE_ODDS_API_KEY in your environment first.")
    return key


def american_to_prob(p):
    if p is None: return None
    return 100.0/(p+100.0) if p > 0 else -p/(-p+100.0)


def fetch(event_id, markets, books):
    params = {"regions": "us", "markets": ",".join(markets),
              "oddsFormat": "american", "bookmakers": books}
    params["apiKey"] = api_key()
    base = "https://api.the-odds-api.com/v4/sports/%s/events/%s/odds/?" % (SPORT, event_id)
    base += urllib.parse.urlencode(params)
    req = urllib.request.Request(base, headers={"User-Agent": "kicker-model/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        quota = (resp.headers.get("x-requests-remaining"), resp.headers.get("x-requests-used"))
        return json.load(resp), quota


def normalize(payload):
    recs = []
    for bm in payload.get("bookmakers", []) or []:
        for m in bm.get("markets", []) or []:
            for o in m.get("outcomes", []) or []:
                recs.append({"book": bm.get("key"), "market": m.get("key"),
                             "player": o.get("description"), "side": o.get("name"),
                             "line": o.get("point"), "price": o.get("price"),
                             "implied_prob": american_to_prob(o.get("price"))})
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default=None)
    ap.add_argument("--alts", default=None, help="event ids for DK alt ladders")
    ap.add_argument("--out-dir", default=OUT_DIR)
    args = ap.parse_args()
    ids = [e.strip() for e in (args.events or "").split(",") if e.strip()]
    alt_ids = [e.strip() for e in (args.alts or "").split(",") if e.strip()]
    games, quota = [], None
    for eid in ids:
        try:
            payload, quota = fetch(eid, CORE, "draftkings,fanduel,betmgm,caesars,bet365,betrivers")
        except Exception as e:
            print("event %s failed: %s" % (eid, e)); continue
        games.append({"event_id": eid, "label": "%s @ %s" % (payload.get("away_team"), payload.get("home_team")),
                      "commence_time": payload.get("commence_time"),
                      "home_team": payload.get("home_team"), "away_team": payload.get("away_team"),
                      "props": normalize(payload)})
        print("fetched %s: %d records" % (games[-1]["label"], len(games[-1]["props"])))
    alts = {}
    for eid in alt_ids:
        try:
            payload, quota = fetch(eid, ALTS, "draftkings")
        except Exception as e:
            print("alts %s failed: %s" % (eid, e)); continue
        alts[eid] = normalize(payload)
        print("alts %s: %d records" % (eid, len(alts[eid])))
    os.makedirs(args.out_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    kind = "alts" if alt_ids and not ids else "core"
    path = os.path.join(args.out_dir, "%s-%s.json" % (stamp, kind))
    with open(path, "w") as f:
        json.dump({"fetched_at": stamp, "source": "the-odds-api v4 kicker props",
                   "games": games, "alts": alts}, f, indent=2)
    print("saved ->", path)
    if quota: print("API quota: %s remaining (used %s)" % quota)
    return 0

if __name__ == "__main__":
    sys.exit(main())
