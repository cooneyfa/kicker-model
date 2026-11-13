#!/usr/bin/env python3
"""
backtest.py -- honest out-of-sample backtest of the kicker model v1.1.

For each target week t in 2..6, every prediction uses ONLY weeks < t:
  - kicker rates, opponent FGA-allowed, league rates, team scoring.
No lines/prices are used (no historical kicker-prop odds file exists), so
this tests CALIBRATION (does a predicted 70% actually hit ~70% of the
time?), not ROI. ROI needs a market price; calibration is the prerequisite.

One deliberate deviation from the live model, disclosed, not hidden:
the live model uses the game's implied team total (ITT) from the odds
board. Historical ITTs are not on file, so the backtest proxies ITT with
the team's season-to-date points per game. That forces EnvFactor = 1.0
and E_TD's ITT scaling to 1.0 -- i.e. the backtest is a slightly
weaker version of the live model (no spread/total information).

A second run ("in-sample") repeats the same predictions but with
aggregates computed over ALL six weeks including the target week --
the leakage the live Week 7 run does NOT have in its per-kicker inputs
(W7 hasn't been played) but DID have in its shrinkage constants, which
were chosen after seeing W1-6. Comparing the two quantifies optimism.
"""
import json, math, os
from collections import defaultdict

# GitHub version: paths point at this repo (data/), not the internal workspace.
# Formulas and backtest logic are unchanged.
BASE = os.path.dirname(os.path.abspath(__file__))
SL = os.path.join(BASE, "data", "sleeper")
WEEKS = [1, 2, 3, 4, 5, 6]


def pois(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def load_week(w):
    return json.load(open(os.path.join(SL, "kstats_2026_w%d.json" % w)))


def aggregates(week_list):
    """Mirror kicker_model.py's aggregates, restricted to week_list."""
    kick = defaultdict(lambda: {"games": 0, "fga": 0.0, "fgm": 0.0,
                                "xpa": 0.0, "xpm": 0.0, "pts": [], "team": None})
    team_week = defaultdict(lambda: {"fga": 0.0, "fgm": 0.0, "xpa": 0.0, "xpm": 0.0})
    opp_allowed = defaultdict(lambda: {"games": 0, "fga": 0.0})
    games_seen = defaultdict(set)
    for w in week_list:
        for e in load_week(w):
            st = e.get("stats") or {}
            if not st.get("gp"):
                continue
            name = "%s %s" % (e["player"]["first_name"], e["player"]["last_name"])
            team, opp = e.get("team"), e.get("opponent")
            k = kick[name]; k["team"] = team; k["games"] += 1
            k["fga"] += st.get("fga", 0) or 0; k["fgm"] += st.get("fgm", 0) or 0
            k["xpa"] += st.get("xpa", 0) or 0; k["xpm"] += st.get("xpm", 0) or 0
            k["pts"].append(st.get("kick_pts", 0) or 0)
            tw = team_week[(team, w)]
            for key in ("fga", "fgm", "xpa", "xpm"):
                tw[key] += st.get(key, 0) or 0
            oa = opp_allowed[opp]
            if e.get("game_id") not in games_seen[opp]:
                games_seen[opp].add(e.get("game_id")); oa["games"] += 1
            oa["fga"] += st.get("fga", 0) or 0
    team_games = defaultdict(int); team_tot = defaultdict(lambda: {"fga": 0.0, "fgm": 0.0, "xpa": 0.0, "xpm": 0.0})
    for (team, w), tw in team_week.items():
        team_games[team] += 1
        for key in tw:
            team_tot[team][key] += tw[key]
    team_pts_pg = {t: (6.0 * team_tot[t]["xpa"] + team_tot[t]["xpm"] + 3.0 * team_tot[t]["fgm"]) / team_games[t]
                   for t in team_games}
    team_fga_pg = {t: team_tot[t]["fga"] / team_games[t] for t in team_games}
    team_xpa_pg = {t: team_tot[t]["xpa"] / team_games[t] for t in team_games}
    league_fga_pg = sum(team_fga_pg.values()) / len(team_fga_pg) if team_fga_pg else 2.1
    league_pts_pg = sum(team_pts_pg.values()) / len(team_pts_pg) if team_pts_pg else 22.0
    return {"kick": kick, "opp": opp_allowed, "tpp": team_pts_pg,
            "txpa": team_xpa_pg, "league_fga": league_fga_pg, "league_pts": league_pts_pg}


def predict(agg, name, team, opp):
    """v1.1 formulas. Returns None if <2 prior games (live rule)."""
    k = agg["kick"].get(name)
    if not k or k["games"] < 2:
        return None
    lg = agg["league_fga"]
    fga_pg = (k["fga"] + 4.0 * lg) / (k["games"] + 4.0)
    fg_pct = (k["fgm"] + 17.0) / (k["fga"] + 20.0)
    xp_pct = min(0.99, (k["xpm"] + 19.0) / (k["xpa"] + 20.0))
    oa = agg["opp"].get(opp, {"games": 6, "fga": lg * 6})
    opp_pg = oa["fga"] / max(1, oa["games"])
    factor = max(0.85, min(1.20, 1.0 + 0.5 * (opp_pg / lg - 1.0)))
    itt = agg["tpp"].get(team, agg["league_pts"])  # backtest proxy (EnvFactor = 1)
    e_fga = min(3.4, fga_pg * factor)
    lam_fg = e_fga * fg_pct
    e_td_solve = max(0.5, (itt - 3.0 * lam_fg - 0.3) / 6.95)
    e_td = 0.5 * e_td_solve + 0.5 * agg["txpa"].get(team, 2.2)
    lam_xp = e_td * xp_pct
    # stress (live formulas)
    lam_fg_s = e_fga * 0.85 * max(0.70, fg_pct - 0.04)
    lam_xp_s = e_td * 0.90 * xp_pct
    def pts_dist(lf, lx, max_pts=36):
        dist = [0.0] * (max_pts + 1)
        for f in range(13):
            pf = pois(f, lf)
            if pf < 1e-9:
                continue
            for x in range(16):
                p = 3 * f + x
                if p <= max_pts:
                    dist[p] += pf * pois(x, lx)
        return dist
    dist = pts_dist(lam_fg, lam_xp); dist_s = pts_dist(lam_fg_s, lam_xp_s)
    mean_pts = sum(i * p for i, p in enumerate(dist))
    return {
        "mean_pts": mean_pts,
        "p_fg2": 1 - pois(0, lam_fg) - pois(1, lam_fg),
        "p_fg2_stress": 1 - pois(0, lam_fg_s) - pois(1, lam_fg_s),
        "p_pat2": 1 - pois(0, lam_xp) - pois(1, lam_xp),
        "p_kp7": sum(p for i, p in enumerate(dist) if i >= 7),   # over 6.5
        "p_kp7_stress": sum(p for i, p in enumerate(dist_s) if i >= 7),
        "p_kp9": sum(p for i, p in enumerate(dist) if i >= 9),   # over 8.5
        "prior_mean_pts": sum(k["pts"]) / k["games"],
    }


def run(mode):
    """mode='oos' expanding window; mode='insample' all 6 weeks."""
    rows = []
    for t in WEEKS[1:]:
        agg = aggregates(WEEKS if mode == "insample" else [w for w in WEEKS if w < t])
        for e in load_week(t):
            st = e.get("stats") or {}
            if not st.get("gp"):
                continue
            name = "%s %s" % (e["player"]["first_name"], e["player"]["last_name"])
            p = predict(agg, name, e.get("team"), e.get("opponent"))
            if p is None:
                continue
            p.update({"week": t, "player": name, "team": e.get("team"), "opp": e.get("opponent"),
                      "a_fgm": st.get("fgm", 0) or 0, "a_xpm": st.get("xpm", 0) or 0,
                      "a_pts": st.get("kick_pts", 0) or 0})
            rows.append(p)
    return rows


def brier(preds, hits):
    return sum((p - h) ** 2 for p, h in zip(preds, hits)) / len(preds) if preds else None


def summarize(rows, label):
    print("\n=== %s: n=%d kicker-games ===" % (label, len(rows)))
    # mean points
    mp = sum(r["mean_pts"] for r in rows) / len(rows)
    ma = sum(r["a_pts"] for r in rows) / len(rows)
    mae = sum(abs(r["mean_pts"] - r["a_pts"]) for r in rows) / len(rows)
    mae_base = sum(abs(r["prior_mean_pts"] - r["a_pts"]) for r in rows) / len(rows)
    print("mean kick pts: predicted %.2f vs actual %.2f | MAE model %.2f vs naive prior-mean %.2f"
          % (mp, ma, mae, mae_base))
    for key, hitfn, name in [
        ("p_fg2", lambda r: 1 if r["a_fgm"] >= 2 else 0, "FG 2+ (o1.5)"),
        ("p_pat2", lambda r: 1 if r["a_xpm"] >= 2 else 0, "PAT 2+ (o1.5)"),
        ("p_kp7", lambda r: 1 if r["a_pts"] >= 7 else 0, "KP over 6.5"),
        ("p_kp9", lambda r: 1 if r["a_pts"] >= 9 else 0, "KP over 8.5"),
    ]:
        preds = [r[key] for r in rows]; hits = [hitfn(r) for r in rows]
        print("%-16s pred avg %.3f | actual rate %.3f | Brier %.3f"
              % (name, sum(preds) / len(preds), sum(hits) / len(hits), brier(preds, hits)))
    # calibration bins for FG 2+
    print("FG 2+ calibration bins (pred range -> n, actual hit rate):")
    for lo, hi in [(0, .30), (.30, .45), (.45, .60), (.60, .75), (.75, 1.01)]:
        sub = [r for r in rows if lo <= r["p_fg2"] < hi]
        if sub:
            print("  %.2f-%.2f: n=%3d pred %.3f actual %.3f"
                  % (lo, hi, len(sub), sum(r["p_fg2"] for r in sub) / len(sub),
                     sum(1 for r in sub if r["a_fgm"] >= 2) / len(sub)))
    # high-confidence cohorts (the ones that would become picks)
    for cut in (0.65, 0.70):
        sub = [r for r in rows if r["p_fg2"] >= cut]
        if sub:
            print("FG 2+ cohort P>=%.2f: n=%d, hit rate %.3f (breakeven at -120 is .545)"
                  % (cut, len(sub), sum(1 for r in sub if r["a_fgm"] >= 2) / len(sub)))
    sub = [r for r in rows if r["p_kp7"] >= 0.65 and r["p_kp7_stress"] >= 0.55]
    if sub:
        print("KP o6.5 cohort P>=.65 + stress>=.55: n=%d, hit rate %.3f"
              % (len(sub), sum(1 for r in sub if r["a_pts"] >= 7) / len(sub)))
    # per-week
    print("per-week FG2+ (pred avg vs actual rate, n):")
    for t in WEEKS[1:]:
        sub = [r for r in rows if r["week"] == t]
        if sub:
            print("  W%d: n=%d pred %.3f actual %.3f" % (t, len(sub),
                  sum(r["p_fg2"] for r in sub) / len(sub),
                  sum(1 for r in sub if r["a_fgm"] >= 2) / len(sub)))
    return rows


if __name__ == "__main__":
    oos = run("oos"); summarize(oos, "OUT-OF-SAMPLE (expanding window, prior weeks only)")
    ins = run("insample"); summarize(ins, "IN-SAMPLE (all 6 weeks incl. target week -- leakage)")
    json.dump({"oos": oos, "insample": ins},
              open(os.path.join(BASE, "data", "backtest-week2-6.json"), "w"), indent=1)
    print("\nwrote data/backtest-week2-6.json")
