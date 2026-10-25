---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 8857d637a736c8dd
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md#The map
  - .claude/agents/docs-writer.md#The shape
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

The documentation map is the file `docs-map.md` that lists every page of a target's documentation and everything the page is made from. This page gives, exactly, the fields of the map, of a writer's task, of a page's front-matter and of the documentation index. It is for the extender who changes the documentation or the scripts that read these files. What the map and the pages are for is on [The documentation](../about/the-documentation.md).

## The map

The map is one Markdown file. Its skeleton is `templates/docs-map.md`. Every path in it is relative to the root of the target. The map is read by the scripts `docs-state`, `docs-index` and `docs-check` through `scripts/docs_map.py`, and by the writers. The reader of the documentation never sees it.

### Front-matter

| Key | Value |
|---|---|
| `target` | `engine` or the slug of the project. Never a path of the machine. |
| `owner` | `projects/<slug>`, the project that owns the map. |

The header carries no name for the previous map. The previous map is taken from git, as last committed, with `python scripts/docs-state.py <map> --previous <path>`. The script prints the path it wrote, or `none` when the map was never committed or the project is outside git.

When `target` is `engine`, the input paths are relative to the engine root. Otherwise they are relative to the directory of the owning project, where the map lies.

### Order of the file

1. The heading `# Documentation map - <target>`.
2. `## Paths`.
3. One section per section of the outline, in this order: `## start`, `## use`, `## about`, `## extend`, `## reference`.
4. `## Unowned`.
5. `## Did not fit`.

### Paths

One line per reader, in the form `- <reader>: <page>, <page>`. The readers are `user`, `extender` and `evaluator`. The pages are paths of this map, in reading order. The index prints them as links.

### An entry

An entry opens with the heading `### docs/<section>/<page>.md`. Below it come the fields, each as `- <field>: <value>`. A value may continue on following lines that are indented by two spaces. The fields stand in this order:

| Field | Holds |
|---|---|
| `title` | The page's title as its heading will carry it, in the reader's words, since a link cites it. |
| `line` | One line for the index: the question the page answers, no more than one sentence. |
| `kind` | `how-to`, `explanation` or `reference`. |
| `reader` | `user`, `extender` or `evaluator`. |
| `says` | What the page says, in a few sentences a writer can work from: its one topic and nothing beside it. Commands are spelled out as they are typed. |
| `inputs` | Exact file paths, one per line. No globs and no versions. Everything the writer must read and nothing else. |
| `links` | Pages of this map, one per line as `` `docs/<section>/<page>.md`: <one sentence on what that page gives> ``. The sentence is all the writer knows of the target page. |
| `must-not` | What the page must not say of its topic. |
| `made` | `mirrored` or `derived`. |
| `evidence` | Derived pages only: what the page is put together from and by what reasoning. |
| `state` | `new`, `keep`, `regenerate` or `remove`. |

#### The parts of an input

An input is a whole file, or a part of a file named after `#`. A part is hashed as that part, so a change elsewhere in the file leaves the page as it is. A part is one of three things:

- A section by its heading: `CLAUDE.md#Isolated reviewers` is the heading line up to the next heading of the same or a higher level. A heading written with spaces is written with the spaces.
- An item by its ID: the list item that carries the ID in bold, up to the next item at the same indent or the next heading.
- A block by its bold label: the paragraph that opens with the label in bold, up to the next label or heading. This applies where no heading of that name exists.

#### The values of `state`

| State | Meaning |
|---|---|
| `new` | No page exists at the path. |
| `keep` | A page exists and its hash equals the hash computed from the entry and its inputs. |
| `regenerate` | A page exists and the hashes differ. |
| `remove` | The page has no material any more. |

The planner writes `new`, `keep` or `remove`. `regenerate` is only ever set by `scripts/docs-state.py`, which rewrites the `- state:` line of each entry and leaves the rest of the map byte for byte.

### Unowned and Did not fit

`## Unowned` lists every fact a page needs and no file supports, with the page that needs it. The writer leaves such a fact out.

`## Did not fit` lists what the planner read that contradicts itself or the outline, and what it did with it.

## The writer's task

For every entry whose state is `new` or `regenerate`, `scripts/docs-state.py` writes one task file into the directory given by `--tasks`. The file is named from the page path, with `/` replaced by `-`. The task file is the whole prompt of a writer. It holds, in this order:

1. The target root, which input paths are relative to.
2. The page to write: its absolute path, its path in `docs/`, and the note that relative links are computed from that place.
3. The date.
4. The version the page is made for. It is the version of the owning project's intent, or `none`.
5. The `inputs-hash` the page is to carry, exactly.
6. The entry, verbatim.
7. The titles of the pages the entry links to, one line each as `` - `<path>`: <title> ``. A linked page that has no title in the map shows `(no title in the map)`. The titles are taken from the paths found in backticks in the entry's body.
8. The closing request: write the page, then report in a few lines.

### The hash

The `inputs-hash` is the first 16 hexadecimal characters of a SHA-256 digest. It is computed over, in this order:

1. The entry's lines, the `state` line excepted.
2. The writer's definition (`.claude/agents/docs-writer.md`) and the documentation contract (`.claude/skills/docs-contract/SKILL.md`), each as a whole.
3. Each input: its name, then its text (the part, for a part). An input the disk does not have is hashed as `<missing>` and reported.

A change to the writer's definition or the contract therefore regenerates every page. The page's hash is read from the first 2000 characters of its file.

## The page

### Front-matter

```
---
generated: <date>
version: <the version the task gives: what the page was made for>
made: mirrored | derived
inputs-hash: <the value the task gives, copied exactly>
inputs:
  - <path or path#part>
  - <path>
---
```

### Body

| Part | Holds |
|---|---|
| `# <title>` | The entry's title. |
| Opening paragraph | What the page is for and for whom. The first sentence says what the thing is. |
| The matter | In the outline of the page's kind. |
| `## See also` | One line per linked entry: `[<title>](<relative path>): <the sentence the entry gives for it>`. |
| Closing line | "Generated on <date> for version <version> from the files the front-matter names; never edited by hand." |

## The index

The index is `README.md` in the documentation directory. It is derived from the map by `python scripts/docs-index.py <map> <docs-dir>` and never edited by hand. The same map gives the same index. No model is involved.

### Front-matter

| Key | Value |
|---|---|
| `generated` | The date. |
| `version` | The version of the owning project's intent beside the map. For the engine it is the engine's version. The key is left out when there is none. |
| `made` | `derived`. |
| `inputs` | One entry: the path of the map. |

### Body

1. The heading `# Documentation` and a fixed opening paragraph, owned by the script.
2. A line giving the date and the version, when there is a version.
3. `## Where to start`, from the Paths section: one line per reader, each page a link under its title.
4. One section per section of the outline that has entries, in the order start, use, about, extend, reference, headed Start, Use, About, Extend, Reference. Each entry that is not marked `remove` is one line: `- [<title>](<relative path>): <line>`. Where an entry has no `line`, the first sentence of `says` stands in its place.
5. A closing note naming the map and the script.

## See also

- [The documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
