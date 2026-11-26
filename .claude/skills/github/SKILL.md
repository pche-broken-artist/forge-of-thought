---
description: Take up what a visitor wrote on GitHub — bare = what waits, with a number = that issue or discussion read, and on the principal's word registered, threaded and answered
argument-hint: "[number] [project-slug]"
---

One issue or discussion of a repository on GitHub taken up (POS.2060,
SOL.1000). Reading and posting go through `scripts/forge-github.py`
and nothing else, never a raw `gh` (CLAUDE.md, prime directive 10);
what the script does, refuses and needs is its header's. The
repository is the engine's, or with a slug that project's. On GitHub
the forge reads and posts one comment: it edits, closes, deletes and
merges nothing, and a pull request is the integrator's with git
(CLAUDE.md, Persistence).

**Bare.** Say what waits: `python scripts/forge-status.py [slug]
--remote`, the `github:` lines as the script prints them. Nothing is
written.

**With a number: the item taken up.**
1. Read it: `python scripts/forge-github.py read <number> [--project
   <slug>]`. Say in a few sentences what it asks and who wrote it;
   what does not fit is raised as CLAUDE.md, prime directive 1, has
   it. Nothing is written, and each step below runs on the
   principal's word alone (CLAUDE.md, Working methods, Step by step).
2. A source, when he says so. The script makes the file, `read
   <number> -o <bundle>/<kind>-<number>-<short-slug>.md`, in the
   growing bundle `sources/github-issues/` of the project the
   repository belongs to, the engine's in `projects/forge`; it is
   registered there as `/ingest` registers a file of a growing bundle
   (`.claude/skills/ingest/SKILL.md`). The file is the item as it
   stood that day; what is said later is read from GitHub again,
   never written into it.
3. A thread, when he says so: `/thread`, its origin the path of the
   file (`.claude/skills/thread/SKILL.md`).
4. A reply, when he says so. Claude drafts it in the language of the
   item and shows it whole; on the principal's word the text is
   written to a file in the engine's `tmp/` and posted, `python
   scripts/forge-github.py reply <number> -F <file> [--project
   <slug>]`, and the address the script prints is said. One reply,
   one word. A reply that says what the forge did, a thread opened
   or a fix on main, is posted after that is done and saved.
