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
