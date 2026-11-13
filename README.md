# NFL Kicker Prop Model

A transparent, Poisson-thinning model for NFL kicker props — kicking points, field goals made, and PATs made — with a stress test before anything is called an edge.

Built in October 2026. Python standard library only, no paid services required to run the model itself. Odds data needs your own [The Odds API](https://the-odds-api.com/) key; kicker stats come from Sleeper's free stats endpoint.

> **Read this first:** the out-of-sample backtest says the model's averages are fine but its *discrimination is weak* — calibration bins invert in the middle, and Brier scores are worse than a constant base-rate predictor on all four thresholds tested. Treat every model probability as optimistic and every edge as soft until live grading reaches the 25-pick checkpoint. See [METHOD.md](METHOD.md) and `backtest.py` for the full, honest numbers. This is a research tool, not betting advice.

## What it does

For every NFL kicker with a prop market that week, it:

1. **Builds shrunk rates** from Sleeper stats (weeks 1..n-1)
   - FGA/game shrunk toward the league mean with a 4-game prior
   - FG% shrunk as `(FGM + 17) / (FGA + 20)`, XP% shrunk toward 95%
2. **Adjusts for opponent** — opponent FGA allowed per game vs league, shrunk 50% toward 1.0, capped [0.85, 1.20]
3. **Adjusts for game environment** — implied team total (ITT) from median spread/total across books, capped [0.75, 1.30], with a hard cap of 3.4 expected FG attempts
4. **Solves for expected touchdowns** from the ITT identity, blended 50/50 with the team's season XPA/game
5. **Prices the distribution** — attempts ~ Poisson, makes are thinned Poissons (`FGM ~ Pois(E_FGA * FG%)`, `XPM ~ Pois(E_TD * XP%)`), kicking points = `3*FGM + XPM` by exact convolution
6. **Stress-tests every play** (pessimistic: `E_FGA * 0.85`, `E_TD * 0.90`, FG% -4pts) — a play whose stress probability falls below implied probability is not a bet, whatever the base edge says

Edge = model P(over) − no-vig implied P(over), from the same-book over/under pair when available.

Markets screened, both sides: kicking points, field goals made, PATs made, plus DraftKings alt ladders for screened candidates.

## The bar

- **Bet:** base edge ≥ 6pp **and** stress P ≥ implied **and** ≥ 2 independent factors (volume/accuracy, opponent allows, venue/weather, stall profile, line gap)
- **Lean:** anything below that, labeled with its true probability — never dressed up as an edge
- **Evidence tier ceiling:** Partial — no kicker-prop ticket/handle splits are published, so there is no verified market signal to claim

Full method, factors, trap checks, coach-intent check, and penalties-per-game rule: [METHOD.md](METHOD.md).

## Quickstart

```bash
# Python 3.12+, no dependencies to install
python3 -m py_compile kicker_model.py backtest.py

# 1. Set your Odds API key (get one at the-odds-api.com)
export THE_ODDS_API_KEY="your-key-here"

# 2. Pull game lines (spreads/totals, median across books)
python3 fetch_game_lines.py <event-id-1,event-id-2> data/game-lines.json

# 3. Pull kicker props for those events
python3 fetch_kicker_props.py --events <event-id-1,event-id-2>

# 4. Run the model (fetches Sleeper kicker stats for WEEKS in kicker_model.py)
python3 kicker_model.py
# writes data/model-output.json

# 5. Run the honest out-of-sample backtest
python3 backtest.py
```

Data layout the scripts expect (created automatically, gitignored):

```
data/
  sleeper/kstats_2026_w1.json ...   # Sleeper stats, fetched by kicker_model.py
  sleeper/players.json              # Sleeper players file, for name -> team
  game-lines.json                   # from fetch_game_lines.py
  odds-snapshots/<timestamp>-core.json
  model-output.json
```

`kicker_model.py` is set up for Weeks 1–6 → Week 7 as built. To run a later week, update `WEEKS` in `kicker_model.py` and `backtest.py` to the prior weeks, and fetch fresh game lines / props.

## Live grading

- `results.md` — graded record, 1u flat at the logged line and price. As of Week 9, 2026: 14-3-0, +10.29u (17 picks). n=17 — do not read as sustainable. Checkpoints: 25 picks (interim), 50 (bettable gate).
- `picks-log.md` — append-only ledger. Picks are locked with timestamp, line, book, price, model/stress probabilities, factors, and tier — before kickoff. Corrections are new appended entries only.

## Files

| File | What it is |
|---|---|
| `kicker_model.py` | The model. Poisson-thinning, shrunk rates, opponent + environment factors, ITT TD solve, stress test |
| `METHOD.md` | The full method, factors, bars, tiers, backtest verdict, and weekly cadence — the source of truth |
| `backtest.py` | Expanding-window out-of-sample backtest (Weeks 3–6, 121 kicker-games), plus the in-sample leakage comparison |
| `fetch_kicker_props.py` | Pulls kicker props + DK alt ladders from The Odds API v4 |
| `fetch_game_lines.py` | Pulls spreads/totals from The Odds API v4, saves median lines |
| `results.md` | Graded live record |
| `picks-log.md` | Append-only picks ledger |

## Known flaws (stated in the code, not hidden)

- FG and XP counts share drive volume (positively correlated), so modeled tails are too thin. The stress test is the guard; alt flags only near the main line.
- Early-season opponent samples are noisy (6 games). Shrinkage is mandatory.
- No prop splits exist, so the evidence tier ceiling is Partial.
- `kicker_model.py` hardcodes `WEEKS = [1..6]` — see Quickstart for running later weeks.

## Disclaimer

For research and education only. Sports betting involves risk; a model with weak discrimination can lose money even when its averages look right. Nothing here is financial or betting advice.
