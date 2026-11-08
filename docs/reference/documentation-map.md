---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: aae2341c69d0ae54
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of a target's documentation with everything the page is made from. This page gives the fields of the map, of a writer's task, of a page's front-matter and of the documentation index, exactly. It is for the extender, who changes a page by changing its entry.

## The map file

The map is one Markdown file. Its shape is the template `templates/docs-map.md`. It is written in parts: the front-matter, the `## Paths` section and the first section of the outline come first, and every further section is appended at the end of the file. It is read by the scripts and by the writers, never by the reader of the documentation.

### Front-matter

| Key | Value |
|---|---|
| `target` | `engine`, or the project's slug; never a path of a machine |
| `owner` | `projects/<slug>` |

The header carries no `previous`. The previous map is the one last committed to git, which `scripts/docs-state.py <map> --previous <path>` writes to a file for the planner. The script prints `none` when the map was never committed or the project is outside git.

Every input path of the map is relative to the target's root. That root is the engine's root when `target` is `engine`, and the owning project's directory, where the map lies, otherwise.

### Order of the file

1. The front-matter.
2. The title `# Documentation map - <target>`.
3. `## Paths`.
4. One section per section of the outline, in this order: `## start`, `## use`, `## about`, `## extend`, `## reference`.
5. `## Unowned`.
6. `## Did not fit`.

### The Paths section

One line per reader, in the form `- <reader>: <page path>, <page path>`. The reader is `user`, `extender` or `evaluator`. A line names three to five pages of the map in reading order. The index prints the lines as links.

### An entry

An entry stands in the section of its page. Its heading is the page's path, `### docs/<section>/<page>.md`. Each field is a line `- <field>: <value>`, and a value may continue on indented lines. The fields come in this order:

| Field | Holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words, since a link cites it |
| `line` | One line for the index: the question the page answers, no more than one sentence |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender` or `evaluator` |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it, the commands spelled out as they are typed |
| `inputs` | Exact file paths, one per line, no globs and no versions; see below |
| `links` | Few pages, only pages of this map, each as the path in backticks and one sentence on what that page gives |
| `must-not` | What the page must not say of its topic |
| `made` | `mirrored` or `derived` |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

The `links` of an entry are every glossary and concept page of the terms the page uses. Every entry is named under `links` by at least one other entry.

#### Naming an input

An input is a file, or a part of a file named after `#`. A part is one of these:

- A section by its heading: `path#Heading`. It runs from the heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces.
- An item by its ID: `path#PREFIX.NNNN`. It runs from the line that carries the ID in bold to the next line that opens an item at the same indent, or to a heading.
- A block by its bold label: `path#Label`. It runs from the paragraph opening with the label in bold, with or without the final full stop, to the next label or heading. It applies where no heading of that name exists.

Each input is hashed as the part it names. A change elsewhere in the file leaves the page as it is. A part or a file the disk does not have is reported and hashed as missing.

#### The state

`state` is set by the planner only to `new` for a page without a previous entry, `keep` for one with a previous entry, and `remove` for one that lost its material. `scripts/docs-state.py` computes the rest from the content of the inputs:

| State | Meaning |
|---|---|
| `new` | No page exists at the path |
| `regenerate` | A page exists and its hash differs |
| `keep` | A page exists with the same hash |

The script rewrites only the `- state:` line of each entry. An entry marked `remove` keeps its state and gets no task. The script also lists as `remove` every page under the documentation directory that no entry names, the index `README.md` and the `videos` folder excepted.

### Unowned and Did not fit

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. `## Did not fit` lists what contradicted itself or the outline, and what was done with it.

## How the hash is made

The hash that `scripts/docs-state.py` computes for an entry is the first 16 hexadecimal characters of a SHA-256 over:

- The lines of the entry, its `state` line excepted.
- The writer's definition and the documentation contract, each with its whitespace collapsed, so that a re-wrap changes nothing and a changed sentence does.
- Each input, as the file or the part it names, or the marker `<missing>`.

The page at the entry's path carries the hash it was made from as `inputs-hash` in its front-matter. The script reads it from the first 2000 characters of the page.

## The writer's task

For each `new` or `regenerate` entry the script writes one task file into the directory named by `--tasks`, named after the page's path with `/` replaced by `-`. The task is a writer's whole prompt. It holds, in this order:

1. The target root.
2. The page to write: its absolute path, the same as the entry's path, relative links computed from that place.
3. The date.
4. The version the page is made for, the `version` of the owning project's intent beside the map, or `none`.
5. The `inputs-hash` the page is to carry.
6. The entry, verbatim.
7. The titles of the pages the entry links to, one line each as the path in backticks and the title, or `none`.
8. The closing line "Write the page, then report in a few lines."

## The page's front-matter and shape

Front-matter:

| Key | Value |
|---|---|
| `generated` | The date of the task |
| `version` | The version the task gives |
| `made` | `mirrored` or `derived`, from the entry |
| `inputs-hash` | The value the task gives, copied exactly |
| `inputs` | One line per input of the entry, a path or `path#part` |

Body, in this order:

1. `# <the entry's title>`.
2. One paragraph on what the page is for and for whom. Its first sentence says what the thing is.
3. The matter, in the outline of the page's kind.
4. `## See also`, one line per linked entry: the title as a link by a relative path, a colon and the sentence the entry gives for it.
5. The closing line "Generated on <date> for version <version> from the files the front-matter names; never edited by hand."

## The index

`scripts/docs-index.py <map> <docs-dir>` writes `<docs-dir>/README.md` from the map, with no model. The same map gives the same index. It is never edited by hand.

Front-matter:

| Key | Value |
|---|---|
| `generated` | The date |
| `version` | The version of the owning project's intent beside the map, left out when there is none; for the engine, its own version |
| `made` | `derived` |
| `inputs` | The map, as one line |

Body, in this order:

1. `# Documentation` and a fixed opening paragraph. It is text of the script.
2. Where a version exists, a line giving the date and the version.
3. `## Where to start`, one line per reader of the `## Paths` section, each page a link by its title.
4. One section per section of the outline that has entries, headed Start, Use, About, Extend or Reference, in that order. Each entry not marked `remove` is a line `- [<title>](<relative path>): <line>`. Where an entry has no `line`, the first sentence of its `says` stands in its place; where it has no `title`, the page's file name stands in.
5. A closing paragraph naming the map and the script that derived the index.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
