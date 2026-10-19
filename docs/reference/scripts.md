---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: d801decfde8fba30
inputs:
  - scripts/forge-save.py
  - scripts/forge-pull.py
  - scripts/forge-status.py
  - scripts/forge-clone.py
  - scripts/forge-branch.py
  - scripts/forge-history.py
  - scripts/forge-report.py
  - scripts/forge-ledger.py
  - scripts/forge-migrate.py
  - scripts/forge_repos.py
  - scripts/forge_docs.py
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

This page lists every file in `scripts/` with its synopsis, options, forms, what it needs installed and where its output lands. It is for the user who runs a script by hand and for the extender who reads or adds one. Each script carries the same help in its module docstring; this page restates it. To write a script of your own, see [Add a script](../extend/add-a-script.md). Terms of the forge are in the [Glossary](glossary.md).

Every script is run as `python scripts/<name>.py`. The git scripts are the only door to git for Claude (the model that works with the principal, the person whose thinking is forged), reading state included.

## Overview

| Script | What it is for | The command that runs it | What it needs |
|---|---|---|---|
| `forge-save.py` | Commit and push the engine and every project repository | `/save`, `/release` | Python 3.8+, git |
| `forge-pull.py` | Fast-forward the engine and the projects from their remotes | `/pull` | Python 3.8+, git |
| `forge-status.py` | Report the git state of the engine and every project | none named in its help | Python 3.8+, git |
| `forge-clone.py` | Clone an existing project into `projects/` | `/import-project` | Python 3.8+, git |
| `forge-branch.py` | Switch a repository to a branch, or report its branch | none named in its help | Python 3.8+, git |
| `forge-history.py` | Print the history of one item by its ID | `/history` | Python 3.8+ |
| `forge-report.py` | Complete the unique name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python 3.8+ |
| `forge-ledger.py` | Make a project's ledger from its documents | none named in its help | Python 3.8+, git |
| `forge-migrate.py` | Bring a project to the current shape | `/migrate` | Python 3.8+, git |
| `doc2md.py` | Convert documents to Markdown | none named in its help | Python 3.8+, markitdown |
| `md2pptx.py` | Make a PowerPoint deck from a Markdown deck | `/render` (pandoc), `/publish` (claude) | Python 3.8+, pandoc or the claude engine |
| `md2docx.py` | Make a Word document from a Markdown render | `/render` (pandoc), `/publish` (claude) | Python 3.8+, pandoc or the claude engine |
| `md2video.py` | Make a screenplay's video or player events | `/render` | Python 3.8+; for video, Pillow and ffmpeg |
| `hook-walkthrough.py` | Repeat the walkthrough rule at every prompt | the prompt hook of `.claude/settings.json` | Python 3.8+ as `python` |
| `docs-state.py` | Compute each page's state and prepare the writers' tasks | `/document` | Python 3.8+ |
| `docs-index.py` | Derive the documentation index from the map | `/document` | Python 3.8+ |
| `docs-check.py` | Check the generated documentation, or scan one file | `/document`, `/render` | Python 3.8+ |

The shared modules are not commands:

| Module | What it holds |
|---|---|
| `forge_repos.py` | What the git scripts share |
| `forge_docs.py` | What the scripts that read a project's documents share |
| `forge_tools.py` | What the conversion scripts share |
| `docs_map.py` | The one reader of the documentation map |

Installing what the scripts need is described in [Install what the forge needs](../start/install.md).

## The git scripts

All five need Python 3.8 or newer and git on PATH, with `forge_repos.py` beside them. The scripts set no commit identity, no remote and no URL, and do not initialise a repository. The slug `forge` means the engine itself.

### forge-save.py

Commits and pushes the engine and every project that is a repository of its own.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

- Without a slug it visits the engine and every `projects/<slug>` that has a `.git`, and gives each one with changes its own commit.
- With a slug it saves that repository only. A project directory without a repository is skipped with a note when bare, and refused when named.
- Per repository it stages everything, commits (the message from `-m`, otherwise a generated one) and, when an origin is configured, integrates remote changes by rebase and pushes.
- A clean repository that is ahead of its upstream is pushed the same way. A branch with no upstream reaches the remote with its first commit.
- A rebase that conflicts is aborted and nothing is lost. The script prints the steps to finish it by hand: pull with rebase, resolve, add, continue, then run the script again.
- Without an origin the commit is kept locally and reported.
- `--tag NAME` needs a slug. It tags the commit and pushes the tag with it. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.
- It never uses `git add -f` and never `git clean`.

```
python scripts/forge-save.py forge --tag <tag>
```

### forge-pull.py

Pulls the engine (its upgrade channel) and every project that has an origin.

```
python scripts/forge-pull.py [slug]
```

- Fast-forward only. Without a slug it pulls the engine, then every project with an origin. With a slug it pulls that one repository.
- A repository with unsaved changes is reported and skipped when bare, and refused when named. Run `forge-save.py` first.
- A project without a repository or without an origin is reported and skipped.
- A repository whose history has diverged from its origin is refused and nothing is pulled. The script never merges on its own.
- After a pull it prints where the repository moved from and to (`before: <hash> <subject>`, `after: <hash> <subject>`) and the subjects of the commits between. The releases crossed can be read off them, and their required actions looked up in `RELEASE-NOTES.md`.

### forge-status.py

Reports the git state of the engine and every project. It is read-only and changes nothing.

```
python scripts/forge-status.py [--remote]
```

- First it prints the global configuration file git actually reads, and the registration of the merge drivers in it: `ok`, or the keys that are missing (`merge.ours.driver`, `rebase.backend`, `merge.renormalize`). It also reports a registered forge-records driver whose script does not exist. `/setup` repairs a missing registration.
- Then, for the engine and each project, it prints the unsaved changes (or `clean`), the branch, the last commit and the origin (or `no origin` or `not under git`).
- `--remote` also fetches each origin and reports the branch against it: `up to date`, `behind N`, `ahead N` or `diverged (ahead N, behind M)`. The fetch changes nothing in the working tree. Without the flag the script touches no network.

### forge-clone.py

Brings an existing project in by cloning its repository into `projects/`.

```
python scripts/forge-clone.py <url>
```

- The directory is `projects/<repository name>`, taken from the URL. An existing directory is never overwritten.
- Afterwards it reports the last commit, the origin and the commit identity git resolves for the fresh clone.
- It also reports the project file: the project's kind and language, or, for a project of the shape before the migration, that it needs `/migrate`. A project with neither file nor ledger was not scaffolded by the forge, which is a fact and not a defect.

```
python scripts/forge-clone.py https://example.com/team/my-idea.git
```

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports which branch it is on.

```
python scripts/forge-branch.py <slug> [branch]
```

- With a branch name it switches to that branch, creating it from the current state when it does not exist. `main` switches back.
- Without a name it reports the current branch and lists the branches the repository has.
- The slug is required; there is no bare form.
- Unsaved changes stop the switch. Save first, then switch.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote with the first `forge-save.py` made on it. A release is made from `main` only.

```
python scripts/forge-branch.py forge my-branch
```

## The scripts that read a project

### forge-history.py

Prints the history of one item of a project, by its ID, as one timeline. It is read-only and involves no model.

```
python scripts/forge-history.py <ID> <slug> [--full]
```

- The ID is `PREFIX.NNNN`. A short form such as `pos580` is read as `POS.0580`.
- Output, in three parts:
  - Today: the file that holds the item and its wording.
  - Timeline: one line per event, oldest first, each with its version, its date where the log has one, and what happened (`born`, `changed`, `closed`, `removed`, `approved`), from every history log of the project. Records of other items that name the ID show as `mentioned by <ID>`. Rows of the history archives that mention it show as `archive`.
  - Cited today: every other place in the project that names the ID, as file and line.
- A record's reason follows its line; its Action and Was follow as marked lines. Was is shortened to its first sentences unless `--full` is given.
- Long text is wrapped at 78 columns with a hanging indent. An ID with no item and no record is said so.
- The pages of `docs/`, the documentation map, the renders, the resources and `tmp/` are never searched.
- It needs Python 3.8 or newer, with `forge_repos.py` and `docs_map.py` beside it.

The job behind it is described in [Read the history of an item](../use/read-the-history-of-an-item.md).

```
python scripts/forge-history.py <ID> <slug> --full
```

### forge-report.py

Completes the unique name of a reviewer's report.

```
python scripts/forge-report.py <path>
```

- The command that files a report writes it under `YYYY-MM-DD-<kind>-<name>.md` in the project's `reviews/` or `challenges/`, then calls this script with the path.
- The script renames the file in place to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`. `HHMM` is the local time to the minute, and `<hash>` is the first four hex characters of the SHA-256 of the file's bytes. It prints the new path.
- It exists so that two branches do not make the same name. Names given earlier stay as they are.
- It refuses, with exit 1 and the reason printed, a path that is not a file, a name that already carries the tail `-HHMM-<hash>`, and a target name that exists.
- No model and no git are involved. It needs Python 3.8 or newer.

```
python scripts/forge-report.py <path>
```

### forge-ledger.py

Makes the ledger of a project at read time from its documents.

```
python scripts/forge-ledger.py <slug> [--out PATH]
```

- It reads eleven kinds of document and builds `ledger.md` in the shape of `templates/ledger.md`:
  - the project file (or, for a project of the shape before the migration, the hand-kept ledger's header)
  - the artefacts' headers
  - the histories
  - the decisions
  - the resource indexes
  - the reviews and the challenges
  - the provenance of the renders and of the documentation index
  - the published companions
  - the work specifications
  - the threads
  - `ledger.archive.md`
- Dependencies are the citations of `projects/lib-*/` anywhere in the project.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header. It is never a crash; the exit code is 0.
- It writes `ledger.md` only where that file is out of git's index. Where the file is tracked, it refuses to write and prints to stdout, or to the path given by `--out`. The dry run of a real project goes to `tmp/`.
- It needs Python 3.8 or newer and git on PATH, with `forge_docs.py`, `forge_repos.py` and `forge_tools.py` beside it, and `templates/ledger.md`.

```
python scripts/forge-ledger.py <slug> --out tmp/<slug>-ledger.md
```

### forge-migrate.py

Brings one project to the current shape of the forge's files.

```
python scripts/forge-migrate.py <slug>            # dry run
python scripts/forge-migrate.py <slug> --apply    # perform
python scripts/forge-migrate.py <slug> --undo     # take back
```

The job behind it is described in [Migrate a project](../use/migrate-a-project.md).

The shape of a project is a set of marks, one per step. No engine version is kept in the project.

| Mark | Meaning |
|---|---|
| B0 | The project file exists. |
| A | No header of an artefact, a specification, a recipe, an index or the map carries a field that changes with a round. |
| C1 | `threads/` exists, or the project has no threads file. |
| D | `.gitattributes` exists. |
| B | `ledger.md` is out of git's index. |

The three forms:

- The dry run is the default. It prints the marks and, for every step still missing, what it would change.
- `--apply` runs the missing steps in the order A, B0, B, C1, D. Each step verifies its own mark afterwards. A library takes A, B0, B and D. The script commits nothing; `/save` follows.
- `--undo` takes back the last `--apply` from the script's own manifest, `tmp/forge-migrate-<slug>.json` at the engine root. Changed and deleted tracked files are restored from the index, created files are removed, the ledger is put back into the index and the `.gitignore` line is taken out.

The steps:

- A: the fields `date` and `last_change` leave the headers of the artefacts and the work specifications. `updated` and `last_change` leave the recipes', `updated` the indexes', and `generated` and `previous` the map's.
- B0: `project.md` is made from `templates/project.md`. `project` is the slug (the directory's name). `kind` and `language` come from the hand-kept ledger's header (`thought` and `en` when absent). `fixture: true` is set for a slug that starts with `fixture`.
- B: what only the ledger knew becomes records.
  - The mining of a brief becomes a record in the intent's history, with the brief as its subject.
  - The state of a work product becomes a record in its specification's history.
  - A source's date, origin and form become the fields `Date` and `Form` of its entry in `sources/00-INDEX.md`.
  - A published file's provenance becomes the companion `published/<recipe>.md`.
  - The hand-kept ledger is copied as it stands to `ledger.archive.md`, immutable. `ledger.md` is taken out of the index (`git rm --cached`, nothing deleted) and put into the project's `.gitignore`.
  - A Waiting line without an ID is printed for the principal, because it has no home in records.
- C1: `threads.md` (in older projects `10-intent.threads.md`) is cut by `- **THR.NNNN**` into `threads/THR.NNNN.md` from `templates/thread.md`. `concerns` comes from the bracket (`intent` when there is none), `origin` is guessed from the first sentence and printed for judgement, and `status` is `open`. The text is kept. What follows the last thread and is not a thread is printed. The old file is deleted from the tree.
- D: `.gitattributes` is made from `templates/gitattributes`. The engine carries a list of its own, which the step only verifies.

The refusals:

- The author of every record it writes is the handle in `CLAUDE.local.md` (`Author:`). Without it the script refuses.
- `--apply` refuses a project that is not a repository, a working tree that is not clean, a branch behind or diverged from its origin, and any branch but `main`. The migration is one large change, run once, on one clone.

It needs Python 3.8 or newer and git on PATH, with `forge_repos.py` and `forge_tools.py` beside it, and the templates `project.md`, `thread.md` and `gitattributes`.

## The scripts that convert

### doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel) to Markdown using markitdown.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- Inputs can be mixed and repeated, in four notations: a single file name, a glob (`"*.pdf"`, `"docs/**/*.pptx"`), a list file (plain text, one path or glob per line, `#` or `;` starting a comment, relative paths resolved against the list file's directory) and a directory (with `--recurse`).
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the `.md` extension. A name collision within one run gets `_1`, `_2`.
- `--dry-run` lists what would be converted and writes nothing. `--list-tools` checks that markitdown is reachable and exits.
- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported; resave them as `.docx`, `.pptx` or `.xlsx` first.
- It needs Python 3.8 or newer and markitdown, resolved from PATH or named by `--markitdown-path`. The script installs nothing. Install it with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

Two engines, chosen by `--engine`:

- `claude` (the default): a model does the conversion. It runs Claude Code non-interactively (`claude -p`) with Anthropic's official pptx skill. The definition is free-form, and the recipe may carry instructions for the model. It is expensive and never the same twice. This is the engine of `/publish`.
- `pandoc`: a deterministic conversion, one slide per second-level heading, nothing interpreted by a model. It is cheap and the same every time, a deck for reading and not for showing. This is the engine of `/render`.

Options:

- `--template` names a `.potx` or `.pptx` by path, typically a file in a library project. Without it the claude engine designs the style itself and the pandoc engine uses pandoc's built-in one.
- `--recipe` names the recipe the definition was rendered from; the claude engine reads its Format section.
- `--model` is the model of the headless run (default `opus`); the claude engine only.
- The output lands next to the input with the same basename unless `-o` names a path.

It needs Python 3.8 or newer and `forge_tools.py` beside it. What pandoc and the claude engine need is under `forge_tools.py` below. The script installs nothing.

```
python scripts/md2pptx.py deck.md --engine pandoc
```

### md2docx.py

Converts a Markdown render into a Word document.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

Two engines, chosen by `--engine`:

- `pandoc` (the default): a deterministic conversion, nothing interpreted by a model. This is the engine of `/render`.
- `claude`: a model does the conversion, with Anthropic's official docx skill and the recipe's Format section (`--recipe`). It is expensive and never the same twice. This is the engine of `/publish`.

The Markdown render stays the source of truth; the `.docx` is a derivation for recipients who read Word. The rest describes the pandoc engine unless the claude engine is named.

- The YAML front-matter of the render is read as metadata and does not appear; the document starts with the first heading.
- Mermaid diagrams are not rendered; they land as blocks of code.
- `--reference` names a `.docx`, `.dotx` or `.dotm`, typically a file in a library project. pandoc takes its styles and ignores its content. Without it, pandoc's built-in styles apply.
- The page is A4 by default. Without `--reference` the script writes the page size (`--page-size A4` or `Letter`) into pandoc's built-in reference. With `--reference`, the reference document's own page setup applies and `--page-size` is not applied. The claude engine takes the reference as the template it starts from, and A4 where none is given.
- `--model` is the model of the headless run (default `opus`); the claude engine only.
- The output lands next to the input with the same basename unless `-o` names a path.

It needs Python 3.8 or newer and `forge_tools.py` beside it. The script installs nothing.

```
python scripts/md2docx.py <render.md> -o out/brief.docx
```

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser. The job it serves is described in [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date "<date>"] [-o <file>]
    [--frame <seconds> <file.png>]
```

It reads a screenplay render: the YAML front-matter for the language, a title card, a card of what the viewer will see, scenes with the real time of day (each with a caption of two parts, Now and Why, and a fenced block of what the terminal shows) and an end card. It computes the timeline from the pace and writes one of two formats:

- `video`: every frame is painted with Pillow as a simulated terminal (1280x890, a monospace font for the terminal and a sans font for the caption band) and piped into ffmpeg (H.264, 30 fps). It is deterministic.
- `html-player`: the timeline as JSON of events for the player page `docs/videos/index.html`, wrapped as a script (`forgeVideo({...})` in `<name>.html-player.js`). A page on disk cannot read a data file, so the page loads the script by a script tag, from disk as well as from GitHub Pages.

Options:

- `--pace` is three reading rates in words a second: the principal's lines, Claude's answers, and the lines that only report a file (a path, a version, a ledger row). The default is `4,8,16`.
- `--date` is the date shown in the tab bar.
- The pace, the date and the look come from the recipe's Format section, as arguments. The render carries none of it.
- The output lands next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path.
- Where the output lands under the engine's `docs/videos/`, the player page is written anew from `templates/html-player.html`, with the folder's files listed and loaded. GitHub Pages cannot list a folder, which is why the page carries the list.
- `--frame <seconds> <file.png>` paints one frame of the video at the given second to a PNG and stops. It checks the look without making the whole video.

It needs Python 3.8 or newer and `forge_tools.py` beside it. For video it also needs Pillow (`pip install pillow`) and ffmpeg on PATH (Windows: `winget install Gyan.FFmpeg`; macOS: `brew install ffmpeg`; Linux: the package manager). Fonts are taken from the system where they exist (Cascadia Mono or Consolas and Segoe UI; Menlo and Helvetica; DejaVu), and Pillow's built-in font otherwise. The script installs nothing.

```
python scripts/md2video.py <path>/<render>.md --format html-player -o docs/videos/<name>.html-player.js
```

## The hook

### hook-walkthrough.py

The prompt hook of the engine. Claude Code runs it on every user prompt (configured in `.claude/settings.json`) and adds its standard output to the context of that turn.

- It prints two lines on the walkthrough (the one-item rule, with the verdict line that closes every proposition, and the pointer to the skill that holds the full shape) and three lines of conduct: use the forge's scripts, explain and ask before running a command of one's own, and change nothing that was not agreed and approved.
- It reads nothing, writes nothing and takes no arguments. It is independent of the working directory, because a hook runs in the session's current working directory (a session is one running conversation with Claude), not the engine root. The settings file invokes it in exec form and hands it its own path through the `${CLAUDE_PROJECT_DIR}` placeholder.
- It needs Python 3.8 or newer on PATH as `python`, and nothing else.

## The documentation scripts

The three scripts serve the run of `/document`, described in [Generate the documentation](../use/generate-the-documentation.md). They need Python 3.8 or newer with `docs_map.py` beside them, and nothing else. None involves a model.

### docs-state.py

Computes the state of every page of the documentation from the content of its inputs, and prepares the writers' tasks. It runs before the writers.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
python scripts/docs-state.py <map> --previous <path>
```

- For every entry of the documentation map it hashes the entry's text (its `state` line excepted) together with the content of every input the entry names. A whole file is hashed whole; the part of a file named after `#` (a section by its heading, an item by its ID) is hashed as that part, so that a change elsewhere in the file leaves the page as it is.
- The writer's definition (`.claude/agents/docs-writer.md`) and the contract (`.claude/skills/docs-contract/SKILL.md`) are hashed with the inputs, so a change of the rule a page is made by regenerates every page made by the old one.
- The page at the entry's path carries the hash it was made from, `inputs-hash`, in its front-matter. The two are compared and the entry's `state` is set in the map:

| State | Meaning |
|---|---|
| `new` | No page at the path. |
| `regenerate` | A page exists and its hash differs (an input or the entry changed). |
| `keep` | A page exists with the same hash. |
| `remove` | A page under the docs directory that no entry names, or the page of an entry the planner marked `remove`. The index `README.md` is excepted. Such an entry keeps its state and gets no task. |

- For every `new` or `regenerate` entry one task file is written to the `--tasks` directory: the engine root, the page's path, the date, the version the page is made for (the owning project's intent beside the map), the hash the page is to carry, the entry verbatim and the titles of the pages it links to. The task is a `docs-writer` agent's whole prompt.
- An input the map names and the disk does not have is reported and hashed as missing. The page is regenerated and its writer reports the gap.
- The input paths are relative to the target's root: the engine root when `target: engine`, otherwise the owning project's directory. The script rewrites only the `- state:` line of each entry and leaves the rest of the map byte for byte.
- The `--previous <path>` form takes the map and a path and gives the map as last committed, for the planner.

### docs-index.py

Derives the documentation index from the documentation map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

- It writes `<docs-dir>/README.md`: before the sections, the reader paths of the map's `## Paths` section, each page a link; then one line per page, grouped by section in the order start, use, about, extend, reference. Each line is the page's title linked to its relative path and the entry's `line` (the first sentence of its `says` where an entry has no `line`).
- It is deterministic: the same map gives the same index. The index is never edited by hand; change the map and run the script again.
- The index's front-matter names the map as its one input and carries the version of the owning project's intent beside the map. The opening paragraph is fixed text of this script.

### docs-check.py

Mechanical check of the generated documentation.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

The first form verifies the pages under the docs directory against the map and the rules of a page, and prints every failure with its file and line:

- Every entry of the map not in state `remove` has its page, and no page lies in the docs directory that the map does not name (the index `README.md` excepted).
- Every relative link to a `.md` file resolves.
- No long dash (em or en) stands in the prose of any page. A code span and a fenced block are exempt.
- Every page opens with a front-matter.
- No instance fact appears: the values of `CLAUDE.local.md` at the engine root (every word of four letters or more in a value, looked for outside URLs), any e-mail address but a placeholder at `example.*`, any absolute path of a machine (a drive letter, a user's home directory), and every `--fact` pattern given.

The second form, `--file <path>`, scans one file for instance facts only: the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns. It has no map, no link check, no dash rule and no e-mail rule. This is the scan `/render` runs on a render it has just written, and a render may carry an address its recipe fixes. See [Render an output](../use/render-an-output.md).

- The exit code is 0 when everything holds and 1 when anything fails.
- The check mends nothing. A page that fails is regenerated by the documentation command, never edited by hand.
- The script carries no name, address or host of its own; it reads the instance facts from `CLAUDE.local.md` at run time. A match is reported with its line, so a false hit is seen and the rule, not the page, is adjusted.

## The shared modules

None of these is a command. What several scripts share lives in a module beside them, never twice.

- `forge_repos.py`: what the git scripts share, namely the engine root, the git check, the list of repositories to visit, running git, a repository's state against its origin, the registration of the merge drivers on the machine and coloured output. It reads the project file too.
- `forge_docs.py`: what the scripts that read a project's documents share, namely front-matter, the records of a history companion, the tables of a hand-kept ledger or its archive, the entries of a resource index and the threads. It is used by `forge-ledger.py`, `forge-migrate.py` and `forge-history.py`. A reader here never raises on a malformed file; it returns what it could read and lists the rest in `problems`.
- `forge_tools.py`: what the conversion scripts share, namely finding an external tool on PATH, resolving paths, running a tool, the headless Claude Code run, and the console set to UTF-8.
- `docs_map.py`: the one reader of the documentation map, shared by `docs-state.py`, `docs-index.py` and `docs-check.py`. It also reads the part of a file that an input names after `#`, which `forge-history.py` uses.

What the conversions need, as `forge_tools.py` states it. Every tool is resolved from PATH and never installed by a script; the model of the claude engine is told to install and download nothing either.

- pandoc (the engine of `/render`): install it once from https://pandoc.org/installing.html (Windows: `winget install JohnMacFarlane.Pandoc`; macOS: `brew install pandoc`; Linux: the package manager).
- The claude engine (behind `/publish`): the `claude` CLI on PATH and the official document skill of the format, pptx or docx, under either name, `anthropic-skills:<format>` or `document-skills:<format>`. Where neither is there, install the plugin once from an interactive Claude Code session: `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills`.

## Portability

The scripts run unchanged on Windows, Linux and macOS: Python 3.8 or newer, run as `python scripts/<name>.py`, with paths composed with `pathlib` and external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the conversions and the one-file scan.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job `md2video.py` serves.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Migrate a project](../use/migrate-a-project.md): the command behind the migration script.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
