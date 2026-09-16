---
project: forge
type: research
topic: how long a save and a release of the engine take, and where the time goes — the operating measurements of 2026-09-02 to 2026-09-06
date: 2026-09-14
derived_from: the ledger's Waiting on principal as it stood on 2026-09-14 (the "save duration (watch)" entry, kept there since 2026-09-02); 10-intent.md v4.9 (POS.1100, POS.0810)
status: immutable
---

# Save and release duration — the measurements so far

## Question

How long does a save and a release of the engine take, and which
step costs the time, so that the lever pulled on 2026-09-05 (renders
and the check moved from `/save` to `/release`, POS.1100) can be
judged and the watch continued at the next releases? This note moves
the measurements out of the ledger, where they had lived as a free
text entry since 2026-09-02 (POS.0160, 2026-09-14: the ledger cites
and never copies; a measurement is a research note's).

## Measurements

| Date | Operation | Renders (parallel) | Check(s) | Notes |
|---|---|---|---|---|
| 2026-09-02 | first `/save` with parallel renders and the isolated `/check-forge` | 6:54 (README 6:54, release notes 2:45) | 5:00, a full `/check` of the forge project folded in | twelve minutes in all |
| 2026-09-03 | `/save` of intent 3.19 | 8:18 (README 8:18, release notes 2:24) | 4:19 | — |
| 2026-09-05 | first `/release` (release 3.34), after the lever | 7:07 (README 3:44, release notes 7:07) | 4:56 | `/save` now runs no render |
| 2026-09-06 | release 4.0 | 5:48 (README 5:48, release notes 5:11) | three checks in parallel 4:37 (light 2:13, project 3:03, engine 4:37); pre-save light check 1:33 | — |

## What the numbers say

- A render of the README or the release notes costs five to eight
  minutes; the two run in parallel, so the pair costs the longer of
  the two. A check costs four to five minutes; three in parallel
  cost the longest.
- Moving renders and the full check out of `/save` (POS.1100) cut a
  save to the light check alone, about a minute and a half; a
  release still costs ten to twelve minutes end to end.
- The README dominates: it is the longest render in every
  measurement but one. THR.0340 (the README split) bears on this
  directly: more renders per `/release` cost more minutes unless the
  README itself shrinks.

## Consult when

Judging the cost of a further render at `/release` (THR.0340),
revisiting what `/save` runs (POS.1100, POS.1140), or continuing the
watch at the next releases — append the next measurements as a new
note, never here.
