---
date: 2026-10-14
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-14

2 findings

## Findings

### FND.1640 — low — The line for POS.1530 to POS.1550 under Waiting on principal still says the solution design is to realise them, which 0.16 has done
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:366-371` ("decided at 5.9, to be realised in the solution design and the operating layer …") against `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:2-5` (version 0.16 of 2026-10-14, `last_change`: SOL.0650 and SOL.0660 created, SOL.0130, SOL.0400, SOL.0420 and SOL.0460 follow) and the six records of 0.16 in `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.history.md:54-59`; the ledger's own Documents row already carries 0.16 (`ledger.md:40`), so the line went stale within the same update.
- **Rule:** CLAUDE.md, Ledger — the ledger is kept current after every operation and Waiting on principal matches what is actually open.
- **Fix:** immediate fix: cut "the solution design and" from the line so that it reads "to be realised in the operating layer (…), then the README", keeping the rest.

### FND.1650 — low — Two open items the solution design assigns to the principal have no line under Waiting on principal
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:925-930` (TBC.0040, owner: principal, opened at 0.16 on 2026-10-14: whether the player page `docs/videos/index.html` gets a document kind) and `:922-924` (TBC.0030, owner: principal, since 0.1: the independent challengers of POS.0800); neither ID appears in `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:363-457`. The other two TBCs are covered: TBC.0010 names THR.0370's line itself (`:913-917`), TBC.0020 is carried by THR.0520's (`:918-921`, `ledger.md:381-382`). The POS.1530 line (`ledger.md:366-371`) and THR.0660 (`threads.md:947-956`) name `docs/videos/` but not the kind question.
- **Rule:** CLAUDE.md, Ledger — Waiting on principal lists what waits on the principal, one line per matter that has an ID: the ID, a few words, its state (`templates/ledger.md`, Waiting on principal).
- **Fix:** immediate fix: add one line each — "TBC.0040 — a document kind for the player page, or none; opened 2026-10-14 (solution design 0.16)" and "TBC.0030 — the independent challengers of POS.0800, not built; open since solution design 0.1" — or, if the principal would rather carry TBC.0040 with POS.1530's line, name it there.

## Facts
- The source `word-default-a4.docx` is a binary without an extract (POS.1040): the normal case, not a finding.
- The brief `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- No `work/` directory and no `sources/.gitignore` exist; the Work table is empty and consistent with the disk. The one Dependencies row (`ledger.md:105`) has its path on disk with its inner index (`C:\pche\_dev\forge-of-thought\projects\lib-allwyn\sources\fork-brd\00-INDEX.md`), is cited from `sources/00-INDEX.md:48` and from the research row and index entry of 2026-10-13; no index entry, recipe or chain file cites any other path outside the project (the only other `projects/<other>/` citations stand in the immutable challenge reports and in the `derived_from` front-matter of one immutable research note, neither a registrable citation under the Lens).
- FND.1610, FND.1620 and FND.1630 of the light check of 2026-10-13 stand resolved in the ledger and on disk (Documents rows 5.9 and 0.16 matching both front-matters, the `strategy` line saying it is tracked in the project ai-strategy, the bare file name in the FND.1600 row): verified, not reopened.
- Everything else agrees: the four briefs, the intent, the solution design and the seven recipes with their front-matter (status against version, `last_change` of the intent and of the solution design derived from the records of 5.9 at `10-intent.history.md:354-357` and of 0.16 at `40-solution-design.history.md:54-59`); all thirteen companions present with the template's front-matter, its current comment and their newest records in the log's shape (the two 1.0 briefs with their logs empty after the archive, as the rule allows); the eight Renders rows mirror the provenance of README.md, RELEASE-NOTES.md, CONTRIBUTING.md, docs/README.md and the four files of `renders/`; the three Published rows have their files and the three files their rows; the five sources and forty-four research notes each have a ledger row and an index entry and every row and entry its file; every file of `reviews/` and `challenges/` is cited by a Findings or Challenges row (the four files named outside the convention accepted under DEC.0140); all thirty-four open threads of `threads.md` have their line under Waiting on principal; every state word in the Findings and Challenges tables is the template's.
