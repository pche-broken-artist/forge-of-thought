origin: pasted into the conversation by the principal on 2026-10-18, the third piece of the review of the architect's second challenge of the cutover plan (`sources/cutover-challenge-review-2.md`), written in the conversation's language by a model in a session outside the forge after reading the write of that review: four corrections of the plan and of POS.1730; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-18

# Review of the architect's second challenge of the cutover plan, third piece

The introduction says the trigger of the fourth release is "a second
author writing into a project", the heading of Release 4 already has
the second clone too. Complete the introduction.

R1.26 says "the engine and every project together", but the tag in
that step goes to the engine alone (`forge-save forge --tag`); the
projects tag in R1.25, immediately before their migration, as
decided. Let R1.26 say the engine only; "together" belongs to the
way back, not to the tag.

R1.00's tag `shape-5.x`: a concrete number, not x; at the time of
R1.00 it is the intent's version before R1.24 (today 5.22). And since
the script adds the tag "at every release with a migration", that
sentence belongs into R1.24 and R5.07 as a closing too (the fixture
tagged `shape-<version>` after the release), otherwise nobody will
remember it.

R2.13's test: "no duplicate after the merge" assumes that the two
branches allocate one after the other (the second sees the first in
the refs). A concurrent allocation in two windows before the save of
either branch can clash, because the refs carry only what is
committed; that is a known limit of the rule (not a defect) and
belongs into POS.1730 as a sentence: "reads the committed state of
the branches; two windows allocating in the same round before a save
may clash, the remedy POS.0220". Let the test mirror it: the
allocation after the save of the first branch.
