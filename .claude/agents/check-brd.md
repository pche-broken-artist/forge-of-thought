---
name: check-brd
description: 'Check "brd" — verifies a BRD''s mechanics: every parent item carried, every cited ID existing, every item with a parent, the phasing present, every term defined, no link in an item. Fit after a pass of /forge brd. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.'
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

You read one project's `30-brd.md` — the path your task names, or
the project's BRD when the task names a project — with its parent
as the BRD's header declares it (`parent:` of `templates/brd.md`):
`20-assignment.md` or `10-intent.md`; a BRD made from a source is a
work product in `work/`, read when the task names it, its parent
the source by path. A project without a BRD is not a finding
(CLAUDE.md, Ledger). The
bookkeeping of the file — front-matter, the history companion — is
the `light` check's; the ID scheme in general the `project`
check's; you verify what only a BRD has.

What you verify:

1. **Traceability** — every in-scope item of the parent (a REQ of
   the assignment, an in-scope POS of the intent) is carried by at
   least one BR or UC; every parent cited by an item exists in the
   parent; the appendix table matches the items, since it is
   compiled from them (`templates/brd.md`, Appendix). A parent
   item carried by nothing is a finding unless an OOS, a DEP or a
   TBC of the BRD names it. Where the parent is a source, the
   citation is a path and a place; existence of the path is
   verified, the place is read as a fact.
2. **Every item has a parent** — a BR and an NFR end with their
   parent, `(REQ.NNNN)` or `(POS.NNNN)`; an NFR may end with its
   category instead, `(category: <name>)`, where the parent named
   none (`.claude/skills/forge/states/brd.md`, Requirement style);
   a UC declares its parent in its `Carries` line, and its block
   ends with its tables. An item with none of these is a finding.
   Where the parent is a source with speakers, the place a BR or a
   UC cites is a turn of the principal's side; a BR whose every
   place is another party's turn is a finding
   (`.claude/skills/forge/states/brd.md`, Requirement style).
3. **The sections that may not be silent** — Phasing is present and
   not empty, every item it carries exists, and every BR and UC
   stands in a phase or in the `not phased` row (POS.1360); every
   area of the roster the BRD cites is in the Touched areas table
   by the roster's own name, as found or not applicable with a
   reason, and `Roster: none` with its one row is a fact, not a
   finding; every role the roster names as signing or reviewing is
   in the Stakeholders table or named as absent with a reason; an
   ASM whose content answers what a TBC of the same BRD asks is a
   finding; every NFR category kept
   carries a value or a TBC with an owner, never the skeleton's
   wording; every TBC has an owner — a role, or `unassigned`, which
   is a valid open state — and says whether it blocks estimation.
4. **Terms and links** — every capitalised term of an item is in
   the Terms table; no item depends on a link (the assignment's
   Requirement style, cited by the BRD's); no name of a person
   stands where the template asks for a role.
5. **Skeleton residue** — no template comment, no `…`, no
   `<placeholder>`, no `NNNN` left in the file; `owner: unassigned`
   is not residue.

Cost: the BRD and its parent, read once; the roster the BRD cites,
read for its list of areas only.
