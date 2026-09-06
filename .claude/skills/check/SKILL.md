---
description: Run a check on the conformance of a project or the engine with the conventions — bare = check roster
argument-hint: "[check] [project-slug]"
---

Checks live as `.claude/agents/check-<name>.md` — one isolated agent
per check, each defined by what it verifies, said in its
`description`; the roster is the scan of those files. Adding a check
means adding an agent file from `templates/check.md`; this command
does not change (who creates a check, and when: CLAUDE.md, Isolated
reviewers; a rule verified by two checks is a defect).

The rules shared by every check — isolation, the conformance-only
remit, read-only, findings only, the shape of the report — live in
the contract skill `.claude/skills/check-contract/SKILL.md`, preloaded into
every check file through its front-matter, whose own part is its Lens
section; nothing of them is restated here (POS.1070, POS.1140). The
check runs on the same mechanism as the critic (`/critique`) and the
challenger (`/challenge`): a roster, one agent per entry, a
walkthrough after. Unlike them it files nothing: the report returns
to the session and its findings are settled there. This command only
chooses the check, passes the target and presents the report.

**Bare `/check` — the roster.** List the available checks (scan
`.claude/agents/check-*.md`, their `description` fields) and recommend
which fits the moment — `single-source-of-truth` before a major or
after a round on the operating layer; what a save or a release runs
is `/save`'s and `/release`'s to say. A recommendation, never a
gate; no check runs on Claude's own judgement.

**`/check <name> [slug]` — run it.** The target: for `project` and
`light` a project by its slug (the engine's own project is `forge`;
`project` without a slug runs over every project under `projects/`
except `forge`, each reported on its own); for `engine` and
`single-source-of-truth` the engine root, no slug needed — a slug
given to `single-source-of-truth` names a project to read against the
engine's owners. Invoke the `check-<name>` subagent (Agent tool,
session model) with the target path and nothing else — no summary of
the working conversation, no explanation of what was meant; its
isolation is the point (POS.0930). More than one check on one target
may be launched at once and awaited together.

When it returns:
1. Present the report to the principal as it came: the one-line
   verdict, then the findings in their ranking, compactly.
2. Offer at once every finding marked "immediate fix" as one step
   (CLAUDE.md, Working methods, Step by step); apply on his word.
3. End by offering a **walkthrough** of the remaining findings
   (CLAUDE.md, Working methods); its rules are stated there and
   nowhere else (POS.1070). Verdict vocabulary here: **fix** (agreed
   here, written once at the round's end — CLAUDE.md, Working
   methods, Walkthrough), **defer** (recorded in the project's ledger
   under "Waiting on principal"), **accept** (the state stays as it
   is; a rule worth changing goes to the intent). Nothing blocks
   (POS.0430): a release may proceed with a finding deferred.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. A check verifies conformance only.
