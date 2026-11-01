---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 542d035c2b630828
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of the documentation with everything the page is made from. This page gives its fields exactly, with the fields of a writer's task, of a page's front-matter and of the documentation index, for the extender who changes how the documentation is planned or generated. The reader of the documentation never sees the documentation map.

## The file

One Markdown file named `docs-map.md`. Every path in it is relative to the root of its target. For the engine the root is the engine's root; for a project it is the project's directory, where the file lies.

The file has these parts, in this order:

1. The front-matter.
2. The heading `# Documentation map - <target>`.
3. The section `## Paths`.
4. One section per section of the outline, in the outline's order.
5. The section `## Unowned`.
6. The section `## Did not fit`.

## Front-matter

| Key | Value |
|---|---|
| `target` | `engine`, or the slug of the project. Never a path of the machine. |
| `owner` | The owning project, as `projects/<slug>`. |

The previous documentation map is not named in the header. It is taken from git, as last committed, with `python scripts/docs-state.py <map> --previous <path>`. The script prints the path it wrote, or `none` when the documentation map was never committed.

## Paths

One line per reader:

```
- <reader>: docs/<section>/<page>.md, docs/<section>/<page>.md
```

- `<reader>` is `user`, `extender` or `evaluator`.
- The line holds three to five pages of this documentation map, in reading order, separated by commas.
- The index prints each page as a link.

## The sections of the outline

The sections follow the outline, in this order, each a heading of level two:

1. `## start`
2. `## use`
3. `## about`
4. `## extend`
5. `## reference`

Each section holds one entry per page. An entry opens with a heading of level three that carries the page's path, `### docs/<section>/<page>.md`, and then lists its fields, each as `- <field>: <value>`. A value may continue on the following lines, indented by two spaces.

### The fields of an entry

The fields stand in this order.

| Field | Holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words, since a link cites it. |
| `line` | One line for the index: the question the page answers, no more than one sentence. |
| `kind` | `how-to`, `explanation` or `reference`. |
| `reader` | `user`, `extender` or `evaluator`. |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it, the commands spelled out as they are typed. |
| `inputs` | Exact file paths, one per line, with no globs and no versions. Everything the writer must read and nothing else. |
| `links` | Few, only pages of this documentation map. One per line, as the page's path in backticks, a colon, and the one sentence the writer will know of that page. |
| `must-not` | What the page must not say of its topic. |
| `made` | `mirrored` or `derived`. |
| `evidence` | For a derived page only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove`. |

### Parts of an input

An input is a file, or a part of one named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is.

| Form | The part |
|---|---|
| `path#Heading` | A section by its heading: the heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces. |
| `path#ID.NNNN` | An item by its ID: the line that carries the ID in bold to the next line that opens an item at the same indent, or to a heading. |
| `path#Label` | A block by its bold label: the paragraph opening with the label in bold, to the next label or heading. It applies where no heading of that name exists. |

A part that the disk does not have is reported and hashed as missing.

### The state of an entry

- The planner writes `new` for a page without a previous entry, `keep` for one with, and `remove` for one that lost its material.
- `scripts/docs-state.py` then sets the state from the content of the inputs. It rewrites only the `- state:` line of each entry and leaves the rest of the file byte for byte.

| State | Meaning |
|---|---|
| `new` | There is no page at the path. |
| `regenerate` | A page exists and its hash differs: an input or the entry changed. |
| `keep` | A page exists with the same hash. |
| `remove` | The planner marked the entry. Its page is listed for removal and the entry gets no task. |

The hash covers the entry's text (its `state` line excepted), the content of every input or named part, the writer's definition `.claude/agents/docs-writer.md` and the shared contract `.claude/skills/docs-contract/SKILL.md`. The first 16 hexadecimal characters are kept. A page under the documentation directory that no entry names is listed as `remove`, the index `README.md` and `videos` excepted.

### An entry, in outline

```
### docs/<section>/<page>.md
- title: <title>
- line: <one sentence>
- kind: how-to | explanation | reference
- reader: user | extender | evaluator
- says: <what the page says>
- inputs:
  <path>
  <path>#<part>
- links:
  `docs/<section>/<page>.md`: <one sentence>
- must-not: <what the page must not say>
- made: mirrored | derived
- evidence: <derived pages only>
- state: new | keep | regenerate | remove
```

## Unowned

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. The writer leaves such a fact out.

## Did not fit

`## Did not fit` lists what the planner read that contradicts itself or the outline, and what it did with it.

## The writer's task

`scripts/docs-state.py` writes one task file for every entry whose state is `new` or `regenerate`, into the directory given by `--tasks`. The task file is the writer's whole prompt. Its parts, in order:

| Part | Holds |
|---|---|
| Target root | The root that every input path is relative to. |
| Page to write | The page's absolute path, with its path in the documentation (`docs/...`), from which relative links are computed. |
| Date | The date given by `--date`, today by default. |
| Version | The version the page is made for: the `version` of the owning project's intent beside the documentation map, or `none`. |
| inputs-hash | The hash the page is to carry in its front-matter, exactly. |
| The entry | The entry from the documentation map, verbatim. |
| Titles | The title of every page the entry links to, to cite them by. |

The directory is emptied of earlier task files at each run. The synopsis is:

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

## The page's front-matter and shape

A page opens with this front-matter:

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

After it come, in this order:

1. The heading `# <the entry's title>`.
2. One paragraph on what the page is for and for whom.
3. The matter, in the outline of the page's kind.
4. The section `## See also`, with one line per linked entry: `- [<title>](<relative path>): <the sentence the entry gives for it>`.
5. The fixed closing line: "Generated on `<date>` for version `<version>` from the files the front-matter names; never edited by hand."

The page's `inputs-hash` is read from the first 2000 characters of the page and compared with the hash computed from the entry.

## The index

`python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]` writes `<docs-dir>/README.md` from the documentation map. It is deterministic: the same documentation map gives the same index, and no model is involved.

- The front-matter holds `generated`, `version` (when the intent has one), `made: derived`, and one input, the documentation map.
- The `version` is that of the owning project's intent (`10-intent.md` beside the documentation map). For the engine it is the engine's version.
- The heading is `# Documentation`, followed by a fixed opening paragraph that belongs to the script.
- Where there is a version, a line says the index was generated on the date for that version.
- `## Where to start` follows, with one line per reader of the `## Paths` section, each page a link.
- One section per section of the outline follows, in the outline's order, headed Start, Use, About, Extend and Reference. A section with no entry is left out.
- Each section has one line per page: the title linked to its relative path, then the `line` field. Where an entry has no `line`, the first sentence of `says` stands in. An entry with state `remove` is skipped.
- The index closes with a sentence naming the documentation map and `scripts/docs-index.py`.

The index is never edited by hand. A change goes into the documentation map, and the script is run again.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
