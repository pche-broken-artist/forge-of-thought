---
description: Run a critic lens on the quality of a project's documents — bare = lens roster
argument-hint: "[lens] [artefact|path] [project-slug]"
---

Critic lenses live as `.claude/agents/critic-<lens>.md` — one isolated
agent per lens, each defined by what it reads, said in its
`description`; the roster is the scan of those files. Adding a lens
means adding an agent file from `templates/critic-definition.md`; this command
does not change (who creates a lens, and when: CLAUDE.md, Isolated
reviewers).

Shared behaviour: the contract skill named in each lens file's
front-matter (CLAUDE.md, Isolated reviewers). Like `/check`, the lens
agent writes nothing: it returns its report and this command files
it. This command chooses the lens, passes the target, files the
report and presents it.

**Bare `/critique` — the roster.** List the available lenses (scan
`.claude/agents/critic-*.md`) and recommend which fits the project's
state, by the fit each lens states in its `description`. A
recommendation, never a gate. No lens runs at a save; what a release
offers is `/release`'s (`.claude/skills/release/SKILL.md`); every run
is the principal's word.

**`/critique <lens> [artefact|path] [slug]` — run it.** The target is an
artefact named as `/forge` names it, or any file of the project by its
path (CLAUDE.md, Isolated reviewers); how it narrows the run is the lens
file's. Remake the project's ledger first, `python
scripts/forge-ledger.py <slug>`, so that the agent reads a current
file (SOL.0680); then invoke the `critic-<lens>`
subagent on the project (infer it from context; if ambiguous, ask),
naming the target if given. Pass only the project path and the
target, nothing else (CLAUDE.md, Isolated reviewers).

When it returns:
1. File the report. Write it into the project as
   `reviews/YYYY-MM-DD-critique-<lens>.md`: the agent's text word for
   word, its front-matter included, nothing added, dropped or reworded
   but the IDs: the next free `FND.NNNN` of the project's sequence, in
   tens, set at the head of each new finding and listed in the delta
   summary's New line; then `python scripts/forge-report.py <path>`;
   the printed name is the one the ledger cites. Then `python
   scripts/forge-ledger.py <slug>`: how the report becomes rows is
   `templates/ledger.md`'s (Findings); a finding the report has as
   newly obsolete gets a DEC with the Verdict `obsolete` at the
   walkthrough.
2. Present the delta summary to the principal in the conversation
   language (`CLAUDE.local.md`): new findings (with severity), verified
   resolved, still open, newly obsolete, and what awaits his verdict.
   For `essence`, the distillations first — they are what the findings
   rest on.
3. End by offering a **walkthrough** of the open findings
   (`.claude/skills/walkthrough/SKILL.md`, the one owner of its
   shape and of the verdict words). What `accept` writes here: an
   iteration of the artefact concerned, through `/forge`, state
   `resolved`. The other verdicts are the walkthrough's. If he
   declines the walkthrough, the findings wait.
