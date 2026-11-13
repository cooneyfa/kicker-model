#!/usr/bin/env python3
"""
kicker_model.py -- NFL kicker prop model v1 (transparent, Poisson-thinning).

DATA
- Lines: latest core snapshot in data/odds-snapshots/ (The Odds API).
- Game spread/total: /tmp/nfl_events.json style pull saved to
  data/game-lines.json (median across books).
- Kicker/team stats W1-6: Sleeper stats endpoint (free, no key)
  https://api.sleeper.app/stats/nfl/2026/<week>?season_type=regular&position[]=K
  Each entry carries the kicker's opponent that week -> opponent-allowed
  FGA / kicking points are computed from the same file. No invented stats.

MODEL (per kicker)
- fg_pct shrunk to league: (fgm + 17) / (fga + 20); xp_pct shrunk to 95%.
- Factor_opp = opp FGA allowed per game / league FGA per game, capped [0.80, 1.25].
- EnvFactor = 0.5 + 0.5 * (implied team total / team season pts per game),
  capped [0.75, 1.30]. (Half-weight: ITT also enters the TD solve below.)
- E_FGA = season FGA/g * Factor_opp * EnvFactor
- E_FGM_rate = E_FGA * fg_pct
- E_TD from the implied team total identity:
    ITT ~= 6*TD + 0.95*TD(XP) + 3*FGM + 0.3 (safeties/2pt/defense avg)
    E_TD_solve = max(0.5, (ITT - 3*E_FGM - 0.3) / 6.95)
  blended 50/50 with season XPA/g scaled by ITT/team_pts.
- Distribution: attempts ~ Poisson, makes are thinned Poissons:
    FGM ~ Pois(E_FGA * fg_pct), XPM ~ Pois(E_TD * xp_pct), independent.
    Kicking points = 3*FGM + XPM (exact convolution).
  Known flaw: FG and XP counts share drive volume (positive correlation),
  so true tails are wider than modeled. The stress test is the guard.
- Stress (pessimistic): E_FGA*0.85, E_TD*0.90, fg_pct-0.04, xp_pct-0.02.

OUTPUT: ranked table JSON + stdout. Edge = model P(over) - no-vig implied
(from the over/under pair at the same book when available, else raw implied
of the best over price).
"""
import json, math, os, sys, urllib.request
from collections import defaultdict
from statistics import median

# GitHub version: paths point at this repo (data/), not the internal workspace.
# Formulas, shrinkage, caps, and stress test below are unchanged from the
# internal model.
BASE = os.path.dirname(os.path.abspath(__file__))
SNAP_DIR = os.path.join(BASE, "data", "odds-snapshots")
SL_DIR = os.path.join(BASE, "data", "sleeper")
WEEKS = [1, 2, 3, 4, 5, 6]

VENUE = {  # team (home) -> (venue type, note)
    "NO": ("outdoor", "Stade de France, Saint-Denis (Paris game) - open air"),
    "ATL": ("dome", "Mercedes-Benz Stadium - retractable, treated indoor"),
    "BAL": ("outdoor-calm", "M&T Bank - 64F, wind ~2-4 mph, 0% precip"),
    "CAR": ("outdoor-gusty", "Bank of America - 64F, NE 12 mph gusts 20"),
    "HOU": ("dome", "NRG Stadium - retractable"),
    "MIN": ("dome", "U.S. Bank Stadium - indoor"),
    "NYJ": ("outdoor-calm", "MetLife - 64F, wind ~2 mph, 0% precip"),
    "TEN": ("outdoor-calm", "Nissan Stadium - 72F, calm, sunny"),
    "ARI": ("dome", "State Farm Stadium - retractable"),
    "DET": ("dome", "Ford Field - indoor"),
    "LV": ("dome", "Allegiant Stadium - indoor"),
    "SEA": ("outdoor-rain-risk", "Lumen Field - 55F, wind 3 mph, ~44% light rain"),
    "PHI": ("outdoor-calm", "Lincoln Financial - 60F, wind ~5 mph, clear"),
}


def fetch_sleeper():
    os.makedirs(SL_DIR, exist_ok=True)
    for w in WEEKS:
        path = os.path.join(SL_DIR, "kstats_2026_w%d.json" % w)
        if os.path.exists(path):
            continue
        url = "https://api.sleeper.app/stats/nfl/2026/%d?season_type=regular&position[]=K" % w
        req = urllib.request.Request(url, headers={"User-Agent": "kicker-model/0.1"})
        with urllib.request.urlopen(req, timeout=30) as r:
            json.dump(json.load(r), open(path, "w"))
        print("fetched sleeper week", w)


def pois_pmf(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def points_dist(lam_fg, lam_xp, max_pts=36):
    """P(points = p) for points = 3*FGM + XPM, FGM~Pois(lam_fg), XPM~Pois(lam_xp)."""
    dist = [0.0] * (max_pts + 1)
    for f in range(0, 13):
        pf = pois_pmf(f, lam_fg)
        if pf < 1e-9: continue
        for x in range(0, 16):
            px = pois_pmf(x, lam_xp)
            p = 3 * f + x
            if p <= max_pts:
                dist[p] += pf * px
    return dist


def p_over(dist, line):
    return sum(pr for pts, pr in enumerate(dist) if pts > line)


def no_vig_over(recs):
    """recs: list of dicts for one player+market. Return (line, best_over_price,
    best_over_book, implied_for_edge, pair_found). Line = median over line."""
    overs = [r for r in recs if r["side"] == "Over" and r["line"] is not None]
    if not overs: return None
    from collections import Counter
    line = Counter([r["line"] for r in overs]).most_common(1)[0][0]
    at_line = [r for r in overs if r["line"] == line]
    best = max(at_line, key=lambda r: r["price"])
    # no-vig from same-book pair at that line
    unders = [r for r in recs if r["side"] == "Under" and r["line"] == line and r["book"] == best["book"]]
    raw = best["implied_prob"]
    if unders:
        u = unders[0]["implied_prob"]
        return line, best["price"], best["book"], raw / (raw + u), True
    return line, best["price"], best["book"], raw, False


def main():
    fetch_sleeper()
    # ---------- season aggregates ----------
    kick = defaultdict(lambda: {"games": 0, "fga": 0.0, "fgm": 0.0, "xpa": 0.0, "xpm": 0.0,
                                "pts": [], "lng": 0.0, "team": None, "fg50": 0.0})
    team_week = defaultdict(lambda: {"fga": 0.0, "fgm": 0.0, "xpa": 0.0, "xpm": 0.0})  # (team,week)
    opp_allowed = defaultdict(lambda: {"games": 0, "fga": 0.0, "pts": 0.0})  # by defending team
    games_seen = defaultdict(set)  # defending team -> game ids
    all_pts = []
    for w in WEEKS:
        entries = json.load(open(os.path.join(SL_DIR, "kstats_2026_w%d.json" % w)))
        for e in entries:
            st = e.get("stats") or {}
            if not st.get("gp"): continue
            name = "%s %s" % (e["player"]["first_name"], e["player"]["last_name"])
            team = e.get("team"); opp = e.get("opponent")
            k = kick[name]; k["team"] = team; k["games"] += 1
            k["fga"] += st.get("fga", 0) or 0; k["fgm"] += st.get("fgm", 0) or 0
            k["xpa"] += st.get("xpa", 0) or 0; k["xpm"] += st.get("xpm", 0) or 0
            k["pts"].append(st.get("kick_pts", 0) or 0)
            k["lng"] = max(k["lng"], st.get("fgm_lng", 0) or 0)
            k["fg50"] += (st.get("fgm_50p", 0) or 0)
            tw = team_week[(team, w)]
            tw["fga"] += st.get("fga", 0) or 0; tw["fgm"] += st.get("fgm", 0) or 0
            tw["xpa"] += st.get("xpa", 0) or 0; tw["xpm"] += st.get("xpm", 0) or 0
            oa = opp_allowed[opp]
            if e.get("game_id") not in games_seen[opp]:
                games_seen[opp].add(e.get("game_id")); oa["games"] += 1
            oa["fga"] += st.get("fga", 0) or 0; oa["pts"] += st.get("kick_pts", 0) or 0
            all_pts.append(st.get("kick_pts", 0) or 0)
    team_games = defaultdict(int); team_tot = defaultdict(lambda: {"fga": 0.0, "fgm": 0.0, "xpa": 0.0, "xpm": 0.0})
    for (team, w), tw in team_week.items():
        team_games[team] += 1
        for key in tw: team_tot[team][key] += tw[key]
    team_pts_pg = {t: (6.0 * team_tot[t]["xpa"] + team_tot[t]["xpm"] + 3.0 * team_tot[t]["fgm"]) / team_games[t]
                   for t in team_games}
    team_fga_pg = {t: team_tot[t]["fga"] / team_games[t] for t in team_games}
    team_xpa_pg = {t: team_tot[t]["xpa"] / team_games[t] for t in team_games}
    league_fga_pg = sum(team_fga_pg.values()) / len(team_fga_pg)
    league_pts_pg = sum(team_pts_pg.values()) / len(team_pts_pg)

    # hypothesis check: FG share of scoring in low- vs high-scoring games (W1-6 actuals)
    game_pts = defaultdict(float); game_kick = defaultdict(float)
    for w in WEEKS:
        entries = json.load(open(os.path.join(SL_DIR, "kstats_2026_w%d.json" % w)))
        by_game = defaultdict(list)
        for e in entries:
            if (e.get("stats") or {}).get("gp"): by_game[e["game_id"]].append(e)
        for gid, es in by_game.items():
            kick_pts = sum((e["stats"].get("kick_pts", 0) or 0) for e in es)
            td_pts = sum(6.0 * (e["stats"].get("xpa", 0) or 0) + (e["stats"].get("xpm", 0) or 0) for e in es)
            game_kick[gid] = kick_pts; game_pts[gid] = kick_pts + td_pts
    low = [(game_pts[g], game_kick[g]) for g in game_pts if game_pts[g] < 40]
    high = [(game_pts[g], game_kick[g]) for g in game_pts if game_pts[g] >= 50]
    def avg(xs, i): return sum(x[i] for x in xs) / len(xs) if xs else 0
    hypothesis = {
        "n_games": len(game_pts),
        "low_scoring_lt40": {"n": len(low), "avg_kick_pts_both_teams": round(avg(low, 1), 2),
                             "kick_share_of_points_pct": round(100 * avg(low, 1) / avg(low, 0), 1) if low else None},
        "high_scoring_gte50": {"n": len(high), "avg_kick_pts_both_teams": round(avg(high, 1), 2),
                               "kick_share_of_points_pct": round(100 * avg(high, 1) / avg(high, 0), 1) if high else None},
    }

    # ---------- game lines (median spread/total) ----------
    gl = json.load(open(os.path.join(BASE, "data", "game-lines.json")))
    lines = {}
    for ev in gl["events"]:
        totals, spreads = [], {}
        for bm in ev.get("bookmakers", []):
            for m in bm.get("markets", []):
                if m["key"] == "totals":
                    totals += [o["point"] for o in m["outcomes"] if o.get("point") is not None]
                if m["key"] == "spreads":
                    for o in m["outcomes"]:
                        spreads.setdefault(o["name"], []).append(o["point"])
        if not totals: continue
        total = median(totals)
        sp = {t: median(v) for t, v in spreads.items()}  # negative = favorite
        lines[(ev["away_team"], ev["home_team"])] = (total, sp)

    # ---------- latest core snapshot ----------
    snaps = sorted(f for f in os.listdir(SNAP_DIR) if f.endswith("core.json"))
    snap = json.load(open(os.path.join(SNAP_DIR, snaps[-1])))
    name2team = {}
    for name, k in kick.items():
        name2team[name] = k["team"]
    players_meta = json.load(open(os.path.join(SL_DIR, "players.json")))
    for pid, p in players_meta.items():
        if p.get("full_name"): name2team[p["full_name"]] = p.get("team")
    ABBR = {"Pittsburgh Steelers": "PIT", "New Orleans Saints": "NO", "San Francisco 49ers": "SF",
            "Atlanta Falcons": "ATL", "Cincinnati Bengals": "CIN", "Baltimore Ravens": "BAL",
            "Tampa Bay Buccaneers": "TB", "Carolina Panthers": "CAR", "Cleveland Browns": "CLE",
            "Tennessee Titans": "TEN", "New York Giants": "NYG", "Houston Texans": "HOU",
            "Indianapolis Colts": "IND", "Minnesota Vikings": "MIN", "Miami Dolphins": "MIA",
            "New York Jets": "NYJ", "Denver Broncos": "DEN", "Arizona Cardinals": "ARI",
            "Green Bay Packers": "GB", "Detroit Lions": "DET", "Los Angeles Rams": "LAR",
            "Las Vegas Raiders": "LV", "Kansas City Chiefs": "KC", "Seattle Seahawks": "SEA",
            "Dallas Cowboys": "DAL", "Philadelphia Eagles": "PHI"}

    results = []
    for g in snap["games"]:
        key = (g["away_team"], g["home_team"])
        if key not in lines: continue
        total, sp = lines[key]
        by_player = defaultdict(list)
        for r in g["props"]: by_player[r["player"]].append(r)
        for player, recs in by_player.items():
            team_abbr = name2team.get(player)
            if not team_abbr: continue
            is_home = (ABBR[g["home_team"]] == team_abbr)
            team_name = g["home_team"] if is_home else g["away_team"]
            opp_name = g["away_team"] if is_home else g["home_team"]
            opp_abbr = ABBR[opp_name]
            team_spread = sp.get(team_name, 0.0)  # negative if favorite
            itt = (total - team_spread) / 2.0
            k = kick.get(player)
            if not k or k["games"] < 2:
                results.append({"player": player, "team": team_abbr, "game": g["label"],
                                "note": "INSUFFICIENT/NEW KICKER - no model (regime change)", "edge_kp": None})
                continue
            # v1.1 shrinkage (added after the v1 audit: raw 5-6 game rates
            # double-stacked -- Reichard E_FGA hit 4.1, a number almost no
            # kicker sustains). Kicker FGA/g shrunk toward league with a
            # 4-game prior; opponent factor shrunk 50% toward 1.0.
            fga_pg_raw = k["fga"] / k["games"]
            fga_pg = (k["fga"] + 4.0 * league_fga_pg) / (k["games"] + 4.0)
            fg_pct = (k["fgm"] + 17.0) / (k["fga"] + 20.0)
            xp_pct = min(0.99, (k["xpm"] + 19.0) / (k["xpa"] + 20.0))
            oa = opp_allowed.get(opp_abbr, {"games": 6, "fga": league_fga_pg * 6})
            opp_fga_pg = oa["fga"] / max(1, oa["games"])
            factor_opp = max(0.85, min(1.20, 1.0 + 0.5 * (opp_fga_pg / league_fga_pg - 1.0)))
            tpp = team_pts_pg.get(team_abbr, league_pts_pg)
            env = max(0.75, min(1.30, 0.5 + 0.5 * (itt / tpp))) if tpp else 1.0
            e_fga = min(3.4, fga_pg * factor_opp * env)  # v1.1 hard cap
            lam_fg = e_fga * fg_pct
            e_td_solve = max(0.5, (itt - 3.0 * lam_fg - 0.3) / 6.95)
            e_td_season = team_xpa_pg.get(team_abbr, 2.2) * max(0.7, min(1.3, itt / tpp)) if tpp else e_td_solve
            e_td = 0.5 * e_td_solve + 0.5 * e_td_season
            lam_xp = e_td * xp_pct
            dist = points_dist(lam_fg, lam_xp)
            mean_pts = sum(i * p for i, p in enumerate(dist))
            # stress
            dist_s = points_dist(e_fga * 0.85 * max(0.70, fg_pct - 0.04), e_td * 0.90 * xp_pct)
            row = {"player": player, "team": team_abbr, "opp": opp_abbr, "game": g["label"],
                   "venue": VENUE.get(ABBR[g["home_team"]], ("?", "")),
                   "total": total, "itt": round(itt, 1),
                   "season": {"g": k["games"], "fga_pg": round(fga_pg, 2), "fg_pct_shrunk": round(fg_pct, 3),
                              "pts_pg": round(sum(k["pts"]) / k["games"], 2), "pts_median": median(k["pts"]),
                              "pts_by_week": k["pts"], "lng": k["lng"], "fg50_made": k["fg50"]},
                   "opp_fga_allowed_pg": round(opp_fga_pg, 2), "factor_opp": round(factor_opp, 2),
                   "team_fga_pg": round(team_fga_pg.get(team_abbr, 0), 2),
                   "e_fga": round(e_fga, 2), "e_td": round(e_td, 2),
                   "lam_fg": round(lam_fg, 2), "lam_xp": round(lam_xp, 2),
                   "model_mean_pts": round(mean_pts, 2)}
            for mkt, dist_key in [("player_kicking_points", "kp"), ("player_field_goals", "fg"), ("player_pats", "pat")]:
                mrecs = [r for r in recs if r["market"] == mkt]
                nv = no_vig_over(mrecs)
                if not nv: continue
                line_, price, book, implied, pair = nv
                if mkt == "player_kicking_points":
                    p_model = p_over(dist, line_); p_stress = p_over(dist_s, line_)
                elif mkt == "player_field_goals":
                    p_model = 1 - pois_pmf(0, lam_fg) - (pois_pmf(1, lam_fg) if line_ >= 1.5 else 0)
                    if line_ >= 2.5: p_model = 1 - sum(pois_pmf(i, lam_fg) for i in range(3))
                    p_stress = p_model  # stress shown for KP only in v1
                else:
                    p_model = 1 - sum(pois_pmf(i, lam_xp) for i in range(int(line_ + 0.5)))
                    p_stress = p_model
                row[dist_key] = {"line": line_, "price": price, "book": book,
                                 "implied_novig": round(implied, 4), "pair": pair,
                                 "model_p": round(p_model, 4),
                                 "edge_pp": round(100 * (p_model - implied), 1),
                                 "stress_p": round(p_stress, 4)}
            row["edge_kp"] = row.get("kp", {}).get("edge_pp")
            results.append(row)
    results.sort(key=lambda r: (r["edge_kp"] is None, -(r["edge_kp"] or -99)))
    out = {"snapshot": snaps[-1], "league_fga_pg": round(league_fga_pg, 2),
           "league_team_pts_pg": round(league_pts_pg, 1), "hypothesis_low_total": hypothesis,
           "results": results}
    path = os.path.join(BASE, "data", "model-output.json")
    json.dump(out, open(path, "w"), indent=2)
    print(json.dumps(hypothesis, indent=1))
    for r in results:
        if r.get("kp"):
            print("%-20s %s vs %s ITT %.1f mean %.2f KP O%s @%+d (%s) impl %.1f%% model %.1f%% edge %+.1fpp stress %.1f%% | FG edge %s PAT edge %s" % (
                r["player"], r["team"], r["opp"], r["itt"], r["model_mean_pts"],
                r["kp"]["line"], r["kp"]["price"], r["kp"]["book"], 100 * r["kp"]["implied_novig"],
                100 * r["kp"]["model_p"], r["kp"]["edge_pp"], 100 * r["kp"]["stress_p"],
                r.get("fg", {}).get("edge_pp"), r.get("pat", {}).get("edge_pp")))
        else:
            print("%-20s %s" % (r["player"], r.get("note", "no KP market")))
    print("wrote", path)
    return 0

if __name__ == "__main__":
    sys.exit(main())
