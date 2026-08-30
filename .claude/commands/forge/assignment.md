---
description: Iterate 20-assignment.md — distil the intent for the recipients
argument-hint: [project-slug]
---

Target: `20-assignment.md`.
Inputs: `10-intent.md`, `decisions.md`, the ledger.

Role: drafter. Distil the current `10-intent.md` into `20-assignment.md`
(audience: the recipients), using `templates/assignment.md`.

1. Read the inputs of the project ($1, or infer the current project
   from context; if ambiguous, ask), plus the existing 20-assignment.md
   if any.
2. Drafting rules:
   - Structured items, IDs `PREFIX.NNNN`, items in tens, each new group
     starting at the next hundred. Never renumber existing IDs.
   - Narrative only in Purpose & Context and Objective.
   - Write requirements as **shall / shall not**. Never use would, could,
     should, might, may, or MoSCoW wording.
   - **No priority tags and no priority column.** Everything is essential;
     an exception carries a note reading *optional*.
   - One idea per item, written once, in full correct UK English
     sentences. No item may depend on an external link to be understood.
   - Capitalise defined Terms and list them in the Terms section together
     with the prefixes actually used.
   - Carry the complete in-scope substance of the intent, as precisely
     as it can be written; omit nothing for brevity — there is no size
     target in either direction. Leaving a matter out is legitimate
     only as an explicit delegation (a DEL or TBC item). The boundary
     is assigning, not solving: machinery of executing delivery
     belongs to the recipients, but any apparatus (a stakeholder
     matrix, an impact analysis) may appear where the principal
     judges it part of setting direction.
   - Success criteria may be present, delegated, or deliberately absent.
     Ask the principal which, do not decide alone.
   - Delete empty sections and all template comments.
3. Where intent is ambiguous or silent on something the assignment needs,
   do not invent: raise it as a `TBC` item or ask the principal directly.
4. Versioning: drafts are `0.x`; `1.0` marks approval; after approval,
   changes go `1.1, 1.2 …` until the next approved integer. Update the
   Version History table (what changed and why) and the ledger. Status in
   front-matter must agree with the number.
5. Substance changes must trace back to 10-intent.md. If the principal
   asks for a substantive change directly in the assignment, propose the
   corresponding intent update in the same step. Wording-only fixes may
   edit the assignment directly.
6. Finish with a short delta summary in Czech and a recommendation whether
   a `/critique` run would be useful now.
