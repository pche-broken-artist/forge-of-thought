---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 6f7430a0cf21e567
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
  - scripts/md2video.py
  - scripts/forge_tools.py
  - scripts/hook-walkthrough.py
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
  - scripts/docs_map.py
  - CLAUDE.md#Persistence (git)
---

# Scripts

This page lists every file in the `scripts/` directory of the engine: what each script does, how it is called, what it needs and where its output lands. It is for the user who runs a script and for the extender who writes one. Each script carries the same help in its own module docstring. A command is run by the principal (the person whose thinking is forged) through Claude, and the scripts are the door to git and to the conversions.

## Overview

| Script | What it is for | The command that runs it | What it needs | Where it lives |
|---|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save` | Python 3.8+, git | `scripts/forge-save.py` |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python 3.8+, git | `scripts/forge-pull.py` |
| `forge-status.py` | report the git state, changing nothing | none of its own | Python 3.8+, git | `scripts/forge-status.py` |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python 3.8+, git | `scripts/forge-clone.py` |
| `forge-branch.py` | switch to a branch, or report the current one | none of its own | Python 3.8+, git | `scripts/forge-branch.py` |
| `forge-history.py` | the history of one item, by its ID | `/history` | Python 3.8+ | `scripts/forge-history.py` |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python 3.8+, markitdown | `scripts/doc2md.py` |
| `md2pptx.py` | make a PowerPoint deck from a Markdown deck | `/render` (pandoc), `/publish` (claude) | Python 3.8+, pandoc or the claude engine | `scripts/md2pptx.py` |
| `md2docx.py` | make a Word document from a Markdown render | `/render` (pandoc), `/publish` (claude) | Python 3.8+, pandoc or the claude engine | `scripts/md2docx.py` |
| `md2video.py` | make a video, or the timed events for the player page, from a screenplay render | the render of a screenplay recipe | Python 3.8+; for video Pillow and ffmpeg | `scripts/md2video.py` |
| `hook-walkthrough.py` | repeat the walkthrough rule and the conduct lines at every prompt | none: Claude Code runs it as a hook | Python 3.8+ as `python` | `scripts/hook-walkthrough.py` |
| `docs-state.py` | compute the state of every documentation page and prepare the writers' tasks | `/document` | Python 3.8+ | `scripts/docs-state.py` |
| `docs-index.py` | derive the documentation index from the documentation map | `/document` | Python 3.8+ | `scripts/docs-index.py` |
| `docs-check.py` | check the generated documentation; scan one file for instance facts | `/document`; `/render` for the one-file scan | Python 3.8+ | `scripts/docs-check.py` |

Three modules sit beside the scripts and are not commands: `forge_repos.py`, `forge_tools.py` and `docs_map.py`. They are described at the end.

Every script is run as `python scripts/<name>.py`. Where a script names the repository by a slug, `forge` means the engine.

## forge-save.py

Saves the engine and every project that is a repository of its own: commit, then push.

Synopsis:

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

Options:

| Option | Meaning |
|---|---|
| `slug` | one repository (`forge` means the engine); bare, every repository with changes |
| `-m`, `--message` | the commit message; default, one generated from the files |
| `--tag` | tag the commit; needs a slug |

Forms:

- Bare: visits the engine and every `projects/<slug>/.git` and gives each one with changes its own commit. A project directory without a repository is skipped with a note.
- With a slug: saves that repository only. A project directory without a repository is refused.
- With `--tag <name>`: the commit is tagged and the tag is pushed with it. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.

Per repository the script stages everything and commits. When an origin is configured it integrates remote changes by rebase and pushes. Without an origin the commit is kept locally and reported. It never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never uses `git clean`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

Output: commits and pushes in the repositories; messages on the console.

## forge-pull.py

Pulls the latest from the remotes: the engine (its upgrade channel) and every project that has an origin.

Synopsis:

```
python scripts/forge-pull.py [slug]
```

Forms:

- Bare: pulls the engine, then every `projects/<slug>/.git` with an origin.
- With a slug: pulls that repository only.

Fast-forward only. A repository with unsaved changes is not touched: it is reported and skipped (bare) or refused (slug); run `forge-save.py` first. Projects without a repository or without an origin are reported and skipped. A repository whose history has diverged from its origin is refused and nothing is pulled. The script never merges on its own.

After a pull it prints where the repository moved from and to (`before: <hash> <subject>`, `after: <hash> <subject>`) and the subjects of the commits between. The releases crossed (`release <version>`) can be read off there, and their Action required lines looked up in `RELEASE-NOTES.md`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

## forge-status.py

Reports the git state of the engine and every project. It is read-only and changes nothing.

Synopsis:

```
python scripts/forge-status.py [--remote]
```

Options:

| Option | Meaning |
|---|---|
| `--remote` | fetch each origin and report the branch against it |

It prints first the global configuration file git actually reads, which `/setup` needs to know. Then, for the engine and each `projects/<slug>`, it prints the unsaved changes (or "clean"), the branch, the last commit and the origin, or "no origin" or "not under git".

With `--remote` it also reports the branch against its origin: "up to date", "behind N", "ahead N" or "diverged (ahead N, behind M)". The fetch changes nothing in the working tree. Without the flag the script touches no network.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

## forge-clone.py

Brings an existing project in by cloning its repository into `projects/`.

Synopsis:

```
python scripts/forge-clone.py <url>
```

It clones into `projects/<repository name>`. The directory name comes from the URL, and an existing directory is never overwritten. The script sets no commit identity and carries no identity and no URL.

Afterwards it reports the last commit, the origin, the commit identity git resolves for the fresh clone, and whether the project carries a ledger with a `kind:` header.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

## forge-branch.py

Switches one repository to a branch, creating it if needed, or reports which branch it is on.

Synopsis:

```
python scripts/forge-branch.py <slug> [branch]
```

Forms:

- With a branch name: switches the repository to that branch. When the branch does not exist, it is created from the current state. `main` switches back.
- Without a name: reports the current branch and lists the branches the repository has.

The repository is named by its slug; there is no bare form. Unsaved changes stop the switch: save first, then switch. Merging, deleting and pushing branches stay with git. A new branch reaches the remote by the first `forge-save.py` made on it.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

## forge-history.py

Prints the history of one item of a project, by its ID, as one timeline. It is read-only, changes nothing and involves no model.

Synopsis:

```
python scripts/forge-history.py <ID> <slug> [--full]
```

Options:

| Option | Meaning |
|---|---|
| `<ID>` | the item, as `PREFIX.NNNN`; a short form such as `pos580` is read as `POS.0580` |
| `<slug>` | the project `projects/<slug>` (`forge` is the engine's own project) |
| `--full` | print every `Was` in full; otherwise it is shortened to its first sentences |

It prints three parts:

- Today: the file that holds the item and its wording.
- Timeline: one line per event, oldest first, each with its version, its date where the log has one, and what happened (`born`, `changed`, `closed`, `removed`, `approved`, `mentioned by <ID>`, `archive`). A record's reason follows its line, then its Action and its Was as marked lines.
- Cited today: every other place in the project that names the ID, as file and line.

Long text is wrapped at 78 columns with a hanging indent. An ID with no item and no record is said so. The pages of `docs/`, the documentation map, the renders, the resources and `tmp/` are never searched.

Needs: Python 3.8 or newer, `forge_repos.py` and `docs_map.py` beside it.

## doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel) to Markdown using markitdown.

Synopsis:

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

Options:

| Option | Meaning |
|---|---|
| `-o`, `--out-dir` | where to write the `.md` files; default, next to each source |
| `--suffix` | text inserted before the `.md` extension (`--suffix .text` gives `report.text.md`) |
| `--recurse` | descend into directories and globs without `**` |
| `--force` | overwrite existing `.md` files |
| `--as-list` | treat every input as a list file |
| `--markitdown-path` | explicit path to the markitdown executable |
| `--dry-run` | show what would be converted and write nothing |
| `--list-tools` | check that markitdown is available and exit |

Forms (input notations, which can be mixed and repeated):

- A single file name.
- Glob notation, such as `"*.pdf"` or `"docs/**/*.pptx"`.
- A list file: plain text, one path or glob per line; `#` or `;` starts a comment; relative paths are resolved against the list file's own directory.
- A directory, with `--recurse`.

Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force` is given. A name collision within one run gets `_1`, `_2` and so on.

Handled extensions: `.pdf`, `.docx`, `.docm`, `.pptx`, `.pptm`, `.xlsx`, `.xlsm`, `.xls`, `.epub`, `.html`, `.htm`, `.csv`, `.json`, `.xml`, `.msg`. The legacy binary formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported; resave them as `.docx`, `.pptx` or `.xlsx` first.

Needs: Python 3.8 or newer, and markitdown, resolved from PATH or named by `--markitdown-path`. The script never installs anything. Install markitdown with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

## md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

Synopsis:

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

Options:

| Option | Meaning |
|---|---|
| `--engine` | `claude` (default) or `pandoc` |
| `--template` | a `.potx` or `.pptx` template, named by path |
| `--recipe` | the recipe the definition was rendered from; the claude engine reads its Format section |
| `-o`, `--out` | the output `.pptx`; default, next to the input with the same basename |
| `--model` | the model of the headless Claude Code run (default `opus`); the claude engine only |

The two engines:

- `claude` (the default): a model does the conversion. The script runs Claude Code non-interactively (`claude -p`) with Anthropic's official pptx skill. It is expensive and never the same twice. This is the engine of `/publish`.
- `pandoc`: the conversion is deterministic. Pandoc writes a plain deck, one slide per second-level heading, nothing interpreted by a model. This is the engine of `/render`.

Without `--template`, the claude engine designs the visual style itself and the pandoc engine uses pandoc's built-in one.

Needs: Python 3.8 or newer and `forge_tools.py` beside it, whose docstring says what pandoc and the claude engine need. The script installs nothing.

## md2docx.py

Converts a Markdown render into a Word document.

Synopsis:

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

Options:

| Option | Meaning |
|---|---|
| `--engine` | `pandoc` (default) or `claude` |
| `--reference` | a `.docx`, `.dotx` or `.dotm` whose styles the output takes |
| `--page-size` | `A4` (default) or `Letter`, used when no `--reference` is given |
| `--recipe` | the recipe the render was made from; the claude engine reads its Format section |
| `-o`, `--out` | the output `.docx`; default, next to the input with the same basename |
| `--model` | the model of the headless Claude Code run (default `opus`); the claude engine only |

The two engines:

- `pandoc` (the default): the conversion is deterministic and nothing is interpreted by a model. This is the engine of `/render`.
- `claude`: a model does the conversion. The script runs Claude Code non-interactively (`claude -p`) with Anthropic's official docx skill, and the recipe's Format section gives the model its instructions. It is expensive and never the same twice. This is the engine of `/publish`.

The render's YAML front-matter is read as metadata and does not appear in the document, which starts with the first heading. Mermaid diagrams are not rendered; they land in the document as blocks of code.

With `--reference`, pandoc takes the styles of the reference document and ignores its content, and the page setup is the reference document's own: `--page-size` is not applied. Without it, pandoc's built-in styles apply and the page size is written in. The claude engine takes the reference document as the template it starts from, and A4 where none is given.

Needs: Python 3.8 or newer and `forge_tools.py` beside it, whose docstring says what pandoc and the claude engine need. The script installs nothing.

## md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser.

Synopsis:

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date "<date>"] [-o <file>]
    [--frame <seconds> <file.png>]
```

Options:

| Option | Meaning |
|---|---|
| `--format` | `video` or `html-player` |
| `--pace` | three reading rates in words a second: the principal's lines, Claude's answers, the lines that only report a file (a path, a version, a ledger row); default `4,8,16` |
| `--date` | the date shown in the tab bar |
| `-o` | the output path |
| `--frame` | paint one frame of the video at the given second to a PNG and stop; a check of the look without the whole render |

The script reads a render of the genre `screenplay`: the YAML front-matter for the language, a title card, a card of what the viewer will see, scenes with the real time of day (each with a caption of two parts, Now and Why, and a fenced block of what the terminal shows) and an end card. It computes the timeline from the pace and writes one of two formats:

- `video`: every frame is painted with Pillow as a simulated terminal (1280x890) and piped into ffmpeg (H.264, 30 fps). The same render gives the same file every time.
- `html-player`: the timeline as JSON of events for the player page of the engine, `docs/videos/index.html`, wrapped as a script (`forgeVideo({...})` in `<name>.html-player.js`). The page can then load it by a script tag from a file on disk as well as from GitHub Pages.

The pace, the date and the look come from the recipe's Format section, as arguments; the render carries none of it.

Where the file lands: next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`), unless `-o` names a path. Where the output lands under the engine's `docs/videos/`, the player page is written anew from `templates/html-player.html`, with the folder's files listed and loaded.

Needs: Python 3.8 or newer and `forge_tools.py` beside it. For video, Pillow (`pip install pillow`) and ffmpeg on PATH. Fonts are taken from the system where they exist (Cascadia Mono or Consolas, Segoe UI; Menlo and Helvetica; DejaVu) and Pillow's built-in font otherwise. The script installs nothing.

## hook-walkthrough.py

The `UserPromptSubmit` hook of the engine. Claude Code runs it on every prompt, configured in `.claude/settings.json`, and adds its standard output to the context of that turn.

It prints:

- two lines on the walkthrough: the one-item rule with its verdict line, and the pointer to the skill that holds the full shape;
- three lines of conduct: use the forge's scripts, explain and ask before running a command of one's own, and change nothing that was not agreed and approved.

It reads nothing, writes nothing and takes no arguments. It is independent of the working directory: `.claude/settings.json` invokes it in exec form and hands it its own path through the `${CLAUDE_PROJECT_DIR}` placeholder.

Needs: Python 3.8 or newer on PATH as `python`. Nothing else.

## docs-state.py

Computes the state of every page of the documentation from the content of its inputs, and prepares the writers' tasks. In the run of `/document` it comes after the documentation map is written and before the pages are.

Synopsis:

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
```

It reads the documentation map and, for every entry, hashes the entry's text (its `state` line excepted) together with the content of every input the entry names: a whole file, or the part of a file named after `#`. The writer's definition and the documentation contract are hashed with the inputs. The page at the entry's path carries the hash it was made from in its front-matter as `inputs-hash`, and the two are compared. The entry's `state` is set in the map:

| State | Meaning |
|---|---|
| `new` | no page at the path |
| `regenerate` | a page exists and its hash differs |
| `keep` | a page exists with the same hash |

A page under the docs directory that no entry names, and the page of an entry marked `remove`, are listed as `remove` (the index `README.md` excepted). For every `new` or `regenerate` entry one task file is written to `<tmp-dir>`: the engine root, the page's path, the date, the version, the hash the page is to carry, the entry verbatim and the titles of the pages it links to. An input the map names and the disk does not have is reported and hashed as missing.

The inputs of the map are relative to the target's root: the engine root when `target: engine`, else the owning project's directory. The script rewrites only the `- state:` line of each entry.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

## docs-index.py

Derives the documentation index from the documentation map. In the run of `/document` it comes after the pages are written.

Synopsis:

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

It writes `<docs-dir>/README.md`: before the sections, the reader paths of the map's `## Paths` section, each page a link; then one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its relative path and the entry's `line`. It is deterministic, involves no model, and is never edited by hand.

The index's front-matter names the map as its one input and carries the version of the owning project's intent.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

## docs-check.py

Checks the generated documentation mechanically. In the run of `/document` it comes last, after the index. It mends nothing.

Synopsis:

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

Options:

| Option | Meaning |
|---|---|
| `--fact` | a pattern that must not appear; may be repeated |
| `--file` | scan this one file for instance facts only |

Forms:

- Map and docs directory: verifies the pages against the map and the rules of a page, and prints every failure with its file and line:
  - every entry of the map not in state `remove` has its page, and no page lies in the docs directory that the map does not name (the index `README.md` excepted);
  - every relative link to a `.md` file resolves;
  - no long dash (em or en) in the prose of any page; a code span and a fenced block are exempt;
  - every page opens with a front-matter;
  - no instance fact: the values of `CLAUDE.local.md` at the engine root, any e-mail address but a placeholder at `example.*`, any absolute path of a machine (a drive letter, a user's home directory), and every `--fact` pattern.
- `--file <path>`: the one-file scan. One file is scanned for instance facts only (the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns), with no map, no links, no dash rule and no e-mail rule. This is the scan `/render` runs on a render it has just written.

Exit code 0 when everything holds, 1 when anything fails. The script carries no name, address or host of its own: the instance facts are read from `CLAUDE.local.md` at run time.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

## Shared modules

Not commands; each lies beside the scripts that use it.

- `forge_repos.py`: what the git scripts share (the engine root, the git check, the list of repositories to visit, running git, the state of a repository against its origin, coloured output).
- `forge_tools.py`: what the conversion scripts share (finding an external tool on PATH, resolving paths, running a tool, the headless Claude Code run, the console set to UTF-8); the one owner of the text on what the conversions need.
- `docs_map.py`: the one reader of the documentation map, shared by the `docs-*` scripts and by `forge-history.py`.

## Portability

The scripts run unchanged on Linux, macOS and Windows: Python 3.8 or newer, run as `python scripts/<name>.py`, paths composed with `pathlib`, external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH and installed by nobody but you.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the conversions and the one-file scan.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job `md2video.py` serves.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
