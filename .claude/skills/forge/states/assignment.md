---
description: Iterate 20-assignment.md — distil the intent for the recipients
---

Target: `20-assignment.md`.
Inputs: `10-intent.md`, `decisions.md`, the ledger.

Role: drafter. Distil the current `10-intent.md` into `20-assignment.md`
(audience: the recipients), using `templates/assignment.md`.

1. Read the inputs of the project (the slug argument, or infer the current project
   from context; if ambiguous, ask), plus the existing 20-assignment.md
   if any. Whether the intent is ready to be derived from: CLAUDE.md,
   Document chain 2 — say so before drafting, never as a gate.
2. Drafting rules: the ID scheme, Requirement style and prime
   directives 7 and 8 (structure over prose; completeness, assigning
   not solving) of CLAUDE.md apply as written there (POS.1070). This
   command's own rules:
   - The Terms section lists only the prefixes and terms actually
     used, as the template says.
   - Success criteria may be present, delegated, or deliberately
     absent. Ask the principal which, do not decide alone.
   - Delete empty sections and all template comments.
3. Where intent is ambiguous or silent on something the assignment needs,
   do not invent: raise it as a `TBC` item or ask the principal directly.
4. Write per CLAUDE.md, Versioning & status, into
   `20-assignment.history.md` — created from `templates/history.md`
   with the first draft — and update the ledger.
5. Substance and wording changes follow intent-first (CLAUDE.md,
   Working methods). If the principal asks for a substantive change
   directly in the assignment, propose the corresponding intent
   update in the same step.
6. Finish with a short delta summary
   and a recommendation whether
   a `/critique <lens>` run would be useful now.
