---
description: Run a critic lens on the quality of a project's documents — bare = lens roster
argument-hint: "[lens] [artefact] [project-slug]"
---

Critic lenses live as `.claude/agents/critic-<lens>.md` — one isolated
agent per lens, each defined by what it reads, said in its
`description`; the roster is the scan of those files. Adding a lens
means adding an agent file from `templates/critic.md`; this command
does not change (who creates a lens, and when: CLAUDE.md, Isolated
reviewers).

Shared behaviour: the contract skill named in each lens file's
front-matter (CLAUDE.md, Isolated reviewers). This command only
chooses the lens, passes the project and verifies the bookkeeping.

**Bare `/critique` — the roster.** List the available lenses (scan
`.claude/agents/critic-*.md`) and recommend which fits the project's
state — `essence` as soon as a second layer exists, `clarity` before a
handover. A recommendation, never a gate. No lens runs at a save;
`/release` offers `essence` once (POS.1100); every run is the
principal's word.

**`/critique <lens> [artefact] [slug]` — run it.** The target is an
artefact named as `/forge` names it (CLAUDE.md, Isolated reviewers);
how it narrows the run is the lens file's. Invoke the `critic-<lens>`
subagent on the project (infer it from context; if ambiguous, ask),
naming the target if given. Pass only the project path and the
target — no summary of the drafting conversation, no explanation of
intent beyond the documents themselves. Its isolation from the
conversation is the point.

When it returns:
1. Verify it created the review file and updated the ledger; fix ledger
   bookkeeping if needed (states, links), without altering the findings
   themselves.
2. Present the delta summary to the principal in the conversation
   language (`CLAUDE.local.md`): new findings (with severity), verified
   resolved, still open, newly obsolete, and what awaits his verdict.
   For `essence`, the distillations first — they are what the findings
   rest on.
3. End by offering a **walkthrough** of the open findings
   (`.claude/skills/walkthrough/SKILL.md`, the one owner of its
   shape). Verdict vocabulary here: **fix** (an iteration of the
   artefact concerned, through `/forge`), **overrule** (a DEC with the
   principal's reason, in the shape of `templates/decisions.md`),
   **leave open**. Finding states in the ledger
   change only, never delete. If he declines the walkthrough, the
   findings wait.
