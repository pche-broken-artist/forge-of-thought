---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 31dc24418b3b895f
inputs:
  - scripts/forge-save.py
  - scripts/forge-pull.py
  - scripts/forge-status.py
  - scripts/forge-clone.py
  - scripts/forge-branch.py
  - scripts/forge-history.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/md2pptx.py
  - scripts/md2docx.py
  - scripts/forge_tools.py
  - scripts/hook-walkthrough.py
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
  - scripts/docs_map.py
  - CLAUDE.md#Persistence (git)
---

# Scripts

The scripts are the files in `scripts/`: the one door through which the forge reaches git, converts documents and generates the documentation. This page lists every script with its synopsis, options, forms, what it needs and the command that runs it, for the user who runs them and the extender who writes one. Each script carries the same help in its own header.

Every script is run as `python scripts/<name>.py`. A system that has only `python3` gives the interpreter that name. The scripts install nothing and carry no URL and no identity.

## Overview

| Script | What it is for | Run by | What it needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save` | Python, git |
| `forge-pull.py` | fast-forward the engine and the projects from their remotes | `/pull` | Python, git |
| `forge-status.py` | report the git state, read-only | `/pull`, `/setup` | Python, git |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | switch or create a branch of one repository | run directly | Python, git |
| `forge-history.py` | print the history of one item by its ID | `/history` | Python |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | make a PowerPoint deck from a Markdown deck | `/render`, `/publish` | Python, pandoc or the claude engine |
| `md2docx.py` | make a Word document from a Markdown render | `/render`, `/publish` | Python, pandoc or the claude engine |
| `hook-walkthrough.py` | repeat the working rules at every prompt | the hook of `.claude/settings.json` | Python |
| `docs-state.py` | compute the state of every page, prepare the writers' tasks | `/document` | Python |
| `docs-index.py` | derive the documentation index from the map | `/document` | Python |
| `docs-check.py` | check the generated documentation, or one file | `/document`, `/render` | Python |

Three modules beside them are shared and are not commands:

- `forge_repos.py`: what the git scripts share (the engine root, the git check, the list of repositories to visit, running git, the state of a repository against its origin, coloured output).
- `forge_tools.py`: what the conversion scripts share (finding a tool on PATH, resolving paths, running a tool, the headless Claude Code run).
- `docs_map.py`: the one reader of the documentation map, shared by the three documentation scripts and by `forge-history.py`.

## forge-save.py

What it does: saves the engine and every project that is a repository of its own. Per repository it stages everything, commits, and, when an origin is configured, integrates remote changes by rebase and pushes. Without an origin the commit stays local and is reported. It never uses `git add -f` and never `git clean`.

Synopsis:

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

Options:

- `-m`, `--message`: the commit message; generated from the files when absent.
- `--tag`: tags the commit and pushes the tag with it. It needs a slug. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.

Forms:

- bare: every repository with changes, each with its own commit. A project directory without a repository is skipped with a note.
- `<slug>`: that one repository. A project directory without a repository is refused.
- `forge`: the engine only.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py`.

Example:

```
python scripts/forge-save.py forge --tag v3.33
```

## forge-pull.py

What it does: pulls the latest state from the remotes, fast-forward only. A repository with unsaved changes is not touched. A repository whose history has diverged from its origin is refused and nothing is pulled. The script never merges. After a pull it prints where the repository moved from and to (`before` and `after`, each a hash and a subject) and the subjects of the commits between.

Synopsis:

```
python scripts/forge-pull.py [slug]
```

Forms:

- bare: the engine, then every project with an origin. A repository with unsaved changes, without a repository or without an origin is reported and skipped.
- `<slug>`: that one repository; the same conditions refuse instead of skip.
- `forge`: the engine only, which is its upgrade channel.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py`.

Example:

```
python scripts/forge-pull.py forge
```

## forge-status.py

What it does: reports the git state without changing anything. It prints the global git configuration file git actually reads. Then, for the engine and each project: unsaved changes (or "clean"), the branch, the last commit and the origin (or "no origin" or "not under git").

Synopsis:

```
python scripts/forge-status.py [--remote]
```

Options:

- `--remote`: fetches each origin and reports the branch against it. Without the flag the script touches no network. The fetch changes nothing in the working tree.

The states reported with `--remote`:

| State | Meaning |
|---|---|
| `up to date` | the branch equals its origin |
| `behind N` | the origin has N commits the branch lacks |
| `ahead N` | the branch has N commits the origin lacks |
| `diverged (ahead N, behind M)` | both have commits the other lacks |
| `no origin` | the repository has no origin |
| `no upstream` | no branch, or no counterpart on the origin |

Forms: no slug; it always visits the engine and every project.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py`.

Example:

```
python scripts/forge-status.py --remote
```

## forge-clone.py

What it does: clones an existing project into `projects/<repository name>`. The directory name falls out of the URL, and an existing directory is never overwritten. It sets no identity. Afterwards it reports the last commit, the origin, the commit identity git resolves for the clone, and whether the project carries a ledger with a `kind:` header.

Synopsis:

```
python scripts/forge-clone.py <url>
```

Forms: one URL, no bare form.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py`.

Example:

```
python scripts/forge-clone.py https://example.com/team/my-idea.git
```

## forge-branch.py

What it does: switches one repository to a branch, creating it from the current state when it does not exist; `main` switches back. Without a branch name it reports the current branch and lists the branches. Unsaved changes stop the switch. Merging, deleting and pushing branches stay with git: a new branch reaches the remote with the first save made on it.

Synopsis:

```
python scripts/forge-branch.py <slug> [branch]
```

Forms:

- `<slug> <branch>`: switch, creating the branch when missing.
- `<slug>`: report the current branch and the branches.
- `forge` as the slug: the engine. There is no bare form.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py`.

Example:

```
python scripts/forge-branch.py forge work-release
```

## forge-history.py

What it does: prints the history of one item of a project as one timeline, read-only and without a model. For an item named by its ID (a short form such as `pos580` is read as `POS.0580`) in `projects/<slug>` (`forge` is the engine's own project) it gathers three parts:

1. Today: the file that holds the item and its wording.
2. Timeline: one line per event, oldest first, with version, date where the log has one, and what happened (`born`, `changed`, `closed`, `removed`, `approved`) from every history log of the project whose subject names the ID; `mentioned by <ID>` from the records of other items that name it; `archive` from the rows of the history archives that mention it. A record's reason follows its line; its Action and its Was follow as marked lines.
3. Cited today: every other place in the project that names the ID, as file and line.

Long texts are wrapped at 78 columns. An ID with no item and no record is said so. The pages of `docs/`, the map, the renders, the resources and `tmp/` are never searched.

Synopsis:

```
python scripts/forge-history.py <ID> <slug> [--full]
```

Options:

- `--full`: prints every Was in full; without it a Was is shortened to its first sentences.

Needs: Python 3.8 or newer, `forge_repos.py` and `docs_map.py`.

Example:

```
python scripts/forge-history.py REQ.0120 <slug> --full
```

The command behind it is described in [Read the history of an item](../use/read-the-history-of-an-item.md).

## doc2md.py

What it does: converts documents to Markdown through markitdown. Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. A name collision within one run gets `_1`, `_2` and so on. The handled extensions are `.pdf`, `.docx`, `.docm`, `.pptx`, `.pptm`, `.xlsx`, `.xlsm`, `.xls`, `.epub`, `.html`, `.htm`, `.csv`, `.json`, `.xml` and `.msg`. The legacy `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported: resave them as `.docx`, `.pptx` or `.xlsx` first.

Synopsis:

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

Forms of an input, which can be mixed and repeated:

- a file name
- a glob such as `"*.pdf"` or `"docs/**/*.pptx"`
- a list file: plain text, one path or glob per line, `#` or `;` starts a comment, relative paths resolved against the list file's directory
- a directory, with `--recurse`

Options:

- `-o`, `--out-dir`: where to write the `.md` files.
- `--suffix`: text inserted before the `.md` extension (`.text` gives `report.text.md`).
- `--recurse`: descend into directories and globs without `**`.
- `--force`: overwrite existing `.md` files.
- `--as-list`: treat every input as a list file.
- `--markitdown-path`: explicit path to the markitdown executable.
- `--dry-run`: list what would be converted and write nothing.
- `--list-tools`: check that markitdown is reachable and exit.

Needs: Python 3.8 or newer and markitdown, resolved from PATH or named by `--markitdown-path`. The script never installs anything. Install it yourself with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

Example:

```
python scripts/doc2md.py "*.pdf" "*.docx" -o md
```

## md2pptx.py

What it does: makes a PowerPoint deck from a Markdown deck definition. The output lands next to the input with the same basename unless `-o` names a path.

Synopsis:

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

The two engines:

| Engine | What it does | Run by |
|---|---|---|
| `claude` (default) | a model designs the deck through headless Claude Code with the official pptx skill; expensive, never the same twice | `/publish` |
| `pandoc` | pandoc writes a plain deck deterministically, one slide per second-level heading | `/render` |

Options:

- `--template`: a `.potx` or `.pptx`, named by path, typically a file in a library project. Without it the claude engine designs the style itself and pandoc uses its built-in one.
- `--recipe`: the recipe the definition was rendered from; the claude engine reads its Format section.
- `-o`, `--out`: the output file.
- `--model`: the model of the headless run; default `opus`; the claude engine only.

Needs: Python 3.8 or newer and `forge_tools.py`. What pandoc and the claude engine need is in the section on `forge_tools.py` below.

Example:

```
python scripts/md2pptx.py deck.md --template <path>/template.potx
```

## md2docx.py

What it does: converts a Markdown render into a Word document. The YAML front-matter of the render is read as metadata and does not appear. Mermaid diagrams are not rendered and land as blocks of code. The output lands next to the input with the same basename unless `-o` names a path.

Synopsis:

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

The two engines:

| Engine | What it does | Run by |
|---|---|---|
| `pandoc` (default) | pandoc writes the plain document deterministically | `/render` |
| `claude` | a model designs the document through headless Claude Code with the official docx skill, the recipe's Format section giving it instructions; expensive, never the same twice | `/publish` |

Options:

- `--reference`: a `.docx`, or a Word template `.dotx` or `.dotm`, typically a file in a library project. pandoc takes its styles and ignores its content. The claude engine takes it as the template it starts from.
- `--page-size`: `A4` (default) or `Letter`. It applies only when no `--reference` is given, because a template decides its own paper.
- `--recipe`: the recipe the render was made from; the claude engine reads its Format section.
- `-o`, `--out`: the output file.
- `--model`: the model of the headless run; default `opus`; the claude engine only.

Needs: Python 3.8 or newer and `forge_tools.py`.

Example:

```
python scripts/md2docx.py brd.md --reference <path>/styles.docx
```

## What the conversions need

This is owned by `forge_tools.py`. Every tool is resolved from PATH and never installed by a script. The model of the claude engine is told to install and download nothing as well.

- pandoc, the engine of `/render`: install it yourself, once, from https://pandoc.org/installing.html (Windows: `winget install JohnMacFarlane.Pandoc`; macOS: `brew install pandoc`; Linux: your package manager).
- The claude engine, behind `/publish`: the `claude` CLI on PATH and the official document skill of the format (pptx or docx), under either of its names, `anthropic-skills:<format>` where Claude Code brings it, `document-skills:<format>` where the plugin does. Where neither is there, install the plugin yourself, once, from an interactive Claude Code session:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

The page [Install what the forge needs](../start/install.md) covers installing these.

## hook-walkthrough.py

What it does: Claude Code runs it on every prompt (configured in `.claude/settings.json`) and adds its output to the context of that turn. It prints the one-item walkthrough rule, the pointer to the walkthrough skill, and three lines of conduct: use the forge's scripts rather than the raw tool, say what a command of one's own does and wait for the principal's yes before running it, and change nothing that was not agreed and approved. It reads nothing, writes nothing, takes no arguments and is independent of the working directory.

Synopsis:

```
python scripts/hook-walkthrough.py
```

Needs: Python 3.8 or newer on PATH as `python`.

## The documentation scripts

Three scripts serve the run of `/document`, described in [Generate the documentation](../use/generate-the-documentation.md). In order of the run: `docs-state.py` computes which pages need writing and prepares the writers' tasks, the writers write the pages, `docs-index.py` derives the index, and `docs-check.py` checks the result. All three need Python 3.8 or newer and `docs_map.py` beside them, and nothing else.

### docs-state.py

What it does: computes the state of every page from the content of its inputs and prepares the writers' tasks. For every entry of the documentation map it hashes the entry's text (its `state` line excepted) together with the content of every input the entry names: a whole file, or the part of a file named after `#` (a section by its heading, an item by its ID), hashed as that part. A change elsewhere in the file leaves the page as it is.

The generator is hashed with the inputs: the writer's definition (`.claude/agents/docs-writer.md`) and the contract (`.claude/skills/docs-contract/SKILL.md`). A change of the rule a page is made by therefore regenerates every page made by the old one. The planner's rules reach the pages through the entries it writes.

The page that exists at the entry's path carries in its front-matter the hash it was made from, `inputs-hash`. The two are compared and the entry's `state` is set in the map:

| State | Meaning |
|---|---|
| `new` | no page at the path |
| `regenerate` | a page exists and its hash differs (an input or the entry changed) |
| `keep` | a page exists with the same hash |
| `remove` | a page under the docs directory that no entry names, or the page of an entry the planner marked `remove`; the index `README.md` is excepted |

A `remove` entry keeps its state and gets no task. The state is computed, never judged. An input the map names and the disk does not have is reported and hashed as missing; the page is regenerated and its writer reports the gap.

For every `new` or `regenerate` entry one task file is written to the tasks directory: the engine root, the page's path, the date, the version the page is made for, the hash the page is to carry, the entry verbatim and the titles of the pages it links to. A task is a `docs-writer` agent's whole prompt.

The map's `inputs` are relative to the target's root: the engine root when `target: engine`, else the owning project's directory. The script rewrites only the `- state:` line of each entry and leaves the rest of the map byte for byte.

Synopsis:

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

Example:

```
python scripts/docs-state.py projects/<slug>/docs-map.md projects/<slug>/docs --tasks tmp/docs-tasks
```

### docs-index.py

What it does: writes `<docs-dir>/README.md` from the documentation map. It has one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its relative path and the entry's `line` (the first sentence of its `says` where an entry has no `line`). Before the sections come the reader paths of the map's `## Paths` section, each page a link. It is deterministic: the same map gives the same index. No model is involved. The index is never edited by hand.

Synopsis:

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

The front-matter of the index names the map as its one input and carries the version of the owning project's intent beside the map. The opening paragraph is fixed text of this script.

Example:

```
python scripts/docs-index.py projects/<slug>/docs-map.md projects/<slug>/docs
```

### docs-check.py

What it does: verifies the pages under the docs directory against the map and against the rules of a page, and prints every failure with its file and line:

- every entry of the map not in state `remove` has its page, and no page lies in the docs directory that the map does not name (the index `README.md` excepted);
- every relative link to a `.md` file resolves;
- no long dash (em or en) in the prose of any page; a code span and a fenced block are exempt;
- every page opens with a front-matter;
- no instance fact: the values of `CLAUDE.local.md` at the engine root (every word of four letters or more in a value, looked for outside URLs), any e-mail address but a placeholder at `example.*`, any absolute path of a machine (a drive letter, a user's home directory), and every `--fact` pattern given.

The exit code is 0 when everything holds and 1 when anything fails. The check mends nothing: a page that fails is regenerated by the documentation command.

The one-file form: with `--file <path>` in place of a map and a directory, one file is scanned for instance facts only (the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns). There is no map, link, dash or e-mail rule. This is the scan `/render` runs on a render it has just written, described in [Render an output](../use/render-an-output.md).

The script carries no name, address or host of its own: the instance facts it looks for are read from `CLAUDE.local.md` at run time. A match is reported with its line, so a false hit is seen and the rule, not the page, is adjusted.

Synopsis:

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

Examples:

```
python scripts/docs-check.py projects/<slug>/docs-map.md projects/<slug>/docs --fact <pattern>
python scripts/docs-check.py --file README.md
```

## Portability

The scripts are the only platform-bound layer of the forge: they run unchanged on Linux, macOS and Windows with Python 3.8 or newer, paths composed with `pathlib`, external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH, and usage examples free of Windows-specific paths. To write a script of one's own see [Add a script](../extend/add-a-script.md). For the terms used here see the [Glossary](glossary.md).

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the one-file scan.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
