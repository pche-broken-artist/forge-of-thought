---
generated: 2026-10-10
made: mirrored
inputs-hash: 4a8df66caa536fc0
inputs:
  - templates/docs-map.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - .claude/skills/docs-contract/SKILL.md
  - scripts/docs_map.py
  - scripts/docs-state.py
  - scripts/docs-index.py
---

# Documentation map

This page is a reference for the extender. It states the shape of the
documentation map `docs-map.md`, of the task a page's writer receives,
of a page, and of the index `docs/README.md`, as the map's skeleton,
the planner's and the writer's definitions, the shared contract and the
scripts own them.

## The map

The skeleton is `templates/docs-map.md`. The map is read by the scripts
and by the writers, never by the reader of the documentation.

### Front-matter

| Key | Holds |
|---|---|
| `generated` | the date of the run |
| `target` | `engine`, or a project's slug; never a path of the machine |
| `owner` | the project that owns the documentation |
| `previous` | the map of the previous run, or `none` |

Every path in the map is relative to the target's root: the engine root
when `target` is `engine`, otherwise the owning project's directory.

### Sections and entries

The map has one section per section of the outline, in the outline's
order: `start`, `use`, `about`, `extend`, `reference`. A section with no
material is left out. In each section there is one entry per page,
headed `### docs/<section>/<page>.md`. Page names are lowercase with
hyphens, the job or topic as the name, never a number.

### Fields of an entry

The fields stand in this order, each as `- <field>: <value>`, a long
value continued on indented lines.

| Field | Holds |
|---|---|
| `title` | the page's title as its heading will carry it, in the reader's words, since a link cites it |
| `kind` | `how-to`, `explanation` or `reference` |
| `reader` | one or more of `user`, `extender`, `evaluator` |
| `says` | what the page says, its one topic and nothing beside it, in a few sentences a writer can work from |
| `inputs` | exact file paths, one per line; whole files, no globs, no sections, no versions; everything the writer must read and nothing else |
| `links` | few, only pages of this map; each a path in backticks and one sentence on what that page gives |
| `must-not` | what the page must not say or contain |
| `made` | `mirrored` or `derived` |
| `evidence` | derived pages only: what the page is put together from and by what reasoning |
| `state` | `new`, `keep`, `regenerate` or `remove` |

Where only part of an input matters, the file is named in `inputs` and
the part in `says`. A mirrored page restates what its inputs say. A
derived page puts together what no single file says, from evidence in
several.

### State

The planner writes `new` for a page without a previous entry, `keep`
for one with, and `remove` for one that lost its material. The state
script `scripts/docs-state.py` then sets the state from the content of
the inputs, and `regenerate` is only ever set by it:

| State | Meaning |
|---|---|
| `new` | no page exists at the entry's path |
| `regenerate` | a page exists and its hash differs: an input or the entry changed |
| `keep` | a page exists with the same hash |

The hash covers the text of the entry (its `state` line excepted) and
the content of every input file. A page carries the hash it was made
from in its `inputs-hash`. The script rewrites only the `- state:` line
of each entry and leaves the rest of the map byte for byte. A page under
the documentation directory that no entry names is listed as `remove`;
the index `README.md` is excepted. An input the map names and the disk
lacks is reported and hashed as missing, so the page is regenerated and
its writer reports the gap.

### Closing sections

After the page sections come two more:

- `## Unowned`: every fact a page needs and no file supports, with the
  page that needs it.
- `## Did not fit`: what contradicted itself or the outline, and what
  was done with it.

### The reader of the map

`scripts/docs_map.py` is the one reader shared by `docs-state`,
`docs-index` and `docs-check`. It splits the map into the front-matter
and the entries. An entry has a path, a section, a name, its fields and
its lines verbatim. An entry is recognised by a heading of the form
`### docs/<section>/<name>.md`, a field by a line of the form
`- <field>: <value>`. The links of an entry are the paths in backticks
that begin with `docs/`, without the entry's own.

## The writer's task

For every page whose state is `new` or `regenerate`, `docs-state` writes
one task file into the directory named by `--tasks`; it is a writer's
whole prompt. The writer reads it first. It holds, in this order:

1. the engine root, which the input paths are relative to
2. the page's path, with the note that relative links are computed from
   that place
3. the date
4. the hash the page is to carry in its front-matter
5. the entry from the map, verbatim
6. the titles of the pages the entry links to, to cite them by

The directory is emptied of old task files at each run. Invocation:

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

## The page

Front-matter, in this order:

| Key | Holds |
|---|---|
| `generated` | the date |
| `made` | `mirrored` or `derived` |
| `inputs-hash` | the hash the task gives, copied exactly |
| `inputs` | the entry's input paths, one per line |

Then, in this order:

1. the title, the entry's
2. one paragraph on what the page is for and for whom; on a derived
   page it also says the page was put together from those files
3. the matter, under headings where the topic needs them
4. `## See also`, one line per linked page: its title as the task gives
   it, a relative link, and the sentence the entry gives for it

Links into `docs/` go only to pages the entry lists, as relative paths
from the page's directory. A link to a file of the engine is a path in
backticks, not a hyperlink. A page of one kind states what that kind
does: a how-to says what the person does and sees, an explanation says
what a thing is and why, a reference states facts in the structure of
what it mirrors.

### What must never reach a page or the map

- a name of a person, a company, a host, an account, an e-mail, an
  identifier of an instance; a placeholder slug replaces a real one in
  every example
- an address, except the public home of the target where the target's
  own documents name it as such
- a document of any project but the owning one
- anything of a skill or an agent copied as an instruction; a page says
  what a command does for the person, in the person's terms
- an ID of the chain; the reason is given, its ID is not
- a long dash; a colon, a full stop or a spaced hyphen stands instead

Pages are in English, plain, in the spelling the inputs use. Where the
operating layer and the intent differ, the page takes the operating
layer's wording and the intent's reason.

## The index

`docs/README.md` is derived from the map by `scripts/docs-index.py`,
deterministically and without a model: the same map gives the same
index. It is never edited by hand and never planned as a page.

| Part | Content |
|---|---|
| front-matter | `generated`, `version` (when found), `made: derived`, and the map as its one input |
| opening | a fixed paragraph; where a version is found, a line with the date and the version |
| reading paths | the user: `start/`, then `use/`; the extender: `extend/`, then `reference/`; the evaluator: `about/` |
| the pages | one line per page, grouped by section in the outline's order: the title linked to its relative path, then the first sentence of `says`; a page in state `remove` is skipped |
| closing | the path of the map and the note that the index is derived |

The version is the one in the front-matter of `10-intent.md` beside the
map, which for the engine is its own version; a release carries the same
number. Invocation:

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

## See also

- [About the documentation](../about/the-documentation.md): what the map and the pages are for.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
