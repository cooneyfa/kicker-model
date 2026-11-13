# Kicker Model — Picks Log (APPEND-ONLY)

Locked before kickoff. Never edit an entry; corrections are new entries.
Method: METHOD.md (model v1.1). Grading: results.md.

---

## Week 7 — locked Sat 2026-10-24 01:12 ET (before Sunday kickoffs)

Lines: The Odds API snapshot 2026-10-24T05-02-07Z-core.json (162 credits
remaining after pull); alt ladders 2026-10-24T05-08-20Z-alts.json.
Stats: Sleeper W1-6. Game totals/spreads: median across books via Odds API.
Splits: NOT available for kicker props (books don't publish them) — every
Week 7 play is capped at Partial tier for exactly that reason.
Weather (all games): no wind flag anywhere — sustained winds <=12 mph;
only flags are TB@CAR gusts to 20 and KC@SEA ~44% light rain. No vetoes.
TNF (CHI 30, NE 24) already played before this model existed — not a pick,
not graded. Cairo Santos scored 12 kicking points in it; noted, not counted.

### Pick 1 — BET (Partial tier)
**Matt Gay (LV) — Kicking Points OVER 6.5 @ -109, DraftKings** (LAR @ LV, Sun 4:25pm ET, Allegiant Stadium, indoor)
- No-vig implied 49.3% | Model 69.7% | Edge +20.4pp | Stress 57.5% (clears implied by +8.2pp — the only Week 7 play whose stress clears comfortably)
- Model inputs: E_FGA 2.70, lam_FGM 2.39, lam_XPM 2.14, model mean 9.31 pts. LV implied team total 22.5, game total 48.5.
- Season (W1-6, all LV): 2.5 FGA/g raw, 14 FGM (T-3rd in NFL), 56 pts (3rd), kick pts by week 9/6/11/13/5/12 — median 10, over 6.5 in 4 of 6.
- Factors: F1 volume/accuracy (above-league FGA + makes, long 59), F2 opponent (LAR allows 2.83 FGA/g, highest in this slate's sample; shrunk factor 1.17), F3 venue (dome), F5 line gap (model mean 9.31 vs line 6.5).
- FG market corroboration (same model, correlated — not counted as an independent factor): FG made o1.5 @ -105 DK, model 75.5% vs 48.3% no-vig, +20.6pp... [logged: fg edge_pp 20.6]
- ALT FLAGS (DraftKings ladder): o5.5 @ -170 — implied 63.0%, model 77.0%, +14.1pp (safer expression, Finn's use case). o7.5 @ +140 — implied 41.7%, model 60.7%, +19.1pp (aggressive rung). o9.5 @ +311 flagged in the run but tail-sensitive; not a logged play.
- Trap check: no team change (LV all season), no QB regime change flagged, line is explainable (market prices LV's 22.5 ITT, not Gay's FG-heavy split of it). PASS.

### Pick 2 — BET (Partial tier)
**Will Reichard (MIN) — Kicking Points OVER 8.5 @ -103, DraftKings** (IND @ MIN, Sun 1:00pm ET, U.S. Bank Stadium, indoor)
- No-vig implied 47.8% | Model 63.8% | Edge +16.0pp | Stress 49.9% (clears implied by only +2.1pp — thinnest stress pass on the card; sized accordingly in the delivery)
- Model inputs: E_FGA 3.23 (cap 3.4 not hit), lam_FGM 2.95, lam_XPM 1.95, model mean 10.80 pts. MIN implied team total 24.0, game total 41.5.
- Season (W1-5, MIN on bye W6): 15/15 FG, 34 straight makes dating to 2025, 5 makes from 50+, kick pts 7/9/11/15/11 — over 8.5 in 4 of 5. Scored ALL 15 of MIN's points vs MIA in W4.
- Factors: F1 volume/accuracy (3.0 FGA/g raw, perfect season, elite range), F2 opponent (IND allows 2.67 FGA/g), F3 venue (dome), F4 stall profile (MIN offense 27th in EPA/DVOA, hasn't topped 23 pts in 4 straight; MIN wins with defense + Reichard — the FG mix IS the team identity, not a hot streak).
- PAT market agrees with the profile (model UNDER the 2.5 PAT line, -11.6pp on the over) — the points come from FGs, as priced.
- ALT FLAGS (DraftKings ladder): o7.5 @ -156 — implied 60.9%, model 70.5%, +9.6pp (safer rung). o5.5 @ -406 — implied 80.2%, model 84.2%, only +3.9pp: NOT flagged, juice eats it (logged as a deliberate non-flag).
- Trap check: QB is Kyler Murray all season (no regime change); post-bye Justin Jefferson healthier is the named headwind — it shifts FG->XP mix, which the kicking-points market partly absorbs (XP still count). Line explainable: market is pricing mean reversion on a 5-game sample. PASS with headwind noted.

### Pick 3 — BET (Partial tier)
**Dominic Zvada (NYG) — Kicking Points OVER 5.5 @ -113, BetRivers** (NYG @ HOU, Sun 1:00pm ET, NRG Stadium, retractable roof)
- Raw implied 53.0% (BetRivers lists no under for a pair — no-vig unavailable, edge is overstated by roughly the vig; haircut noted) | Model 67.3% | Edge +14.3pp raw | Stress 55.8% (clears raw implied; vs a no-vig ~51% it clears by ~+4.8pp)
- Model inputs: E_FGA 2.59, lam_FGM 2.16, lam_XPM 1.32, model mean 7.81 pts. NYG implied team total only 16.0 (HOU -10), game total 42.5.
- Season (W1-6, NYG): 2.67 FGA/g raw, kick pts 4/6/12/10/9/7 — over 5.5 in 5 of 6, median 8. Long 56, five makes from 50+ (coach attempts from deep instead of punting — how a bad offense still produces kicking points).
- Factors: F1 volume/range, F2 opponent (HOU allows 2.50 FGA/g), F3 venue (retractable roof), F5 line gap (the line is 5.5 because NYG's ITT is 16 — it prices the offense, not the kicker's share; this is the low-total/low-line profile from the hypothesis test).
- FG market: o1.5 @ +115 BetMGM, model 72.6%... [logged: model_p for 2+ FGM from lam 2.16 = 64.4% by Poisson; the +20.2pp fg edge in the model file is vs the 1.5 line at best price] — the FG over at plus money is the aggressive expression.
- ALT FLAGS (DraftKings ladder): o5.5 @ -115 (same rung, DK price). o7.5 @ +213 — implied 31.9%, model 47.2%, +15.2pp (aggressive rung, tail-sensitive).
- Trap check: the named risk is HOU's pass rush (Will Anderson Jr., 7 sacks) ending drives before FG range — that risk is already inside HOU's allowed-FGA number (2.50/g happened against this same defense). Rookie kicker variance noted. PASS.

### Blocked by standing ban
- **Andre Szmyt (CLE) o6.5 (+15.3pp, stress clears) and Joey Slye (TEN) o6.5 (+7.6pp)** — CLE @ TEN. Slye scores AGAINST Cleveland: blocked by the no-Browns rule. Szmyt is Cleveland's own kicker; the model ranks him #3, but I am not stretching the ban's wording on Finn's behalf. Both stay in the log as BLOCKED, ungraded as plays, unless Finn lifts the ban for his own team's kicker.

### Screened and passed (logged for calibration, NOT plays, not graded as Finn's record)
- Spencer Shrader (IND) o6.5 +8.6pp — stress FAILS (42.1% < 45.3% implied). MIN allows the fewest points in the league (12.8/g) and a 25% opponent red-zone TD rate cuts both ways; the duel narrative isn't a factor.
- Chad Ryland (ARI) o6.5 +10.8pp — stress FAILS (48.9% < 50.4%).
- Jason Sanders (NYJ) o6.5 +9.1pp — stress FAILS (50.5% < 53.7%).
- Ka'imi Fairbairn (HOU) — model says the DK o9.5 is the worst over on the board (-13.3pp; every DK alt rung negative). His name + HOU's 26.5 ITT make him the popular pick; the model fades the over. Not a delivered under (v1 is over-only); logged as an avoid.
- Jake Bates (DET) o7.5 -11.8pp — highest ITT on the slate (28.2) but DET finishes with TDs (77.3% red-zone TD rate) and GB has allowed 0.83 FGA/g. Fantasy rank #1 (DraftSharks 8.7 proj) is not a betting edge at this line. Avoid the over.
- Eddy Pineiro (SF) o8.5 -14.7pp — SF's 87.5% red-zone TD rate (best in NFL) is exactly why his FG volume is 1.5/g. Avoid the over.
- Blake Grupe (LAR) — no market posted at any book in the pull (signed Oct 13 off the Jets' practice squad). Regime change; unmodelable this week.
- MIA and NYJ's second kicker slots: only Jason Sanders (NYJ) had a market in the MIA@NYJ game; MIA's kicker had no line in the pull. No line, no play.

### Correction — appended Sat 2026-10-24 01:16 ET (same lock, pre-kickoff, pre-delivery)
Two FG-corroboration lines in the entries above were transcribed from the
superseded v1 run. Correct v1.1 figures (model-week7-v1.json, final):
- Gay FG o1.5 @ -105 DK: model 69.0% vs no-vig 48.3%, +20.6pp (not 75.5%).
- Zvada FG o1.5 @ +115 BetMGM: model 63.6% vs no-vig 43.4%, +20.2pp
  (not 72.6%). The bracketed hand-calc in his entry (64.4%) was also off;
  63.6% is the model figure.
- Reichard FG o1.5 @ -190 BetMGM (for the record): model 79.4% vs no-vig
  61.1%, +18.2pp.
All kicking-points lines, prices, edges, and stress figures in the three
pick entries are the v1.1 figures and stand as written.

---

## Week 7 ADDENDUM — two-sided rerun, locked Sat 2026-10-24 01:27 ET

Trigger: Finn confirmed he can bet all three markets (kicking points, FG
made, PATs made) on BOTH sides, including simple thresholds (2+ FG, 2+ XP).
The original Week 7 run was over-only on kicking points. This rerun uses
the same v1.1 lambdas and the same 05:02Z odds snapshot (two-sided file:
hidden_files/two-sided-week7.json). The three locked picks above STAND as
delivered — append-only means no retro-swapping. What the wider scope adds:

### Pick 4 — BET (Partial tier) [addendum, from the expanded scope]
**Eddy Pineiro (SF) — Field Goals UNDER 1.5 (i.e. 0 or 1 FG made) @ +115, BetMGM** (SF @ ATL, Sun 1:00pm ET, Mercedes-Benz Stadium, retractable/indoor)
- No-vig implied (under) 43.4% | Model 60.9% | Edge +17.6pp | Under-stress (scoring inflation) 51.6% — clears implied by +8.2pp, a wider stress margin than Picks 2 and 3.
- Why: SF owns the NFL's best red-zone TD rate, 87.5% (season to Oct 13) — the 49ers finish drives with touchdowns, which is why Pineiro's attempt volume is 1.5 FGA/g despite SF's 26.0 implied team total, and why the model simultaneously likes his PAT over (TDs yes, FGs no). His shrunk FG% (79.3%) is also the lowest among full-time starters in the pull.
- Factors: F4-inverted (elite RZ finishing = anti-stall profile), F1-inverted (lowest attempt volume among starters), venue neutral-positive (indoor removes weather variance both ways).
- Named headwind: ATL allows 2.17 FGA/g (above league) and a 49.5 game total means SF will have drives. The bet is that they end in the end zone. Disclosed, priced in the stress.
- Note: this is the same read the over-only pass logged as "Pineiro o8.5 -14.7pp, avoid the over." The under was the actual play; the expanded scope found it.

### Expression note on Pick 3 (not a new pick)
Zvada FG over 1.5 (2+ FG) @ +115 BetMGM — model 63.6%, edge +20.2pp,
stress 52.1% — is a stronger-priced expression of the same thesis as his
locked KP over 5.5 @ -113. Pick 3 remains graded as locked (KP o5.5);
the FG line is logged here so the choice Finn makes at the window is on
record as model-backed either way.

### Two-sided leans (NOT picks — logged with true numbers)
- Ka'imi Fairbairn (HOU) KP UNDER 9.5 @ -126 DK: model 65.8%, +13.3pp, under-stress 54.4% vs ~52.6% implied — clears by only +1.8pp, and it shares a game with Pick 3. Lean.
- Jake Elliott (PHI) FG UNDER 1.5 @ -114 DK: model 65.2%, +14.9pp, stress clears by ~+6.5pp. PHI's 0.83 FGA/g is the league's lowest. Held to a lean only because Pick 4 took the addendum slot with the bigger edge + stress margin; Elliott's PAT OVER 1.5 @ -137 (model 67.1%, +12.7pp) is the same PHI thesis (TDs, no FGs) from the other market. MNF — revisit next week if the profile holds.
- Will Reichard PAT UNDER 2.5 @ -160 BetMGM: model 69.0%, +11.5pp, stress 63.5%. Same thesis as Pick 2 (MIN points come from FGs), not an independent pick — noted so a Reichard KP+PAT-under pairing is understood as one bet on one script, not diversification.

### 2+ FG made board (Week 7, model P, for the record)
Reichard 79.3% (stress 69.2) · Szmyt 70.0% [BLOCKED — Browns game] · Gay 68.9% (57.8) · Boswell 63.8% · Zvada 63.6% (52.1) · Fitzgerald 63.6% · Sanders 63.3% · Ryland 63.1% · Shrader 58.0% (47.1 stress — the duel's other leg is the weakest of the volume names).
Finn's three-leg 2+ FG parlay (his message, Oct 24): if the legs are Gay + Reichard + Zvada, model joint = 34.7% (stress joint 20.8%) vs ~15.6% joint raw implied at the logged prices (-105 / -190 / +115). All three legs individually clear the model's bar — no padded leg.

---

## Week 7 ADDENDUM 2 — Browns rule lifted for this model, locked Sat 2026-10-24 01:33 ET

Finn's direction (Oct 24, 2026): the no-Browns rule is OUT for the kicker
model only — he will bet with and against Cleveland here when there is
value. The rule stands everywhere else. Games have not kicked off; this is
an eligibility change, not a retroactive edit. The "Blocked by standing
ban" entry above stays in the log as the record of how the week started.

### Pick 5 — BET (Partial tier) [unblocked, from the original screen]
**Andre Szmyt (CLE) — Field Goals OVER 1.5 (2+ FG made) @ -120, BetMGM** (CLE @ TEN, Sun 1:00pm ET, Nissan Stadium — 72F, calm, sunny)
- No-vig implied 51.0% | Model 70.0% | Edge +19.0pp | Stress 58.9% (clears implied by +7.9pp)
- Model inputs: lam_FGM 2.44, E_FGA 2.78. Season (W1-6, CLE): kicking pts 4/11/7/9/6/7, median 7.
- Factors: F2 opponent (TEN has allowed 2.83 FGA/g, tied for the most generous in the sample; shrunk factor 1.17), F4 stall profile (lowest total on the board, 36.5; CLE implied team total 19.8 — the Browns win with defense while the offense stalls, which is the low-total/low-line FG profile from the hypothesis test), F3 venue (calm, warm, outdoor — no weather tax).
- Alternative expression: KP over 6.5 @ -121 DraftKings — model 67.0%, +15.3pp, stress 54.6%. The FG line is the stronger of the two (bigger edge, wider stress margin) and is the graded pick.
- Board note: Szmyt's 70.0% P(2+ FG) is #2 on the slate behind Reichard — he is a straight swap candidate for any 2+ FG parlay leg.
- Trap check: no kicker/QB regime change for CLE; the line is explainable (market prices the 36.5 total, not TEN's FGA generosity or CLE's FG-heavy scoring split). PASS.

### Still NOT a pick, ban or no ban
- Joey Slye (TEN) — KP o6.5 (+7.6pp) and FG o1.5 (+10.0pp, model 61.0%) both FAIL the stress test (KP stress ~44%, FG stress 49.8% vs 51.0% implied). The lift made him eligible; the bar kept him a lean. Logged to prove the lift didn't lower standards.

---

## Backtest note — Sat 2026-10-24 10:55 ET (does NOT change Week 7 locks)
Finn asked whether the model had ever been backtested on pre-kickoff
predictions. It had not — Week 7 was built in-sample. A real
expanding-window backtest (W3-6, 121 kicker-games, prior weeks only)
now exists in backtest.py. Headline: overall averages calibrate, but
discrimination is weak — Brier worse than a base-rate predictor on all
four thresholds, and the middle calibration bins invert. In-sample
looks far better, which is the leakage gap. Week 7's five plays stand
as locked and will be graded Tuesday, but their model probabilities
(69-70%) and +15-20pp edges should be read as optimistic until live
grading says otherwise. Full write-up in learning.md.

---

## Week 7 INTERIM GRADES — Sun 2026-10-25 17:26 ET (four 1pm games final)
Source: Sleeper Week 7 kicker stats (kstats_2026_w7.json). 1u flat at
logged prices. Gay NOT graded: LAR@LV kicked off 4:25pm ET and is still
in progress at 17:26 ET — his current Sleeper line (1 FGM, 3 pts) is a
live partial and must not be read as a result.
- Pick 1 Gay KP o6.5 -109 DK: PENDING (live partial 3 pts, game in progress).
- Pick 2 Reichard KP o8.5 -103 DK: WIN — 3 FGM, 1 XPM, 10 pts (>= 9). +0.97u.
- Pick 3 Zvada KP o5.5 -113 BetRivers: LOSS — 0 FGM, 3 XPM, 3 pts (< 6). -1.00u.
- Pick 4 Pineiro FG u1.5 +115 BetMGM: WIN — 0 FGM (2 XPM, 2 pts). +1.15u.
- Pick 5 Szmyt FG o1.5 -120 BetMGM: WIN — 2 FGM, 3 XPM, 9 pts. +0.83u.
Interim: 3-1, +1.95u. Final grade (incl. Gay) due Tue Oct 27 cron.
Note for Finn's parlays (legs unconfirmed, graded conditionally): the
Zvada 0-FG game kills any Gay/Reichard/Zvada 2+ FG parlay regardless of
the Gay result — both the Oct 24 ticket (if those were the legs) and
the DK bonus-bet parlay (if placed) are already lost on the Zvada leg.

---

## Week 7 LATE ADD — Sun 2026-10-25 ~20:05 ET (KC @ SEA, SNF, kicks 20:20 ET)
Finn asked for the single best kicking play tonight, alt-down to -200
allowed. Fresh DK alt pull 23:59Z (quota 119 left). Every alt OVER for
both kickers graded NEGATIVE edge — alting down does not create a play
tonight. The best play is a main-line under, not an alt.

### Pick 6 — BET (Partial tier, thin pass)
**Harrison Butker (KC) — Field Goals UNDER 1.5 @ +109, DraftKings**
(KC @ SEA, Lumen Field — outdoor, light-rain risk, wind ~3 mph, no veto)
- No-vig implied 45.1% (pair: over -140 / under +109, DK) | Model under
  57.5% | Edge +12.4pp | Under-stress 47.9% (scoring-inflation stress:
  E_FGA*1.15, E_TD*1.10, FG%+0.04) — clears implied by +2.8pp.
- Model inputs: lam_FGM 1.45, E_FGA 1.77, KC ITT 19.8.
- Factors: (1) Butker's FG expectation (1.45) sits well below 2 — KC's
  offense finishes drives with TDs or stalls out of range rather than
  settling for FGs; (2) KC's 19.8 implied total is the lower of the two
  teams tonight, capping FG chances. Weather is neutral-to-slightly
  favorable (light rain, negligible wind) but is NOT counted as a factor.
- Same-thesis alternative (NOT a second bet): Butker PAT OVER 1.5
  @ -131 DK — model 61.3%, +7.8pp, stress 54.7% vs 53.5% (+1.2pp).
  TD-heavy game wins both legs, so taking both is one thesis twice.
- Caution (backtest, Oct 24): model probabilities read optimistic;
  this is a thin pass — size down accordingly. Graded Tue Oct 27 with
  the rest of Week 7.

---

## Pick 6 REDO — defense research (Finn's challenge, Sun 2026-10-25 ~20:10 ET)
Finn correctly flagged that the original Pick 6 delivery never showed
the Seattle defensive work — it cited the model's opponent factor
(0.86) without the numbers behind it. Redone below, pre-kickoff.
- SEA allows 1.5 FGA/game (9 attempts in 6 games; 6.0 kicker pts/game
  allowed) vs league 2.1 — the model's factor 0.86, now evidenced.
- SEA red-zone defense: opponents convert 78.6% of RZ trips to TDs
  (SI, after Week 6; 66.7% through Week 4 per Hawkblogger — trend
  worsening), and SEA has allowed 7-of-7 fourth downs. Mechanism for
  the low FGA number: teams that reach scoring range against Seattle
  score TDs or convert fourth downs instead of kicking.
- KC counterweight (honest headwind): KC reaches the red zone 4.6
  times/game (23 trips in 5 games) but converts only 57% — trip volume
  gives Butker chances even against a bad RZ defense. Butker's own log:
  2+ FG in 2 of 5 games (W2: 4, W6: 3; W1/W3/W4: 1 each), median 1 FG.
- VERDICT UNCHANGED: Butker FG UNDER 1.5 +109 stands. The defense
  research corroborates the model's factor (independent mechanism, same
  direction) but does NOT add edge on top of it — the 1.5 allowed is
  already priced into lam_FGM 1.45. Stress margin stays +2.8pp; thin
  pass, size down. Process fix logged in learning.md: every future
  kicker delivery carries an opponent-defense box (FGA allowed/g, RZ
  TD allowed, trend) — no more factor-without-evidence.

---

## Week 7 FINAL GRADES — Mon 2026-10-26 11:02 ET (Sleeper W7 final stats)
1u flat at logged prices.
- Pick 1 Gay KP o6.5 -109 DK: WIN — 3 FGM, 0 XPM, 9 pts (>= 7). +0.92u.
- Pick 2 Reichard KP o8.5 -103 DK: WIN — 3 FGM, 1 XPM, 10 pts. +0.97u.
- Pick 3 Zvada KP o5.5 -113 BetRivers: LOSS — 0 FGM, 3 XPM, 3 pts. -1.00u.
- Pick 4 Pineiro FG u1.5 +115 BetMGM: WIN — 0 FGM. +1.15u.
- Pick 5 Szmyt FG o1.5 -120 BetMGM: WIN — 2 FGM. +0.83u.
- Pick 6 Butker FG u1.5 +109 DK: WIN — 1 FGM, 3 pts. +1.15u.
WEEK 7 FINAL: 5-1, +5.02u. Model record: 5-1, +5.02u (6 graded picks).

## Week 7 Pick 7 (MNF late add) — Mon 2026-10-26 11:05 ET, DAL @ PHI 8:15pm ET
Fresh DK core pull 15:03Z (quota 115 left). Model lambdas unchanged
from Week 7 (MNF is still Week 7). Venue: Lincoln Financial, outdoor —
tonight clear, ~61F at kickoff, wind W ~5 mph, rain ~2%: no veto.
Both kickers on the listed rosters, no injury news found; re-check
inactives ~6:45pm ET before placing.

### Pick 7 — BET (Partial tier)
**Jake Elliott (PHI) — Field Goals UNDER 1.5 @ -106, DraftKings**
- No-vig implied 48.6% (pair: over -120 / under -106, DK) | Model under
  65.2% | Edge +16.6pp | Under-stress 56.8% (scoring-inflation stress)
  — clears implied by +8.2pp, the widest stress margin of the week.
- Model inputs: lam_FGM 1.23, E_FGA 1.39, PHI ITT ~20.0.
- Opponent-defense box (DAL): allows 2.0 FGA/g (league ~2.1, neutral)
  but 8.5 kicker pts/g — a bottom-tier defense (2nd-worst EPA/play
  allowed) that gives up TDs, i.e. XPs, not FG attempts. Neutral-to-
  favorable for the under.
- Offense profile (PHI, the real driver): team FGA/g 0.83 — league-low
  (5 attempts in 6 games); Elliott 2+ FG in only 1 of 6 weeks, 2+ XP in
  5 of 6; PHI RZ TD rate 69% (Sharp, 16 trips). When PHI scores, it
  scores TDs.
- Offense counterweight / regime flag (named, not hidden): tonight's
  PHI offense is not the one that built the 0.83 number — McKee at QB
  with Smith/Wicks ruled out, a patched OL (Lane Johnson retired,
  Dickerson IR-questionable), Barkley returning from a hamstring
  issue, run game held to <=35 yards in back-to-back games. A stalling
  offense could settle for MORE FGs than the season profile implies.
  The pick stands because the edge (+16.6pp) and stress margin
  (+8.2pp) are the week's widest and Elliott has attempted <=1 FG in
  5 of 6 weeks, but this flag is the reason it is not sized up.
- Same-thesis alternative (NOT a second bet): Elliott PAT OVER 1.5
  @ -132 DK — model 67.1%, +13.6pp, stress 61.5% vs 53.6% (+7.9pp).
  TD-heavy PHI script wins both legs; take one.
- Aubrey passes: KP o7.5 -3.1pp, FG o1.5 -5.3pp; PAT o2.5 +128 shows
  +7.0pp but stress clears by only +0.2pp — noise, not a bet.
- Backtest caution still applies (Oct 24): model probabilities read
  optimistic until the 25-pick checkpoint. Grades Tue Oct 27 with
  Week 8 setup.

---

## Pick 7 DEEP-RESEARCH ADDENDUM — Mon 2026-10-26 11:10 ET (Finn's McKee worry)
Finn asked: how many FGs did Philly kick last week, and what do the
injuries really do to tonight? Full research below. VERDICT: UNCHANGED
— Elliott FG UNDER 1.5 -106 stands at 1u. Reasoning, not reassurance:

Last week, direct answer: ZERO. In McKee's first start (W6 vs CAR),
Elliott attempted 0 field goals (2 XP, 2 pts). Week before (W5 London
vs JAX): 1 attempt, 1 make. Season: 2+ FG in only 1 of 6 weeks.

What McKee's start actually looked like (not the feared pattern):
- 26/45, 215 yds, 1 TD, 0 INT (4.8 YPA); team 222 total yards, 35 rushing.
- 11 possessions, 8 punts, five 3-and-outs; sacked 3x, hit 11x; six of
  the first 18 plays lost yards (sacks, false starts, holding, bad snap).
- The two sustained drives BOTH ended in touchdowns (2/2 red zone).
  The stalls happened EARLY (own territory, midfield) via negative
  plays — producing punts, not FG-range stalls. That is the opposite
  of the feared mechanism, and it is the only McKee-start sample we have.

Tonight's injury picture (all verified pre-kickoff):
- Hurts: OUT FOR THE SEASON — blood clots in lungs (discovered before
  W6); McKee is the QB for the season, not a one-week fill-in. Offense
  ranks No. 28 in scoring, 14.5 ppg during the 4-game skid.
- Smith (hamstring) + Wicks (ankle): RULED OUT (Schefter Oct 24 +
  Saturday report). One outlet headline suggested a Smith return;
  the Schefter/Saturday-report line (out) is the trusted one.
- Barkley: questionable, missed the last two games (hamstring); 5.1
  YPC on 36 attempts, 0 rushing TDs this year. RBs Bigsby + Shipley on IR.
- OL: Lane Johnson retired Oct 6; Dickerson (knee/pectoral) kept on IR
  / questionable; W6 started Lampkin at LG + Majors at C. Goedert is
  the one clean positive (no designation, full practice Saturday).
- Replacements: rookie Makai Lemon (0.64 yards/route run, 84th of 87)
  + Darius Cooper (8 rec, 139 yds, 4 TDs — 50% of his catches are TDs).

How each piece moves the under:
- FOR the under: McKee stalls produce punts (W6 evidence); PHI scores
  14.5 ppg in the skid (fewer chances of every kind); DAL's red-zone
  defense allows TDs on 66.7% of trips (30th) + 2nd-worst EPA/play
  allowed — sustained PHI drives disproportionately end in TDs, and
  DAL allows only 2.0 FGA/g anyway. Note the under needs 2+ MAKES to
  lose — missed FGs do not hurt it.
- AGAINST the under (the real risk, named): DAL's terrible defense
  could let McKee sustain MORE drives than CAR did, and a gutted WR
  room + patched OL could stall some of them in FG range rather than
  the red zone. That is the kill scenario. It is not what happened in
  McKee's only start, and it is not what PHI's season pattern shows
  (0.83 FGA/g), but it is plausible enough that the pick stays 1u
  and is NOT sized up.
- Barkley note for inactives (~6:45pm ET): if he sits, fewer sustained
  drives — mildly good for the under. If he plays, he sustains drives
  but finishes them as TDs vs this DAL RZ defense — roughly neutral.
  Either way the pick stands; only an Elliott injury scratch would
  void it.

---

## Pick 7 DALLAS-SPECIFIC STRESS — Mon 2026-10-26 ~15:00 ET (Finn's question)
Finn asked whether the under had been stress-tested against the
Cowboys defense specifically. Honest answer: NO — the stress run
before was generic scoring inflation (E_FGA x1.15, FG% +0.04), and
the base case only included Dallas through the neutral opponent
factor (0.98, from DAL's 2.0 FGA/g allowed). Dallas-specific ladder
below, all vs 48.6% no-vig implied, from Sleeper W1-6 DAL game log
(FGA allowed by week: 0, 3, 2, 3, 1, 3 — mean 2.0, max 3, last two
avg 2.0, i.e. no recent deterioration):
- Base: 65.1% (+16.5pp)
- Generic stress: 56.8% (+8.2pp)
- Dallas at model factor cap 1.20 (its worst game, 3 allowed, maps
  to 1.21 -> capped): 55.5% (+6.9pp)
- Dallas cap + Elliott FG% .92: 53.2% (+4.6pp)
- Dallas cap + PHI scores 24 (McKee overperforms vs weak DAL D):
  50.3% (+1.7pp)
- TRIPLE worst (cap + 24 pts + .92): 48.0% (-0.6pp) — the only failure.
Note: DAL's 66.7% RZ TD allowed works FOR the under (drives become
TDs, not FGs); the Dallas risk stressed here is purely FG-attempt
volume. And DAL's 8.5 kicker pts/g allowed is XP-driven (TDs allowed),
not FG-driven. VERDICT UNCHANGED at 1u: the under survives every
single Dallas adverse shift and every pair, failing only if all three
worst cases hit at once. The backtest's general discrimination warning
still stands on top of this — this ladder tests Dallas, not everything.

---

## Week 7 PICK 7 GRADE — Tue 2026-10-27 10:49 ET (Sleeper W7 final stats + cross-check)
Source: Sleeper Week 7 kicker stats (Jake Elliott, PHI, vs DAL, 2026-10-26): no FGA/FGM fields, 3 XPA, 3 XPM, 3 kick pts. Cross-checked against the Philadelphia Eagles official game log (WK 7 vs Cowboys: FG ATT 0, FGM 0, XP 3/3) and the Sportradar box-score kicking table (Elliott FG —, XP 3/3) — both agree: 0 field goals.
- Pick 7 Elliott FG UNDER 1.5 @ -106 DK: WIN — 0 FGM (< 2). +0.94u (100/106).
- The McKee-stall mechanism held exactly as researched: PHI scored 3 TDs (21 pts), attempted 0 FGs, and Elliott's only points were 3 XPs. The feared kill scenario (gutted WR room + patched OL stalling in FG range vs a weak DAL defense) did not materialize; the Dallas-specific triple-worst case (cap + 24 pts + .92 FG%) was not approached.

## Week 7 CORRECTED FINAL — Tue 2026-10-27 10:49 ET (arithmetic correction, NOT a re-grade)
The Mon Oct 26 "Week 7 FINAL GRADES" entry overstated the week. Recomputed 1u flat at logged prices:
- Gay o6.5 -109: +0.92u | Reichard o8.5 -103: +0.97u | Zvada o5.5 -113: -1.00u | Pineiro u1.5 +115: +1.15u | Szmyt o1.5 -120: +0.83u | Butker u1.5 +109: +1.09u (NOT +1.15u as logged Mon — +109 pays 1.09, not 1.15) | Elliott u1.5 -106: +0.94u.
- Wins sum +5.91u, minus the Zvada loss = WEEK 7 FINAL: 6-1, +4.91u. The Mon entry's +5.02u summed the wins (with the Butker price error) and omitted the -1.00u Zvada loss entirely. Individual W/L calls were all correct; only the total was wrong. Corrected running record: 6-1-0, +4.91u (7 graded picks). Checkpoints: 25-pick interim and 50-pick bettable gate NOT reached — no stakes change, no bar change.

---

## Week 8 TNF EARLY PICK — Thu 2026-10-29 ~17:40 ET (CAR @ GB, 8:15pm ET)
Price source: DraftKings direct read ~17:35 ET (Odds API returned 401 all
day — feed down; see feed note below). This is an EARLY pick, not part
of Saturday's Week 8 top 3; it grades Tue Nov 3 with the rest of Week 8.
### BET: Ryan Fitzgerald (CAR) FG UNDER 1.5 @ -103 DraftKings — 1u flat
- Model: under 58.8% vs 47.9% no-vig implied, edge +10.9pp.
  Under-stress 49.6% clears by +1.7pp (THIN margin — sized 1u flat,
  explicitly NOT sized up). Tier Partial (no kicker-prop splits exist).
- Model inputs: CAR ITT 22.0 (GB -3.5, total 47.5); Fitzgerald 6g,
  11 FGA / 11 FGM / 17 XPA / 12 XPM; shrunk fga/g 1.94, fg% .903,
  lam_fg 1.41, lam_xp 2.12, mean 6.36 pts.
- Factors: (1) GB defense allows 1.00 FGA/g (by week 1,1,2,0,1,0,2) —
  stingiest in the sample, model factor at the 0.85 floor; GB allows
  only 4.7 kicker pts/g. (2) CAR's total tonight (22.0) sits below its
  24.5 pts/g season scoring, and Fitzgerald's attempt volume is low
  (11 FGA in 6 games). (3) CAR's scoring shape is TD-heavy: 17 XPA vs
  11 FGA — when CAR scores, it is more often 7 than 3.
- Defense box + counterweights: GB's stinginess is the factor, but
  Fitzgerald is 11/11 on FGs (perfect accuracy converts attempts at a
  high rate), CAR's patched OL (LG Damien Lewis OUT) could stall drives
  into FG range, and this is a 6-game sample. The 1.7pp stress margin
  is the thinnest of any delivered pick so far.
- News/intent check: Fitzgerald (illness Tue) practiced fully Wed and
  carries NO game designation — active. No coach statement on kicking
  usage found for either team. CAR outs: Lewis, Phillips, Evans,
  Simpkins. GB outs: Rhyan, Glover, Franklin; Golden/Wyatt
  questionable. Inactives land ~6:45pm ET — re-check before placing.
- Weather: Lambeau clear, ~52F at kickoff, wind WNW ~7 mph, no precip
  — no veto.
### Screened and FAILED tonight (not plays)
- Smack FG OVER 1.5 -106: edge +7.4pp but over-stress 44.4% vs 48.4%
  no-vig — FAILS stress by 4.1pp (his 11/16 accuracy is the drag).
- Smack KP OVER 7.5 +102: edge +5.3pp, over-stress 39.0% — fails bar
  AND stress.
- Fitzgerald KP UNDER 6.5 +107: edge +10.4pp but under-stress 45.0%
  vs 45.5% no-vig — FAILS stress by 0.5pp (noise margin, still a fail).
- Fitzgerald PAT OVER 1.5 -184: edge +1.9pp — fails bar.
- Smack PAT UNDER 2.5 -108: edge +4.0pp — fails bar.
### Feed note
The Odds API key returned 401 Unauthorized on every call Thu Oct 29
(core props + game lines). Saturday's Week 8 run is blocked on the same
feed unless the key is replaced (free second key, same fix as the steam
study) — Finn has not yet answered the secure-card offer.

Feed update Thu Oct 29 ~17:51 ET: replacement Odds API key submitted
and VERIFIED — free events call returned 200, quota 500 remaining / 0
used, all 14 Week 8 events visible. Saturday's Week 8 run is unblocked;
the 401 outage above is resolved. Tonight's Fitzgerald pick stands as
logged from the DraftKings direct read (price unchanged by this fix).

Re-run confirmation Thu Oct 29 ~17:52 ET (Finn asked "are we 100%
good?"): fresh Odds API pull (new key) independently confirmed the
TNF screen. Total median moved 47.5 -> 46.75 (ITT GB 25.1, CAR 21.6);
Fitzgerald FG UNDER 1.5 still -103 at DraftKings in the fresh pull.
Recomputed: model under 59.1% vs 48.4% no-vig, edge +10.7pp (was
+10.9pp); under-stress 49.8% clears by +1.4pp (was +1.7pp). PICK
CONFIRMED at the logged price. Other lines unchanged in verdict:
Fitz KP u6.5 still fails stress (-0.3pp), Smack FG o1.5 still fails
stress (-4.4pp), Smack KP o7.5 fails bar and stress. Quota after
re-run: 495 remaining. Inactives (~6:45pm ET) still the one open item.

---

## Week 8 WEEKEND — locked Sat 2026-10-31 ~11:55 ET (before Sunday 1pm ET kickoffs)

Scope: the 13 remaining Week 8 games (Sun Nov 1 + MNF Nov 2, CHI@SEA).
Week 8 TNF (CAR@GB, Oct 29) already played and already has its own early
pick (Fitzgerald FG UNDER 1.5 -103, logged Thu Oct 29) — it is NOT part
of this top 3 and is NOT re-picked here. Week 9 TNF (Nov 6) is out of
scope for this run.
Lines: Odds API core snapshot 2026-10-31T15-50-27Z-core.json (quota 273
remaining after the 13-game pull; 265 after alt ladders), game lines
(median spread/total) in hidden_files/game-lines-week8.json — identical
to the Oct 30 early lines except PHI@WAS spread 5.75 -> 5.5 (ITT 17.4 ->
17.5, immaterial). Alt ladders: 2026-10-31T15-51-17Z-alts.json (4 games).
Stats: Sleeper W1-7. W8 partial (TNF only) deliberately NOT folded into
season aggregates — CAR/GB would carry 8 games against everyone else's 7.
Model: v1.1 formulas via the weekend_screen adaptation (W1-7), NOT
kicker_model.py as written — that script hardcodes WEEKS=[1..6] and reads
the old full-format game-lines.json, so running it verbatim would have
silently dropped Week 7. Same shrinkage, caps, and stress tests as METHOD.
Splits: NOT available for kicker props — every Week 8 play is Partial tier.
Screen: 18 rows passed edge >=6pp + stress survives (week8-saturday-screen.json).

### Data correction found in audit (disclosed, not hidden)
The W7 Sleeper file predates MNF DAL@PHI (no DAL/PHI/WAS/JAX entries).
That leaves DAL's opponent-FGA table at 12 FGA over 6 games (2.00/g)
instead of 12 over 7 (1.71/g, adding Elliott's verified 0 FGA in W7).
Ryland's numbers below are the CORRECTED ones (factor 0.91, not 0.98):
model 63.1% (was 66.9%), edge +16.6pp (was +20.9pp on the screen's
mixed-book no-vig; +20.5pp on the same-book pair), stress 51.8%
(+5.3pp margin). The pick still clears the bar; it drops from #1 on the
screen to #3 on corrected edge. Szmyt and Dicker are unaffected (PIT
W7 vs NO and LAR W7 vs LV are both in the W7 file). The screen's printed
no-vig for Szmyt/Ryland FG also mixed books (best over vs first under);
locked figures below use the SAME-BOOK pair per METHOD (Szmyt 45.2%,
Ryland 46.5%) — both slightly better than the screen printed.

### Pick 1 — BET (Partial tier) ★ STRONGEST PLAY ON THE CARD
**Andre Szmyt (CLE) — Field Goals OVER 1.5 (2+ FG made) @ +105, BetMGM**
(CLE @ PIT, Sun 1:00pm ET, Acrisure Stadium, outdoor)
- Same-book no-vig implied 45.2% (pair: over +105 / under -145, BetMGM) |
  Model 66.9% | Edge +21.7pp | Stress 55.6% (clears implied by +10.4pp —
  the widest stress margin on the card)
- Model inputs: lam_FGM 2.30, lam_XPM 1.54, model mean 8.44 pts.
  CLE implied team total 18.0, game total 39.5.
- Season (W1-7, CLE): 16 FGA / 14 FGM / 12 XPA / 11 XPM; kick pts by week
  4/11/7/9/6/7/9 — 2+ FG in 6 of 7 weeks (only W1 vs JAX, 1 FGA, missed).
  Made the 56-yard game-winner vs PIT in Week 4 and a 32-yarder on the
  final play at TEN in Week 7.
- Factors: F1 volume/accuracy (2.29 FGA/g, 87.5% raw, long 56 — coach
  trusts the range), F2 opponent (PIT allows 3.14 FGA/g, most generous
  on the slate; by week 4/3/2/2/5/4/2 — no single-game dominance, factor
  capped at 1.20), F4 stall profile (lowest total on the board, 39.5;
  CLE ITT 18.0 — defense-first team whose offense stalls into FG range),
  F5 line gap (model mean 8.44 vs KP line 5.5).
- Opponent-defense box (PIT): allows 3.14 FGA/g and 9.4 kicker pts/g.
  Offense counterweight: CLE scores only ~20 pts/g and Watson's Week 7
  was 308 yards — if CLE sustains drives to the red zone, FGs become XPs;
  Szmyt's Week 4 line vs this same defense was 2 FG + 3 XP (9 pts).
- Penalties (RotoWire through W7 + FootballDB differential, both ways):
  CLE commits 9.0/g (60.0 yds/g), draws 6.6/g; PIT commits 6.0/g
  (52.4 yds/g), draws 7.6/g. PIT's defense drawing flags extends CLE
  drives into FG range (mild support, not counted as a factor); CLE's
  own flag rate is the drag, already partly inside the low ITT.
- Weather: Pittsburgh Sun — cloudy, high ~69F, wind SE ~5 mph, rain 0%
  (weather.com 10-day, checked Oct 31). No veto.
- News/intent check: no kicker injury designation for Szmyt in the final
  injury report; no Week 8 statement on kicking usage found. CLE OL:
  Elgton Jenkins practiced fully Friday (no designation), Tytus Howard
  (concussion) questionable — noted, does not change the call. Szmyt's
  Week 4 trust anecdote (told Monken/Watson to get to the 42 for a
  60-yarder, then made the 56-yarder) corroborates range trust.
  No change to the call.
- ALT FLAGS (DraftKings ladder, raw implied — alt markets are over-only):
  KP o5.5 @ -130 — raw implied 56.5%, model 71.6%, +15.1pp (the KP
  expression of the same thesis). KP o7.5 @ +182 — +17.5pp, aggressive
  rung, tail-sensitive, not a separate bet. o3.5 @ -346 and FG o0.5
  @ -444 are below the -260 flag floor: NOT flagged.
- Trap check: no kicker/QB regime change (Szmyt CLE all season; Watson
  QB all season). Line explainable (market prices the 39.5 total, not
  PIT's FGA generosity or CLE's FG-heavy split). PASS. Browns-game
  kickers are screened like everyone else in this model (lift, Oct 24).
- Same-thesis note (NOT a second bet): Szmyt KP OVER 5.5 @ -131 DK
  (no-vig 53.4%, model 71.6%, +18.2pp, stress +7.0pp) is the same thesis;
  the FG line is the graded pick (bigger edge, wider stress margin).

### Pick 2 — BET (Partial tier)
**Cameron Dicker (LAC) — Field Goals OVER 1.5 (2+ FG made) @ -101, DraftKings**
(LAC @ LAR, Sun 4:05pm ET, SoFi Stadium, indoor)
- Same-book no-vig implied 47.4% (pair: over -101 / under -126, DK) |
  Model 65.4% | Edge +18.0pp | Stress 54.0% (clears by +6.6pp)
- Model inputs: lam_FGM 2.24, lam_XPM 1.79, model mean 8.51 pts.
  LAC implied team total 19.4, game total 45.25.
- Season (W1-6, LAC; LAC has played 6 games): 11 FGA / 9 FGM / 9 XPA /
  9 XPM; kick pts by week 2/2/10/11/5/6 — 2+ FG in 3 of 6 weeks, but the
  misses are volume (0, 1, 1 FGA in W1/W2/W5), not accuracy (9/11).
- Factors: F2 opponent (LAR allows 3.00 FGA/g, factor capped at 1.20),
  F3 venue (SoFi, indoor — no weather variance), F5 line gap (model
  mean 8.51 vs KP line 6.5). F1 is NOT counted: Dicker's raw volume
  (1.83 FGA/g) is below league; the edge comes from the matchup + line,
  not from his own volume.
- Opponent-defense box (LAR): allows 3.00 FGA/g and 9.0 kicker pts/g,
  by week 3/2/1/2/3/6/4. Sensitivity (disclosed): the 6 was Ryland's
  6-FG game in Week 6. Excluding that outlier, LAR allows 2.50/g,
  factor 1.095, lam_FG 2.04, model 60.6%, edge +13.2pp, stress 49.2%
  (+1.8pp) — the pick SURVIVES the ex-outlier test, thinner. The
  capped factor already shrinks the outlier; it does not drive the pick.
- Offense counterweight: LAC is 0-6 and scored 6 points in Week 7
  (Dicker's 2 FGs were all of it) — a stalling offense is exactly the
  FG profile, but a shutout-risk offense also caps total chances.
- Penalties: LAC commits 9.0/g (73.5 yds/g, 3rd-most; 15 false starts
  in the FootballDB type split — drive killers, a real headwind) but
  draws 8.8/g; LAR commits 7.6/g (69.9 yds/g), draws 6.3/g. Net roughly
  neutral — noted, not counted as a factor either way.
- Weather: indoor, no check needed beyond venue confirmation (SoFi).
- News/intent check: Chargers Week 8 depth chart lists Dicker as the
  starter; no kicker injury designation. Harbaugh's 4th-down pattern
  (NextGenStats: 0-for-recommended go-for-it calls in 2026 through
  Week 3, "wanted to put up points") runs TOWARD kicking, not away —
  supports, does not change, the call. LAR kicker regime change
  (McManus in after Grupe's ACL) affects McManus, not Dicker, and not
  LAR's defensive FGA-allowed number. No change to the call.
- ALT FLAGS (DK ladder, raw implied): KP o5.5 @ -142 — 58.7% implied,
  model 72.0%, +13.3pp (safer rung, price >= -260). KP o7.5 @ +162 —
  +15.8pp, aggressive rung, tail-sensitive. FG o2.5 @ +330 — +15.5pp,
  aggressive only.
- Trap check: no Dicker team change (LAC all season), Herbert QB all
  season (McConkey/Harris questionable affects receiving, not the
  kicking thesis directly). Line explainable (market prices LAC's
  0-6 offense, not LAR's FGA generosity). PASS.

### Pick 3 — BET (Partial tier)
**Chad Ryland (ARI) — Field Goals OVER 1.5 (2+ FG made) @ +100, BetMGM**
(ARI @ DAL, Sun 1:00pm ET, AT&T Stadium, retractable roof)
- Same-book no-vig implied 46.5% (pair: over +100 / under -135, BetMGM) |
  Model 63.1% (CORRECTED, see audit note above) | Edge +16.6pp |
  Stress 51.8% (clears by +5.3pp)
- Model inputs (corrected): lam_FGM 2.14, lam_XPM 2.25, model mean
  8.67 pts. ARI implied team total 23.8, game total 54.5.
- Season (W1-7, ARI): 19 FGA / 17 FGM / 13 XPA / 13 XPM; kick pts by week
  14/1/12/6/3/18/10 — 2+ FG in 5 of 7 weeks. The two misses are a 0-FGA
  game vs SEA (W2) and a 1-FGA game vs NYG (W4). Week 6 vs LAR: 6 FGs.
- Factors: F1 volume/accuracy (2.71 FGA/g, 89.5% raw, T-3rd in FG made),
  F3 venue (AT&T retractable roof — indoor), F4 stall profile (ARI
  TDs on only 12 of 28 red-zone trips; 1 of last 10 in the past two
  games, 0-for-5 vs LAR and 1-for-5 vs DEN leaving Ryland kicking 3 FGs
  vs DEN), F5 line gap (model mean 8.67 vs KP line 6.5). F2 is NOT
  counted: DAL allows only 1.71/g corrected (factor 0.91) — the edge
  is Ryland + the stall profile, not the matchup.
- Opponent-defense box (DAL): allows 1.71 FGA/g corrected (by week
  0/3/2/3/1/3/0 incl. W7 Elliott 0 FGA) but 8.5 kicker pts/g — a
  bottom-tier defense (30th in EPA allowed) that gives up TDs, i.e.
  XPs, more than FG attempts. Offense counterweight: DAL just scored
  38 at PHI and ARI's defense ranks 31st in dropback EPA — if this
  becomes a shootout, ARI chases TDs late instead of settling for FGs.
  That script risk is why Ryland is #3, not #1, despite the Week 6
  explosion.
- Penalties: ARI commits 7.1/g (65.0 yds/g), draws 6.0/g; DAL commits
  7.6/g (67.0 yds/g), draws 9.6/g with 22 first downs via penalty drawn.
  DAL's defense drawing flags extends ARI drives into FG range (mild
  support, not counted as a factor).
- Weather: retractable roof, no weather tax either way.
- News/intent check: no kicker injury designation for Ryland; ARI
  Week 8 depth chart lists Ryland as kicker; Mike LaFleur has stuck
  with Brissett at QB (no QB regime change). No Week 8 statement on
  kicking usage found. (Note: Packers coach Matt LaFleur's 4th-down
  aggression stories this week are a different person — NOT cited for
  Arizona.) ARI OL is badly banged up (Paris Johnson Jr. IR, Gaines
  out, Wilkinson limited) — that hurts sustained drives but also
  pushes ARI into FG-range stalls, consistent with the stall profile.
  No change to the call.
- ALT FLAGS (DK ladder, raw implied): KP o5.5 @ -184 — 64.8% implied,
  model 75.9% on screen lambdas, +11.1pp (safer rung). KP o7.5 @ +119 —
  +13.6pp, aggressive rung. DK FG o1.5 @ -107 is the same rung at a
  worse price than the locked BetMGM +100.
- Trap check: no kicker/QB regime change for ARI. Line explainable
  (market prices DAL's defense giving up TDs, not ARI's RZ stall rate).
  PASS.

### Screened and passed (logged, NOT plays)
- Chris Boswell (PIT) FG o1.5 -140 BetMGM: model 67.3% (highest on the
  2+ FG board) but edge only +12.1pp and stress clears by just +0.7pp —
  AND it is the same game as Pick 1 (CLE@PIT). Two FG-over picks on one
  39.5-total game is one thesis twice, not diversification. LEAN only.
  His PAT UNDER 2.5 -178 (+8.0pp, stress +1.5pp) is the same PIT script
  from the other side — also not a second bet.
- Jake Bates (DET) FG UNDER 1.5 +114 DK: +13.1pp, stress +3.7pp — a real
  under (DET finishes with TDs: lam_XP 2.84, 22 XPA in 6 games) and the
  first alternate if a locked price moves. Held out because Dicker's
  edge (+18.0pp) and stress margin (+6.6pp) are both wider. Bates PAT
  OVER 2.5 +107 (+8.4pp, stress +1.5pp) is the same DET thesis — not a
  second bet.
- Joey Slye (TEN) FG o1.5 +146 DK: +14.6pp, stress +3.8pp; KP o5.5 +102:
  +13.0pp, stress +1.7pp. LEAN only — TEN ITT 17.0 triggers the Zvada
  lesson (low-ITT overs need a higher bar: few drives at all dominates
  the FG-share effect), and Slye's 11 FGA in 7 games is thin volume.
- Will Reichard (MIN) FG o1.5 -119 DK: +13.6pp, stress +2.4pp. LEAN —
  DET allows only 1.50 FGA/g (stingiest matchup on the card's short
  list), which is the counterweight the model already prices (0.86).
- Spencer Shrader (IND) FG o1.5 +115 / KP o5.5 -111: +13.5pp / +14.0pp,
  stress +2.4pp / +2.6pp. LEAN — JAX allows only 1.67 FGA/g and IND's
  ITT is 18.2 (low-ITT caution again).
- Jake Elliott (PHI) PAT o1.5 +115 BetMGM: +13.5pp, stress +7.8pp on
  screen lambdas — but Elliott's W1-6 log (5 FGA in 6 games) predates
  the W7 MNF game in the same way the DAL table did, and his FG UNDER
  1.5 -159 fails stress on the screen (-1.6pp margin). Mixed signals
  from a stale log: LEAN only, revisit after a clean W1-7 refresh.
- Tyler Bass (BUF) FG o1.5 +100: +10.6pp but stress FAILS (-0.4pp).
  Cairo Santos (CHI) FG u1.5 -108: +9.3pp, stress fails (-0.3pp).
  Both stay leans/passes per the bar.
- Brandon McManus (LAR): 1 game logged (W7 debut, 0 FGA) — insufficient
  sample + new-team regime change. NO MODEL, pass. Zane Gonzalez (MIA):
  1 game logged (W7, 0 FGA) — same, NO MODEL, pass. Andres Borregales
  (NE, listed as "Andres" in the odds feed, "Andy" in Sleeper): model
  P(2+ FG) 46.3% — no edge at -140, pass.
- Week 8 TNF note (already logged Thu): Fitzgerald FG UNDER 1.5 -103
  stands as the early TNF pick; it grades Tue Nov 3 with the rest of
  Week 8. Do NOT double-count it in this top 3.

### 2+ FG made board (Week 8, model P, stress in parentheses)
Boswell 67.3% (55.9) · Szmyt 66.9% (55.6) ★ · Dicker 65.4% (54.0) ★ ·
Reichard 64.8% (53.5) · Little 64.0% (52.6) · Ryland 63.1% (51.8) ★
[corrected] · McPherson 60.4% (49.3) · Butker 58.4% (47.0) · Bass 57.8%
(46.8) · Gay 57.5% (46.4) · Shrader 57.3% (46.3) · McLaughlin 57.2%
(46.3) · Lutz 57.0% (45.8) · Sanders 56.2% (45.1) · Folk 56.0% (44.9) ·
Stevens 54.4% (43.4) · Loop 53.3% (42.3) · Slye 53.0% (42.2) · Aubrey
50.6% (39.8) · Myers 49.7% (39.2) · Borregales 46.3% (36.0) · Bates
42.8% (33.1) · Santos 41.7% (32.0) · Elliott 35.1% (26.6). McManus and
Gonzalez: no model (1 game each). Board is probability, not edge —
Boswell tops the board but his -140 price leaves only +12.1pp with a
+0.7pp stress margin, which is why he is a lean, not a pick.
Full board: hidden_files/week8-fg-board.json. Model file:
hidden_files/week8-saturday-model.json.

## Week 8 SNF — delivered Sun 2026-11-01 ~6:30 PM ET (before 8:20 PM ET kickoff, user-asked screen)
Game: PHI @ WAS, Northwest Stadium, Landover MD, outdoor. Total 40.5,
WAS -6 (median) -> PHI ITT 17.2, WAS ITT 23.2. Lines: Odds API core
snapshot 2026-11-01T23-17-49Z-core.json (quota 449 after pull).
Stats: Sleeper W1-7 FRESH pull (fixes the stale W7 file that missed MNF
DAL@PHI — see flip note below). Splits: NOT available for kicker
props — both plays Partial tier. Alt ladders: NOT pulled for SNF.

### Flip disclosure (read first)
Saturday's run held Elliott as LEAN ONLY on the stale W1-6 log (his FG
UNDER failed stress by 1.6pp on that data). The fresh W1-7 data adds
MNF: Elliott 0 FGA, 3 XPM vs DAL. That game flips FG UNDER to a pass
(stress +3.8pp) and confirms PAT OVER. The Saturday lean is superseded
by this screen, not quietly upgraded — the new data is the reason.

### Play 1 — BET (Partial tier)
**Jake Elliott (PHI) — PATs OVER 1.5 (2+ XP made) @ +105, BetMGM**
- Same-book no-vig implied 45.2% (pair: over +105 / under -145,
  BetMGM) | Model 59.7% | Edge +14.5pp | Stress 54.0% (clears by +8.8pp)
- Model inputs: lam_FGM 1.10, lam_XPM 2.01, model mean 5.32 pts.
  PHI ITT 17.2.
- Season (W1-7, PHI): 5 FGA / 5 FGM / 16 XPA / 16 XPM; XP by week
  3/3/1/2/2/2/3 — 2+ XP in 6 of 7 weeks (only W3 missed, 1 XP).
- Factors: F1 XP volume (16/16, 2.29 XPA/g), F2 TD-heavy shape
  (16 XPA vs 5 FGA; McKee's two starts produced 2 XP + 0 FGA and
  3 XP + 0 FGA), F6 opponent red-zone TD rate (WAS allows TDs on
  83.3% of RZ trips, worst in the league — teams score TDs on WAS,
  not FGs).
- Opponent-defense box (WAS): allows 2.33 FGA/g (by week 1/3/1/3/5/1
  over 6 games, bye W7) and 8.7 kicker pts/g. Offense counterweight:
  PHI ITT is only 17.2 and PHI is missing both starting WRs — if
  McKee's offense stalls completely, XP chances dry up too.
- Penalties: PHI commits 7.4/g (52/365), draws 8.6/g (60/531); WAS
  commits 7.7/g (46/359), draws 6.2/g (37/253). Noted, not counted;
  Quinn's bye-week penalty crackdown is a mild headwind for PHI
  drive extension, not a factor change.
- Weather: Landover ~51F at kickoff, partly cloudy, wind SE ~1 mph,
  gusts ~5, rain 0% — no veto.
- News/intent check: Elliott — no injury designation. McKee third
  straight start (Hurts out for the season, blood clots, IR); PHI
  without Smith (hamstring) and Wicks (ankle), both ruled out;
  Barkley cleared but limited snaps. WAS: Daniels starting, McLaurin
  IR (season-ending knee surgery), Payne out (fractured foot),
  Burks questionable. No kicking-usage intent found. SNF inactives
  due ~6:50 PM ET — NOT out at delivery; re-check before placing.
- Trap check: no kicker/QB regime change for PHI beyond the priced-in
  McKee era. Line explainable (market prices PHI's low total, not
  the 16-to-5 XP-to-FG split). PASS.

### Play 2 — BET (Partial tier)
**Jake Elliott (PHI) — Field Goals UNDER 1.5 (0-1 FG made) @ -159, DraftKings**
- Same-book no-vig implied (under) 57.9% (pair: over +124 /
  under -159, DK) | Under model 69.8% | Edge +11.9pp | Under-stress
  61.7% (clears by +3.8pp). Note the lay: -159 risks 1.59u to win 1u;
  at 1u flat grading a win pays +0.63u.
- Season (W1-7, PHI): 5 FGA in 7 games; 2+ FG in exactly 1 of 7
  weeks (W4, 2 FGA). FG by week 1/1/0/2/1/0/0.
- Factors: F1 scarcity (5 FGA/7g — thinnest volume on the slate),
  F2 McKee regime (0 FGA in both McKee starts, W6 and W7), F4 low
  total / low ITT (40.5 total, PHI ITT 17.2, 6-pt dog).
- Opponent-defense box (WAS) as above: 2.33 FGA/g is ABOVE league
  average — this under is NOT defense-driven, it is PHI-driven
  (PHI's own inability to reach FG range). That is the stated
  counterweight; the model already prices the 1.06 factor.
- Penalties, weather, news/intent: same as Play 1.
- Trap check: model under rate (69.8%) sits BELOW Elliott's actual
  under rate (6/7 weeks, 85.7%) — the model is skeptical of the
  under relative to his log, not hyping it. The -159 price is the
  market agreeing he rarely kicks 2 FGs; the edge is the model
  saying the market still underprices it by ~12pp. PASS.

### Correlation note (read before sizing)
Both plays are Jake Elliott. They are two 1u plays on the ledger,
but with real money they are correlated, not independent: the
"PHI scores TDs, doesn't kick FGs" script wins both; a 2-FG +
1-XP night loses both. Size them as one Elliott position, not two
separate bets.

### Screened and passed (logged, NOT plays)
- Drew Stevens (WAS) FG o1.5 -111 DK: +7.0pp edge but stress FAILS
  (-4.2pp). KP o6.5 -141: +3.7pp, stress fails. PAT u2.5: +4.2pp,
  stress fails. Stevens log (6g, WAS bye W7): 12 FGA/10 FGM/13 XPA/
  10 XPM; PHI allows 2.14 FGA/g (flat 2/2/2/2/2/2/3) and 7.6 kicker
  pts/g. No Stevens play.
- Elliott KP u5.5 -115 DK: under edge +6.9pp but stress FAILS
  (-3.2pp). KP over 5.5 fails on edge. Only the two plays above
  clear both parts of the bar.
- Grades Tue Nov 3 with the rest of Week 8.

---

## Week 8 FINAL GRADES — Tue 2026-11-03 10:49 ET (Sleeper W8 final stats + cross-checks)
Source: Sleeper Week 8 kicker stats (api.sleeper.app/stats/nfl/2026/8, season_type=regular, position=K). 1u flat at logged prices, payout recomputed from price: plus-money = price/100, minus-money = 100/|price|. Wins AND losses summed below so the total re-performs from the lines above it.
Cross-checks (surprising lines only): Fitzgerald 2/2 FG confirmed by Sportradar box-score kicking table (2/2 FG, 1/1 XP, 7 pts) and the scoring summary (39-yd Q1, 50-yd Q3) — the GB-stinginess thesis failed, not the data. Elliott 1/2 FG, 1/1 XP, 4 pts confirmed by Sportradar kicking table and USA TODAY live updates (40-yd FG + Barkley TD XP in Q1, then shut out; 41-yd retry doinked off the upright in Q4 after a penalty wiped out a make) — the PAT-over loss is real, not a stat error.
- TNF Fitzgerald (CAR) FG UNDER 1.5 @ -103 DK: LOSS — 2 FGM, 1 XPM, 7 pts (>= 2). -1.00u.
- Pick 1 Szmyt (CLE) FG OVER 1.5 @ +105 BetMGM: WIN — 2 FGM, 0 XPM, 6 pts (>= 2). +1.05u.
- Pick 2 Dicker (LAC) FG OVER 1.5 @ -101 DK: WIN — 3 FGM, 9 pts (>= 2). +0.99u (100/101).
- Pick 3 Ryland (ARI) FG OVER 1.5 @ +100 BetMGM: WIN — 2 FGM, 3 XPM, 9 pts (>= 2). +1.00u.
- SNF Play 1 Elliott (PHI) PAT OVER 1.5 @ +105 BetMGM: LOSS — 1 XPM (< 2), 1 FGM, 4 pts. -1.00u.
- SNF Play 2 Elliott (PHI) FG UNDER 1.5 @ -159 DK: WIN — 1 FGM (< 2). +0.63u (100/159).
WEEK 8 FINAL: 4-2-0, +1.67u (wins +3.67u, losses -2.00u). Running record: 10-3-0, +6.58u (13 graded picks). Checkpoints: 25-pick interim and 50-pick bettable gate NOT reached — no stakes change, no bar change, no model version change.

---

## Week 9 WEEKEND — locked Sat 2026-11-07 ~12:15 ET (before Sunday 1pm ET kickoffs)

Scope: the 14 remaining Week 9 games (Sun Nov 8 + MNF Nov 9, BUF@MIN).
Week 9 TNF (JAX@BAL, Thu Nov 5) already played — see TNF note below; it
is NOT part of this top 3 and is NOT re-picked here. Week 10 TNF
(Nov 13) is out of scope for this run.
Lines: Odds API core snapshot 2026-11-07T16-51-15Z-core.json (quota 151
remaining after the 14-game pull; 129 after alt ladders), fresh median
game lines in hidden_files/game-lines-week9.json (quota 193 after that
pull — Nov 6 medians overwritten; spreads moved slightly: ATL 3.0->3.25,
DAL -5.5->-4.75, DET -7.0->-6.5, HOU -5.5->-5.75). Alt ladders:
2026-11-07T16-54-02Z-alts.json (4 games: LAR@WAS, LV@SF, NYG@PHI,
NYJ@KC). Stats: Sleeper W1-8. Model: v1.1 formulas via
week9_saturday_screen.py (W1-8 adaptation of the Week 8 screen) — SAME-
BOOK no-vig pairs throughout, fixing the Week 8 screen's mixed-book
pairs that the audit had to correct by hand; Borregales alias added
(odds feed "Andres" = Sleeper "Andy"). Splits: NOT available for kicker
props — every Week 9 play is Partial tier. Screen: 23 rows passed
edge >=6pp + stress survives (week9-saturday-screen.json); leave-one-out
run on all 12 top candidates (week9_loo.py).

### TNF note (read first — a ledger gap, not a pick)
Week 9 TNF (JAX@BAL, Thu Nov 5) was screened Nov 5
(hidden_files/tnf-week9-screen.json; Cam Little FG UNDER 1.5 was the
candidate, with a leave-one-out run) but NO pick was logged in this
ledger and none is added here — the game is played and backfilling is
not allowed. Little went 4/4 FG, 3/3 XP, 15 pts; the under candidate
would have lost. If a TNF pick was delivered anywhere, it is not in
this log — Tuesday's grade run must reconcile it.

### Pick 1 — BET (Partial tier) ★ STRONGEST PLAY ON THE CARD
**Eddy Pineiro (SF) — Field Goals UNDER 1.5 (0 or 1 FG made) @ +105, BetMGM**
(LV @ SF, Sun 4:25pm ET, Levi's Stadium, outdoor)
- Same-book no-vig implied (under) 45.2% (pair: over -145 / under +105,
  BetMGM) | Model under 65.3% | Edge +20.1pp | Under-stress 56.4%
  (clears implied by +11.2pp — the widest stress margin on the card)
- Model inputs: E_FGA 1.55, lam_FGM 1.23, lam_XPM 3.50, model mean 7.19
  pts. SF implied team total 30.6 (highest on the slate), game total
  51.75.
- Season (W1-7, SF; SF bye W8): 9 FGA / 6 FGM / 25 XPA / 21 XPM; kick
  pts by week 9/5/6/6/6/5/2 — 2+ FGM in only 1 of 7 weeks (W1). Most
  recent game W7 vs ATL: 0 FGA, 2/3 XP.
- Factors: F4-inverted (SF red-zone TD rate 87%, best in the NFL per
  Sharp through W8; SF scores on 100% of RZ trips, 6.35 pts/trip;
  3.57 XPA/g vs 1.29 FGA/g — drives end in TDs), F1-inverted (1.13
  FGA/g raw, lowest volume among starters; 6/9 FG, 66.7% raw — his
  misses help the under), F2 opponent (LV allows 1.75 FGA/g, below
  league; LV sees the 9th-fewest FG attempts in the league per
  RotoBaller).
- Opponent-defense box (LV): allows 1.75 FGA/g (by week 3/1/0/1/1/4/0/4)
  and 7.8 kicker pts/g. Offense counterweight: SF's 30.6 ITT means many
  drives and many chances; the bet is they end in the end zone, and
  the 87% RZ TD rate is the mechanism.
- Penalties (RotoWire through W8 + StatRankings drawn, both ways): SF
  commits 6.1/g (55.1 yds/g), draws 6.4/g; LV commits 6.1/g (48.0
  yds/g), draws 8.0/g. LV drawing flags extends LV drives (helps Gay,
  not Pineiro) — neutral for this pick, not counted as a factor.
- Weather: Santa Clara Sun — AM clouds/PM sun, high 72°F, rain 20%,
  wind NW 8 mph (weather.com, checked Nov 7). No veto.
- News/intent check: Pineiro carries no injury designation; Shanahan
  said Oct 26 the 49ers have NO plans to try out other kickers — job
  safe despite 4 missed PATs + 3 missed FGs (all 3 FG misses from 50+).
  HEADWIND (named, not hidden): Raiders HC Klint Kubiak said this week
  the defensive plan is to "get them to kick field goals" — LV's stated
  intent runs directly against this under. The pick stands because the
  intent is the opponent's hope, not SF's behavior: SF's 87% RZ TD rate
  and Pineiro's 1.29 FGA/g are season-long, and the under survives the
  scoring-inflation stress at +11.2pp (worst leave-one-out +6.2pp).
  Not sized up on this flag. SF WRs Evans/Samuel/Kirk all ruled out
  again — Purdy leans on Kittle/McCaffrey; a thinner WR room could stall
  more drives in FG range (mild headwind, same direction as Kubiak).
  No change to the call.
- Leave-one-out: worst case drop W2 or W7 (0-FGA weeks) → stress 51.4%
  (+6.2pp). Survives every single-week drop.
- ALT FLAGS: none — every DK alt OVER rung is negative edge (FG o1.5
  alt -24.4pp; KP o7.5 -24.4pp). Alt ladders are over-only, so no under
  rungs exist; the negative alt overs corroborate the under.
- Trap check: no kicker change (Pineiro SF all season), no QB change
  (Purdy). Line explainable (market prices SF's 30.6 ITT, not the TD-vs-
  FG split of it). PASS.
- Same-thesis alternative (NOT a second bet): Pineiro KP UNDER 8.5
  @ +100 DK — model 66.9%, +16.9pp, stress +5.2pp (RAW implied — no
  same-book pair, so the edge is overstated by roughly the vig). Same
  SF-TDs thesis; the FG line is the graded pick.

### Pick 2 — BET (Partial tier)
**Drew Stevens (WAS) — Field Goals OVER 1.5 (2+ FG made) @ -112, DraftKings**
(LAR @ WAS, Sun 1:00pm ET, Northwest Stadium, outdoor)
- Same-book no-vig implied 49.8% (pair: over -112 / under -114, DK) |
  Model 69.9% | Edge +20.1pp | Stress 58.6% (clears implied by +8.8pp)
- Model inputs: E_FGA 2.91, lam_FGM 2.44, lam_XPM 1.85, model mean 9.16
  pts. WAS implied team total 21.5, game total 47.5.
- Season (W1-8, WAS; bye W7): 17 FGA / 14 FGM / 14 XPA / 11 XPM; kick
  pts by week 4/8/9/7/7/5/13 — 2+ FG in 6 of 7 weeks (only W6, 1 FGA,
  missed).
- Factors: F1 volume (2.43 FGA/g, 14 FGM), F2 opponent (LAR allows 3.00
  FGA/g, most generous on the slate; 9.0 kicker pts/g), F4 stall profile
  (WAS 31st in 3rd-down offense, 31.9%; WAS FG-heavy 2.43 FGA/g vs 2.00
  XPA/g).
- Opponent-defense box (LAR): allows 3.00 FGA/g (by week 3/2/1/2/3/6/4/3;
  the 6 was Ryland's W6 game — ex-outlier 2.57/g, still above league)
  and 9.0 kicker pts/g. Counterweight (named): LAR's RZ defense allows
  TDs on 71.4% of trips (worst in NFL per Sharp) — WAS RZ trips become
  TDs, not FGs, so Stevens's FGs must come from mid-field stalls; the
  3.00 FGA/g already prices this in. WAS WRs Burks + Dyami Brown ruled
  out (foot/calf) — fewer vertical threats could stall more drives in FG
  range (mild support).
- Penalties: WAS commits 7.9/g (61.3 yds/g), draws 6.1/g; LAR commits
  7.6/g (66.1 yds/g), draws 5.9/g (tied 29th). WAS's high commit rate
  stalls its own drives (mild headwind, not counted); LAR draws few flags
  so WAS drives aren't extended by DPI/holding (mild headwind). Noted,
  not counted as factors.
- Weather: Landover Sun — sunny, high 62°F, rain 0%, wind W 9-13 mph,
  gusts to 18 (weather.com + Sharp Football kickoff forecast: 59°F, 9 mph,
  gusts 18). Below the 15 mph downgrade line. No veto.
- News/intent check: Stevens cleared on the final injury report (no
  designation). Daniels (left elbow, non-throwing) practiced fully;
  Stafford (right elbow) practiced fully, no concern per McVay. WAS
  defense is depleted (both starting DTs Payne + Kinlaw on IR). No coach
  statement on kicking usage found for either team. No change to the call.
- Leave-one-out: worst case drop W8 (5-FGA game vs PHI) → stress 52.4%
  (+2.6pp). Survives every single-week drop, thinnest on that one.
- ALT FLAGS (DraftKings ladder, raw implied): KP o5.5 @ -179 — implied
  64.2%, model 76.1%, +12.0pp (safer rung). KP o7.5 @ +126 — +15.0pp
  (aggressive rung, tail-sensitive). FG o2.5 @ +293 — +18.6pp (aggressive
  rung, tail-sensitive). FG o0.5 @ -547 is +6.7pp but price < -260: NOT
  flagged (juice eats it).
- Trap check: no kicker/QB regime change for WAS (Stevens all season;
  Daniels QB). Line explainable (market prices WAS's 21.5 ITT, not LAR's
  FGA generosity). PASS.
- Same-thesis alternative (NOT a second bet): Stevens KP OVER 6.5
  @ -118 BetRivers — model 68.4%, +14.2pp, stress +1.8pp (RAW implied,
  no same-book pair). Same thesis; the FG line is the graded pick.

### Pick 3 — BET (Partial tier)
**Jake Elliott (PHI) — Field Goals UNDER 1.5 (0 or 1 FG made) @ -128, DraftKings**
(NYG @ PHI, Sun 1:00pm ET, Lincoln Financial Field, outdoor)
- Same-book no-vig implied (under) 52.9% (pair: over +100 / under -128,
  DK) | Model under 71.7% | Edge +18.9pp | Under-stress 64.0% (clears
  implied by +11.1pp)
- Model inputs: E_FGA 1.23, lam_FGM 1.05, lam_XPM 2.04, model mean 5.19
  pts. PHI implied team total 17.8, game total 38.5 (lowest on the board).
- Season (W1-8, PHI; bye W7): 7 FGA / 6 FGM / 14 XPA / 14 XPM; kick pts
  by week 6/6/1/8/5/2/4 — 2+ FGM in only 1 of 7 weeks (W4).
- Factors: F1 scarcity (1.00 FGA/g, thinnest volume on the slate), F2
  opponent (NYG allows 1.43 FGA/g, 5.3 kicker pts/g — stingy), F4 low
  total/ITT (38.5 total, PHI ITT 17.8; PHI RZ TD 71%, 4th in NFL).
- Opponent-defense box (NYG): allows 1.43 FGA/g (by week 0/1/1/1/2/3/2)
  and 5.3 kicker pts/g. Offense counterweight: PHI's offense is depleted
  (see regime flag) — a worse offense means fewer drives of every kind,
  which helps the under, but also more FG-range stalls if the new QB
  can't finish drives.
- Penalties: PHI commits 7.3/g (49.4 yds/g), draws 8.6/g (6th-highest —
  flags extend PHI drives, mild headwind, not counted); NYG commits
  7.1/g (60.6 yds/g), draws 7.9/g.
- Weather: Philadelphia Sun — partly cloudy, high 60°F, rain 10%, wind
  W 13 mph (weather.com, checked Nov 7). Below the 15 mph line; wind
  mildly suppresses FG accuracy, which helps an under — noted, not
  counted as a factor.
- News/intent check — REGIME CHANGE (flagged, priced into the call):
  Joe Milton III starts at QB Sunday (first NFL start), replacing Tanner
  McKee (benched Nov 4 after going 0-3; Sirianni confirmed Nov 7 the
  change was deliberately held back to limit NYG prep). The McKee-era
  evidence behind this thesis (0 FGA in both McKee starts, W6/W7) NO
  LONGER APPLIES — the offense playing Sunday is a third QB in 9 weeks.
  Milton (signed off DAL's practice squad Oct 16) brings a strong arm +
  mobility; his shape is unknown. The pick stands because the scarcity
  profile spans all three QBs (FGA by week under Hurts: 1/1/0/2/1; under
  McKee: 0/0/2) and NYG's 1.43 FGA/g allowed is the stingiest opponent on
  the board — but the Milton unknown is why this is Pick 3, not Pick 1,
  and it is NOT sized up. Barkley (back/hamstring) did not practice Wed;
  Smith (hamstring) + Wicks (ankle) still out — re-check inactives
  ~11:30am ET Sunday. If Barkley sits, fewer sustained drives — mildly
  good for the under.
- Leave-one-out: worst case drop W3 or W6 (0-FGA weeks) → stress 59.6%
  (+6.7pp). Survives every single-week drop.
- ALT FLAGS: none — every DK alt OVER rung is negative edge (FG o1.5
  alt -22.0pp; KP o5.5 -17.2pp). Corroborates the under.
- Trap check: kicker unchanged (Elliott PHI all season); QB regime change
  flagged above (not a cut — the profile is QB-spanning, and the
  edge/stress are the week's widest after Pineiro). Line explainable
  (market prices PHI's 17.8 ITT, not the 1.00 FGA/g scarcity). PASS with
  the flag.
- Same-thesis alternatives (NOT a second bet): Elliott PAT OVER 1.5
  @ -106 DK — model 60.4%, +11.9pp, stress +6.2pp; Elliott KP UNDER 6.5
  @ -137 DK — model 68.6%, +14.1pp, stress +4.5pp. Both are the same
  "PHI scores TDs, doesn't kick FGs" script — take one.

### Screened and passed (logged, NOT plays)
- Jason Sanders (NYJ) FG o1.5 +125 BetMGM: +18.8pp, stress +7.5pp, LOO
  worst +3.0pp — clears the bar; loses the #3 tiebreak to Elliott by
  0.1pp of edge and a narrower stress margin, and carries the low-ITT
  caution (NYJ ITT 19.0 — Zvada lesson) plus NYJ's low drawn rate
  (5.9/g, tied 29th) and 8.0 committed/g. FIRST ALTERNATE if a locked
  price moves. Alt flags: FG o1.5 +112 (+13.3pp raw), KP o5.5 -128
  (+10.9pp safer rung). Weather KC: sunny, 66°F, wind WNW 6 mph — calm.
  No kicker designation; Geno Smith (NYJ QB) no designation.
- Matt Gay (LV) FG o1.5 +105 DK: +18.4pp, stress +7.1pp, LOO worst
  +2.9pp — clears the bar; held out because Pick 1 already comes from
  the same game (LV@SF) and Elliott's stress margin is wider. Alt flags:
  KP o5.5 -152 (+12.4pp safer), KP o7.5 +159 (+16.5pp aggressive),
  FG o2.5 +352 (+15.3pp aggressive, tail-sensitive). Same-game note: Gay
  over + Pineiro under can both win (LV stalls, SF scores TDs) — they
  are not one thesis, but the card takes one play from that game.
- Harrison Butker (KC) FG UNDER 2.5 @ -167 DK: +15.2pp, stress +5.2pp,
  LOO worst +2.5pp — clears the bar; held out on the -167 lay (a win pays
  +0.60u at 1u flat) and the Tucker-on-practice-squad overhang. Reid
  confirmed Nov 4 Butker keeps the job for Week 9 (12/18 FG, 66.7%,
  2-for-7 from 50+; Tucker signed to the practice squad late Oct). His
  misses help the under. Lean.
- Andres Borregales (NE) FG UNDER 1.5 @ -107 DK: +14.3pp, stress +5.2pp,
  LOO worst +0.5pp — passes but the thinnest LOO margin of the card; GB
  allows 1.12 FGA/g (stingiest in the league) and 5.0 kicker pts/g.
  Weather Foxborough: 57°F, wind W 15 mph (at the downgrade threshold —
  mildly helps an under, noted not counted). Lean. (Name fix: odds feed
  "Andres" = Sleeper "Andy" — alias added to the screen this week.)
- Spencer Shrader (IND) FG o1.5 -105 DK: +17.9pp, stress +6.6pp — but
  LOO worst +0.2pp (drop W5's 5-FGM game) and his last two weeks are 1
  FGM then 0 FGA (W8 vs JAX: 0 FGA, 1 pt). Thin + fading. Lean.
- Will Reichard (MIN) FG o1.5 -112 DK: +17.1pp, stress +5.8pp — but LOO
  FAILS (drop W4's 5-FGM game → stress -0.6pp) AND a QB regime change:
  Carson Wentz starts Monday night with Kyler Murray out (reported
  Nov 6-7). Lean, not a pick.
- Cameron Dicker (LAC) FG o1.5 +105 BetMGM: +16.2pp, stress +4.8pp, LOO
  worst +0.6pp — low-ITT caution (LAC ITT 17.4, Zvada lesson) keeps it a
  lean.
- Evan McPherson (CIN) FG UNDER 1.5 @ +120 DK: +14.3pp, stress +4.8pp —
  but LOO FAILS (drop either 0-FGA week W7/W8 → stress -0.3pp); his last
  two weeks are 0 FGA. Lean.
- Trey Smack (GB) FG o1.5 +134 DK: +11.8pp, stress +0.8pp — thinnest
  stress pass on the board; 11/16 FG accuracy is the drag. Lean.
- Brandon McManus (LAR) PAT OVER 2.5 @ -122 DK: +23.6pp on paper —
  REJECTED, not a lean: (1) 2-game sample (1 FGA/1 FGM/8 XPA/8 XPM) — a
  leave-one-out is impossible (dropping either week leaves 1 game); the
  edge is driven by his W7 debut's 5-XP game and collapses to ~+6pp on
  LAR's team XPA/g. (2) Alt ladder gives NO support (best rung KP o12.5
  +5.4pp, below the 6pp flag bar). (3) REGIME FLAG: LAR officially carry
  TWO kickers — Joshua Karty was signed to the 53-man roster Nov 6
  alongside McManus (Turf Show Times) after both were active in Week 8;
  McManus's share of kicks is not secure. (4) Edge +23.6pp sits in the
  learning.md near-bug zone. Logged as a pass with reasons, not a bet
  and not a lean at the modeled number.
- Andre Szmyt (CLE) FG o1.5 -123 DK: +10.5pp, stress FAILS (-0.8pp).
  Also CLE QB change: Shedeur Sanders starts (Deshaun Watson
  concussion). Pass.
- Chad Ryland (ARI) KP o4.5 -128: +10.4pp, stress FAILS (-0.5pp). Also
  SEA QB change: Drew Lock starts (Sam Darnold quadricep/ribs,
  week-to-week). Pass.
- Dominic Zvada (NYG) FG o1.5 -140: +10.2pp, stress FAILS (-1.4pp).
  Pass.
- Jason Sanders KP o5.5 -125 BetRivers: +11.4pp, stress +0.0pp —
  exactly at implied, a rounding artifact; effectively fails. The FG line
  is the expression.
- Ka'imi Fairbairn (HOU) FG o1.5 -164: +4.9pp — fails bar. Jake Bates
  (DET) FG u1.5, Nick Folk (ATL) FG o1.5 and the rest below bar per the
  screen file.
- No market: Daniel Carlson (NO — CLE@NO), MIA kickers Riley Patterson /
  Zane Gonzalez (DET@MIA), Tyler Bass (BUF — BUF@MIN MNF). No line, no
  play. MIA sticks with Gonzalez for Week 9 (Jeff Hafley via Sun
  Sentinel) but no line was posted.

### 2+ FG made board (Week 9, model P, over-stress in parentheses)
Stevens 70.0% (58.7) ★ · Reichard 66.9% (55.7) · Shrader 66.2% (54.8) ·
Zvada 65.3% (53.6) · Gay 64.3% (53.2) · Aubrey 64.1% (52.5) · Fairbairn
63.6% (52.3) · Szmyt 62.6% (51.2) · Dicker 61.8% (50.5) · Sanders 60.5%
(49.3) · Folk 59.4% (48.0) · Lutz 54.3% (43.3) · Fitzgerald 54.0% (43.2) ·
Myers 53.4% (42.6) · Santos 53.1% (42.0) · Butker 52.5% (41.3) · McLaughlin
52.5% (41.7) · Smack 52.2% (41.2) · Ryland 50.1% (39.7) · Bates 49.7%
(39.3) · McManus 49.7% (39.0) · McPherson 42.9% (33.2) · Borregales 37.0%
(28.1) · Pineiro 34.8% (26.1) ★ · Elliott 28.3% (20.9) ★. Board is
probability, not edge — Reichard tops the board on probability but his
-112 price leaves +17.1pp with a LOO-failing stress, which is why he is
a lean, not a pick; Elliott sits at the bottom of the board because the
play is his UNDER, not his over.

## SUNDAY RE-CHECK — Sun Nov 8, 2026 ~11:50 AM ET (fresh core pull, snapshot 2026-11-08T16-44-48Z-core.json; quota 51 after pull, below 60 — no more fetches today)
- Pineiro FG u1.5: CONFIRM. MGM +105 unchanged; DK +112 (was +116 Sat). Model 65.3%, edge +20.8pp (DK pair), stress +11.9pp. Still Pick 1.
- Stevens FG o1.5: CONFIRM AT NEW BOOK. DK over moved -112 -> -131; BetMGM -118 unchanged. Re-graded at MGM -118: model 70.1%, edge +19.4pp, stress +8.1pp. Still a play.
- Elliott FG u1.5: CONFIRM AT WORSE PRICE. DK under -128 -> -136; MGM -150 (was -135). Re-graded at DK -136: model 72.3%, edge ~+17.9pp (DK pair), stress +10.2pp. Still a play.
- INACTIVES (11:31 AM ET): Barkley ACTIVE but pitch-count/limited (15.1% snaps W7, 31.9% W8, 22 snaps W8; Mitchell elevated RB2). Smith/Wicks/Covey out as known. McKee active as backup; Payton active. NEW: Elliott limited Thu with right ankle, no game designation, active — mildly helps an under, not counted. Skattebo doubtful (NYG).
- WEATHER re-checked: PHI 1pm W 14 mph, gusts 24, 0% rain (Sat: W 13) — below 15 mph sustained line, no veto. Landover 1pm W 11 mph, gusts 19, sunny — unchanged, no veto. SF not re-checked this run (4:25pm kick; Sat: 72F, wind 8).
- McManus PAT o2.5 still top on paper (+22.9pp) — STILL REJECTED (2-game sample, two kickers). Butker FG u2.5 OFF the board: u1.5 @ +135 MGM edge +8.0pp but stress FAILS -2.3pp; KP u8.5 stress fails -7.1pp (yesterday's hypothetical answer no longer clears).
- Sanders FG o1.5 +125 MGM unchanged (+18.8pp, stress +7.5) — still first alternate. Gay FG o1.5 +109 DK — still held out (same game as Pick 1). Reichard still fails LOO — lean. New same-thesis alts (NOT second bets): Elliott KP u5.5 +103 DK (+13.6pp, stress +3.7); Stevens PAT u2.5 -190 (+9.5pp, correlated stall profile).
- Passes 23 -> 20; no new locked plays. Card stands as the same three.

## SNF SCREEN — Sun Nov 8, 2026 ~7:05 PM ET (TB@CHI, 8:20pm ET; fresh pull, snapshot 2026-11-09T00-00-25Z-core.json; game-lines-week9-snf.json)
- VERDICT: NO PLAY. 0 passes. Only near: McLaughlin KP OVER 6.5 @ -110 BetMGM — model 53.5%, edge +4.5pp (below 6pp bar), stress 41.8% FAILS by -7.2pp. Closest miss, not a lean that clears anything.
- Lambdas: Santos CHI lam_fg 1.78 / lam_xp 3.01 / mean 8.35 (P2+ FG 53.1%, P2+ XP 80.2%); McLaughlin TB lam_fg 1.76 / lam_xp 2.04 / mean 7.30 (P2+ FG 52.5%, P2+ XP 60.5%). Lines: total 47.5, CHI -6.0 (ITT CHI 26.75 / TB 20.75). Santos PAT o2.5 @ -143 DK: model 57.9%, edge only +2.4pp — highest-probability leg, not a play. Santos FG o1.5 edge +1.7pp; McLaughlin FG o1.5 ~0.
- INACTIVES: no kickers out. CHI: Monangai OUT (turf toe, 5th straight), Muhammad II OUT. TB: Diaby OUT; Egbuka BACK (foot, missed 2 games). Baker thumb-limited, TB run-heavy last 2 games (582 rush yds, 4 rush TDs).
- WEATHER: Soldier Field clear, 52-54F, WNW 8 mph, gusts 16 — no veto.
- QUOTA: 5 remaining after this pull (used 495). No more Odds API pulls until reset — check reset date before Sat Nov 14 run; MNF single-event core pull (3 credits) still possible if asked.

## WEEK 9 GRADE — Sun Nov 8, 2026 ~7:45 PM ET (early grade at Finn's request; Tuesday Nov 10 cron reconciles)
Sleeper W9 live stats (kstats_2026_w9_live.json), 1u flat at logged prices. All three games final, verified vs box scores.
- Pineiro FG UNDER 1.5 @ +105 BetMGM — WIN (1 FGM, 5/5 XP; SF 38-17 LV; lone FG a 35-yarder with 5:21 left). +1.05u.
- Stevens FG OVER 1.5 @ -112 DraftKings — WIN (2 FGM, 1/1 XP). +0.89u.
- Elliott FG UNDER 1.5 @ -128 DraftKings — WIN (1 FGM, 45-yarder with 1:56 left; 0 XPA — PHI scored 11: 1 TD + 2-pt + 1 FG; NYG 19-11 final). +0.78u.
Week 9: 3-0, +2.72u. Running record: 13-3-0, +9.30u (16 graded picks). 25-pick checkpoint at 16/25 — not reached.
NOT graded: TNF Little FG-under lean (lean only); SNF no-play; McLaughlin PAT o1.5 hypothetical probability ranking (ranking, not a delivered play).
Finn's actual ticket prices never confirmed. If he took the Sunday re-run prices (Stevens MGM -118, Elliott DK -136, Pineiro MGM +105), his actuals are +2.64u.

## MNF PLAY — Mon Nov 9, 2026 ~3:45 PM ET (BUF@MIN, 8:15pm ET; fresh pull on new key, snapshot 2026-11-09T20-31-42Z-core.json; quota 485 after)
- PLAY: Will Reichard (MIN) FG OVER 1.5 @ -101 DraftKings, 1u flat, Partial tier. No-vig 47.4% (pair over -101 / under -126 DK) | model 67.5% | edge +20.1pp | stress 56.2% (+8.8pp) | LOO worst +2.5pp (drop W4, his 5-FG game vs MIA) — survives every drop.
- THIS FLIPS SATURDAY'S LEAN. Saturday: +17.1pp, LOO FAILED (-0.6pp) at -112, plus the Wentz flag. The flip is PRICE, not model: DK over moved -112 -> -101 (no-vig 49.9% -> 47.4%) and the total moved 44.25 -> 45.5; the model barely moved (67.0% -> 67.5%). Stated plainly so the flip is not mistaken for a model change of mind.
- Inputs: lam_fg 2.33 / lam_xp 1.77 / mean 8.75; MIN ITT 21.0, total 45.5, BUF -3.5. Season (7 games): 20 FGA / 18 FGM (90.0%) / 10 XPA / 10 XPM; 2+ FG in 5 of 7 weeks (W1: 1, W8: 0 missed).
- Factors: (1) volume 2.86 FGA/g, 2+ in 5/7; (2) 90% accuracy; (3) home dome, total 45.5, ITT 21.0. Counterweight: BUF allows only 1.86 FGA/g (factor 0.94, already in the model).
- REGIME FLAG (named, not a veto): Carson Wentz starts for MIN (Murray out, hamstring) — 101st career start, 7th for MIN. Backup QB can stall drives (helps FG over) or produce fewer drives (hurts); the ITT 21.0 already prices the Wentz-led offense. Jennings OUT (calf) for MIN; Palmer OUT for BUF.
- PENALTIES: BUF commits 8.7/g (most in NFL, 75.1 yds/g), draws 7.9/g; MIN commits 5.6/g (fewest, 44.9 yds/g), draws 8.0/g. BUF flags extend MIN drives — mild support, not counted as a factor.
- WEATHER: dome (U.S. Bank Stadium), no tax.
- SAME-THESIS ALT (NOT a second bet): Reichard KP OVER 6.5 @ -106 DK (model 65.4%, +16.9pp, stress +4.5pp, LOO worst +0.2pp — survives by a hair). Take one, not both — one position.
- Bass (BUF): NO MARKET again — no props in the feed at any book. Nothing to screen.
- INACTIVES PENDING (~6:45pm ET): re-check ~7:15pm for price + inactives. Watch: Darrisaw (MIN LT, shoulder, DNP Fri, no designation), BUF OL Dawkins (rib) / Anderson (ankle) questionable. Neither kicker is on any injury list.
- Grades Tue Nov 10 with Week 9 (pick 17 if locked-and-delivered).

---

## WEEK 9 FINAL GRADES — Tue 2026-11-10 10:49 ET (Sleeper W9 final stats + cross-checks)
Source: Sleeper Week 9 kicker stats (api.sleeper.app/stats/nfl/2026/9, season_type=regular, position=K), saved as hidden_files/kstats_2026_w9_final.json. 1u flat at logged prices, payout recomputed from price: plus-money = price/100, minus-money = 100/|price|. Wins AND losses summed below so the total re-performs from the lines above it.
Reconciliation of the Sun Nov 8 early grade: all three Sunday lines re-checked against FINAL Sleeper stats — identical to the live stats graded Sunday (Pineiro 1 FGM / 5 XPM, Stevens 2 FGM / 1 XPM, Elliott 1 FGM / 0 XPA). Early grade CONFIRMED, no changes.
Cross-check (MNF): Reichard 2/2 FG confirmed by the Sportradar box-score kicking table (2/2 FG, 0 XP) and Reuters/NBC game reports (43-yd and 53-yd makes; MIN's only points in a 23-6 BUF win). Sleeper's absent XPA/XPM fields = 0 XP attempts (MIN scored no TDs) — the same rendering quirk as Elliott W9 / Butker W7, not a missing-data error.
- Pick 1 Pineiro (SF) FG UNDER 1.5 @ +105 BetMGM: WIN — 1 FGM, 5 XPM, 8 pts. +1.05u.
- Pick 2 Stevens (WAS) FG OVER 1.5 @ -112 DraftKings: WIN — 2 FGM, 1 XPM, 7 pts. +0.89u (100/112).
- Pick 3 Elliott (PHI) FG UNDER 1.5 @ -128 DraftKings: WIN — 1 FGM, 0 XPA. +0.78u (100/128).
- MNF Play Reichard (MIN) FG OVER 1.5 @ -101 DraftKings: WIN — 2 FGM (43, 53 yds), 0 XPM, 6 pts. +0.99u (100/101).
WEEK 9 FINAL: 4-0-0, +3.71u (wins +3.71u, losses 0). Running record: 14-3-0, +10.29u (17 graded picks). Checkpoints: 25-pick interim at 17/25 and 50-pick bettable gate NOT reached — no stakes change, no bar change, no model version change.
NOT graded (reconciled): TNF Cam Little FG-under candidate — a lean only, never locked as a pick; Sleeper final confirms 4/4 FG, 3/3 XP, 15 pts, so the candidate would have LOST. SNF was a no-play (McLaughlin KP o6.5 failed bar and stress); his 3/3 FG, 1 XP, 10 pts would have cleared 6.5, but a no-play is not a graded play. No other locked Week 9 pick exists in the ledger.
