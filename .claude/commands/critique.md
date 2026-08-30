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
2. Present the delta summary to the principal in Czech: new findings
   (with severity), verified resolved, still open, newly obsolete, and
   what awaits his verdict.
3. Offer a **walkthrough** of the open findings (CLAUDE.md, Working
   methods): one finding at a time in order of severity, your
   recommendation with a one-sentence reason first — fix (an iteration
   of the assignment or intent), overrule (a DEC with the principal's
   reason), or leave open — then his verdict. Verdicts are carried in
   the conversation and written once at the end: states in the ledger,
   DEC records for overruled findings, fixes through `/forge`. Never
   delete findings; states only. Recommend, do not push; if he
   declines the walkthrough, the findings wait.
