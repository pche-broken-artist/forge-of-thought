---
date: 2026-09-06
project: forge
lens: clarity
target: intent v3.41
reviewed: 10-intent.md v3.41; 10-intent.history.md (rows 3.38–3.41,
  for last_change and version agreement); decisions.md (DEC.0010–0090);
  ledger.md (updated 2026-09-06); reviews/2026-09-03-critique-clarity.md;
  reviews/2026-09-05-critique-harness.md; for one fact only: the
  listing of .claude/commands/ (sixteen files). The retired
  single-critic reports (2026-08-17, 2026-08-27) were not re-read:
  their findings of this lens were verified on 2026-09-03 and concern
  documents outside this run's target.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) — 2026-09-06

## Prompt check
My context contains the sections Subject, How to work and Output; all
three arrived in the first user message, after the task text, wrapped
as a command message (`<command-message>critic</command-message>`), not
in the system prompt. The Lens section is in the system prompt.

## Delta summary
- **New:** FND.0290, FND.0300, FND.0310, FND.0320, FND.0330, FND.0340
- **Verified resolved:** FND.0100, FND.0110, FND.0120, FND.0130,
  FND.0140, FND.0150, FND.0160, FND.0170, FND.0180
- **Still open:** —
- **Newly obsolete:** —
- **Respected:** FND.0090 (overruled, DEC.0090). Its return condition —
  THR.0220 changing POS.0550 — did fall at 3.33, but POS.0550 now reads
  "branches allowed and left to git (POS.1110)" and no longer states
  the absolutes the finding named; nothing returns, as the ledger
  records.

## Scope note
Target: the intent alone, read as the record of current intent. The
ledger and decisions were read for regression and for the overruled
finding, not critiqued; nothing below is raised against them. The
front-matter agrees with the companion: `version: 3.41`, `status:
draft`, and `last_change` summarises the newest history row.

## Regression
- **FND.0100 — verified resolved.** POS.0960: "`/check` … reports a
  project that is not a repository … as a fact, never as a defect
  (POS.0940)"; the one term "reports" in both items.
- **FND.0110 — verified resolved.** POS.0400's closing sentence now
  answers the question it used to hand away: "Neither runs at a save;
  `/release` offers `critique essence` once … (POS.1100)".
- **FND.0120 — verified resolved.** POS.1000 cites "(POS.0720,
  POS.0730; POS.0810 for the review of the regenerated output)".
- **FND.0130 — verified resolved.** POS.0970 lists the library's
  contents once, `recipes/readme.md` and the README included, with no
  "only".
- **FND.0140 — verified resolved.** POS.0950 opens with the current
  rule ("The commit identity is set locally per repository; the engine
  carries none"); the 3.0/3.6/3.8 narrative is gone. One residue —
  "adopted at 3.6" — is noted under Recommendations.
- **FND.0150 — verified resolved.** POS.0500 and POS.0600 name the
  repository `forge-of-thought` and `forge` as the project slug and
  the short form in speech.
- **FND.0160 — verified resolved.** POS.0560 is gone; POS.1010 carries
  the avatar rule and the `assets/` deferral.
- **FND.0170 — verified resolved.** The ledger's migration entry is one
  closed statement; the Executive pitch entry states what was decided
  and what waits ("Waits for a round of `/forge intent`").
- **FND.0180 — verified resolved.** POS.0005: "PCHe (CTO) is the
  engine's author and its first principal (POS.0990)"; "instance fact"
  keeps its one meaning.

## Findings

### FND.0290 [medium] [contradiction]
- **Location:** 10-intent.md POS.0540 and the Essence ("Two isolated
  AI reviewers") vs POS.1120 and THR.0290
- **Issue:** POS.0540 states that the conformance checks have "their
  own guard, distinct from the two reviewers" and that document quality
  and substance "remain the reviewers' territory". POS.1120 states that
  "each kind of reviewer — the critic, the challenger, and check as the
  third kind at the same level (THR.0290)" owns a contract skill, and
  THR.0290 records: "Fixed 2026-09-06 by the principal's word: check is
  a kind of reviewer at the level of the critic and the challenger".
  The document thus says check is not a reviewer and that it is one.
  The decided half lives inside an open thread, and that thread also
  carries its own superseded layer: one sentence says "which checks run
  at a save or a release is the same question as for the reviewers
  (THR.0220)" — a closed thread — and a later sentence says the
  question "is thereby answered".
- **Why it matters:** POS.0540 is the position a reader consults to
  learn what `/check` is; POS.1120 is the one consulted to build it.
  Read separately they give two answers; read together the reader must
  guess which is current, and the decision that settles it is not
  findable among the positions.
- **Suggested fix:** Move the decided sentence of THR.0290 (check is a
  kind of reviewer with its own contract) into a position — POS.1120,
  or POS.0540 rewritten as "conformance is the third kind of review;
  until its kinds exist, `/check` and `/check-forge` run as today" —
  and let THR.0290 carry only what is open (the kinds, `/research`,
  the fate of `/check-forge`, the order of work). Reword the Essence's
  "two reviewers" so it does not age with the third kind.

### FND.0300 [medium] [duplication]
- **Location:** 10-intent.md POS.0570, POS.0810, POS.0930, POS.1100;
  THR.0290
- **Issue:** The division of labour between `/save` and `/release` is
  written four times: POS.0570 ("`/save` runs no check at all … `/release`
  then re-renders `README.md` and `RELEASE-NOTES.md`"), POS.0810 ("A
  render is regenerated only by `/release` or by the principal's
  explicit `/render`"), POS.0930 ("`/release` launches … the only
  renders any command runs … `/save` runs none"), POS.1100 ("`/save` is
  commit and push … with no check and no render … `/release` … the full
  check … the README and release notes"). The light check that `/save`
  will one day run is described twice with the same list — POS.0570
  and THR.0290 ("ledger bookkeeping, version and status agreement, the
  companion row").
- **Why it matters:** The document's own POS.1070 names the failure
  mode: copies drift, and the copy without a rule loses it. The four
  statements already differ in what they mention (POS.0810 omits the
  check, POS.0930 omits the tag), so the next change to the split will
  be made in one and missed in three.
- **Suggested fix:** Let POS.1100 own the two-command shape in full;
  reduce the sentences in POS.0570, POS.0810 and POS.0930 to a clause
  citing it ("only `/release` and an explicit `/render` regenerate,
  POS.1100"). Name the light check's content once — in THR.0290 as the
  open matter — and let POS.0570 cite the thread.

### FND.0310 [low] [ambiguity]
- **Location:** 10-intent.md POS.1120 ("decided when a third kind
  exists"; "every lens or persona file of that kind"), THR.0290 ("one
  agent per kind of check (`check-<name>`)"), POS.0960, POS.1080
- **Issue:** "Kind" now denotes four things in the document: the kind
  of a project (POS.0960, `thought | library`), the kind of a document
  (POS.1080, thirteen kinds), the kind of a reviewer (POS.1120: critic,
  challenger, check) and the kind of a check (THR.0290). Within
  POS.1120 the word is undecidable: the item names check as "the third
  kind at the same level" and, five sentences later, defers a further
  skill to "when a third kind exists" — check already exists as a kind
  by the first sentence, so the reader cannot tell whether the deferral
  has lapsed. The third reviewer's variants have no name: the critic
  has lenses and the challenger personas (POS.0400), POS.1120 speaks of
  "every lens or persona file of that kind", and THR.0290 calls them
  "kinds of check".
- **Why it matters:** The vocabulary is what the operating layer, the
  rosters and `/check-forge` will be written against; a builder reading
  "when a third kind exists" today will either build the shared skill
  now or never.
- **Suggested fix:** In POS.1120 replace "when a third kind exists"
  with the event meant (for instance "when the `check` contract is
  built"). Give the check's variants a word and use it in POS.1120 and
  THR.0290 alike. Where "kind" is used for reviewers, qualify it
  ("kind of reviewer") so it stays apart from the kinds of POS.0960 and
  POS.1080.

### FND.0320 [low] [contradiction]
- **Location:** 10-intent.md THR.0330 ("the fifteen commands") vs
  POS.1090
- **Issue:** THR.0330 counts fifteen commands. POS.1090 enumerates the
  command set: eight guarded (`/save`, `/release`, `/spinoff`,
  `/setup`, `/new-project`, `/import-project`, `/ingest`, `/render`)
  and eight model-invocable (`/forge`, `/ledger`, `/check`,
  `/check-forge`, `/critique`, `/challenge`, `/research`, `/recipe`) —
  sixteen. The directory holds sixteen files. POS.0550 records the
  document's own lesson on counts ("the count stated here went stale
  three times and is no longer stated").
- **Why it matters:** THR.0330 prescribes a migration "all in one round
  and none before it", where a partial migration is the named risk; a
  count that is one short invites exactly that.
- **Suggested fix:** Drop the number in THR.0330 ("every command file")
  or correct it to sixteen.

### FND.0330 [low] [contradiction]
- **Location:** 10-intent.md POS.0840 ("as a reviewer agent carries
  its skeleton's fixed sections"); POS.0420 ("The shared skeleton is
  invariant … The shared skeleton has one owner, the contract skill …
  created from the lens-file skeleton")
- **Issue:** POS.0840 explains the bundle index by analogy to a
  mechanism POS.1120 retired: a reviewer file no longer carries its
  skeleton's sections verbatim — it "carries its front-matter and its
  Lens section, nothing else" and names a contract skill. POS.0420 uses
  "skeleton" for two different things in one item: the shared
  behaviour (now the contract skill) and the template a persona file
  is created from (`templates/challenger.md`, "the lens-file
  skeleton").
- **Why it matters:** "Skeleton" was the defined name of the copied
  shared text; after POS.1120 it names the template only. An analogy to
  the retired meaning teaches a newcomer the old mechanism, and the
  double use in POS.0420 leaves "shared skeleton" and "contract"
  competing for one thing.
- **Suggested fix:** In POS.0840 drop the analogy or replace it with
  the current one ("as a lens file names its contract skill"). In
  POS.0420 call the shared behaviour the contract throughout and keep
  "skeleton" for the template.

### FND.0340 [low] [duplication]
- **Location:** 10-intent.md POS.0160, POS.0180, POS.0840, POS.1080
- **Issue:** The rules of the resource index are written more than
  once. The bundle index's shape appears in POS.0180 ("a YAML header
  (bundle, project, date, origin), one paragraph …, and one entry per
  file in the shape of the directory index") and in POS.0840 ("the
  bundle's header and opening paragraph its own, the entry carried
  verbatim from `templates/index.md`"), while POS.0840 also names the
  owner of that shape, `templates/index-bundle.md`. That the index is
  freely rewritten while its files stay immutable is stated in
  POS.0160, POS.0180 ("a rewritten catalogue, not an immutable
  document"), POS.0840 and the POS.1080 table. Raised as a
  recommendation on 2026-08-27 and 2026-09-03; since 2026-09-04
  POS.0840 carries the shape in full, so the two descriptions now
  coexist at equal weight.
- **Why it matters:** Two full descriptions of one shape, each citing
  the other, are the copy pair POS.1070 forbids in the operating layer;
  in the intent they are the source those files are aligned to, so
  drift starts here.
- **Suggested fix:** Let POS.0840 own the index (shape, owner template,
  rewritability) and reduce POS.0180 to the ingest-side facts (when a
  bundle index is created or validated) with a citation; drop the
  index clause from POS.0160, whose content the POS.1080 table now
  carries.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- POS.0730 uses "highlights" before saying what they are ("names its
  tag in its highlights … and opens with two to four sentences of
  them"); putting the two-to-four-sentence opening first would define
  the word where it is met.
- POS.1120 carries its own trial log and build log (what arrived in
  which prompt, line counts before and after, which findings were
  settled with it). The position is the rule; the trial facts are what
  the history companion and the ledger hold, and the last run noted the
  same pattern in POS.0950 and POS.1050. One residue of FND.0140
  survives in POS.0950 ("adopted at 3.6").
- POS.0850 still states the recommendation-first rule twice (noted
  2026-09-03); POS.0830 still ends "until then it is a writing rule,
  not a claim" with the Linux verification owned by nobody (noted
  2026-08-27 and 2026-09-03); THR.0200 still cites "readme recipe 0.24"
  while the recipe is at 0.37 (noted 2026-09-03).
- POS.0110 says "every brief to date was composed outside the forge"
  as of 2026-08-27; a reader in September must know the date to read
  it correctly. "At that date" or the fact without the "so far" would
  keep it true.
- Typography: POS.0970 opens with two colons ("kind `library`: no
  chain: a ledger"); the headings "### Structure and style of an
  assignment" and "## Open threads" follow their previous item with no
  blank line, unlike every other heading in the document.

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous? **yes** — the Essence and
  POS.0780 say what the forge is and where a run ends.
- Scope boundaries stated, with out-of-scope items where the topic
  invites creep? **yes** — POS.0780, THR.0140, the REJ list, the public
  boundary of POS.0980.
- Requirements written as shall / shall not, one idea each, no
  duplicates? **n-a** — no assignment by design; among the positions
  the save/release split and the index rules are written more than
  once (FND.0300, FND.0340).
- Constraints separated from requirements (no leaked solutioning)?
  **n-a** — no assignment; positions and threads are separated, though
  THR.0290 carries a decision that belongs in a position (FND.0290).
- Deliverables actionable, with owners and timing where relevant?
  **n-a** — the handover artefacts are the core and README.
- Open questions each have an owner? **yes** — every THR sits with the
  principal and is mirrored in the ledger with its trigger or order.
- Success criteria present, or explicitly delegated, or deliberately
  absent? **deliberately absent** — POS.0780; no SCR convention binds
  the intent layer.
- Detail of the assigning kind, not the solving kind? **n-a** — no
  assignment; the intent is the working document and may solve.
- Terms section present and matching what the document actually uses?
  **n-a** — the Terms rule binds assignments; the one term used in
  more senses than it can carry is "kind" (FND.0310), and "skeleton"
  has kept a retired sense in two items (FND.0330).
- Any item that cannot be understood without an external link? **no**
  — external tools, plugins and hosts are named with their role in
  the text.
