---
date: 2026-09-03
project: forge
lens: clarity
reviewed: 10-intent.md v3.16, 00-brief.md (placeholder), 00-brief-public-engine.md v1.0,
  decisions.md (DEC.0010–0080), ledger.md (updated 2026-09-03),
  reviews/2026-08-17-critique.md, reviews/2026-08-27-critique.md;
  for regression only: CLAUDE.md (Persistence), README.md (render of
  2026-09-02), templates/ledger.md, scripts/*.ps1 (help text and
  identity handling)
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) — 2026-09-03

## Delta summary
- **New:** FND.0090, FND.0100, FND.0110, FND.0120, FND.0130, FND.0140,
  FND.0150, FND.0160, FND.0170, FND.0180
- **Verified resolved:** FND.0050, FND.0060, FND.0080
- **Still open:** —
- **Newly obsolete:** —
- **Delegated:** FND.0070 (divergence — the `essence` lens's category;
  not re-tested here)

## Scope note
First run of the clarity lens. This project has no `20-assignment.md`
by recorded decision (ledger, DEC.0010); each artefact was read on its
own — the intent as the record of current intent, the ledger as the
state record, decisions.md as the append-only log, the locked brief as
the principal's text (immutable; nothing is raised against it). The
findings of the two retired single-critic reports were divided by
category: FND.0050 (gap), FND.0060 (contradiction) and FND.0080
(inconsistency, read as contradiction within the ledger) are this
lens's; FND.0070 (divergence) is the `essence` lens's.

## Regression
- **FND.0050 — verified resolved.** CLAUDE.md (Persistence) now carries
  the Portability paragraph in POS.0830's terms; no script's help text
  contains a Windows path; `forge-save.ps1` carries no URL and no
  identity — it checks whether git resolves one and reports when it
  does not. The THR.0090 deferral recorded in the ledger's resolution
  is moot: the instance facts left the scripts at 3.0.
- **FND.0060 — verified resolved.** The Essence reads "Two isolated AI
  reviewers", the CLAUDE.md heading "Two isolated reviewers"; the only
  "independent" left in the README is "Independent challengers on a
  different model family" — the one use the finding allowed.
- **FND.0080 — verified resolved.** Both the forge ledger and
  `templates/ledger.md` open with "Freely rewritten (as are the
  material indexes …)".

## Findings

### FND.0090 [medium] [contradiction]
- **Location:** 10-intent.md POS.0550 vs THR.0220 (facts paragraph and
  option B); POS.0940
- **Issue:** POS.0550 states two absolutes — "linear history on `main`,
  no branches" and "Four PowerShell scripts are the only door to git —
  reading state included, no exceptions". THR.0220 records as facts,
  in the same document, that the scripts already commit, rebase, pull
  and push whatever branch is checked out ("only POS.0550's 'main only'
  says otherwise"), and that the git tag POS.0940 prescribes at every
  approved major "is today a manual git act outside the scripts". A
  thread may weigh options, but these are not options — they are the
  document's own statement that its position is not the case.
- **Why it matters:** A reader of POS.0550 alone (the position an
  agent editing the scripts or CLAUDE.md consults) takes "no
  exceptions" as the rule and will treat the manual tag, or a branch,
  as a breach; a reader of THR.0220 alone learns the opposite. Which
  reading governs `/check-forge` today is undecidable from the text.
- **Suggested fix:** Amend POS.0550 to what holds now — the scripts
  are branch-agnostic and the engine's convention (not the scripts'
  capability) is `main` only; the tag at an approved major is the one
  git act still outside the scripts, pending THR.0220 — so that the
  position is true and the thread carries only what is open.

### FND.0100 [medium] [contradiction]
- **Location:** 10-intent.md POS.0960 vs POS.0940
- **Issue:** POS.0960: "`/check` … reports a project that is not a
  repository as a finding." POS.0940: "a project starting 'not under
  git' is a property, not a defect." Both describe the same state of
  the same project, and one calls it a finding while the other says it
  is not a defect. POS.0820 ("a fact to report, never a defect to
  chase") offers a third vocabulary — a report that is not a finding —
  which neither of the two items uses.
- **Why it matters:** Whoever writes or reads the `/check` definition
  must choose between the two; the ledger's Findings table either gains
  a row for every fresh project or it does not. Two competent readers
  act differently.
- **Suggested fix:** Give POS.0960 the POS.0940 wording: `/check`
  *reports* a project not under git as a fact, never as a finding —
  and use the one term ("reports") in both items.

### FND.0110 [medium] [gap]
- **Location:** 10-intent.md POS.0400, closing sentence ("Which of them
  run at a save or a release is not decided here (THR.0220)")
- **Issue:** POS.0400 hands a question — whether the critic and
  challenger run at a save or a release — to THR.0220. THR.0220 does
  not contain it: the thread is the cost of regenerating README and
  release notes, and its three options mention only `/check` and
  `/check-forge`, never the two reviewers. The open matter has no home
  in the document.
- **Why it matters:** A reader following the reference finds nothing
  to weigh; the question is silently open with no thread and no owner,
  and at the next write of THR.0220 it will not be there to settle.
- **Suggested fix:** Either add the sentence to THR.0220's "to think
  through" list (whether `/release` in option B also runs a critique
  lens, and which) or open it as its own THR and cite that instead.

### FND.0120 [low] [contradiction]
- **Location:** 10-intent.md POS.1000, first sentence ("exactly as the
  engine has them (POS.0800, POS.0810)")
- **Issue:** The citation names the positions that define the engine's
  README and release-notes mechanism. POS.0800 is "Independent
  challengers will be built" and has nothing to do with renders; the
  engine's README and release notes are POS.0720 and POS.0730. POS.0810
  (regenerated renders pass under the principal's eyes) is at best a
  neighbour of the claim.
- **Why it matters:** The cross-reference is the reader's only pointer
  to the mechanism POS.1000 generalises; followed, it lands on the
  wrong subject.
- **Suggested fix:** Replace with "(POS.0720, POS.0730; POS.0810 for
  the review of the regenerated output)".

### FND.0130 [low] [contradiction]
- **Location:** 10-intent.md POS.0970 (opening sentence) vs POS.1000
- **Issue:** POS.0970 defines a library as "only `sources/` with its
  `00-INDEX.md`, a ledger and `research/`, no chain". POS.1000 gives
  every library a README rendered from `recipes/readme.md`; the
  ledger's Waiting-on-principal note goes further (recipes and renders
  for company audiences in a library) and says POS.0970 is to gain a
  sentence for it. As written, "only" excludes what POS.1000 requires.
- **Why it matters:** `/new-project` for a library and `/check` of a
  library are specified by these two items; one says the recipe and
  README must be there, the other that nothing else is.
- **Suggested fix:** Drop "only" in POS.0970 and list the library's
  contents once: ledger, `sources/` and `research/` with their
  indexes, `recipes/readme.md` and the README it renders (POS.1000) —
  the pending sentence on further recipes then has its place.

### FND.0140 [low] [ambiguity]
- **Location:** 10-intent.md POS.0950 (first paragraph: "The commit
  author comes from the user's git configuration"; last paragraph:
  "Rewritten at 3.8 back to the per-repository rule (adopted at 3.0,
  replaced by per-host at 3.6)")
- **Issue:** The item opens with the 2.21 sentence that the commit
  author "comes from the user's git configuration" and continues, a
  paragraph later, with the rule that the identity is a property of
  the project, set locally per repository by the command layer from
  the roster in `CLAUDE.local.md`. Read together the two sentences
  describe two sources of the identity; the first is what the second
  paragraph explicitly dropped. The closing sentence narrates the
  item's own version history (3.0, 3.6, 3.8) inside the position.
- **Why it matters:** POS.0950 is the item `/setup`, `/import-project`
  and `forge-save` are written against; "the user's git configuration"
  is exactly the global default the `useConfigOnly` guard exists to
  refuse. The history inside the item is what the Version History and
  THR.0260 are for.
- **Suggested fix:** Rewrite the first paragraph to the current rule
  in one sentence (the commit identity is set locally per repository;
  the engine carries none) and move the 3.0/3.6/3.8 narrative to the
  Version History, where it already is.

### FND.0150 [low] [ambiguity]
- **Location:** 10-intent.md POS.0500 ("one git repository named
  `forge` on disk"), POS.0600 ("Slug `forge` on disk") vs POS.0990
  (repository `forge-of-thought`)
- **Issue:** Two names are given for the engine "on disk": `forge`
  (POS.0500, POS.0600) and `forge-of-thought` (POS.0990, the public
  repository — which is also what a clone produces). `forge` is the
  slug of the system's own project under `projects/`, which POS.0500
  names separately in the same sentence.
- **Why it matters:** "Named `forge` on disk" is read by a newcomer as
  the directory to clone into; the README and `/setup` say otherwise.
  The one word that must be unambiguous — what `forge` refers to — is
  used for the repository, the project slug and the short name.
- **Suggested fix:** POS.0500 and POS.0600: the engine's repository is
  `forge-of-thought` (POS.0990); `forge` is the slug of its own
  project (`projects/forge`) and the short form in speech.

### FND.0160 [low] [duplication]
- **Location:** 10-intent.md POS.0560 vs POS.1010
- **Issue:** Both items state that `logo.png` in a repository root is
  the avatar. POS.0560 does so for the engine, "relying on GitLab's
  auto-detection" — a host the engine left at 3.0 (POS.0990) — and
  adds a deferred `assets/` directory; POS.1010 generalises to every
  project and to "hosts that do so". The general rule covers the
  engine; the special one names a host that no longer applies.
- **Why it matters:** Two items differing only in scope and in one
  stale host name; the next change to the avatar convention will be
  made in one and missed in the other.
- **Suggested fix:** Retire POS.0560 into POS.1010 (the engine is a
  project like any other for this purpose), carrying over only the
  `assets/` deferral if it is still wanted.

### FND.0170 [low] [contradiction]
- **Location:** ledger.md, "Waiting on principal": the migration entry
  and the Executive pitch entry
- **Issue:** The migration entry ends "Migration complete; the runbook
  stays as the record …" and, two sentences later, "Migration
  complete; nothing outstanding." — a closed matter, stated closed
  twice, under a heading that lists what waits. The Executive pitch
  entry says the recipe and its Renders row are "both uncommitted"
  and that the change "needs a future intent iteration (the next one —
  3.5 was consumed …)", while the same ledger's Documents table shows
  the intent at 3.16.
- **Why it matters:** The ledger is the single source of truth for
  state; `/ledger` reads it aloud. A reader is told a finished
  migration is pending and that the next intent version after 3.5 has
  not yet happened.
- **Suggested fix:** Drop the migration entry (its record lives in
  POS.0980 and the runbook) or reduce it to one line under a closed
  heading; rewrite the pitch entry to its present state — what was
  decided, what is still to be written into the intent — without the
  "next iteration" and "uncommitted" clauses.

### FND.0180 [low] [contradiction]
- **Location:** 10-intent.md POS.0005 ("PCHe (CTO) is the first
  principal and the owner of the engine — an instance fact") vs
  POS.0950 ("The engine carries no instance facts") and POS.0990 (the
  author named in the README "is not an instance fact")
- **Issue:** The intent of the public forge project is part of the
  engine (POS.0760). POS.0005 places a statement in it and labels that
  statement an instance fact; POS.0950 says the engine carries none;
  POS.0990 resolves the same person's name as the author's, not an
  instance's. The three cannot all hold as worded.
- **Why it matters:** "Instance fact" is a defined boundary term
  (POS.0950, `CLAUDE.local.md`, THR.0210); using it for something the
  engine deliberately carries blurs the one line the public boundary
  rests on.
- **Suggested fix:** In POS.0005 replace "an instance fact" with the
  POS.0990 term — the first principal is the engine's author — so that
  "instance fact" keeps its one meaning.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- POS.0850 states the recommendation-first rule twice ("For each item
  Claude first gives its recommendation with a one-sentence reason …"
  and "Claude puts one item in front of the principal, with its
  recommendation and the reason, and stops"). The 3.15 extension could
  absorb the earlier sentence.
- POS.0180 still describes the bundle index's shape in prose (YAML
  header, one paragraph, File table) while POS.1070 gives that shape
  an owner, `templates/index-bundle.md`. By POS.1070's own rule the
  prose description is the second copy; POS.0180 could cite the
  skeleton. The wider POS.0180 / POS.0840 overlap noted in the two
  previous runs stands.
- POS.0830 still ends "until then it is a writing rule, not a claim",
  with the Linux verification owned by nobody — repeated from
  2026-08-27; a note under Waiting on principal would keep it from
  becoming a claim by lapse.
- THR.0210 promises settlement "at the next iteration of this intent";
  sixteen iterations later the ledger says "deferred since". Rewording
  to "deferred" would stop the text disagreeing with its own state.
- THR.0200 cites "readme recipe 0.24" for the placeholder sentence;
  the recipe is at 0.33. A recipe version in a thread ages at every
  save — "the readme recipe" without a number would not.
- Several positions carry their own revision narrative (POS.0950's
  3.0/3.6/3.8, POS.1050's "3.7; narrowed … at 3.8", POS.1000's "(3.6)").
  If THR.0260 moves the Version History into a companion, these
  in-item histories are the residue worth sweeping at the same time.

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous? **yes** — the Essence and
  POS.0780 say what the forge is and where a run ends.
- Scope boundaries stated, with out-of-scope items where the topic
  invites creep? **yes** — POS.0780, THR.0140, the REJ list and the
  public boundary of POS.0980.
- Requirements written as shall / shall not, one idea each, no
  duplicates? **n-a** — no assignment by design; among the positions
  POS.0560/POS.1010 duplicate (FND.0160).
- Constraints separated from requirements (no leaked solutioning)?
  **n-a** — no assignment; positions and threads are separated, though
  THR.0220 now states facts that belong in a position (FND.0090).
- Deliverables actionable, with owners and timing where relevant?
  **n-a** — the handover artefacts are the core and README.
- Open questions each have an owner? **yes, with one orphan** — every
  THR sits with the principal and is mirrored in the ledger; the
  reviewers-at-save question of POS.0400 has no thread (FND.0110).
- Success criteria present, or explicitly delegated, or deliberately
  absent? **deliberately absent** — POS.0780; no SCR convention binds
  the intent layer.
- Detail of the assigning kind, not the solving kind? **n-a** — no
  assignment; the intent is the working document and may solve.
- Terms section present and matching what the document actually uses?
  **n-a** — the Terms rule binds assignments; the one defined term
  used inconsistently is "instance fact" (FND.0180).
- Any item that cannot be understood without an external link? **no**
  — external tools and hosts are named with their role in the text.
