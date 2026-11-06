---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: bb3d522d8e8b7f4f
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

This page is the reference for the documentation map `docs-map.md`, for the task file a writer is given, for the front-matter and shape of a page, and for the index. It is written for the extender who changes the files that these four shapes come from.

## The map

The map is one Markdown file. It is written by the planner, the agent that plans the pages. It is read by the scripts `scripts/docs-state.py`, `scripts/docs-index.py` and `scripts/docs-check.py` through `scripts/docs_map.py`, and by the writers, the agents that write one page each. The reader of the documentation never sees it. Its shape is the skeleton `templates/docs-map.md`. Every path in it is relative to the root of the target.

The planner writes the map in parts: the front-matter, the Paths section and the first section of the outline first, then each further section appended at the end of the file.

### Front-matter

| Field | Holds |
|---|---|
| `target` | `engine` or the slug of the project. Never a path of the machine. |
| `owner` | `projects/<slug>` |

The previous map is not named in the header. It is taken from git, as the map last committed, by `python scripts/docs-state.py <map> --previous <path>`. The command prints the path it wrote, or `none` when the map was never committed or the project is not under git.

The heading after the front-matter is `# Documentation map - <target>`.

### The sections, in order

1. `## Paths`
2. One section per section of the outline, in the outline's order: `## start`, `## use`, `## about`, `## extend`, `## reference`. A section with no page may stand empty.
3. `## Unowned`
4. `## Did not fit`

### Paths

One line per reader, in the form `- <reader>: <page path>, <page path>`. The readers are `user`, `extender` and `evaluator`. Each line names three to five pages of the map in reading order. The index prints them as links.

### An entry

An entry opens with a heading `### docs/<section>/<page>.md`. Each field is a line `- <field>: <value>`. A continuation line is indented by two spaces. The fields stand in this order.

| Field | Holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words. A link cites it. |
| `line` | One sentence for the index: the question the page answers. |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender` or `evaluator` |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it. Commands are spelled out as they are typed. |
| `inputs` | Exact file paths, one per line. No globs, no versions. See Inputs below. |
| `links` | Few, and only pages of this map. Each is the path in backticks, a colon and one sentence on what that page gives. |
| `must-not` | What the page must not say of its topic. |
| `made` | `mirrored` or `derived` |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove` |

### Inputs

An input is a file, or a part of a file named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is.

| Part | Written as | Taken |
|---|---|---|
| A section | `path#Heading` | The heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces. |
| An item | `path#ABC.NNNN` | The line that carries the bold ID, to the next line that opens an item at the same indent, or to a heading. |
| A block | `path#Label` | Where no heading of that name exists: the paragraph opening with the bold label (`**Label.**`), to the next label or heading. |

### State

The planner writes `new` for a page with no previous entry, `keep` for one with a previous entry and `remove` for one that lost its material. `regenerate` is set only by `scripts/docs-state.py`.

`scripts/docs-state.py` computes the state from a hash of the entry's text (its `state` line excepted), the content of every input and the generator, that is the writer's definition and the documentation contract with their whitespace normalised. The page at the entry's path carries the hash it was made from, `inputs-hash`, in its front-matter. The two are compared.

| State | Set when |
|---|---|
| `new` | No page exists at the path. |
| `regenerate` | A page exists and its hash differs. |
| `keep` | A page exists with the same hash. |
| `remove` | The planner marked the entry `remove`, or a page under the documentation directory is named by no entry (the index excepted). Such an entry gets no task. |

The script rewrites only the `- state:` line of each entry. An input the map names and the disk does not have is reported, hashed as missing, and the page is regenerated.

### Unowned

Every fact a page needs and no file supports, with the page that needs it. The writer leaves such a fact out.

### Did not fit

What the planner read that contradicts itself or the outline, and what it did with it.

## The task file

For each entry in state `new` or `regenerate`, `scripts/docs-state.py` writes one task file into the directory named by `--tasks`. The task file is the writer's whole prompt. Its lines, in order:

| Line | Holds |
|---|---|
| Target root | The root that input paths are relative to. |
| Page to write | The absolute path of the page, with the page's path in the documentation. Relative links are computed from that place. |
| Date | The date of the run. |
| Version | The version the page is made for: the version of the owning project's intent beside the map, or `none`. |
| `inputs-hash` | The hash the page is to carry, exactly. |
| The entry | The entry from the map, verbatim. |
| Titles | One line per page the entry links to, `` `<path>`: <title> ``, or `(no title in the map)`. Links are the paths in backticks found in the entry. |
| Closing line | "Write the page, then report in a few lines." |

## A page

### Front-matter

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

### Body

1. `# <the entry's title>`
2. One paragraph: what the page is for and for whom. The first sentence says what the thing is.
3. The matter, in the outline of the page's kind.
4. `## See also`, one line per linked page: `- [<title>](<relative path>): <the sentence the entry gives>`.
5. The closing line: "Generated on <date> for version <version> from the files the front-matter names; never edited by hand."

## The index

The index is `README.md` in the documentation directory. It is derived from the map by `python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]`. The same map gives the same index. No model is involved.

| Part | Holds |
|---|---|
| Front-matter | `generated`, `version` (the version of the owning project's intent beside the map, left out when there is none), `made: derived`, and the map as the one input. |
| `# Documentation` | An opening paragraph of fixed text. When a version is known, a line gives the date and the version. |
| `## Where to start` | The reader paths of the map, one line per reader, each page a link by its title. |
| One section per outline section | `## Start`, `## Use`, `## About`, `## Extend`, `## Reference`, in that order. Each page is one line: the title linked to its relative path, a colon and the entry's `line`. An entry with no `line` gives the first sentence of its `says`. An entry in state `remove` is left out. |
| Closing | A fixed note naming the map and the script. |

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
