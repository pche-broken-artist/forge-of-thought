origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the brief `00-brief-collaboration.md` v0.4; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the brief `collaboration` 0.4

## 1. The record of the mining belongs in the intent's history, not the brief's

B puts mined: partial, <note> into the brief's history as a changed
record. But the brief does not change by the mining; the intent
changes. The forge's rule reads "the record is written in the same
step as the change", and that change is in the intent. The record
therefore belongs in the intent's history with the subject
00-brief-<name>.md (the template allows a file as a subject). A side
gain that decides it: the version column of that record on main says
which version of the intent mined the brief, which is exactly the
information of today's row "mined into intent 4.32"; in the brief's
history that information would not be there. The brief's history
stays the history of the brief's changes. The same logic B already
uses for findings ("in the history of the artefact whose version
settled it").

## 2. State records and versions: decide whether they raise

The records mined, state: by hand, FND | closed, THR | closed are not
a change of a document's content. On main they are written today by
a round that as a rule changes content too; after B there will also
be rounds that are only state (a walkthrough of /check that fixes
skills and closes findings, the intent does not change). Two
questions the brief must answer: (a) does a state record raise the
version on main? I recommend no: it carries the current version, a
round of state records only is not a version. (b) Does forge-land
raise the version when a branch has only state + records? Either the
same rule (it raises only at a record created | changed | removed |
approved over an item or a section of the document; landed is
appended with the version unchanged), or simply always raises and the
release-notes recipe tolerates a version without content changes. The
second is simpler and I would take it; just write it, today it cannot
be told from the text. A small consequence: +N in the provenance
counts state records too, so a state record marks a render stale; the
same as today at every raise of the version, acceptable.

## 3. F2, three additions

- The reservation at the reflection, not at the write. The write step
  is one write per round on confirmation; a round may bring new items
  of three prefixes, so three network rounds inside the write, and
  when the network drops in the middle, the write of the whole round
  fails, whose content until then is only in the conversation. The
  reflection before the write already knows which prefixes the round
  needs; the reservation belongs there. The write does not touch the
  network.
- Which hundred. The example "THR 1600 to 1690" suggests a distant
  block; with a reservation per prefix the natural one is the nearest
  free hundred of the prefix (THR at 0680 reserves 0700). Say it.
- Blocks are never released, and that has a consequence for groups: a
  group of positions born on a branch has the hundred reserved by
  that branch; after the landing main adds further items to it by the
  rule "overflow anywhere", not in its hundred. The readability
  "group = hundred" for groups from branches falls. Acceptable, and
  one more argument for five digits, where dead hundreds cost
  nothing. Write it as a known consequence, do not leave it to be
  discovered.
- Minor: the name and the place of the reservation file (ids.md in
  the project's root, for the engine projects/forge/ids.md) are
  missing.

## 4. Five digits: the scope is larger than two regexes

I searched the repository: the four-digit shape of an ID is fixed in
27 places in 15 files. The code is two scripts (forge-history.py,
docs_map.py); the rest is the text NNNN in CLAUDE.md, eight templates
and four skills (critic-contract, check-contract, check, spinoff).
The change of code is therefore small, as the brief says, but the
textual one is 13 files and belongs in M. The recommendation of five
digits does not fall by it, only let "two regular expressions" not
sound like the whole scope.

## 5. The rule of Waiting diverges from today's practice

B: "parked ones do not wait". Today's ledger, however, keeps FND.0650
in Waiting (parked, "needs a pass over the recipe genres"), because
it waits for the principal's pass. The derived rule must say when a
parked item waits: either never, and the parked ones get a heading of
their own under Waiting with the note from the DEC, or it waits when
its DEC says "until <event>" and the event has occurred, which the
script cannot judge. I recommend the first: Waiting = open threads,
TBCs owned by the principal, open findings of a critic and open
challenges (they wait for a verdict); open findings of a check do not
wait (Claude fixes them in a walkthrough); the parked ones under a
heading of their own. Today's list is hand-curated and differs in
both directions, so let that decision be explicit.

## 6. Minor

- A: "nothing else enters a header" would take title and author from
  the brief and project, directory from the index; what is meant is
  "nothing that changes". Reword.
- A2: add to the list of traps >, |, *, + and 1) at the start of a
  sentence; the same category as - and #.
- F1 and a double landed with the same key (two clones on main, both
  landed the same day, the same author): the driver leaves them side
  by side and the script reports "two versions with one number". It
  is an unsupported case, but let it be written that this path
  reports it, so that nobody looks for another.
- Verification: let test 1 have at least one round of state only (a
  closed finding without a change of the intent), to verify point 2.
