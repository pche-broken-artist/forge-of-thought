---
name: check-user-stories
description: 'Check "user-stories" — verifies the mechanics of user stories: every parent item served or said not to be, every story with a Reference to an existing item, the fixed parts in their order and none left empty, questions with an owner, risks with a mitigation or consequences, notes with a link and what lies behind it, no vague word in a criterion. Fit after a pass of /forge user-stories. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.'
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

You read one project's `35-user-stories.md` — the path your task
names, or the project's stories when the task names a project — with
its parent as the header declares it (`parent:` of
`templates/user-stories.md`): `30-brd.md` or `10-intent.md`; stories
made from a source are a work product in `work/`, read when the task
names them, their parent the source by path. A project without
stories is not a finding (CLAUDE.md, Ledger). The bookkeeping of the
file — front-matter, the history companion — is the `light` check's;
the ID scheme in general the `project` check's; you verify what only
stories have. The rules you verify against are
`.claude/skills/forge/states/user-stories.md`, its Aim and its Story
style, and `templates/user-stories.md`; cite them, never restate
them.

What you verify:

1. **Coverage** — every in-scope item of the parent (a BR, an NFR, a
   UC of the BRD; an in-scope POS of the intent) is cited in the
   Reference of at least one story. A parent item served by none is
   a finding unless the stories or the parent say why (an OOS, a
   phase later, a question with an owner). Coverage is counted, never
   judged: whether a story truly delivers its item is the principal's
   walkthrough, not yours.
2. **Reference** — every story has a Reference; every ID it cites
   exists in the parent (or, for a DEP, in the BRD); a story citing
   only a POS has a parent `10-intent.md`. Where the parent is a
   source, the citation is a path and a place; existence of the path
   is verified, the place is read as a fact.
3. **Shape** — every story is a level-3 heading `US.NNNN — <name>`,
   then its sentence, then its acceptance criteria as bullets, then
   only the parts it has, in the template's order, under the fixed
   English labels; no part present and empty; no other part (no
   notes of context, no dependencies, no priority, no estimate); no
   two stories with one ID.
4. **Parts** — every question ends with `→ <owner>`; every risk has
   `→ <mitigation | consequences>`; every note carries a link and
   what lies behind it; every edge case is `situation → what
   happens`.
5. **Wording** — no vague word in an acceptance criterion where a
   value is wanted — a word that names a quality without a value,
   in whatever language the project writes (the Story style gives
   the kind); report the word and the place, never propose the value.
   A criterion in the conditional mood ("should", "could", or its
   equivalent in the project's language) is a finding.
6. **Skeleton residue** — no template comment, no `…`, no
   `<placeholder>`, no `NNNN` left in the file.

Cost: the stories and their parent, read once.
