---
date: 2026-10-23
project: forge
lens: essence
target: all
reviewed: 00-brief.md (placeholder, DEC.0010), 00-brief-public-engine.md v1.0, 00-brief-elicitation.md v1.0, 00-brief-documentation.md v0.1, 00-brief-brd.md v0.2 (all four unchanged since 2026-10-18 by their histories; the run of 2026-10-18 distilled them), 00-brief-next-gen.md v0.4 with its history, 00-brief-collaboration.md v0.9 with its history, 10-intent.md v5.32 (Essence, the headings and IDs read whole; Operating environment, Versioning and state, Rejected directions, Candidate structure, POS.0220, POS.1590 read in full), 10-intent.history.md (the records of 5.30 to 5.32), threads/ (the open set by status), 40-solution-design.md v0.40 (whole), decisions.md (DEC.0280), ledger.md (2026-10-23: Briefs, Documents, Findings), reviews/2026-10-18-critique-essence.md (regression), .claude/agents/critic-essence.md
reviewer: critic lens essence (isolated context)
---

# Critique (essence) — 2026-10-23

## Delta summary
- **New:** FND.2440, FND.2450, FND.2460, FND.2470, FND.2480
- **Verified resolved:** FND.1790, FND.1800, FND.1810, FND.1820
- **Still open:** none
- **Newly obsolete:** none

Regression:
- **FND.1790:** POS.1750 now says the verification runs on the fixture alone and never on a real clone (DEC.0240). The fixture is one project made by hand, and the results stand in the cells of the cutover plan. Verified.
- **FND.1800:** THR.0710 was closed at 5.31 on the principal's word ("neither form"), and POS.1760 was removed into REJ.0350. Nothing in the design is held provisional against the intent any more. Verified.
- **FND.1810:** POS.1640 and SOL.0680 carry "a THR cited without a file". The left-out report has its reason in the record of 5.24. Verified.
- **FND.1820:** POS.1580 named the source until 5.31, when the position was removed into REJ.0380. Nothing remains to hold. Verified.

I checked mechanically that every POS of intent 5.32 is cited in the design. Two positions are missing (finding 4 below). Every other position has a part's Realises or a mention.

## Findings

### FND.2440 [medium] [shifted] — The design's opening still describes the merging and the git door that the intent let go
- **Location:** 40-solution-design.md, "How the parts work together", the paragraphs "Git, the conversion of documents and the hook are scripts …" and "Every file has a way of merging …"; against 10-intent.md POS.1560, POS.0550, POS.1200 and the design's own SOL.0730, SOL.0520, SOL.0840.
- **Issue:** The head names five ideas that carry the forge. Two of them no longer hold:
  - It says "records merge as sets by a driver". POS.1560 (5.31) has three ways of merging, the record files merging as text with a conflict settled as two tails kept both. The driver is REJ.0340. SOL.0730 in the same document says this correctly.
  - It says "The harness denies Claude raw `git`, so the scripts are the only door". POS.0550 has made reading git open (since 2026-10-21). POS.0550 and POS.1200 give the finishing commands of a conflict to the hook's ask (2026-10-23). SOL.0520 and SOL.0840 describe that.
- **Why it matters:** The head is the part of the design that says how the whole fits together. Someone reading it first gets the architecture of brief 0.8 and of the old door, which the intent has abandoned. Only the parts below correct it.
- **Suggested fix:** Bring the two paragraphs to POS.1560 and POS.0550/POS.1200:
  - three ways, with records merging as text and a conflict settled in the step of a conflict;
  - scripts as the door to a *write* of git, reading open, and the ask for the commands that finish a conflict.

### FND.2450 [medium] [provenance] — Six rejected directions and one position still give the let-go driver, landing and blocks as their reason
- **Location:** 10-intent.md:
  - REJ.0270 ("(POS.1730)")
  - REJ.0280 ("(POS.1670)")
  - REJ.0290 ("the driver has the mutable case for the map anyway (POS.1670)")
  - REJ.0300 ("the version on a branch is computed and reported, never written (POS.1660, POS.1640)")
  - REJ.0310 ("the records stay one file one line and merge by the driver (POS.1670)")
  - REJ.0320 ("blocks per author assigned by hand need neither (POS.1730)")
  - POS.1600 ("tolerates the shape one release back, as the driver does (CHL.0280)")
  - Against: 00-brief-collaboration.md v0.9 (Principle, "Let go 2026-10-23"); REJ.0330, REJ.0340, REJ.0370; the mining record of 5.31.
- **Issue:** The 5.31 mining of brief 0.9 rewrote or removed every *position* that rested on the driver, the landing and the blocks. It did not touch the *reasons* of the rejections made on 2026-10-17 against those same mechanisms. Four of them now state as the forge's present something that brief 0.9 and REJ.0330/0340/0370 let go:
  - REJ.0310 says records "merge by the driver".
  - REJ.0300 says a branch's version is "computed and reported".
  - REJ.0320 says blocks per author make the reservation unnecessary.
  - REJ.0290 says the driver has a mutable case for the map.
  The other three citations point at positions that no longer exist (POS.1660, POS.1670, POS.1730). The mining record lists the positions it changed and does not name these rejections.
- **Why it matters:** A rejection's reason is what stops the direction from coming back. Where the reason is "the driver does it instead", and the driver is itself rejected, the old direction loses its ground silently. `merge=union` (REJ.0280) is a live case: both proposals of 2026-10-23 asked for it again (DEC.0280).
- **Suggested fix:**
  - Restate each reason on what stands today: text merging and two tails kept both for REJ.0280, REJ.0290 and REJ.0310; POS.1790 for REJ.0270, REJ.0300 and REJ.0320.
  - Point the citations at REJ.0330, REJ.0340 and REJ.0370 where the removed position was the alternative.
  - Drop "as the driver does" from POS.1600.

### FND.2460 [low] [shifted] — The fifth digit of an ID outlived the let-go of F2, and its only reason is the reservations that were rejected
- **Location:** 10-intent.md POS.0220 ("Why: … reservations by the hundred spend them faster than use; the widening costs less before the reservations than after"); against 00-brief-collaboration.md v0.9, Mechanism ("Let go 2026-10-23: … F2"), section F2 and section M ("the fifth digit is a textual migration of the engine"); REJ.0370; the 5.31 record of POS.0220.
- **Issue:**
  - In the brief, the five-digit shape is part of F2, and brief 0.9 lets F2 go whole.
  - The intent keeps the fifth digit, which CLAUDE.md also carries. That may well be intended, since it was built and costs nothing.
  - However, the 5.31 rewrite of POS.0220 kept "Why" word for word. That reason rests entirely on the reservations, which REJ.0370 rejects.
  - Neither the mining note nor any record says that the fifth digit was deliberately kept out of what F2 let go.
- **Why it matters:** Measured against brief 0.9, the intent carries a piece of F2 that the brief no longer wants. The reason it gives is one the same version rejects. A reader cannot tell a deliberate keep from something the mining overlooked.
- **Suggested fix:** Either give the fifth digit a reason that stands without the reservations (a prefix has 99 hundreds and the engine's POS already stand past 1700), and add a clause to the mining record that it was kept from F2. Or, if it was not meant to survive, open a thread.

### FND.2470 [low] [lost] — Two positions of the intent have no place in the design since the worktree part was removed
- **Location:** 10-intent.md POS.1700 and POS.1780; against 40-solution-design.md, every part's Realises and the head's list of positions no part answers.
- **Issue:**
  - POS.1700 (a bare `/save` is for one window; two windows on one project are left to git) was realised by SOL.0770 (the worktree). SOL.0770 was removed at 0.39, and no part or head mention took POS.1700 over.
  - POS.1780 (born at 5.31) is an order of work, the same kind as POS.1380, which the head lists among the positions no part answers. POS.1780 stands neither there nor in any Realises.
  - The design cites every other position of intent 5.32.
- **Why it matters:** The design says of itself that every position has a part or is named as having none. These two are the only exceptions, so the claim is no longer true. POS.1700 does carry a buildable rule, the slug on a bare `/save` across two windows. Whether that rule has a home is now invisible.
- **Suggested fix:** Add POS.1780 to the head's list of positions no part answers. Name the part that realises POS.1700's bare `/save` (SOL.0530 or SOL.0510), or add it to the same list if it is conduct only.

### FND.2480 [low] [shifted] — The design still plans the fixture script that the intent dropped
- **Location:** 40-solution-design.md SOL.0830 (the body: `scripts/fixture.py`, two projects, `--shape`, `--no-git`, "until it is built") and SOL.0510 ("`fixture.py` (SOL.0830) is not built"); against 10-intent.md POS.1750 ("one project made by hand", 5.31) and its record of 5.31, whose `Was` read "one project made by hand until the script that makes it is built".
- **Issue:**
  - At 5.31 the intent removed "until the script that makes it is built". The fixture is now one project made by hand, with no script waiting.
  - SOL.0830 still opens with the script as the part. It says "Not built; let go with the deferred releases (DEC.0280)", and two sentences later "until it is built". It keeps Realises: POS.1750.
  - By SOL.0530's rule, every release's walkthrough walks the "Not built" items to turn them over to built.
- **Why it matters:** The layer below plans a mechanism that the layer above stopped wanting. As written, the item invites building the script at a later release on the authority of a decision that let it go.
- **Suggested fix:** Make SOL.0830 the hand-made fixture that POS.1750 describes. Move the design of `fixture.py` into the item's Choice as what was designed and let go (DEC.0280), and drop "until it is built" and the "not built" in SOL.0510. If the script is meant to stay a plan, say so in POS.1750 first (intent-first).

## Recommendations
- 00-brief-next-gen.md v0.4, "Where it stands on 2026-10-22", still says "the second and the fourth deferred, DEC.0250". DEC.0280 has since cancelled them. The brief is pending and is to be worked through again before mining (the principal's word of 2026-10-22), so this is something to carry into that pass, not a defect of the intent.
- SOL.0530 cites POS.1650 (the state render) in its text but not in its Realises. Adding it there would make the coverage readable from the Realises lines alone.
- The head of the design names `/save` running the check `light` but not POS.1100's `--quick`. This is carried over from the last run; wording.

## Distillations

### 40-solution-design.md v0.40 — essence
Read first, before the intent.
- **What it is:** The architecture of the forge, handed over to Claude and not judged whole by the principal. It says what cannot be read off the files, part by part: what each part answers for, the choice behind it, and where it lives.
- **The ideas it rests on:** One always-on core with everything else read when its situation arises. State in the project's Markdown. Isolation bought with subagents on one model. Git, conversions and hooks as scripts. Every file with a way of merging that the forge tells git. The head's own wording of the last two ideas still carries the record driver and "no raw git".
- **Since the last run:**
  - The brief's later releases are gone: driver, landing, worktree, ID allocation, `/merge`, the conversion.
  - The first release is marked built: project file, ledger at read time, header without changing fields, threads as files, attributes, registration, migration.
  - SOL.0840 is new: the step of a conflict. `forge-save` leaves a conflicting rebase standing, the conflict is a walkthrough over both sides, and the finishing commands run on the hook's ask.
  - SOL.0520's hook now answers allow / ask / deny.
- **What it rules out:** designing the wording of any file, how an artefact is found, or anything beyond the forge's files.
- **What it leaves open:** Mermaid in Word, the check that keeps it true, the independent challengers, and `forge-branch` tracking an origin branch. The fixture script stays half-planned (SOL.0830).

### 10-intent.md v5.32 — essence
Read second, before the briefs.
- **What it wants:** A general-purpose engine in Claude Code in which anyone's thought travels from briefs through an intent into the layers a project needs. Claude is the cognitive extension that proposes and never decides, and isolated reviewers provide adversarial pressure. It holds:
  - the working methods;
  - elicitation per artefact in seven blocks;
  - the brief, intent, assignment and solution design, each with its aim;
  - history as a log, the header without changing fields, the ledger made at read time with its state in records, threads as files;
  - one reviewer mechanism with unique report names;
  - git through scripts for writes, with reading open and the finishing commands of a conflict on the hook's ask;
  - three ways of merging;
  - for collaboration, one person as the norm and two as the exception handled with git. The forge helps settle a conflict (the step of a conflict), IDs stay sequential, and a clash or a version given twice is settled by whoever merges. The model is one integrator and N contributors, and the engine's own project runs as an open-source repository;
  - two windows as a direction, not a mechanism;
  - a migration command for shape changes;
  - an order for operating-layer changes that need a test: brief, build and test, then intent and design.
- **What it rules out:** gates, priorities, a feedback channel, a wrapper of git, plugins now, recipes per page, a site, `merge=union`. Since 5.31 also the version as a landing, the driver, `/merge`, the worktree, blocks of IDs, and one sentence per line.
- **What it leaves open:** 30 open threads, among them the engine split, user extensions, the gate, the behaviour test, and work on another model.
- **What no longer holds:** Several older rejections still reason with the let-go mechanisms.

### 00-brief.md — essence
A placeholder: the brief stage was skipped (DEC.0010). No pair to review.

### 00-brief-public-engine.md v1.0, 00-brief-elicitation.md v1.0, 00-brief-documentation.md v0.1, 00-brief-brd.md v0.2 — essence
None of these changed since 2026-10-18; their histories carry no record after that day. Their essences are as the run of 2026-10-18 distilled them: the public engine and its conditions; one shape of definition for elicitation; the documentation as generated pages; the BRD from the fork's.

### 00-brief-next-gen.md v0.4 — essence
- **Aim:** The requirements for a forge that can be rolled out into real operation, thrown in to be sifted and thought of as a whole. It looks for no solutions.
- **Sections:** the shape of the whole, user modifications, work without a known artefact, further outputs, automation, several people, connection to systems, upgrade, behaviour testing, operation in a company, clean-up, news, the threshold of entry. Each section has its research.
- **New at 0.4:** "Where it stands on 2026-10-22" records what was taken up elsewhere: documentation, collaboration, the solution design and the migration. It folds in the plan of THR.0620 (the pilot, the second pass of the intent, extensions before the split, the behaviour test, small items) and the questions for the mining. The principal's word is that the brief is worked through again before it is mined.

### 00-brief-collaboration.md v0.9 — essence
- **Principle:**
  - The forge never merges, pulls or rebases on its own judgement.
  - One person is the norm.
  - Two people are the exception, handled with git as everyone knows it; the forge does not stand in for git.
  - Where git leaves a conflict, Claude lays both sides out, the person decides and Claude writes.
  - The forge's own project meets other hands as an open-source repository with one integrator.
- **What was built and what was let go:** The first release (5.26) removed the causes of the collisions. Everything designed beyond it is called "a git built over git" and let go: the driver, `/merge`, worktrees, the landing, blocks of IDs (F2 whole), one sentence per line. Where a rule of the forge or its harness stands in the way, it changes, the hook's wall included.
- **The promise:**
  - Derived state never conflicts.
  - A record file's conflict is two tails kept both.
  - An artefact's conflict is the same item changed on both sides, settled with Claude's help.
  - `/save` leaves the conflict standing, and the finishing commands run on the hook's ask.
  - IDs stay sequential, with a clash renumbered by POS.0220. A version given twice is settled by whoever merges.
  - Two windows are not solved.
- **Verification:** one test on the fixture with two clones.
- **Open:** nothing in the mechanism. Two windows remain a direction.

### 00-brief-public-engine.md, 00-brief-elicitation.md, 00-brief-documentation.md, 00-brief-brd.md → 10-intent.md — comparison
Unchanged since the last run. The intent changes since then that touch them have provenance of their own:
- the project outside git (POS.0550, POS.1740) cites GitHub issue #3 and the repo-detection challenges;
- the growing bundle (POS.0180) cites THR.0730.
Nothing lost and nothing added without provenance.

### 00-brief-next-gen.md → 10-intent.md — comparison
The brief is pending by the ledger and is to be reworked before mining, so nothing of it is expected in the intent. Its new section names what was answered elsewhere, which settles the recommendation of the last run. Only its reference to DEC.0250 has gone stale (Recommendations).

### 00-brief-collaboration.md → 10-intent.md — comparison
The redirection is mined (record of 5.31):
- POS.1560 reaches three ways;
- POS.1710 the step of a conflict;
- POS.1200 the ask;
- POS.1750 the promise;
- POS.1770 the open-source integrator;
- POS.1790 IDs and versions after a merge;
- POS.1700 two windows as a direction.
Every let-go mechanism has its REJ (REJ.0330 to REJ.0380) and DEC.0280. The brief's verification matches POS.1750, and its "what does not change" matches POS.0220 and POS.1110.

Two differences have no trace:
- The older rejections and POS.1600 still reason with the let-go driver, landing and blocks (finding, provenance).
- The fifth digit, part of F2 in the brief, stays in the intent with a reason the same version rejects (finding, shifted).

POS.1780 cites no brief. It cites the principal's confirmation, which is its stated provenance.

### 10-intent.md → 40-solution-design.md — comparison
The design was brought to 5.31 part by part:
- SOL.0730 three ways;
- SOL.0520 the ask;
- SOL.0840 the step of a conflict, realising POS.1710, POS.1750, POS.1790, POS.1560 and POS.1770;
- SOL.0740 and SOL.0150 without the driver's key;
- removed parts traced to REJ.0330 to REJ.0380.

Three differences remain:
- The head's summary of merging and of the git door is still the old one (finding, shifted).
- POS.1700 lost its part with SOL.0770, and POS.1780 is in neither a part nor the head's list (finding, lost).
- SOL.0830 still plans `fixture.py`, which POS.1750 replaced with a hand-made project (finding, shifted).

No part of the design carries substance that the intent lacks beyond these.
