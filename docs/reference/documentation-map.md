---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: d29d23ca4d37902c
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of the documentation with everything the page is made from. This page gives the exact fields of the map, of the task a page's writer receives, of a page's front-matter and of the documentation index, for the extender who changes one of them.

The map lies beside the owning project's ledger. It is written by the planner, an agent of the documentation run. It is read by the scripts `scripts/docs-state.py`, `scripts/docs-index.py` and `scripts/docs-check.py` through `scripts/docs_map.py`, and by the writers, the agents that each write one page. The reader of the documentation never sees it. Its shape is owned by the skeleton `templates/docs-map.md`.

## The map file

Every path in the map is relative to the root of the target. For the engine that is the engine root. For a project it is the project's directory, where the map lies.

### Front-matter

| Key | Value |
|---|---|
| `target` | `engine` or the project's slug, never a path of the machine |
| `owner` | `projects/<slug>` |

The header carries no name for the previous map. The previous map is the one last committed in git. `python scripts/docs-state.py <map> --previous <path>` writes it to `<path>` and prints the path, or prints `none` when the map was never committed or the project is outside git.

### Sections, in order

1. The heading `# Documentation map - <target>`.
2. `## Paths`.
3. One section per section of the outline, in the outline's order: `## start`, `## use`, `## about`, `## extend`, `## reference`. A section with no page stays without entries.
4. `## Unowned`.
5. `## Did not fit`.

### Paths

One line per reader, in the form `- <reader>: <page>, <page>`. The readers are `user`, `extender` and `evaluator`. Each line names three to five pages of the map in reading order, as paths. The index prints them as links.

### Entry

An entry opens with a heading `### docs/<section>/<page>.md`. The section is lowercase letters. The page name is lowercase with hyphens, the job or topic as the name, never a number.

Below the heading each field stands on a line `- <field>: <value>`. A value may continue on following lines, indented by two spaces. The fields are in this order:

| Field | What it holds |
|---|---|
| `title` | The page's title as its heading carries it, in the reader's words, since a link cites it |
| `line` | One line for the index: the question the page answers, one sentence at most |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender` or `evaluator` |
| `says` | The page's one topic and nothing beside it, in a few sentences a writer can work from, commands spelled out as they are typed |
| `inputs` | Exact file paths, one per line, no globs, no versions: everything the writer must read and nothing else |
| `links` | Pages of this map only, one per line as `` `docs/<section>/<page>.md`: <one sentence on what that page gives> `` |
| `must-not` | What the page must not say of its topic |
| `made` | `mirrored` or `derived` |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

A part of a file is named after `#` in `inputs`:

| Part | Written as | Taken to be |
|---|---|---|
| A section | `path#Heading` | The heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces. |
| An item | `path#ABC.NNNN` | The line that carries `**ABC.NNNN**`, to the next line that opens an item at the same indent, or to a heading |
| A block | `path#Label` | Where no heading of that name exists, the paragraph opening with `**Label.**`, to the next bold label or heading |

An input that names a part is hashed as that part, so that a change elsewhere in the file leaves the page as it is. An input that names a file whole is hashed whole.

The pages an entry links to are found by the paths in backticks under `links`; the entry's own path is left out.

### State

The planner writes `new` for a page without a previous entry, `keep` for one with, and `remove` for one that lost its material. `regenerate` is never written by the planner. The script `scripts/docs-state.py` sets the state from the content of the inputs after the map is written, and rewrites only the `- state:` line of each entry.

| State | Set when |
|---|---|
| `new` | No page exists at the path |
| `regenerate` | A page exists and its hash differs |
| `keep` | A page exists with the same hash |
| `remove` | The planner marked the entry; the entry keeps this state and gets no task |

The hash covers the entry's lines (the `state` line excepted), the content of every input or part, the writer's definition `.claude/agents/docs-writer.md` and the contract `.claude/skills/docs-contract/SKILL.md`. An input the disk does not have is hashed as missing and reported. The page carries its hash in its front-matter as `inputs-hash`.

A page under the documentation directory that no entry names is listed as `remove`. The index `README.md` and the folder `videos` are left out of that listing.

### Unowned and Did not fit

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. `## Did not fit` lists what contradicted itself or the outline, and what was done with it.

## The writer's task

`python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir>` writes one task file into `<tmp-dir>` for every entry whose state is `new` or `regenerate`. The old task files in that directory are removed first. The file is named after the page's path, with `/` turned to `-`. It is the whole prompt of the writer and holds, in this order:

1. The target root, to which the input paths are relative.
2. The page to write, as a path, with the page's path in the map.
3. The date.
4. The version the page is made for: the version of the owning project's intent beside the map, or `none`.
5. The `inputs-hash` the page is to carry.
6. The entry, verbatim.
7. The titles of the pages the entry links to, one per line as `` - `<path>`: <title> ``, or `- none`.

## The page's front-matter and shape

```
---
generated: <date>
version: <the version the task gives>
made: mirrored | derived
inputs-hash: <the value the task gives, copied exactly>
inputs:
  - <path or path#part>
  - <path>
---

# <the entry's title>

<One paragraph: what the page is for and for whom>

<The matter, in the outline of the page's kind>

## See also

- [<the linked entry's title>](<relative path>): <the sentence the entry gives for it>

<The fixed closing line: "Generated on <date> for version <version>
from the files the front-matter names; never edited by hand.">
```

The headings of the matter depend on the kind of the page. A heading with no material is left out and never left empty.

## The index

`python scripts/docs-index.py <map> <docs-dir>` writes `<docs-dir>/README.md` from the map. It is derived, deterministic and never edited by hand. No model is involved.

Its front-matter:

| Key | Value |
|---|---|
| `generated` | The date |
| `version` | The version of the owning project's intent beside the map, which for the engine is the engine's version; left out when there is none |
| `made` | `derived` |
| `inputs` | The path of the map, as its one input |

Its body, in order:

1. The heading `# Documentation` and a fixed opening paragraph, which belongs to the script.
2. When a version exists, a line giving the date and the version.
3. `## Where to start`: one line per reader of the `## Paths` section, in the form `- **the <reader>**: <links>.`, each page a link cited by its title.
4. One section per section of the outline in order (`Start`, `Use`, `About`, `Extend`, `Reference`), one line per page as `- [<title>](<relative path>): <line>`. Where an entry has no `line`, the first sentence of its `says` stands in. An entry in the state `remove` is left out.
5. A closing paragraph that names the map and says the index is derived from it.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
