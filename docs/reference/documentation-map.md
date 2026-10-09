---
generated: 2026-10-09
made: mirrored
inputs-hash: 00afff0df6c88bad
inputs:
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

This page states the shapes the documentation is built on: the map, a
writer's task, a page and the index. It is for the extender who
changes how the documentation is planned, written or derived.

## The map

One Markdown file in the owning project, never in `docs/`. The
planner's definition owns its content; the scripts read it.

### Front-matter

| Key | Value |
|---|---|
| `generated` | the date |
| `target` | `engine`, or a project's slug |
| `owner` | the owning project |
| `previous` | the earlier map, or `none` |

Every path in the map is relative to the target's root: the engine
root when `target` is `engine`, otherwise the directory of the owning
project, where the map lies.

### Sections

One section per section of the outline, in the outline's order:
`start`, `use`, `about`, `extend`, `reference`. A section with no
material is left out. In each section there is one entry per page,
headed `### docs/<section>/<page>.md`. A field is a line `- <field>:
<value>`; a value may continue on indented lines.

### Fields of an entry

The fields stand in this order.

| Field | Content |
|---|---|
| `title` | the page's title as its heading carries it; a link to the page cites it |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender`, `evaluator`; one or more |
| `says` | what the page says: its one topic, in two to five sentences |
| `inputs` | whole files, one path per line; no globs, no sections, no versions |
| `links` | a page path in backticks and one sentence saying what that page gives, one per line; only pages that exist in the map |
| `must-not` | what the page must not say or contain |
| `made` | `mirrored` or `derived` |
| `evidence` | derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

Inputs are whole files because a script hashes them. Where only part
of a file matters, the file is named in `inputs` and the part in
`says`.

### State

| State | Set by | Meaning |
|---|---|---|
| `new` | the planner | a page without a previous entry; the state script also sets it when no page exists at the path |
| `keep` | the planner, then the state script | a page exists and carries the hash the entry and its inputs give now |
| `regenerate` | the state script only | a page exists and its hash differs: an input or the entry changed |
| `remove` | the planner | a page that lost its material |

The state script hashes the entry's text (its `state` line excepted)
together with the content of every input file, and compares the
result with the `inputs-hash` in the front-matter of the page at the
entry's path. It rewrites only the `state` line of each entry. A page
under the documentation directory that no entry names is reported as
`remove`; the index `README.md` is excepted. An input the map names
and the disk lacks is reported and hashed as missing.

### After the sections

| Section | Content |
|---|---|
| `## Unowned` | every fact a page needs and no file supports, with the page that needs it |
| `## Did not fit` | what the planner read that contradicts itself or the outline, and what it did with it |

## A writer's task

For every `new` or `regenerate` entry the state script writes one
task file into the task directory. It is the writer's whole prompt,
and the writer reads it first. It carries, in this order:

1. the engine root, which input paths are relative to;
2. the path of the page to write, with the note that relative links
   are computed from that place;
3. the date;
4. the hash the page is to carry in its front-matter, exactly;
5. the entry from the map, verbatim;
6. the titles of the pages the entry links to, to cite them by.

## A page

A front-matter, then the body.

| Part | Content |
|---|---|
| front-matter `generated` | the date |
| front-matter `made` | `mirrored` or `derived` |
| front-matter `inputs-hash` | the hash from the task, copied exactly |
| front-matter `inputs` | the entry's input paths, one per line |
| heading | the entry's title |
| opening paragraph | what the page is for and for whom |
| matter | under headings where the topic needs them |
| `## See also` | one line per linked page: its title as the task gives it, linked by a relative path, then the sentence the entry gives |

A derived page says in its opening that it was put together from its
inputs. Links into `docs/` go only to the pages the entry lists. A
link to a file of the engine is a path in backticks. A page has no
long dash and no ID of the chain.

## The index

`docs/README.md` is derived from the map by `scripts/docs-index.py`,
without a model, and never edited by hand. The same map gives the
same index.

- Its front-matter carries `generated`, `version`, `made: derived`
  and the map as its one input. The version is that of the owning
  project's intent, `10-intent.md` beside the map.
- The opening says what the documentation is and, where a version is
  known, the date and version it was generated for.
- The section "Where to start" gives one reading path per reader: the
  user, `start/` then `use/`; the extender, `extend/` then
  `reference/`; the evaluator, `about/`. This text is fixed in the
  script.
- Then one section per outline section, in the outline's order, one
  line per page: the title linked to its relative path, then the
  first sentence of `says`. A page in state `remove` is left out.
- It closes by naming the map it is derived from.

## See also

- [About the documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
