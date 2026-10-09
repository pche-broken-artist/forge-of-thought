---
generated: 2026-10-09
made: mirrored
inputs-hash: b4e40c911de6383e
inputs:
  - scripts/forge-save.py
  - scripts/forge-pull.py
  - scripts/forge-status.py
  - scripts/forge-clone.py
  - scripts/forge-branch.py
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
  - CLAUDE.md
---

# Scripts

This page lists every file in `scripts/`: what it does, how it is called,
what it needs and where its output lands. It is for the person who runs
the scripts and for the one who extends them. Every script is run as
`python scripts/<name>.py`, needs Python 3.8 or newer, and installs
nothing itself.

In the forms below, `<slug>` names a project under `projects/`, and
`forge` names the engine itself.

## Git scripts

The scripts in `scripts/` are the only door to git, reading state
included. They carry no URL and no identity: the commit identity is
git's own, resolved from the user's configuration. All five need `git`
on PATH and `forge_repos.py` beside them.

### forge-save.py

Saves to git: commit and push, for the engine and every project that is
a repository of its own.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

| Form | Effect |
|---|---|
| bare | visits the engine and every `projects/<slug>/.git`, and gives each one with changes its own commit |
| `<slug>` | saves that repository only; `forge` means the engine |

| Option | Meaning |
|---|---|
| `-m MESSAGE` | the commit message; without it one is generated from the files |
| `--tag NAME` | tags the commit and pushes the tag with it; needs a slug, because it concerns one repository |

Per repository it stages everything, commits, and, when an origin is
configured, integrates remote changes by rebase and pushes. Without an
origin the commit is kept locally and reported. When there is nothing to
commit, `--tag` tags the current HEAD, so a tag can mark a state before a
large change. An existing tag is refused. A project directory without a
repository is skipped with a note (bare) or refused (slug). The script
never sets an identity or a remote, never initialises a repository,
never uses `git add -f` and never `git clean`.

### forge-pull.py

Pulls the latest from the remotes: the engine (its upgrade channel) and
every project that has an origin.

```
python scripts/forge-pull.py [slug]
```

Forms: bare pulls the engine, then every project with an origin;
`<slug>` pulls that one repository, `forge` the engine. The pull is
fast-forward only. A repository with unsaved changes is not touched: it
is reported and skipped (bare) or refused (slug), and `forge-save.py` is
run first. Projects without a repository or without an origin are
reported and skipped.

### forge-status.py

Reports the git state of the engine and every project. Read-only.

```
python scripts/forge-status.py
```

It first names the global configuration file git actually reads. Then,
for the engine and each project, it shows unsaved changes (or "clean"),
the branch, the last commit and the origin, or "no origin" or "not under
git". It takes no slug.

### forge-clone.py

Brings an existing project in by cloning its repository into `projects/`.
`/import-project` is its door.

```
python scripts/forge-clone.py <url>
```

The directory is `projects/<repository name>`, taken from the URL; an
existing directory is never overwritten. Afterwards it reports the last
commit, the origin, the commit identity git resolves for the clone, and
whether the project carries a ledger with a `kind:` header. The absence
of one is a fact, not a defect.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports
which branch it is on.

```
python scripts/forge-branch.py <slug> [branch]
```

The repository is named by its slug (`forge` for the engine); there is
no bare form. With a branch name it switches to that branch, creating it
from the current state if it does not exist; `main` switches back.
Without a name it reports the current branch and lists the branches.
Unsaved changes stop the switch: save first. Merging, deleting and
pushing branches stay with git; a new branch reaches the remote with the
first `forge-save.py` made on it, and a release is made from `main` only.

## Conversion scripts

### doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel) to Markdown using
markitdown. `/ingest` runs it for a source that is a binary.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

Inputs may be mixed and repeated, in these notations:

- a single file name;
- glob notation, such as `"*.pdf"` or `"docs/**/*.pptx"`;
- a list file: plain text, one path or glob per line, `#` or `;` starting
  a comment, relative paths resolved against the list file's own
  directory;
- a directory, with `--recurse`.

| Option | Meaning |
|---|---|
| `-o <dir>` | write the results in this directory; default is next to each document |
| `--suffix <text>` | insert text before the `.md` extension (`.text` gives `report.text.md`) |
| `--recurse` | descend into directories |
| `--force` | overwrite an existing `.md`; otherwise it is skipped |
| `--as-list` | treat the input as a list file |
| `--markitdown-path <exe>` | name the markitdown executable |
| `--dry-run` | list what would be converted, write nothing |
| `--list-tools` | check that markitdown is reachable, and exit |

Each document becomes `<name>.md`; a name collision within one run gets
`_1`, `_2` and so on. Handled extensions: `.pdf` `.docx` `.docm` `.pptx`
`.pptm` `.xlsx` `.xlsm` `.xls` `.epub` `.html` `.htm` `.csv` `.json`
`.xml` `.msg`. The legacy binaries `.doc` `.ppt` `.rtf` `.odt` `.odp`
`.ods` are reported as unsupported and are to be resaved as
`.docx`, `.pptx` or `.xlsx` first.

Needs: markitdown, resolved from PATH or named by `--markitdown-path`.
The script never installs it; install it with
`pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

| Engine | What it does |
|---|---|
| `claude` (the default) | a model converts the free-form definition, through headless Claude Code with Anthropic's pptx skill; expensive, never the same twice; the engine of `/publish` |
| `pandoc` | deterministic: one slide per second-level heading, nothing interpreted by a model; cheap, plain, the same result every time; the engine of `/render` |

| Option | Meaning |
|---|---|
| `--template <path>` | a `.potx` or `.pptx`, named by path, typically a file in a library project's `sources/`; without it the claude engine designs its own style and pandoc uses its built-in one |
| `--recipe <recipe.md>` | the recipe the definition was rendered from; the claude engine reads its Format section |
| `-o <file.pptx>` | the output path; default is next to the input with the same basename |
| `--model <model>` | model of the headless run; default `opus`; the claude engine only |

Needs: `forge_tools.py` beside it. The pandoc engine needs pandoc on
PATH. The claude engine needs the pptx skill under either of its names,
`anthropic-skills:pptx` or `document-skills:pptx`; where neither is
there, install the plugin once from an interactive Claude Code session
(`/plugin marketplace add anthropics/skills`, then
`/plugin install document-skills@anthropic-agent-skills`). The model is
told to install and download nothing.

### md2docx.py

Converts a Markdown render into a Word document.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

| Engine | What it does |
|---|---|
| `pandoc` (the default) | deterministic: pandoc reads the Markdown and writes a `.docx`; cheap, the same result every time; the engine of `/render` |
| `claude` | a model converts, through headless Claude Code with Anthropic's docx skill, the recipe's Format section giving its instructions; expensive, never the same twice; the engine of `/publish` |

| Option | Meaning |
|---|---|
| `--reference <path>` | a `.docx`, or a Word template `.dotx` or `.dotm`, typically a file in a library project's `sources/`; pandoc takes its styles and ignores its content; the claude engine starts from it as its template |
| `--page-size A4\|Letter` | the page; A4 when absent; applied only without `--reference`, because a reference document decides its own paper |
| `--recipe <recipe.md>` | the recipe the render was made from; the claude engine reads its Format section |
| `-o <file.docx>` | the output path; default is next to the input with the same basename |
| `--model <model>` | model of the headless run; the claude engine only |

The YAML front-matter at the top of the render is read as metadata and
does not appear in the document. Mermaid diagrams are not rendered; they
land as blocks of code. Without `--reference`, pandoc's built-in styles
apply, with the page size written in.

Needs: `forge_tools.py` beside it. The pandoc engine needs pandoc on
PATH. The claude engine needs the docx skill under either of its names,
`anthropic-skills:docx` or `document-skills:docx`, installed as for
`md2pptx.py`. The script installs nothing.

## The per-prompt hook

### hook-walkthrough.py

The `UserPromptSubmit` hook of the engine, configured in
`.claude/settings.json`. It repeats the one-item walkthrough rule at
every prompt.

```
python scripts/hook-walkthrough.py
```

Claude Code runs it on every user prompt and adds its output to the
context of that turn. It prints the walkthrough rule with its verdict
line, the pointer to the skill that holds the full shape, and three
lines of conduct: use the forge's scripts, say what a command of one's
own does and ask before running it, and change nothing that was not
agreed and approved. It reads nothing, writes nothing and takes no
arguments. It is independent of the working directory: the settings
invoke it in exec form and hand it its own path through the
`${CLAUDE_PROJECT_DIR}` placeholder.

Needs: Python 3.8 or newer on PATH as `python`. Nothing else.

## Documentation scripts

The three scripts serve `/document`
(`.claude/skills/document/SKILL.md`). Each reads the documentation map
through `docs_map.py` and needs nothing else. In the run, `docs-state.py`
comes first and prepares the writers' tasks, `docs-index.py` derives the
index, and `docs-check.py` verifies the pages. The map's `inputs` are
relative to the target's root: the engine root when `target: engine`,
else the owning project's directory.

### docs-state.py

Computes the state of every page from the content of its inputs and
prepares the writers' tasks.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

For every entry it hashes the entry's text (its `state` line excepted)
together with the content of every input file it names, and compares the
result with the `inputs-hash` in the front-matter of the page at the
entry's path. It sets the entry's `state` in the map:

| State | Meaning |
|---|---|
| `new` | no page at the path |
| `regenerate` | a page exists, its hash differs |
| `keep` | a page exists with the same hash |

A page under `<docs-dir>` that no entry names is listed as `remove`
(the index `README.md` excepted). For every `new` or `regenerate` entry
one task file is written to `<tmp-dir>`: the engine root, the page's
path, the date, the hash the page is to carry, the entry verbatim and
the titles of the pages it links to. The task is a `docs-writer`
agent's whole prompt. An input the map names and the disk lacks is
reported and hashed as missing. The script rewrites only the `- state:`
line of each entry and leaves the rest of the map byte for byte.

### docs-index.py

Derives the documentation index from the map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

It writes `<docs-dir>/README.md`: one line per page, grouped by section
in the order start, use, about, extend, reference, each line the page's
title linked to its relative path and the first sentence of its `says`.
Deterministic: the same map gives the same index, and no model is
involved. The index is never edited by hand. Its front-matter names the
map as its one input and carries the version of the owning project's
intent (`10-intent.md` beside the map). The opening paragraph and the
three reading paths are fixed text of this script.

### docs-check.py

Mechanical check of the generated documentation.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
```

It prints every failure with its file and line, and exits 0 when
everything holds and 1 when anything fails. It verifies that:

- every entry of the map not in state `remove` has its page, and no page
  lies in `<docs-dir>` that the map does not name (the index excepted);
- every relative link to a `.md` file resolves;
- no page carries a long dash (em or en);
- every page opens with a front-matter;
- no page carries an instance fact: the values of `CLAUDE.local.md` at
  the engine root (every word of four letters or more in a value,
  looked for outside URLs), any e-mail address but a placeholder at
  `example.*`, any absolute path of a machine (a drive letter, a user's
  home directory), and every `--fact` pattern given.

The check mends nothing: a page that fails is regenerated by the
documentation command. The script carries no name, address or host of
its own; the instance facts are read from `CLAUDE.local.md` at run time.

## Shared modules

These are not commands. They are what the scripts beside them share.

- `forge_repos.py`: what the `forge-*` git scripts share, namely the
  engine root, the git check, the list of repositories to visit, running
  git and coloured output.
- `forge_tools.py`: what the conversion scripts (`doc2md.py`,
  `md2pptx.py`, `md2docx.py`) share, namely finding an external tool on
  PATH, resolving paths, running a tool and the headless Claude Code run.
- `docs_map.py`: the one reader of the documentation map, shared by
  `docs-state.py`, `docs-index.py` and `docs-check.py`.

## Portability

Every script is Python 3.8 or newer, run as `python scripts/<name>.py`.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
