origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of Claude's proposal for mining the brief `00-brief-collaboration.md` v0.8 into the intent (the proposal of 2026-10-17, intent 5.12 to 5.13); translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the mining proposal for the brief `collaboration`

## 1. The positions are too large and carry realisation and history

POS.1600 is the whole section B of the brief in one paragraph: the
ledger outside git, six homes of state, state records and the
version, the script's reports, v+N, the price and the state render.
POS.1650 joins two windows, the worktree, the addressing, the
engine's exception and "the path through git". The intent's own
rules (prime directive 7 "structure over prose", POS.0310 "the way
to an item goes into its record, never into the item", the stable ID
as the unit of change) speak for a finer cut: when the Waiting rule
changes, it must not rewrite the position on the ledger outside git.
Proposed:

- Split 1600 into: the ledger derived at read time, outside git;
  state lives in records, never in a header (the six homes); state
  records and the version; what the script reports beyond that; the
  state render at a release.
- Split 1650 into: two windows (two projects, two trees, addressing
  by slug); the path through git (the state as the map's last word,
  pull before writing, the write step not fetching, the push of an
  ahead repository, a conflicting rebase by hand). The second is not
  about two windows.
- Take out of the positions what belongs to a history record or to
  the solution design: "over the principal's first word of immutable
  blocks", "the numbers put on the table changed the recommendation",
  "from the collision at the save of its 0.6" (that is `Was` and a
  reason in a record, not a stance); commit-tree, `--reserve`,
  `--worktree`, `--apply`, `--undo`, the dry run as the default (that
  is realisation, which the plan itself sends to the solution design,
  and two owners of one mechanism are against prime directive 10).
  POS.1660 is a good model of size: the stance, the reason, done.

## 2. A bare `/save` contradicts itself across the positions

POS.1650 says rightly for two projects: a bare `/save` would commit
the half-written work of the other window, so it takes a slug. For
two trees of one project it says "a bare save visits both trees" as
a desirable property, and POS.1690 repeats it. It is the same risk.
One rule: with two windows `/save` always takes a slug (`<slug>` or
`<slug>@<branch>`); the bare save is for one window.

## 3. Missing changes to existing positions

New positions were added, but the old ones that say the opposite
stayed untouched:

- The owner of the sentence "front-matter carries version, date,
  status and last_change" (POS.0300 or a neighbour): the list is
  supplemented only by "version and status on main only", not by the
  departure of `date` and `last_change`; without it POS.1570
  contradicts the older position.
- The owner of the language rule ("the language of its ledger
  header", prime directive 6): the brief named it, the mining plan
  did not; after POS.1590 the language is in the project file.
- POS.0960 (a library is born as the ledger alone): cited from 1590
  but not changed; after B0 it is born as the project file.
- The owner of the Waiting rule ("cite, never copy; free text only
  for a matter with no ID yet, which gets one at the next write"):
  the new rule in 1600 says "free text has no place", so the old
  wording must leave, not merely be overlaid.

## 4. Double ownership

- The driver's ordering rule (the side with `landed` first) is in
  1610 and in 1620. One owner; proposed 1620 (the driver), 1610
  cites.
- The rule of the free number ("neither used nor reserved") is in
  the addition to POS.0220 and in 1670. The owner is 0220 (the
  scheme), 1670 cites.

## 5. The horizon and the tests

The four releases in POS.1690 are a plan, not a stance; after the
second release the text will be history. "Decided" does not mean
"lasting". It belongs to the solution design (which realises) or to
THR.0620, where the plan after 5.0 already is and where row 9 is
being changed anyway. Of 1690 I would keep only the promise (that is
a real stance) and drop "what does not change", because it only
repeats other positions.

## 6. Small

- REJ: besides 0270 and 0280 I would record the directions someone
  will propose again: immutable blocks of the indexes (your own
  first word), a hundred across all prefixes per branch, `<base>+` in
  the header. The iterations of the brief as a whole no, that would
  be noise.
- Groups: 1560, 1620, 1640, 1650, 1660 and 1690 have no group
  assigned; they most likely belong where POS.1110 and POS.1490 sit
  (persistence).
- Write `v5.12+N` in a position as `v<base>+N`; the concrete number is
  an example from the brief.
- The assumptions you chose: the thread in the group state, the
  fifth digit as a change of 0220, the conversion as THR.0690, agreed
  with all three; the horizon inside 1690 no, see point 5.

Order: 1 and 2 before the write, 3 and 4 in the same round, 5 and 6
at your decision.
