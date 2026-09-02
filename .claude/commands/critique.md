---
description: Run the isolated critic subagent on the current project
argument-hint: [project-slug]
---

Invoke the `critic` subagent on project $1 (or the current project; if
ambiguous, ask). Pass it only the project path — no summary of the
drafting conversation, no explanation of intent beyond the documents
themselves. Its isolation from the conversation is the point.

When it returns:
1. Verify it created the review file and updated the ledger; fix ledger
   bookkeeping if needed (states, links), without altering the findings
   themselves.
2. Present the delta summary to the principal in the conversation language (`CLAUDE.local.md`): new findings
   (with severity), verified resolved, still open, newly obsolete, and
   what awaits his verdict.
3. End by offering a **walkthrough** of the open findings (CLAUDE.md,
   Working methods); its rules are stated there and nowhere else
   (POS.1070). Verdict vocabulary here: **fix** (an iteration of the
   assignment or intent, through `/forge`), **overrule** (a DEC with
   the principal's reason), **leave open**. Finding states in the
   ledger change only, never delete. If he declines the walkthrough,
   the findings wait.
