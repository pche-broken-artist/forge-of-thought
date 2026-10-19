---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: c268b6f21251a738
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

This page lists the fields of the documentation map, of a writer's task file, of a page's front-matter and of the documentation index. It is for the extender who changes how the documentation is planned, written or indexed. Terms of the forge are defined in the [Glossary](glossary.md).

The documentation map is the file `docs-map.md`. It holds one entry per page of the documentation and everything a page is made from. The planner (the agent that plans the pages) writes it. The scripts and the writers (the agents that write one page each) read it. The reader of the documentation never sees it. Its shape is the skeleton `templates/docs-map.md`.

## The map

The map has these parts, in this order.

| Part | What it holds |
|---|---|
| Front-matter | `target` and `owner` |
| `## Paths` | one line per reader |
| one section per section of the outline | the entries of that section's pages |
| `## Unowned` | facts a page needs that no file supports |
| `## Did not fit` | what contradicted itself or the outline |

### Front-matter

| Field | Value |
|---|---|
| `target` | `engine`, or the slug of the project. Never a path of the machine. |
| `owner` | `projects/<slug>` |

The previous map is not named in the header. It is taken from git: `python scripts/docs-state.py <map> --previous <path>` writes the map as last committed to `<path>` and prints that path, or prints `none` when the map was never committed.

Every input path in the map is relative to the target's root. That root is the engine root when `target` is `engine`, else the directory of the owning project.

### Paths

One line per reader, in the form `- <reader>: <page path>, <page path>`. The readers are `user`, `extender` and `evaluator`. Each line names three to five pages of the map in reading order. The index prints them as links.

### Sections

After Paths comes one section per section of the outline, in the outline's order: `start`, `use`, `about`, `extend`, `reference`. A section with no pages stays as a heading without entries.

### An entry

An entry opens with a heading `### docs/<section>/<page>.md`, then one line per field, in this order. A value may continue on the following lines, indented.

| Field | What it holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words. A link cites it. |
| `line` | One line for the index: the question the page answers, one sentence at most. |
| `kind` | `how-to`, `explanation` or `reference`. |
| `reader` | `user`, `extender` or `evaluator`. |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it. Commands are spelled out as they are typed. |
| `inputs` | Exact file paths, one per line. No globs, no versions. A part of a file is named after `#`. |
| `links` | Pages of this map, each as the path in backticks, a colon and one sentence on what that page gives. |
| `must-not` | What the page must not say of its topic. |
| `made` | `mirrored` or `derived`. |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove`. |

The generic shape of an entry:

```
### docs/<section>/<page>.md
- title: <the page's title>
- line: <the question the page answers>
- kind: how-to | explanation | reference
- reader: user | extender | evaluator
- says: <the page's one topic>
- inputs:
  <path>
  <path>#<part>
- links:
  `docs/<section>/<page>.md`: <one sentence on what that page gives>
- must-not: <what the page must not say>
- made: mirrored | derived
- evidence: <derived pages only>
- state: new | keep | regenerate | remove
```

### Parts of an input

A part is hashed as that part, so that a change elsewhere in the file leaves the page as it is. A part is named in one of three ways.

| Part | Form | The text taken |
|---|---|---|
| A section by its heading | `path#Heading` | The heading line to the next heading of the same or a higher level. A heading with spaces is written with the spaces. |
| An item by its ID | `path#ABC.0000` | The list line that carries the ID in bold, to the next list line at the same indent or the next heading. |
| A block by its bold label | `path#Label` | The paragraph opening with the label in bold, to the next label or heading. Used where no heading of that name exists. |

An input that the disk does not have, a file or a part, is reported by `docs-state.py` and hashed as missing. The page is regenerated and its writer reports the gap.

### The state

The planner writes `new` for a page without a previous entry, `keep` for one with, and `remove` for one that lost its material. `regenerate` is never written by the planner. The script `scripts/docs-state.py` sets it, and rewrites only the `- state:` line of each entry.

The script hashes the entry's text (the `state` line excepted) together with the content of every input. It also hashes the writer's definition `.claude/agents/docs-writer.md` and the contract `.claude/skills/docs-contract/SKILL.md`. The hash is compared with the `inputs-hash` in the front-matter of the page at the entry's path.

| State | Condition |
|---|---|
| `new` | No page at the path. |
| `regenerate` | A page exists and its hash differs. |
| `keep` | A page exists with the same hash. |
| `remove` | A page that no entry names, or the page of an entry marked `remove`. Such an entry gets no task. The index `README.md` is excepted. |

### Unowned and Did not fit

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. The writer leaves such a fact out.

`## Did not fit` lists what the planner read that contradicts itself or the outline, and what it did with it.

## The writer's task file

`docs-state.py <map> <docs-dir> --tasks <tmp-dir>` writes one task file to the task directory for every entry whose state is `new` or `regenerate`. The task file is the whole prompt of a writer. It holds, in this order:

| Line or block | What it holds |
|---|---|
| Target root | The root that input paths are relative to. |
| Page to write | The absolute path of the page, with its path in the docs directory. |
| Date | The date of the run, from `--date`, else today. |
| Version | The version the page is made for: the version of the owning project's intent beside the map, or `none`. |
| inputs-hash | The hash the page is to carry, exactly. |
| The entry | The entry verbatim. |
| Titles | The titles of the pages the entry links to, one line each as the path in backticks, a colon and the title, to cite them by. `- none` where the entry links to nothing. |
| Closing line | An instruction to write the page and report in a few lines. |

## The page's front-matter and shape

Every page is written in this shape.

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

- [<the linked entry's title>](<relative path>): <the sentence
  the entry gives for it>

Generated on <date> for version <version> from the files the
front-matter names; never edited by hand.
```

| Front-matter field | Value |
|---|---|
| `generated` | The date from the task. |
| `version` | The version from the task. |
| `made` | `mirrored` or `derived`, as the entry says. |
| `inputs-hash` | The value from the task, copied exactly. |
| `inputs` | The entry's inputs, one per line, as paths or `path#part`. |

## The index

The index `README.md` of the docs directory is derived from the map by `python scripts/docs-index.py <map> <docs-dir>`. It is deterministic: the same map gives the same index. It is never edited by hand.

Its front-matter:

| Field | Value |
|---|---|
| `generated` | The date, from `--date`, else today. |
| `version` | The version of the owning project's intent beside the map, left out when there is none. |
| `made` | `derived` |
| `inputs` | One input: the path of the map. |

Its body, in this order:

| Part | What it holds |
|---|---|
| Heading and opening | The heading `Documentation` and a fixed opening paragraph owned by the script. With a version, a line saying for which version of the intent the index was generated. |
| `## Where to start` | One line per reader of the Paths section, each page a link cited by its title. |
| One section per outline section | `Start`, `Use`, `About`, `Extend`, `Reference`, in that order, skipping a section with no entries. One line per page: the title linked to its relative path, then the entry's `line`. Where an entry has no `line`, the first sentence of its `says`. Where it has no `title`, the file name. Entries marked `remove` are left out. |
| Closing | A fixed paragraph naming the map and the script. |

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
