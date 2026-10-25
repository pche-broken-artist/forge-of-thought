---
id: THR.0760
concerns: intent, solution-design
origin: the principal
status: open
---

The source archive GitHub makes of a tag should hold the engine
alone. Every Release on GitHub carries "Source code (zip)" and
"Source code (tar.gz)", made by `git archive` from the tagged
commit; today they hold the whole tree, `projects/forge/` with its
three hundred files and `tmp/` included, so that a reader who takes
the archive instead of a clone gets the forge's own thought project
beside the engine. `git archive` honours the attribute
`export-ignore` of `.gitattributes`, so the engine's list (SOL.0730)
can leave both out of the archive while they stay in the repository;
the same attribute governs the Download ZIP of the repository's
front page. What the thread must settle: whether an archive is a
way in at all, since the forge runs on git from the first command
and the archive carries no `.git`; what "the engine alone" leaves in
(`docs/` stays, a reader without the net reads it there); and that
the change takes effect only from the next tag, `v6` keeping the
archive it has. Parked 2026-10-25 at the publication of the v6
release on GitHub, to decide before the next tag. Opened 2026-10-25.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
