---
id: THR.0190
concerns: intent
origin: research/2026-08-29-claude-code-packaging.md
status: open
---

A plugin as a later distribution layer. Claude Code
plugins would give the only real upgrade channel and project =
repository, but a plugin carries no `CLAUDE.md`, and commands are
discovered only up to the repository root — so it forces changes
nobody needs yet: shortening the core to a bootstrap skill injected by
a SessionStart hook (as Superpowers does; its repository `CLAUDE.md`
is for contributors only), rewriting the commands from
`projects/<slug>/` to the repository root, solving multi-project
operations. A `CLAUDE.md` split is not a cheap step: 435 lines, and
moving half the rules from always-on to on-demand is a behaviour
change ("200 lines" is a recommendation, not a limit). `@import` of
the forge `CLAUDE.md` into a user's works but carries only
`CLAUDE.md`, not commands and agents. No preparation now; taken up
when `forge-pull` proves an insufficient upgrade channel. Research:
`2026-08-29-claude-code-packaging.md`,
`2026-08-29-framework-distribution-in-the-field.md`.
2026-09-14: to be merged into the brief `engine-split` (THR.0230),
after THR.0350. The research
above answered a different question — how
the forge reaches users with projects of their own, where the clone
with nested repositories won (POS.0940), rightly — and is not
reused for the three-layer question; that question gets research of
its own.
2026-09-28, from `00-brief-elicitation.md`: the objections
recorded here largely fall once CLAUDE.md stays in the engine and
a framework is a package of instances; for the brief
`engine-split`.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
