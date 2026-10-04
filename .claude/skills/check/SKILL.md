---
description: Run a check on the conformance of a project or the engine with the conventions — bare = check roster
argument-hint: "[check] [project-slug]"
---

Checks live as `.claude/agents/check-<name>.md` — one isolated agent
per check, each defined by what it verifies, said in its
`description`; the roster is the scan of those files. Adding a check
means adding an agent file from `templates/check-definition.md`; this command
does not change (who creates a check, and when: CLAUDE.md, Isolated
reviewers).

Shared behaviour: the contract skill named in each check file's
front-matter (CLAUDE.md, Isolated reviewers). Unlike the critic and
the challenger, a check agent writes nothing: it returns its report
and this command files it. This command chooses the check, passes
the target, files the report and presents it.

**Bare `/check` — the roster.** List the available checks (scan
`.claude/agents/check-*.md`, their `description` fields — each says
when it fits) and recommend which fits the moment; what a save or a
release runs is `/save`'s and `/release`'s to say. A recommendation,
never a gate; no check runs on Claude's own judgement.

**`/check <name> [slug]` — run it.** The target is a project by its
slug (the engine's own project is `forge`) or the engine root; which
of the two a check takes, and what a missing or an added slug means
to it, is its Lens section's to say — read it there. Invoke the
`check-<name>` subagent (Agent tool, session model) with the target
path and nothing else (CLAUDE.md, Isolated reviewers). More than one
check on one target may be launched at once and awaited together.

When it returns:
1. File the report, when it has findings. Write it into the target
   project (for the engine `projects/forge`) as
   `reviews/YYYY-MM-DD-check-<name>.md`, suffix `-2` if one exists
   for today: a front-matter of `date`, `project`, `check`, `target`
   and `reviewer: check <name> (isolated context)`, then the agent's
   text word for word — nothing added, dropped or reworded but the
   ID, the next free `FND.NNNN` of the project's sequence, in tens,
   set at the head of each new finding. Add a row per new finding to
   the ledger's Findings table (category `conformance`, state `open`,
   source review = this file); a finding the report names as reopened
   goes back to `open`. A library has no Findings table and no
   `reviews/` until its first finding: add both then, the table as
   `templates/ledger.md` has it. Reports of several checks on one
   target are filed one after another, never at once, so that no ID
   is given twice. A report that says "conforms" is filed nowhere.
2. Present the report to the principal as it came: the one-line
   verdict, then the findings in their ranking with their IDs,
   compactly.
3. Offer at once every finding marked "immediate fix" as one step
   (CLAUDE.md, Working methods, Step by step); apply on his word,
   state `resolved`.
4. End by offering a **walkthrough** of the remaining findings
   (`.claude/skills/walkthrough/SKILL.md`, the one owner of its
   shape and of the verdict words). What `accept` writes here: the
   fix, agreed here and written once at the round's end, state
   `resolved`; a rule worth changing goes to the intent. The other
   verdicts are the walkthrough's. Nothing blocks (POS.0430): a
   release may proceed with a finding parked.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. A check verifies conformance only.
