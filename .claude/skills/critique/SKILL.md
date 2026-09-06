---
description: Run a critic lens on the quality of a project's documents — bare = lens roster
argument-hint: "[lens] [artefact] [project-slug]"
---

Critic lenses live as `.claude/agents/critic-<lens>.md` — one isolated
agent per lens, each defined by what it reads: `clarity` reads each
artefact on its own, `essence` reads the chain for drift. Adding a lens
means adding an agent file; this command does not change. New lenses
are created only by the principal's decision, and only where what they
read genuinely differs.

The rules shared by every lens — isolation, the documents-only remit,
regression first, calibration, the shape of a finding, the report file
and the FND ledger entries — live in the contract skill
`.claude/skills/critic-contract/SKILL.md`, preloaded into every lens file
through its front-matter, whose own part is its Lens section; nothing
of them is restated here (POS.1070, POS.1120). The critic is
the mirror of the challenger (`/challenge`): personas there, lenses
here, CHL there, FND here, a walkthrough for both. This command only
chooses the lens, passes the project and verifies the bookkeeping.

**Bare `/critique` — the roster.** List the available lenses (scan
`.claude/agents/critic-*.md`) and recommend which fits the project's
state — `essence` as soon as a second layer exists, `clarity` before a
handover. A recommendation, never a gate. No lens runs at a save;
`/release` offers `essence` once (POS.1100); every run is the
principal's word.

**`/critique <lens> [artefact] [slug]` — run it.** The target is an
artefact named as `/forge` names it — `brief`, `brief-<name>`,
`intent`, `assignment`, one day `brd` or deeper layers: for `clarity`
that artefact alone, for `essence` that artefact against its parent;
without one, everything the lens reads. Invoke the `critic-<lens>`
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
3. End by offering a **walkthrough** of the open findings (CLAUDE.md,
   Working methods); its rules are stated there and nowhere else
   (POS.1070). Verdict vocabulary here: **fix** (an iteration of the
   artefact concerned, through `/forge`), **overrule** (a DEC with the
   principal's reason), **leave open**. Finding states in the ledger
   change only, never delete. If he declines the walkthrough, the
   findings wait.
