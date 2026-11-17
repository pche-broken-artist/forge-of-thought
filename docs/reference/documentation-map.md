---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: b6a63ab4aea8d3ec
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

This page lists the fields of the documentation map `docs-map.md`, of the task file a page's writer receives, of a page's front-matter and of the documentation index. It is for the extender who reads or changes how the documentation is planned and generated. The map is a Markdown file with one entry per page. The planner agent writes it, the scripts and the writer agents read it, and the reader of the documentation never sees it.

## The map

The map is one file, written in parts: the front-matter, the `## Paths` section and the first section of the outline, then every further section appended. Its skeleton is `templates/docs-map.md`. The parts come in this order.

### Front-matter

| Key | Holds |
|---|---|
| `target` | `engine`, or the slug of the project. Never a path of the machine. |
| `owner` | `projects/<slug>`, the project that owns the map. |

The previous map is not named in the header. It is taken from git (`python scripts/docs-state.py <map> --previous <path>` writes the map as last committed, or prints `none` when it was never committed).

Every input path of the map is relative to the root of the target: the engine root when `target` is `engine`, otherwise the directory of the owning project.

### Heading

`# Documentation map — <target>`

### The `## Paths` section

It comes first. It has one line per reader, in the form `- <reader>: <page path>, <page path>`. The readers are `user`, `extender` and `evaluator`. The index turns these lines into its reading paths.

### One section per section of the outline

The sections follow the outline's order:

- `## start`
- `## use`
- `## about`
- `## extend`
- `## reference`

Each holds one entry per page. An entry opens with `### docs/<section>/<page>.md`, followed by fields written as `- <field>: <value>`. A value may continue on indented lines. The fields stand in this order.

| Field | Holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words, since a link cites it. |
| `line` | One line for the index: the question the page answers, one sentence at most. |
| `kind` | `how-to`, `explanation` or `reference`. |
| `reader` | `user`, `extender` or `evaluator`. |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it, with commands spelled out as they are typed. |
| `inputs` | Exact file paths, one per line, no globs, no versions. Everything the writer must read and nothing else. |
| `links` | Pages of this map, each as `` `docs/<section>/<page>.md` `` followed by a colon and one sentence on what that page gives. Few; the glossary and the page of each term the page uses are among them. |
| `must-not` | What the page must not say of its topic. It narrows and never forbids what `says` or the page's shape requires. |
| `made` | `mirrored` or `derived`. |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove`. |

#### The parts of an input

An input is a file, or a part of a file named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is. A part is one of three things:

- A section, named by its heading: `path#Heading`. It runs from the heading to the next heading of the same or a higher level. A heading with spaces is written with the spaces.
- An item, named by its ID: `path#ID.NNNN`. It runs from the line that carries the ID in bold to the next item at the same indent, or to a heading.
- A block, named by its bold label: `path#Label`. It applies where no heading of that name exists. It runs from the paragraph that opens with the label in bold to the next label or heading.

#### The values of `state`

| Value | Set by | Meaning |
|---|---|---|
| `new` | `scripts/docs-state.py` | No page exists at the path. |
| `keep` | `scripts/docs-state.py` | A page exists and carries the same hash as the entry. |
| `regenerate` | `scripts/docs-state.py` | A page exists and its hash differs, because an input or the entry changed. |
| `remove` | the planner | The page has no material any more. The entry keeps this state and gets no task. |

The script hashes the entry's text without its `state` line, the writer's definition and the contract with their whitespace normalised, and every input or part of an input. An input that the disk lacks is reported and hashed as missing. The script rewrites only the `state` lines of the map. A page under the documentation directory that no entry names is listed as `remove`; the index `README.md` and the videos folder are excepted.

### Unowned

Every fact a page needs and no file supports, with the page that needs it. The writer leaves it out.

### Did not fit

What contradicted itself or the outline, and what was done with it.

## The task file

For every entry in state `new` or `regenerate`, `scripts/docs-state.py` writes one task file into the task directory. The file is the whole prompt of a writer agent. It holds, in this order:

1. The target root, to which the input paths are relative.
2. The page to write, as an absolute path with its map path in brackets.
3. The date.
4. The version the page is made for: the version of the intent of the owning project, beside the map, or `none`.
5. The `inputs-hash` the page is to carry.
6. The entry, verbatim.
7. The titles of the pages the entry links to, each as `` `<path>`: <title> ``, or `- none`.
8. The closing request: write the page, then report in a few lines.

## A page's front-matter

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
```

`inputs-hash` is a 16-digit hexadecimal value. `scripts/docs-state.py` compares it with the hash it computes from the entry to set the entry's state.

## A page's shape

In this order:

1. `# <the entry's title>`
2. One paragraph on what the page is for and for whom. Its first sentence says what the thing is.
3. The matter, in the outline of the page's kind.
4. `## See also`: one line per linked page, as a link with the entry's title and relative path, a colon and the sentence the entry gives for it.
5. The closing line: `Generated on <date> for version <version> from the files the front-matter names; never edited by hand.`

## The index

`scripts/docs-index.py <map> <docs-dir>` derives `<docs-dir>/README.md` from the map. It is deterministic: the same map gives the same index. No model is involved.

The front-matter holds `generated`, `version`, `made: derived` and `inputs` with the map as its one input. `version` is the version of the intent of the owning project, which for the engine is its version. The version is left out when there is no intent beside the map.

The body holds, in this order:

1. The heading `# Documentation` and a fixed opening paragraph.
2. A line naming the date and the version, where a version exists.
3. `## Where to start`: one line per reader of the `## Paths` section, each page a link.
4. One section per section of the outline that has entries, headed Start, Use, About, Extend and Reference. Each holds one line per page, `- [<title>](<relative path>): <line>`. Where an entry has no `line`, the first sentence of its `says` stands in. Entries in state `remove` are left out.
5. A closing paragraph that names the map and states that the index is derived from it and never edited by hand.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
