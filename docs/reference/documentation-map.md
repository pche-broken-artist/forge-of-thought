---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: b8b06b19bd72a471
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` from which every page of the documentation is made, and this page lists its fields exactly, with those of a writer's task, of a page's front-matter and of the index that derive from it. It is for the extender who changes how the documentation is planned, written or indexed. What the map and the pages are for is told in [The documentation](../about/the-documentation.md).

## The map

The shape of the map is the skeleton `templates/docs-map.md`. The planner agent writes the map, and the scripts `scripts/docs-state.py`, `scripts/docs-index.py` and `scripts/docs-check.py` read it through `scripts/docs_map.py`. Every path in the map is relative to the root of the target.

### Front-matter

| Field | Value |
|---|---|
| `generated` | the date, `YYYY-MM-DD` |
| `target` | `engine`, or the slug of the project (never a path of the machine) |
| `owner` | `projects/<slug>` |
| `previous` | `tmp/docs-map.previous.md`, or `none` |

### Sections, in order

1. The title `# Documentation map - <target>`.
2. `## Paths`: one line per reader, in the form `- <reader>: <page path>, <page path>`. The readers are `user`, `extender` and `evaluator`. The skeleton asks for three to five pages per line, in reading order.
3. One section per section of the outline, in the outline's order: `## start`, `## use`, `## about`, `## extend`, `## reference`. In each section there is one entry per page.
4. `## Unowned`: every fact a page needs and no file supports, with the page that needs it.
5. `## Did not fit`: what contradicted itself or the outline, and what was done with it.

### An entry

An entry is headed `### docs/<section>/<page>.md`. Each field is a line `- <field>: <value>`, and a value may continue on indented lines. The fields stand in this order.

| Field | What it holds |
|---|---|
| `title` | the page's title as its heading carries it, in the reader's words, because a link cites it |
| `line` | one line for the index: the question the page answers, one sentence at most |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender` or `evaluator` |
| `says` | what the page says, in a few sentences a writer can work from: its one topic and nothing beside it, the commands spelled out as they are typed |
| `inputs` | exact file paths, one per line, no globs and no versions; everything the writer must read and nothing else |
| `links` | few, only pages of this map: `` `docs/<section>/<page>.md`: <one sentence on what that page gives> `` |
| `must-not` | what the page must not say of its topic |
| `made` | `mirrored` or `derived` |
| `evidence` | derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

### Parts of a file as inputs

An input is a file, or a part of a file named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is.

| Form | The part |
|---|---|
| `path#Heading` | a section: the heading line to the next heading of the same or a higher level |
| `path#ID.NNNN` | an item: the line that carries the ID in bold, to the next line that opens an item at the same indent, or to a heading |
| `path#Label` | a block by its bold label: the paragraph opening with `**Label.**`, to the next label or heading; used where no heading of that name exists |

A heading with spaces is written with the spaces. An input that the disk does not have, a file or a part, is hashed as missing, and `scripts/docs-state.py` reports it.

### The state field

The planner writes `new` for a page without a previous entry, `keep` for one with, and `remove` for one that lost its material. The script `scripts/docs-state.py` sets the rest after the map is written.

| Value | Set by | Meaning |
|---|---|---|
| `new` | planner, or the script | no page exists at the path |
| `keep` | planner, or the script | a page exists and its `inputs-hash` equals the hash computed now |
| `regenerate` | the script only | a page exists and its hash differs, because an input or the entry changed |
| `remove` | planner | the entry lost its material; the entry keeps this state and gets no task |

The script rewrites only the `- state:` line of each entry and leaves the rest of the map byte for byte.

## How the hash is made

The script hashes, for every entry:

- the text of the entry, its `state` line excepted;
- the writer's definition `.claude/agents/docs-writer.md` and the contract `.claude/skills/docs-contract/SKILL.md`;
- the content of every input, whole or as the named part.

The page that exists at the entry's path carries the result as `inputs-hash` in its front-matter, and the two are compared. A page under the documentation directory that no entry names is listed as `remove`. The index `README.md` is excepted.

## The writer's task file

For every entry in state `new` or `regenerate` the script writes one task file, which is the whole prompt of a writer. The task holds, in this order:

1. the engine root, the root that input paths are relative to;
2. the page's path, and the entry's path from which relative links are computed;
3. the date;
4. the version the page is made for, which is the version of the owning project's intent;
5. the `inputs-hash` the page is to carry;
6. the entry, verbatim;
7. the titles of the pages the entry links to, one line each as `` `<path>`: <title> ``.

## The page's front-matter and shape

| Field | Value |
|---|---|
| `generated` | the date the task gives |
| `version` | the version the task gives |
| `made` | `mirrored` or `derived` |
| `inputs-hash` | the value the task gives, copied exactly |
| `inputs` | a list: the entry's inputs, each a path or `path#part` |

After the front-matter a page has, in this order:

1. the title, the entry's `title`, as a level-one heading;
2. one paragraph: what the page is for and for whom, the first sentence saying what the thing is;
3. the matter, in the outline of the page's kind;
4. `## See also`, one line per linked entry: the entry's title as a link with a relative path, then the sentence the entry gives for it;
5. the fixed closing line: "Generated on `<date>` for version `<version>` from the files the front-matter names; never edited by hand."

## The index

The index `README.md` of the documentation directory is derived from the map by `scripts/docs-index.py`. The same map gives the same index, and no model is involved.

| Part | Content |
|---|---|
| front-matter | `generated`, `version` (the version of the owning project's intent, which for the engine is its version), `made: derived`, and `inputs` naming the map |
| opening | a fixed text of the script, with the date and the version |
| `## Where to start` | one line per reader of `## Paths`, each page a link by its title |
| one section per section of the outline | headed Start, Use, About, Extend, Reference; one line per page, `- [<title>](<relative path>): <line>`; the first sentence of `says` stands where an entry has no `line`; an entry in state `remove` is left out |
| closing | the path of the map, and that the index is derived by the script and never edited by hand |

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
