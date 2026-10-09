---
description: Spin a requirement group off into its own project (principal's explicit decision only)
argument-hint: "<source-project> <group-name> <new-slug>"
disable-model-invocation: true
---

Execute only on the principal's explicit instruction — never propose-and-
run in one step (CLAUDE.md, Spin-off rule).

1. Confirm scope with the principal: list the items
   (REQ/OOS/CON/ASM/DEL/TBC/SCR)
   of group "$1" in project $0 that will move. He may adjust the list.
2. Create `projects/$2/` by the `/new-project` procedure (kind
   `thought`) — files only, no git: the new project's repository and
   remote are the principal's one-off act afterwards (CLAUDE.md,
   Persistence).
3. Derive `projects/$2/00-brief.md` from the relevant parts of the
   source 10-intent.md: a short brief, in the language settled at
   step 2, capturing why this became its own project and what it
   inherits. This brief is derived by Claude: present it to the
   principal as a draft and, on his word, approve it through the
   `/forge brief` procedure
   (`.claude/skills/forge/states/brief.md`, its Course).
4. Mine the brief into the new project's intent through the
   `/forge intent` procedure
   (`.claude/skills/forge/states/intent.md`, its Course), which
   creates 10-intent.md and keeps the Mined column.
5. In the source project, intent-first (CLAUDE.md, Working methods):
   record the spin-off in the source intent through the `/forge
   intent` procedure (the group's substance is now delivered by
   project *$2*), then derive the change in the source assignment
   through the `/forge assignment` procedure, which marks the moved
   items superseded (never deleted) and replaces the group with one
   link item — "REQ.NNNN: Delivered by project *$2*, see its
   assignment." This command itself writes only the DEC in
   decisions.md (the shape of a record: `templates/decisions.md`).
6. Update both ledgers and report the result.
