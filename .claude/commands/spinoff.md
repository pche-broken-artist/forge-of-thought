---
description: Spin a requirement group off into its own project (principal's explicit decision only)
argument-hint: <source-project> <group-name> <new-slug>
---

Execute only on the principal's explicit instruction — never propose-and-
run in one step.

1. Confirm scope with the principal: list the items
   (REQ/OOS/CON/ASM/DEL/TBC/SCR)
   of group "$2" in project $1 that will move. He may adjust the list.
2. Create `projects/$3/` by the `/new-project` procedure (kind
   `thought`) — files only, no git: the new project's repository and
   remote are the principal's one-off act afterwards.
3. Derive `projects/$3/00-brief.md` from the relevant parts of the source
   10-intent.md: a short English brief capturing why this became its own
   project and what it inherits. **Exception to the verbatim rule:** this
   brief is derived, so write it as a draft (0.1) and present it to the
   principal; on his approval lock it (1.0, approved) and add its row to
   the ledger's Briefs table (Mined: pending).
4. Seed the new 10-intent.md v0.1 from the moved material.
5. In the source assignment: mark moved items superseded (do not delete),
   replace the group with one link item — "REQ.NNNN: Delivered by project
   *$3*, see its assignment." Bump the version, update Version History, and
   record a DEC in decisions.md.
6. Update both ledgers. Report the result and suggest `/forge intent` on the
   new project.
