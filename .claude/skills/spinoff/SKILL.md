---
description: Spin a requirement group off into its own project (principal's explicit decision only)
argument-hint: "<source-project> <group-name> <new-slug>"
disable-model-invocation: true
---

Execute only on the principal's explicit instruction — never propose-and-
run in one step.

1. Confirm scope with the principal: list the items
   (REQ/OOS/CON/ASM/DEL/TBC/SCR)
   of group "$2" in project $1 that will move. He may adjust the list.
2. Create `projects/$3/` by the `/new-project` procedure (kind
   `thought`) — files only, no git: the new project's repository and
   remote are the principal's one-off act afterwards.
3. Derive `projects/$3/00-brief.md` from the relevant parts of the
   source 10-intent.md: a short English brief capturing why this
   became its own project and what it inherits. **Exception to the
   verbatim rule:** this brief is derived, so present it to the
   principal as a draft; on his approval lock it through the
   `/forge brief` procedure (its step 4).
4. Mine the locked brief into the new project's intent through the
   `/forge intent` procedure (its step 2), which creates 10-intent.md
   and keeps the Mined column.
5. In the source assignment: mark moved items superseded (do not delete),
   replace the group with one link item — "REQ.NNNN: Delivered by project
   *$3*, see its assignment." Write per CLAUDE.md, Versioning & status,
   into the assignment's companion, and record a DEC in decisions.md.
6. Update both ledgers and report the result.
