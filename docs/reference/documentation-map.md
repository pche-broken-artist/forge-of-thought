---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: ea53487fde14f8b3
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of the documentation with everything the page is made from. This page gives the exact fields of the map, of the task a page's writer receives, of a page's front-matter and of the documentation index, for the extender who changes any of them.

The map lies beside the owning project's ledger. The documentation's readers never see it. A planner agent writes it, scripts read it, and a writer agent (an agent that writes one page) reads its own entry.

## The map

The shape is the skeleton `templates/docs-map.md`. Every path in the map is relative to the root of the target: the engine root when `target` is `engine`, otherwise the owning project's directory.

### Front-matter

| Key | Holds |
|---|---|
| `generated` | the date of the run, `YYYY-MM-DD` |
| `target` | `engine`, or the project's slug; never a path of the machine |
| `owner` | `projects/<slug>` |
| `previous` | `tmp/docs-map.previous.md`, or `none` |

### Order of the file

1. The front-matter.
2. The heading `# Documentation map - <target>`.
3. The section `## Paths`.
4. One section per section of the outline, in the outline's order: `## start`, `## use`, `## about`, `## extend`, `## reference`. A section with no page stays empty.
5. The section `## Unowned`.
6. The section `## Did not fit`.

### The Paths section

One line per reader, in the form `- <reader>: <page path>, <page path>`. The readers are `user`, `extender` and `evaluator`. The pages are pages of this map, in reading order. The index prints them as links.

### An entry

An entry opens with the heading `### docs/<section>/<page>.md`. The section in the path is one of the outline's sections. Below the heading stand the fields, each as `- <field>: <value>`. A value may continue on the following lines when they are indented. The fields come in this order:

| Field | Holds |
|---|---|
| `title` | the page's title as its heading will carry it, in the reader's words, because a link cites it |
| `line` | one line for the index: the question the page answers, one sentence |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | `user`, `extender` or `evaluator` |
| `says` | what the page says, in a few sentences: its one topic and nothing beside it, commands spelled as they are typed |
| `inputs` | exact file paths, one per line; no globs, no versions |
| `links` | one line per linked page: the page's path in backticks, a colon, one sentence on what that page gives |
| `must-not` | what the page must not say of its topic |
| `made` | `mirrored` or `derived` |
| `evidence` | derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

#### Inputs

An input is a file, or a part of a file named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is. A part is one of three things:

| Written as | The part is |
|---|---|
| `path#Heading` | the section: the heading line to the next heading of the same or a higher level; a heading with spaces is written with the spaces |
| `path#XXX.NNNN` | the item that carries that ID: its line to the next item at the same indent, or to a heading |
| `path#Label` | a block opened by a bold label such as `**Label.**`, to the next label or heading; used where no heading of that name exists |

A file or a part the disk does not have is hashed as missing. The page is regenerated and its writer reports the gap.

#### Links

Only pages of the same map are linked. A writer sees only its own entry and its inputs, so the sentence beside a link is all it knows of the target page.

#### State

| Value | Set by | Meaning |
|---|---|---|
| `new` | the planner for a page without a previous entry; the script when no page exists at the path | no page at the path |
| `keep` | the planner for a page with a previous entry; the script when the hashes agree | a page exists and its hash is the same |
| `regenerate` | the script only | a page exists and its hash differs: an input or the entry changed |
| `remove` | the planner, for an entry that lost its material; the script, for a page under the documentation directory that no entry names | the page is to be deleted |

An entry marked `remove` keeps its state and gets no task. The script rewrites only the `- state:` line of each entry and leaves the rest of the map as it was.

### Unowned and Did not fit

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. The writer leaves such a fact out.

`## Did not fit` lists what the planner read that contradicts itself or the outline, and what it did with it.

## The state hash

The script `scripts/docs-state.py` computes one hash per entry, 16 hexadecimal characters. Three things go into it:

- the text of the entry, the `state` line excepted
- the writer's definition `.claude/agents/docs-writer.md` and the contract `.claude/skills/docs-contract/SKILL.md`
- the content of every input, whole or as the named part

The page at the entry's path carries the hash it was made from in its front-matter as `inputs-hash`. The script compares the two and sets `state`.

## The writer's task

For every entry whose state is `new` or `regenerate` the script writes one task file, named after the page's path with `/` replaced by `-`. The task is the whole prompt of the writer. It holds, in this order:

1. the target root, to which the input paths are relative
2. the page to write: its absolute path and its path in `docs/`, from which relative links are computed
3. the date
4. the version the page is made for: the version of the owning project's intent beside the map, or `none`
5. the `inputs-hash` the page is to carry
6. the entry, verbatim
7. the titles of the pages the entry links to, each as the path in backticks and the title, to cite them by; `none` where the entry links to no page

The command is run as `python scripts/docs-state.py projects/<slug>/docs-map.md projects/<slug>/docs --tasks tmp/docs-tasks`. The script prints the counts of `new`, `regenerate` and `keep`, the pages to remove and every missing input.

## A page

Every page has this shape:

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

Generated on <date> for version <version> from the files the front-matter names; never edited by hand.
```

The headings of the matter depend on the kind of the page. A heading with no material is left out and never left empty.

## The index

The index is `README.md` in the documentation directory. The script `scripts/docs-index.py` derives it from the map and no model is involved, so the same map gives the same index. It is never edited by hand. The command is `python scripts/docs-index.py projects/<slug>/docs-map.md projects/<slug>/docs`.

The front-matter holds four keys:

| Key | Holds |
|---|---|
| `generated` | the date |
| `version` | the version of the owning project's intent beside the map; left out where there is none |
| `made` | `derived` |
| `inputs` | the path of the map, its one input |

The body, in this order:

1. The heading `# Documentation`, and an opening paragraph fixed in the script. Where a version is known, a line says the date and the version of the intent, which for the engine is the version a release carries.
2. `## Where to start`: one line per reader of the Paths section, as `- **<the reader>**: <links>.`, each page a link cited by its title.
3. One section per outline section that has entries, in the outline's order and headed `## Start`, `## Use`, `## About`, `## Extend`, `## Reference`. Each entry is a line `- [<title>](<path relative to docs/>): <line>`. Where an entry has no `line`, the first sentence of its `says` stands in its place. An entry marked `remove` is left out.
4. A closing paragraph naming the map and the script the index is derived by.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
