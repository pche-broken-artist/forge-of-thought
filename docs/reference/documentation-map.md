---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: a549f1067823ffe5
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of the documentation with everything the page is made from. This page gives its fields exactly, then the fields of a writer's task, the front-matter and shape of a page, and the shape of the index. It is for the extender who changes the documentation or the scripts that read it.

The map is written by the planner (the agent that plans the pages), read by the scripts `docs-state`, `docs-index` and `docs-check` through `scripts/docs_map.py`, and read by the writer agents. The reader of the documentation never sees it. Every path in it is relative to the root of the target.

## The front-matter of the map

| Key | Holds |
|---|---|
| `target` | `engine`, or the slug of the project |
| `owner` | `projects/<slug>` |

The `target` is never a path of the machine. The header carries no name of the previous map. The previous map is taken from git, as last committed, with `python scripts/docs-state.py <map> --previous <path>`; the command prints the path, or `none` where the map was never committed.

The heading after the front-matter is `# Documentation map - <target>`.

## The file in order

1. The front-matter.
2. `## Paths`.
3. One section per section of the outline, in the outline's order: `## start`, `## use`, `## about`, `## extend`, `## reference`.
4. `## Unowned`.
5. `## Did not fit`.

The planner writes the file in parts: the front-matter, `## Paths` and the first section first, every further section appended at the end.

## Paths

One line per reader, in the form `- <reader>: <page>, <page>`. The reader is `user`, `extender` or `evaluator`. The pages are paths of pages of this map, three to five of them, in reading order. The index prints them as links.

```
## Paths
- user: docs/<section>/<page>.md, docs/<section>/<page>.md
```

## An entry

An entry opens with a heading `### docs/<section>/<page>.md`. The section is one of the outline. The fields follow, one per line in the form `- <field>: <value>`, a continuation line indented by two spaces. The scripts read the fields by name.

| Field | Holds |
|---|---|
| `title` | The title as the page heading carries it, in the reader's words, since a link cites it. |
| `line` | One line for the index: the question the page answers, one sentence at most. |
| `kind` | `how-to`, `explanation` or `reference`. |
| `reader` | `user`, `extender` or `evaluator`. |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it, the commands spelled out as they are typed. |
| `inputs` | Exact file paths, one per line. No glob, no version. Everything the writer must read and nothing else. |
| `links` | Pages of this map only, each as `` `docs/<section>/<page>.md`: <one sentence> ``. The sentence is all the writer knows of the target page. |
| `must-not` | What the page must not say of its topic. |
| `made` | `mirrored` or `derived`. |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove`. |

The fields stand in this order: `title`, `line`, `kind`, `reader`, `says`, `inputs`, `links`, `must-not`, `made`, `evidence`, `state`.

### Parts of a file in `inputs`

An input is a whole file, or a part of one named after `#`. A part is hashed as that part, so that a change elsewhere in the file leaves the page as it is.

| Part | Written | Taken |
|---|---|---|
| A section | `path#Heading` | The heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces. |
| An item | `path#ID.NNNN` | The item line that carries the ID in bold, to the next line that opens an item at the same indent, or to the next heading. |
| A block | `path#Label` | Where no heading of that name exists: the paragraph that opens with the bold label, to the next label or heading. |

A file or a part that the disk does not have is reported by `docs-state` and hashed as missing. The page is regenerated and its writer reports the gap.

### The state of an entry

The planner writes `new` for a page without a previous entry, `keep` for one with, and `remove` for one that lost its material. The script `docs-state` sets the state from the inputs afterwards.

| State | Meaning |
|---|---|
| `new` | No page exists at the path. |
| `regenerate` | A page exists and its hash differs: an input or the entry changed. Only the script sets it. |
| `keep` | A page exists with the same hash. |
| `remove` | The planner marked the entry. Its page, if any, is listed for removal. The entry keeps this state and gets no task. |

The script also lists as `remove` every page under the documentation directory that no entry names. The index `README.md` and the `videos` folder are excepted.

The hash is made from the text of the entry with its `state` line left out, the writer's definition and the contract with their whitespace normalised, and the content of every input. The script rewrites only the `- state:` line of each entry and leaves the rest of the map as it was.

## Unowned and Did not fit

Both sections hold free text.

- `## Unowned`: every fact a page needs and no file supports, with the page that needs it.
- `## Did not fit`: what contradicted itself or the outline, and what was done with it.

## The writer's task

For every entry that is `new` or `regenerate`, `docs-state` writes one task file into the folder named by `--tasks`. The task file is the whole prompt of a writer. Command:

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

The task holds, in this order:

1. The target root, to which the input paths are relative.
2. The path of the page to write, with the note that relative links are computed from that place.
3. The date.
4. The version the page is made for: the version of the intent of the owning project, beside the map, or `none`.
5. The `inputs-hash` the page is to carry, copied exactly.
6. The entry from the map, verbatim.
7. The titles of the pages the entry links to, one line each as `` `<path>`: <title> ``, or `none`.
8. The closing request: write the page, then report in a few lines.

A task file is named from the page's path, the folder separators replaced by hyphens.

## The front-matter and shape of a page

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

<One paragraph: what the page is for and for whom.>

<The matter, in the outline of the page's kind.>

## See also

- [<the linked entry's title>](<relative path>): <the sentence the entry gives for it>

<The closing line: "Generated on <date> for version <version>
from the files the front-matter names; never edited by hand.">
```

The `inputs-hash` is read from the first 2000 characters of the page. The page's state is `keep` when it equals the hash computed from the map.

## The index

The index is `README.md` in the documentation directory. It is derived from the map and never edited by hand. Command:

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

The same map gives the same index. No model is involved.

| Part | Content |
|---|---|
| Front-matter | `generated`, `version`, `made: derived`, and `inputs` with the map as the one input. |
| Version | The version of the intent of the owning project beside the map. For the engine it is the engine's version. The key is left out where there is no intent. |
| Opening | A fixed paragraph of the script, then the line "Generated on <date> for ... at version <version>". |
| `## Where to start` | One line per reader of `## Paths`: the reader in bold, then each page as a link by its title. |
| One section per outline section | `## Start`, `## Use`, `## About`, `## Extend`, `## Reference`, in that order. Each holds one line per page: `- [<title>](<relative path>): <line>`. |
| Closing | The path of the map, and that the index is derived from it by `scripts/docs-index.py`. |

Where an entry has no `line`, the index takes the first sentence of its `says`. Where it has no `title`, the index takes the file name with hyphens as spaces. An entry in the state `remove` has no line.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
