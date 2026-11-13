# NFL Kicker Model — Method

Built 2026-10-24 at Finn's request, in this side chat. Same operating system
as the NBA/NHL daily models: a private append-only ledger, a real model with
a stress test before anything is named, honest lean-vs-bet labels, graded
every week, checkpoints locked before results are known.

## Objective
Each week, screen EVERY NFL kicker prop (kicking points, field goals made,
PATs made + DraftKings alt ladders), lock the top plays in the ledger BEFORE
kickoff, and deliver Finn the top 3 for the week in this chat. Operator
mandate applies (Finn, Oct 10, extended here Oct 24): this is my project —
I decide what clears the bar, I pass weeks that don't, and a "no plays" week
is the system working.

## Markets
- Main: kicking points o/u (primary), field goals made o/u, PATs made o/u.
- **Two-sided, all three markets (Finn, Oct 24, 2026 — confirmed and made
  permanent):** the model prices OVERS and UNDERS in all three markets.
  Simple threshold bets are first-class picks, named the way Finn bets
  them: "2+ FG made" = FG over 1.5, "3+ FG" = over 2.5, "2+ XP made" =
  PAT over 1.5, "under 2 FG" = FG under 1.5, and so on. The weekly top 3
  is chosen across every market and both sides, not from kicking points
  alone. Unders get the mirror-image stress test (scoring inflation:
  E_FGA*1.15, E_TD*1.10, FG% +4pts) and need the same bar: >=6pp edge,
  stress survives, >=2 independent factors. First application (Week 7
  rerun): Pineiro FG under 1.5 cleared everything and was added as an
  addendum pick; several big KP "avoid" reads from the over-only pass
  (Fairbairn, Bates, Pineiro) are under/lean candidates every week, not
  just avoids.
- Alt ladders (DraftKings): kicking points alternate, field goals alternate.
  The alt flag is core to the ask: when a lower rung is priced well below the
  model's probability (e.g. over 5.5 at -170, 63% implied, when the model
  says 77%), flag it as the safer expression of the same play. Aggressive
  rungs (+money) get flagged only when the edge is large AND labeled as
  tail-sensitive (see model flaw below).

## Data (never invented)
- Lines: The Odds API via `fetch_kicker_props.py` — core markets for every
  game (3 credits/game), alt ladders ONLY for screened candidate games
  (~2 credits/game). Snapshots in `hidden_files/odds-snapshots/`.
  Quota discipline: ~45-50 credits/week all-in; the pool is shared.
- Stats: Sleeper's free stats endpoint, weeks 1..n-1 —
  `https://api.sleeper.app/stats/nfl/<season>/<week>?season_type=regular&position[]=K`
  Per-kicker FGA/FGM by distance, XPA/XPM, kick points, long, AND the
  opponent faced that week (drives the opponent-allowed table).
- Game environment: median spread/total across books (Odds API) -> implied
  team total ITT = (total - spread_for_team)/2. Venue (dome / retractable /
  open) and gameday forecast (wind, precip) checked weekly; wind >= 15 mph
  sustained or heavy precip is a downgrade factor, never ignored.
- Splits: books do not publish kicker-prop ticket/handle splits. They are
  NEVER claimed. Every delivered play is therefore capped at Partial tier
  until a verified market signal exists (see tiers).

## Model v1.1 (kicker_model.py)
Per kicker:
1. Shrunk rates: FGA/g shrunk toward the league mean with a 4-game prior
   (v1.1 — v1's raw rates double-stacked form + opponent and produced a
   4.1 FGA expectation for Reichard; that was model theater and it was
   caught in audit before any pick was named). FG% shrunk (fgm+17)/(fga+20);
   XP% shrunk toward 95%.
2. Opponent factor: opponent FGA allowed per game vs league, shrunk 50%
   toward 1.0, capped [0.85, 1.20]. (6-game opponent samples are noisy —
   Green Bay's 0.83 FGA/g allowed is a fact about the sample, not a law.)
3. Environment factor: 0.5 + 0.5*(ITT / team's season points per game),
   capped [0.75, 1.30]. E_FGA = shrunk FGA/g * opp factor * env, hard cap 3.4.
4. TD solve from the ITT identity: ITT ~= 6*TD + 0.95*TD + 3*FGM + 0.3,
   blended 50/50 with the team's season XPA/g scaled by ITT.
5. Distribution: attempts ~ Poisson, makes are thinned Poissons —
   FGM ~ Pois(E_FGA * FG%), XPM ~ Pois(E_TD * XP%); kicking points =
   3*FGM + XPM by exact convolution.
   KNOWN FLAW: FG and XP counts share drive volume (positively correlated),
   so modeled tails are too thin. Guard: the stress test, and alt flags
   only near the main line.
6. Edge = model P(over) - no-vig implied P(over) (same-book pair when
   available; raw implied otherwise, and that limitation is stated).
7. Stress test (pessimistic): E_FGA*0.85, E_TD*0.90, FG% -4pts. A play
   whose stress probability falls below the implied probability is NOT a
   bet, whatever the base edge says.

## The low-total question (Finn's hypothesis, tested on W1-6 2026, n=93 games)
Low-scoring games (<40 combined pts): kickers scored 12.9 pts/game combined,
40.3% of all points. High-scoring games (>=50): 17.8 pts, 27.3% share.
Verdict: the FG SHARE rises sharply in low-total games, but absolute kicking
points still FALL. A low total alone is not an over signal — a low total
with a LOW LINE on a volume kicker whose offense stalls in FG range is.
That profile (not the total itself) is a named factor below.

## Factors (a bet needs >= 2 independent ones + the bar)
- F1 Volume/accuracy: kicker's shrunk FGA/g and FG% both above league; a
  made-50+ history (coach trusts the range -> attempts other teams punt on).
- F2 Opponent allows: opponent FGA / kicking points allowed above league.
- F3 Venue/weather: dome or retractable, or calm outdoor (wind < 10, no
  precip), supporting accuracy and attempt willingness.
- F4 Stall profile: the kicker's offense moves the ball but finishes drives
  with FGs (poor red-zone TD rate, elite opposing red-zone D, or a defense-
  first team identity whose offense is built to cash field position).
- F5 Line gap: model mean clears the line by >= 1.5 points, or the line sits
  a full point below a same-game line at another book (line shopping).

## Bars and tiers (Finn's standing rules, unchanged)
- BET: base edge >= 6pp AND stress P >= implied AND >= 2 independent factors.
- LEAN: anything below that, labeled with its true probability. Never
  dressed up as an edge.
- Evidence tiers per the betting-pick labeling skill: Verified needs a
  verified market signal on top of model + stress; with no prop splits
  published, the ceiling today is Partial (model + stress clear, market
  signal missing — stated on every card).
- Browns rule: **DOES NOT APPLY to this model** (Finn, Oct 24, 2026 —
  lifted explicitly and only for the kicker model: "I will bet with and
  against the Browns here if there is value"). Browns-game kickers are
  screened like everyone else. This exception is scoped to this model
  only; the standing no-Browns rule remains in full force for every
  other card and model. First application: Szmyt (CLE) was blocked in
  the original Week 7 run, unblocked on the lift, and added as Pick 5
  (see picks-log addendum) because he clears the same bar — the lift
  changed his eligibility, not his standards. Slye (TEN, same game)
  still failed the stress test and stayed a lean.
- Bankroll rule applies: the sharpest play of the week gets the weight;
  parlays stay $5 lottery tickets; reminder on every delivery.
- Trap check before delivery: regime change (kicker changed teams — e.g.
  Blake Grupe to LAR in Week 6: no LAR market even exists yet, and his
  "season" would mix two teams), QB/offense changes that flip a team's
  FG:TD mix, unexplained lines (a line far below a kicker's median is the
  market saying something — explain it or pass), game-script correlation.
- Media / coach-intent check — MANDATORY (Finn's rule, Oct 26, 2026):
  before delivery, check recent team news for every game involved:
  beat writers, coach/coordinator press conferences, team media, and
  reputable reporting from the last ~7 days, especially that week's
  comments. Flag stated intent that moves kicking volume — e.g. a
  coach saying he will be more aggressive on 4th down (fewer FG
  attempts), will lean on the run / red-zone offense (more PATs,
  fewer FGs), trusts the kicker from longer range, or plans a
  conservative, field-position game (more FG attempts). Vague praise
  and coach-speak do not count; a flag needs a specific, actionable
  statement, ideally corroborated. If intent runs against a pick, do
  not deliver the old edge unchanged: re-screen, downgrade, or cut it.
  Origin: the Oct 26, 2026 Javonte Williams lesson — a season log was
  delivered as an Under while the team had said that week it wanted to
  get the run game more involved, and the line was cleared in the
  first half. Every delivered pick/lean carries a one-line
  "News/intent check:" note (what was checked, what was found, or
  "nothing material found") and whether it changed the call.

## Penalties per game — MANDATORY, Finn's rule Oct 29, 2026
For every game screened, record penalties per game BOTH ways, for
BOTH teams, from the season log:
- Penalties committed BY each team: penalties/game and penalty
  yards/game, with the split where available (holding, false start,
  DPI, etc.).
- Penalties AGAINST each team: penalties/game and penalty yards/game
  committed by their opponents in games against them — i.e. flags
  drawn, including first downs via penalty.
Use them as a drive-outcome input: penalties that extend drives
(DPI, defensive holding, roughing) create more FG attempts; penalties
that stall drives (offensive holding, false start) or push a team out
of FG range kill attempts; penalties in FG range directly move the
expected FGA count. A material penalty gap can support or counter a
pick and count toward the two-factor bar; a penalty gap alone never
clears it. Every delivered pick/lean carries its penalty numbers in
the research note (by-team and against-team, both teams in the game).

## Backtest status (Oct 24, 2026 — read before trusting any edge)
- `backtest.py` runs an expanding-window out-of-sample test (W3-6,
  121 kicker-games, prior weeks only). Verdict: averages are fine but
  DISCRIMINATION IS WEAK — calibration bins invert in the middle and
  Brier scores are worse than a constant base-rate predictor on all
  four thresholds. In-sample numbers look far better (leakage). Until
  live grading reaches the 25-pick checkpoint, treat every model
  probability as optimistic and every edge as soft. Re-run the
  backtest with real ITTs after each week's actuals land.

## Ledger and grading
- `picks-log.md` is APPEND-ONLY. Picks are locked with timestamp, line,
  book, price, model/stress probabilities, factors, tier — before kickoff.
  Corrections are new appended entries only. "Append-only" is a procedural
  rule, not cryptographic immutability; it is never overstated as such.
- Grading: final kicking lines from Sleeper stats for that week
  (FGM/XPM/kick points), 1u flat at the logged price, W/L/P + units in
  `results.md`; lessons appended to `learning.md`.
- Checkpoints (locked now, before any results): 25 picks = interim
  calibration review, no stakes change. 50 picks = bettable at full
  confidence ONLY if ROI > 0 at flat 1u, calibration is sane (60% buckets
  hitting near 60%), and no single market (e.g. only kicking-points overs)
  carries the record. Otherwise keep researching, no goalpost moves.
- 60-70% bucket marker (Finn, Nov 10, 2026 — formatting only, no bar or
  model change): any pick whose model probability falls in 60-70% is tagged
  ★★ (60–70% bucket, record) in deliveries and grades, so the hot bucket
  stands out. Current: 12-1 (92%) vs ~65% modeled.
- 70%+ marker (Finn, Nov 10, 2026 — same, formatting only): any pick with
  model probability above 70% is tagged ★★★ and gets a one-line callout in
  the delivery as the highest-probability band. Bucket is by the model %
  as recorded in the ledger (one decimal); 70.0% exactly sits in 60-70%
  (Szmyt W7, recorded 70.0%). Current 70%+ bucket record: 1-0 (Elliott W9
  only, n=1 — too small to read anything into it).

## Weekly cadence
- Run: Saturday ~11am ET (cron `nfl-kicker-model-weekly`) — pull lines,
  run the model, trap-check, lock the ledger, deliver top 3 (or an honest
  no-play) in this chat.
- Grade: Tuesday ~10am ET (cron `nfl-kicker-model-grade`) — grade the
  finished week incl. MNF, update results/learning, report the record.
