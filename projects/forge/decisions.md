---
project: forge
---

# Decisions

<!-- Append-only. DEC.NNNN: decision, reason, date. Design-phase rejected
directions are recorded in 10-intent.md (REJ.NNNN); whether to back-fill
them here was THR.0070, resolved by DEC.0040 (no back-fill). -->

## DEC.0010 — No brief exists for this project; reconstruction discarded
- **Decision:** `00-brief.md` holds no brief content, only a note that
  the brief stage was skipped. The attempted reconstruction of a brief
  from the correspondence is discarded.
- **Reason:** The system was designed directly in conversation and the
  intent is the earliest authoritative record. A reconstructed brief was
  artificial and did not make sense; honestly recording the skipped
  stage preserves provenance better than a fabricated anchor.
- **Date:** 2026-08-02

## DEC.0020 — `/challenge` runs before the first draft (THR.0040)
- **Decision:** `/challenge` is run before the first `/draft`. Any
  further runs — after a draft, before approval — are at the discretion
  of whoever is running the process; no rule prescribes them.
- **Reason:** Before the draft, accepted challenges are cheap: the
  intent is still freely rewritten and nothing built on it has to be
  undone. The alternatives (end-only, or a size-based twice/once rule)
  either make changes expensive or introduce a large-vs-small criterion
  that would itself need defining.
- **Date:** 2026-08-02

## DEC.0030 — `/status` renamed to `/ledger` (THR.0050)
- **Decision:** The state-report command is renamed from `/status` to
  `/ledger` everywhere: command file, core `CLAUDE.md`, `README.md`,
  templates and ledger comments.
- **Reason:** Claude Code ships a built-in `/status` command and
  built-ins take precedence, so the collision is real, not
  hypothetical; the custom command could not be invoked reliably.
- **Date:** 2026-08-02

## DEC.0040 — No back-fill of design decisions (THR.0070)
- **Decision:** Decisions made before `decisions.md` was in use are not
  back-filled as DEC records. DEC records are kept from 2026-08-02
  onward.
- **Reason:** The design history is already recorded in the intent as
  POS and REJ items, with reasons; back-filling would duplicate it
  without adding information.
- **Date:** 2026-08-02

## DEC.0050 — DEC.0020 generalised: a layer is challenged before the next is derived
- **Decision:** The rule of DEC.0020 is generalised, as adopted in
  intent v1.20 (2026-08-15): `/challenge` may target any chain
  artefact, and a layer is best challenged before the next layer is
  first derived from it — for the intent, before the first
  `/forge assignment`. Any further runs remain at the discretion of
  whoever is running the process. The wording of DEC.0020 — tied to
  the retired `/draft` command and the version-1 world ending at the
  assignment — is superseded by this record; its reasoning stands.
- **Reason:** Recorded on critique finding FND.0040: the
  generalisation happened in intent v1.20 but the append-only log
  carried no amending record, so DEC.0020 read alone stated an
  outdated rule.
- **Date:** 2026-08-17

## DEC.0060 — CHL.0030 rejected: the growth path names direction, not destination
- **Decision:** CHL.0030 (the growth path contradicts the assignment
  boundary and displaces the functions owning BA and architecture) is
  rejected.
- **Reason:** The challenge reads POS.0700 as a commitment to a
  destination; the growth path names a direction only, and POS.0780
  (intent 2.8) fixes the scope: the chain deepens specification,
  never its reach into execution, and whether a delivery side would
  even live in the forge is deliberately open (THR.0140). The
  boundary of kind at a deeper layer, and the engagement of the
  functions owning it, are defined when that layer is taken up — the
  standing mechanics-when-taken-up discipline; this record marks
  CHL.0030 to be revisited at that moment.
- **Date:** 2026-08-18

## DEC.0070 — CHL.0060 rejected: the forge is a chosen pursuit, not a budgeted work stream
- **Decision:** CHL.0060 (the meta-work consumes the scarcest
  resource and the ceremony is already leaking) is rejected.
- **Reason:** The challenge governs the principal's attention as if
  the forge were a budgeted work stream; intent 2.8 records the
  opposite (POS.0780): the forge is a deliberately chosen pursuit,
  developed at the principal's discretion and pace, by his needs and
  by rollout feedback — a cost accounting of his own hours is not a
  dimension the intent will carry. The empirical premise also
  under-reads the subject work: both subject projects travelled the
  chain to a handover — agentic-platform to approved intent and
  assignment 1.0, flow-ba handed over and sleeping by decision while
  its recipients respond — and the seventeen-day meta share was the
  construction of the engine itself. The challenge stays on record
  as the standing counter-case.
- **Date:** 2026-08-18

## DEC.0080 — CHL.0120 rejected: the public engine starts with a fresh history; the company copy stays read-only
- **Decision:** CHL.0120 (a fresh history discards the git record
  the design relies on and leaves the only full copy on the
  employer's server; `git filter-repo` by path not considered) is
  rejected in its remedy; its risk is accepted.
- **Reason:** Filtering the history by path would remove the company
  projects' files but not the company in the text — commit messages,
  every version of the forge intent and its history, the challenge
  of 2026-08-17 and the research notes name it — so a clean history
  would need text filtering as well, work comparable to a fresh
  start with a residual risk that one leak becomes public for good.
  POS.0710 ("history lives in git") is not voided but started on the
  day of publication: recipes and renders are traceable in the public
  copy from its first commit. The one true point — the only complete
  record living on the employer's server — is accepted as it is: the
  GitLab copy stays read-only while it exists. Brief public-engine
  0.5.
- **Date:** 2026-08-29

## DEC.0090 — FND.0090 overruled: a position states the convention; the scripts' capability is no contradiction
- **Decision:** FND.0090 (POS.0550's "main only, no branches" and
  "only door to git, no exceptions" contradicted by THR.0220's facts
  that the scripts work on any branch and that the tag at an
  approved major is a manual git act) is overruled.
- **Reason:** POS.0550 states the forge's convention; that the
  scripts are capable of more than the convention uses is not a
  contradiction but the normal relation of a rule to its tool. The
  manual tag is a known gap and is settled in THR.0220 together with
  the rest of the git ceremony (option B introduces `forge-save
  -Tag`), not ahead of it; fixing it now would fix it twice. The
  finding returns only if THR.0220 changes POS.0550.
- **Date:** 2026-09-03

## DEC.0100 — CHL.0160 rejected: no migration tool for a third-party instance; the migration path is the same as the principal's
- **Decision:** CHL.0160 (the upgrade channel has one user who never
  upgrades; convention migrations between 3.0 and 3.45 are paid by
  hand by every other instance, and the observed response is a fork)
  is rejected.
- **Reason:** The colleague's system the challenge cites is a
  different project, not a fork of the forge, so the observed "fork
  point" is no evidence. The principal's own projects migrate at every
  change, in the same session as the convention. What holds is the
  fact the challenge names: no migration tool exists for a third-party
  instance — knowingly. Its migration path is the principal's own:
  after `forge-pull`, `/check project` on each project says what the
  conventions changed, the release notes' Action required lines say
  what to do, and Claude migrates on the user's word (POS.0940). A
  tool is built when a third-party instance needs one (THR.0190's
  trigger).
- **Date:** 2026-09-06

## DEC.0110 — Two IDs outside the tens and two recorded one-off edits of immutables accepted, never raised again
- **Decision:** The project check of release 4.0 raised two findings
  against the forge project's own record: `POS.0005` and `REJ.0125`
  sit outside the numbering in tens, and the ledger records two
  knowing edits of immutable documents — `last_change` written into
  the locked `00-brief-public-engine.md` on 2026-09-04, and the
  pre-publication rewrite of the challenges and research notes on
  2026-08-30. Both findings are overruled; the state stays as it is.
- **Reason:** IDs are never renumbered (CLAUDE.md, ID scheme), so the
  two IDs stay; the two edits were the principal's recorded one-off
  acts, each with its reason in the ledger, and immutability is a
  process rule, not a mechanism. No later check raises either again.
- **Date:** 2026-09-06

## DEC.0120 — `main` of the engine rewritten once to remove a private directory
- **Decision:** The save of intent 3.21–3.22 (commit b717a67) carried
  the principal's private `tmp/` at the engine root into the public
  repository — the directory had never been added to `.gitignore`
  though he had asked for it the day before. On his word the commit
  was amended without `tmp/` and `main` rewritten
  (`git push --force-with-lease`, 1f7cc06), and `/tmp/` added to
  `.gitignore`. Direct git outside the scripts and a rewrite of
  `main`, knowingly, once. GitHub may still hold the objects of
  b717a67 in its cache; only GitHub support can purge them, on the
  principal's request if he wants certainty.
- **Reason:** private content in a public repository outweighs the
  rule that the scripts are the only door to git and that `main` is
  never rewritten; the rewrite happened minutes after the push, before
  any other clone could have taken it. Recorded here on 2026-09-14,
  moved out of the ledger's Waiting section (POS.0160).
- **Date:** 2026-09-04

## DEC.0130 — The group "Working methods" of the intent starts at POS.0850, accepted, never raised again
- **Decision:** The project check at the release of 2026-09-20 found
  that the group "Working methods" of `10-intent.md` does not start at
  a hundred: its first item is POS.0850 and it runs POS.0850–0910,
  while every other group starts at a hundred. The finding is
  overruled; the numbering stays as it is.
- **Reason:** IDs are never renumbered (CLAUDE.md, ID scheme), so the
  numbers stay whatever their origin; a group is a plain heading with
  no ID of its own, and nothing that cites these positions is
  affected. The principal's word of 2026-09-20 to fix the low
  findings of the release by Claude's recommendation, which for this
  one is acceptance. On the pattern of DEC.0110; no later check
  raises it again.
- **Date:** 2026-09-20
## DEC.0140 — Four review files named outside the convention accepted, never raised again
- **Decision:** The project check at the release of 2026-09-27 raised,
  for the third time, four files under `reviews/` whose names fall
  outside `YYYY-MM-DD-critique-<lens>.md`: `2026-08-17-critique.md`
  and `2026-08-27-critique.md` carry no lens,
  `2026-09-06-critique-clarity-2.md` and
  `2026-09-06-critique-clarity-3.md` carry a run suffix. The finding
  is rejected; the names stay as they are.
- **Reason:** The first two are reports of the retired single critic,
  written before lenses existed (POS.0410); the other two are three
  runs of one lens on one day, which the convention does not foresee.
  All four are immutable and cited by the Findings rows of the
  ledger, so a rename would break the record for a cosmetic gain.
  Accepted in the ledger on 2026-09-11 and 2026-09-20; on the pattern
  of DEC.0110, no later check raises them again.
- **Date:** 2026-09-27

## DEC.0150 — The account of what stood before the reversal stays in POS.0950; FND.0450 rejected
- **Decision:** The check `history` of 2026-10-02 found that POS.0950
  tells how its rule on the commit identity was reversed and what
  stood before, and proposed to move both sentences into the history
  (FND.0450). The finding is rejected; the sentences stay.
- **Reason:** The reason of the position is what the field showed
  against the earlier state, and the sentence on the two-roles case
  rests on it; without the account the item said in one breath that
  the identity is resolved per host and that the per-host include was
  rejected. The principal restored the sentence by his verdict of
  2026-10-01, at step 7 of THR.0470. Settled by Claude on the
  principal's word of 2026-10-02 to resolve the findings of this
  report, his rule being that the intent must stay understandable.
- **Date:** 2026-10-02

## DEC.0160 — The clause on what the principal wants to be told stays in POS.0020; FND.0480 rejected
- **Decision:** The check `history` of 2026-10-02 found that POS.0020
  keeps what was rejected on the way to it, the clause "the record's
  "no warnings unless asked" rejected by the principal — he wants to
  be told of problems, holes and contradictions, as a question", and
  proposed to move it into the history (FND.0480). The finding is
  rejected; the clause stays.
- **Reason:** The clause says why the position holds, that the
  principal wants to be told, and without it "he" in the sentence
  reads as Claude. It was returned to the item at step 7 of THR.0470
  on a verifier's finding. Settled by Claude on the principal's word
  of 2026-10-02 to resolve the findings of this report, his rule
  being that the intent must stay understandable.
- **Date:** 2026-10-02

## DEC.0170 — The sweep of /ingest goes on reporting changed sources; FND.0710 rejected
- **Decision:** The check `single-source-of-truth` of 2026-10-02
  found that the sweep of `/ingest` reports sources changed since
  registration while the `project` check verifies the immutability
  of registered sources, one concern with two detectors, and
  proposed to leave the detection to the check (FND.0710). The
  finding is rejected; the sweep stays as it is.
- **Reason:** The sweep reports a changed file at the moment it asks
  what to do with it, which is the command's own work and what
  POS.0180 gives it; the principal confirmed its three ways for a
  thought project the same day. The check finds a breach by other
  signs and at another moment. Two moments of one concern are not
  one rule written twice. Settled by Claude on the principal's word
  of 2026-10-02 to decide the low findings of this report by his
  recommendation.
- **Date:** 2026-10-02

## DEC.0180 — The YAML quoting caveat stays in the three skeletons; that part of FND.0720 rejected
- **Decision:** The check `single-source-of-truth` of 2026-10-02
  found that the caveat on quoting a description that carries a colon
  followed by a space stands in `templates/check.md`,
  `templates/critic.md` and `templates/challenger.md` with no owner,
  and proposed to state it once in CLAUDE.md, Isolated reviewers
  (FND.0720). That part of the finding is rejected; the caveat stays
  in the three skeletons. The other part, the parts of a Lens section
  listed twice, is accepted.
- **Reason:** The caveat is a property of the harness's parser, not a
  rule of the forge, and it stands where it is acted on, in the
  skeleton a new agent file starts from. In CLAUDE.md it would be
  read at every session and by every reviewer for nothing (THR.0240).
  Where the rules for creating new types live is THR.0480.
- **Date:** 2026-10-02

## DEC.0190 — The major 5.0 claims no readiness for a company rollout; CHL.0210 rejected
- **Decision:** The challenge of 2026-10-09 read POS.0980's order of
  the audiences, the company first, as a claim that 5.0 is ready to
  be run in a company, and stacked on it the managed settings of a
  company's Claude Code, the eleven steps to a first question, one
  user per instance and the untouched cost lever (CHL.0210). The
  challenge is rejected; the intent does not change.
- **Reason:** A major closes a package of features and sends it out;
  it claims nothing about readiness for a deployment (POS.0300, the
  sentence of 4.65). POS.0980 names whom the engine is published for
  and in which order, not a date of a rollout. The company rollout
  has its own project, `forge-rollout`, and its questions, the
  managed settings first, belong to it and to the brief `next-gen`,
  where they stay; a fact about a company deployment is found there,
  with the deployment in front of it. The principal's words of
  2026-10-09: nobody said version 5 is ready for a company rollout.
- **Date:** 2026-10-09

## DEC.0200 — The rules stay as written, the principal's word above them recorded; CHL.0230 rejected
- **Decision:** The challenge of 2026-10-09 read five recorded
  exceptions as one pattern, that the rules are written as walls and
  held as preferences, and asked for a marking of positions into walls
  and defaults with a degraded form (CHL.0230). The challenge is
  rejected; no such marking is introduced.
- **Reason:** The five cases are three different things. POS.0930 was
  not bent: the position changed, the mirrored page on a faster model
  is the rule and THR.0410 its predecessor. DEC.0110, DEC.0120 and
  THR.0410 are the principal's word, recorded where every reader
  finds it: the rules of the forge bind Claude, not the principal,
  who is the final authority (CLAUDE.md, Roles; prime directive 5),
  and his recorded exception is the designed form, not a bend. The
  six edits of 2026-10-03 were a failure of conduct, and the answer
  was to tighten the rule into POS.1460, not to soften it. The lens
  `essence` ran on 2026-10-09. What is true for the user, that the
  principal's word stands above every rule and his exceptions are in
  `decisions.md`, CLAUDE.md says already and the documentation reads
  from it. A marking of positions would add a mechanism for five
  cases in sixty versions.
- **Date:** 2026-10-09
