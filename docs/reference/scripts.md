---
generated: 2026-10-10
made: mirrored
inputs-hash: 43354a93d316ac8d
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

This page lists every file in `scripts/`: what it does, how it is called, what it needs and where its output lands. It is for the person who runs the forge and for the one who extends it. Each script carries the same help in its own module docstring.

Every script runs as `python scripts/<name>.py`, with Python 3.8 or newer, on Linux, macOS and Windows alike.

In the synopses, `[slug]` is a project's slug, and `forge` stands for the engine itself. Where a script has a bare form, running it without a slug acts on every repository it applies to.

## Git scripts

These are the only door to git, reading state included. They carry no URL and no identity, and each needs Python 3.8 or newer, `git` on PATH and `forge_repos.py` beside it.

### forge-save.py

Saves to git: commits and pushes the engine and every project that is a repository of its own. Run by `/save`, and by `/release` when it saves.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

- Bare: visits the engine and every `projects/<slug>/.git` and gives each one with changes its own commit.
- With a slug: saves that repository only. A project directory without a repository is skipped with a note (bare) or refused (slug).
- Per repository: stages everything, commits (the message from `-m`, or a generated one), then, when an origin is configured, integrates remote changes by rebase and pushes. Without an origin the commit is kept locally and reported.
- `--tag NAME` needs a slug. It tags the commit and pushes the tag with it. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.
- It never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never `git clean`.

### forge-pull.py

Pulls the latest from the remotes: the engine, which is its upgrade channel, and every project that has an origin.

```
python scripts/forge-pull.py [slug]
```

- Fast-forward only.
- Bare: the engine, then every project with an origin configured. With a slug: that repository only.
- A repository with unsaved changes is not touched: reported and skipped (bare) or refused (slug). Run `forge-save.py` first.
- Projects without a repository or without an origin are reported and skipped.

### forge-status.py

Reports the git state of the engine and every project. Read-only, changes nothing. `/setup` uses it to learn the global git configuration.

```
python scripts/forge-status.py
```

It prints first the global configuration file git actually reads. Then, for the engine and each project: unsaved changes (or "clean"), the branch, the last commit and the origin, or "no origin" or "not under git".

### forge-clone.py

Brings an existing project in: clones its repository into `projects/`. `/import-project` is its door.

```
python scripts/forge-clone.py <url>
```

- The directory is `projects/<repository name>`, taken from the URL. An existing directory is never overwritten.
- Afterwards it reports the last commit, the origin, the commit identity git resolves for the clone, and whether the project carries a ledger with a `kind:` header.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports which branch it is on.

```
python scripts/forge-branch.py <slug> [branch]
```

- A branch name: switches to it, creating it from the current state when it does not exist yet (`main` switches back).
- No name: reports the current branch and lists the branches.
- The slug is required; there is no bare form. `forge` means the engine.
- Unsaved changes stop the switch: save first.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote with the first `forge-save.py` made on it. A release is made from `main` only.

## Conversion scripts

### doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel) to Markdown using markitdown. `/ingest` converts a binary source through it.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- Inputs, mixed and repeated: a file name, a glob (`"*.pdf"`, `"docs/**/*.pptx"`), a list file (plain text, one path or glob per line, `#` or `;` starts a comment, relative paths resolved against the list file's directory), or a directory with `--recurse`.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the `.md` extension. A name collision within one run gets `_1`, `_2` and so on.
- `--dry-run` lists what would be converted and writes nothing. `--list-tools` checks that markitdown is reachable and exits.
- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy binary `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported: resave them as `.docx`, `.pptx` or `.xlsx` first.
- Needs: Python 3.8 or newer and markitdown, resolved from PATH or named by `--markitdown-path`. The script never installs anything. Install it with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

| Engine | What it does | Run by |
|---|---|---|
| `claude` (the default) | A model does the conversion: it runs Claude Code non-interactively (`claude -p`) with Anthropic's official pptx skill. The recipe may carry instructions for the model. Expensive, never the same twice. | `/publish` |
| `pandoc` | Deterministic: pandoc writes a `.pptx`, one slide per second-level heading, nothing interpreted by a model. Cheap, the same every time, a deck for reading, not for showing. | `/render` |

- A template is named by path: `--template <path to a .potx or .pptx>`, typically a file in a library project. Without it the `claude` engine designs the style itself and the `pandoc` engine uses pandoc's built-in one.
- `--recipe` names the recipe the definition was rendered from; the `claude` engine reads its Format section.
- `--model` sets the model of the headless run, `opus` by default; the `claude` engine only.
- The output lands next to the input with the same basename unless `-o` names a path.
- Needs: Python 3.8 or newer and `forge_tools.py` beside it. What the engines need is under "What the conversions need" below. The script installs nothing.

### md2docx.py

Converts a Markdown render into a Word document.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

| Engine | What it does | Run by |
|---|---|---|
| `pandoc` (the default) | Deterministic: pandoc writes a `.docx`, nothing interpreted by a model. Cheap, the same every time. | `/render` |
| `claude` | A model does the conversion: it runs Claude Code non-interactively (`claude -p`) with Anthropic's official docx skill, the recipe's Format section giving the instructions (`--recipe`). Expensive, never the same twice. | `/publish` |

- The Markdown render stays the source of truth; the `.docx` is a derivation for recipients who read Word.
- The YAML front-matter at the top of the render is read by pandoc as metadata and does not appear in the document, which starts with the first heading.
- Mermaid diagrams (```` ```mermaid ```` fences) are not rendered: they land in the document as blocks of code.
- Styles come from a reference document: `--reference <path to a .docx, or a Word template .dotx/.dotm>`, typically a file in a library project. pandoc takes its styles and ignores its content. Without `--reference`, pandoc's built-in styles apply.
- The page is A4 by default. Without `--reference` the script hands pandoc its built-in reference with the page size written in (`--page-size A4|Letter`, A4 when absent). With `--reference` the page setup is the reference document's own and `--page-size` is not applied. The `claude` engine takes the reference document as the template it starts from, and A4 where none is given.
- The output lands next to the input with the same basename unless `-o` names a path.
- Needs: Python 3.8 or newer and `forge_tools.py` beside it. The script installs nothing.

### What the conversions need

As `forge_tools.py` owns it. Every tool is resolved from PATH and never installed by a script; the model of the `claude` engine is told to install and download nothing as well.

- pandoc, the engine of `/render`: install it yourself, one-off, from https://pandoc.org/installing.html (Windows: `winget install JohnMacFarlane.Pandoc`; macOS: `brew install pandoc`; Linux: your package manager).
- The `claude` engine, behind `/publish`: the `claude` CLI on PATH and the official document skill of the format, pptx or docx, under either of its names, `anthropic-skills:<format>` where Claude Code brings it, `document-skills:<format>` where the plugin does. Where neither is there, install the plugin yourself, one-off, from an interactive Claude Code session:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Examples:

```
python scripts/md2pptx.py <path>/deck.md
python scripts/md2pptx.py deck.md --template <path>/template.potx
python scripts/md2pptx.py deck.md --engine pandoc
python scripts/md2pptx.py deck.md --recipe recipes/deck.md -o published/deck.pptx
python scripts/md2docx.py <path>/render.md
python scripts/md2docx.py brd.md --reference <path>/styles.docx
python scripts/md2docx.py brd.md --engine claude --recipe recipes/brd.md -o published/brd.docx
```

## The hook

### hook-walkthrough.py

The `UserPromptSubmit` hook of the engine, configured in `.claude/settings.json`.

```
python scripts/hook-walkthrough.py
```

- Claude Code runs it on every user prompt and adds its standard output to the context of that turn.
- It prints two lines on the walkthrough (the one-item rule, including the verdict line that closes every proposition, and the pointer to the skill that holds the full shape) and three lines of conduct: use the forge's scripts, explain and ask before running a command of one's own, and change nothing that was not agreed and approved.
- It reads nothing, writes nothing, takes no arguments and is independent of the working directory. `.claude/settings.json` invokes it in exec form and hands it its own path through the `${CLAUDE_PROJECT_DIR}` placeholder.
- Needs: Python 3.8 or newer on PATH as `python`. Nothing else.

## Documentation scripts

All three need Python 3.8 or newer and `docs_map.py` beside them, nothing else. `/document` runs them in this order: `docs-state.py` first, which says what to write and prepares the writers' tasks, then the page writers, then `docs-index.py` for the index and `docs-check.py` for the check.

### docs-state.py

Computes the state of every page of the documentation from the content of its inputs, and prepares the writers' tasks.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

- For every entry of the map it hashes the entry's text (its `state` line excepted) together with the content of every input file the entry names. The page at the entry's path carries in its front-matter the hash it was made from, `inputs-hash`. The two are compared and the entry's `state` is set in the map:

| State | Meaning |
|---|---|
| `new` | no page at the path |
| `regenerate` | a page exists, its hash differs (an input or the entry changed) |
| `keep` | a page exists with the same hash |

- A page under `<docs-dir>` that no entry names is listed as `remove` (the index `README.md` excepted).
- The state is computed, never judged: a page whose inputs did not change is not regenerated.
- For every `new` or `regenerate` entry one task file is written to `<tmp-dir>`: the engine root, the page's path, the date, the hash the page is to carry, the entry verbatim and the titles of the pages it links to. The task is a `docs-writer` agent's whole prompt.
- An input the map names and the disk does not have is reported and hashed as missing; the page is regenerated and its writer reports the gap.
- The map's `inputs` are relative to the target's root: the engine root when `target: engine`, else the owning project's directory. The script rewrites only the `- state:` line of each entry and leaves the rest of the map byte for byte.

### docs-index.py

Derives the documentation index from the documentation map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

- Reads the map a `docs-planner` run wrote and writes `<docs-dir>/README.md`: one line per page, grouped by section in the order of the outline (start, use, about, extend, reference), each line the page's title linked to its relative path and the first sentence of its `says`.
- Deterministic: the same map gives the same index. No model is involved.
- The index is a derivation of the map and never edited by hand: change the map and run the script again.
- The front-matter of the index names the map as its one input and carries the version of the owning project's intent (`10-intent.md` beside the map), which for the engine is its version. The opening paragraph and the three reading paths are fixed text of the script.

### docs-check.py

Mechanical check of the generated documentation.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

First form, the check of the pages. It verifies the pages under `<docs-dir>` against the map and against the rules of a page (`.claude/agents/docs-writer.md`), and prints every failure with its file and line:

- every entry of the map not in state `remove` has its page, and no page lies in `<docs-dir>` that the map does not name (the index `README.md` excepted);
- every relative link to a `.md` file resolves;
- no long dash (em or en) on any page;
- every page opens with a front-matter;
- no instance fact: the values of `CLAUDE.local.md` at the engine root (every word of four letters or more in a value, looked for outside URLs), any e-mail address but a placeholder at `example.*`, any absolute path of a machine (a drive letter, a user's home directory), and every `--fact` pattern given.

Second form, `--file <path>`, the one-file scan. In place of a map and a directory, one file is scanned for instance facts only: the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns. No map, no links, no dash and no e-mail rule. This is the scan `/render` runs on a render it has just written.

- Exit code 0 when everything holds, 1 when anything fails.
- The check mends nothing: a page that fails is regenerated by the documentation command, never edited by hand.
- The script carries no name, address or host of its own: the instance facts are read from `CLAUDE.local.md` at run time. A match is reported with its line, so a false hit is seen and the rule, not the page, is adjusted.

Examples of the documentation scripts:

```
python scripts/docs-state.py projects/<slug>/docs-map.md projects/<slug>/docs --tasks tmp/docs-tasks
python scripts/docs-index.py projects/<slug>/docs-map.md projects/<slug>/docs
python scripts/docs-check.py projects/<slug>/docs-map.md projects/<slug>/docs --fact <pattern>
python scripts/docs-check.py --file README.md
```

## Shared modules

These are not commands. Each lies beside the scripts that share it.

| Module | What the scripts beside it share |
|---|---|
| `forge_repos.py` | the engine root, the git check, the list of repositories to visit, running git, and coloured output, for the `forge-*` git scripts |
| `forge_tools.py` | finding an external tool on PATH, resolving paths, running a tool and the headless Claude Code run, for `md2pptx.py` and `md2docx.py` |
| `docs_map.py` | the one reader of the documentation map, for `docs-state.py`, `docs-index.py` and `docs-check.py` |

## Portability

Python 3.8 or newer, run as `python scripts/<name>.py`; external tools (`git`, `markitdown`, `pandoc`, `claude`) are resolved from PATH.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the one-file scan.
