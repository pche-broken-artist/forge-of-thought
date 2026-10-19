---
id: THR.0240
concerns: intent
origin: the principal
status: open
---

The size of CLAUDE.md. 523 lines on 2026-09-03 and
growing with every iteration; THR.0190 already records that a split
moves rules from always-on to on-demand and is a behaviour change, not
a cut. To be dealt with sooner or later whatever becomes of THR.0230,
which would help. Opened 2026-09-03 at the principal's direction. To
think through: what must be always-on, what can live in commands,
skills and templates and be read when its situation arises, and how
the effect is measured — by behaviour, never by line count. Measured
2026-09-06 at the THR.0270 trial (POS.1120): every reviewer subagent
receives, in its first user message before the task, the whole
CLAUDE.md together with `CLAUDE.local.md` (then still carrying the
git identities, since moved out, POS.0950), the assistant's memory
file and the git status — about 600 lines, the largest block of its
context, several times its own agent body and contract together; the
instance facts of `CLAUDE.local.md` (principal, language, git
identities) thereby reach an isolated reviewer that needs none of
them. The cost of CLAUDE.md is paid once per reviewer run, not once
per session. The single-source-of-truth check of 2026-09-06 (history
3.49) took CLAUDE.md from 636 to 584 lines by citation alone; what
must be always-on is still this thread's question. First instance
of the answer, 2026-09-14: the walkthrough paragraph became one
sentence and a pointer to a skill, with a hook repeating the hard
sentence at every prompt (POS.1170) — always-on is one sentence and
a pointer, the detail a file read when its situation arises.
The single-source-of-truth check of 2026-09-20 found seventeen
restatements; nine were settled the same day (history 4.16) and
eight low ones deferred until after THR.0390, whose condition fell
when that thread closed on 2026-09-26 — they are on the table
again, with no date set. They reach
into the wording of CLAUDE.md and into the Commands table the
README and `/man` derive from: state vocabularies enumerated in
three places, the critic contract restating prime directive 8, the
brief's rules restated in two state files, genre checklists beside
their skeletons, index fields and ledger columns restated by
`/ingest` and `/research`, the bundle index entry as a declared
copy, sentences echoed inside CLAUDE.md and in skills, rosters
written out by name. The report is not filed; a re-run of the check
gives them again.
2026-09-28: the elicitation per artefact (POS.1310) is the move of
the rules of particular artefacts out of CLAUDE.md into their
definitions. The brief's estimate is 43 to 53 lines fewer of 663
in the always-on part, the state files growing by about as much;
the line count is an effect, the proof is conduct (POS.1380).
2026-10-02: the move is done, by walkthrough (intent 4.49). The
eight low restatements, filed that day as findings of the check,
are settled with it; one stays parked, FND.0650, the genre
checklists beside their skeletons. What must be always-on beyond
that is still this thread's question.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
