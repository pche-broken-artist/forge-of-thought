---
generated: YYYY-MM-DD
target: engine | <slug>
owner: projects/<slug>
previous: tmp/docs-map.previous.md | none
---

# Documentation map — <target>

<!-- The one owner of the map's shape (kind `map`, CLAUDE.md,
Document kinds; what the map is for: CLAUDE.md, Document chain,
Documentation). Written by the planner agent of /document, read by
the scripts docs-state, docs-index and docs-check through
scripts/docs_map.py and by the writer agents; never by the reader of
the documentation. Every path is relative to the target's root. The
Paths section first: one line per reader, three to five pages of
this map in reading order, printed as links by the index. Then one
section per section of the outline, in the outline's order; in each,
one entry per page in the form below. What each field must hold and
how an entry is judged: .claude/agents/docs-planner.md, The map. -->

## Paths
- user: docs/<section>/<page>.md, docs/<section>/<page>.md
- extender: docs/<section>/<page>.md, docs/<section>/<page>.md
- evaluator: docs/<section>/<page>.md, docs/<section>/<page>.md

## start

### docs/<section>/<page>.md
- title: <the page's title as its heading will carry it>
- line: <one line for the index: the question the page answers>
- kind: how-to | explanation | reference
- reader: user | extender | evaluator
- says: <what the page says, its one topic and nothing beside it>
- inputs:
  <exact file path, one per line; a part of a file as path#Heading
  or path#ID.NNNN, hashed as that part>
- links:
  `docs/<section>/<page>.md`: <one sentence on what that page gives>
- must-not: <what the page must not say of its topic>
- made: mirrored | derived
- evidence: <derived pages only: what the page is put together from
  and by what reasoning>
- state: new | keep | regenerate | remove

## use

## about

## extend

## reference

## Unowned
<!-- every fact a page needs and no file supports, with the page that
needs it -->

## Did not fit
<!-- what contradicted itself or the outline, and what was done with
it -->
