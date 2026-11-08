---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: a2509588e857a054
inputs:
  - scripts/forge-save.py
  - scripts/forge-pull.py
  - scripts/forge-status.py
  - scripts/forge-clone.py
  - scripts/forge-branch.py
  - scripts/forge-config.py
  - scripts/forge-history.py
  - scripts/forge-report.py
  - scripts/forge-ledger.py
  - scripts/forge-migrate.py
  - scripts/forge-check.py
  - scripts/forge_check.py
  - scripts/forge-engine.py
  - scripts/forge-cite.py
  - scripts/forge_repos.py
  - scripts/forge_docs.py
  - scripts/doc2md.py
  - scripts/md2pptx.py
  - scripts/md2docx.py
  - scripts/md2video.py
  - scripts/forge_tools.py
  - scripts/hook-walkthrough.py
  - scripts/hook-git.py
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
  - scripts/docs_map.py
  - CLAUDE.md#Persistence (git)
  - projects/forge/10-intent.md#POS.0830
---

# Scripts

This page lists every file in `scripts/`: what it does, how it is called, what it needs installed and where its output lands. It is for the user who runs a script by hand and for the extender who changes or adds one. A script is a Python program run as `python scripts/<name>.py`; the commands of the forge call them, and they are the only layer of the forge that is tied to a platform.

Terms used below: the principal is the person whose thinking is forged. The ledger is the state of a project, made at read time from its documents. A hook is a script that Claude Code, Anthropic's agent for the command line, runs at a fixed moment of its own work. A thing marked "none" under the command is run by hand or by Claude directly.

Every script that takes a project takes it by its slug or by the path of its directory. A bare word is a slug, anything with a separator or an absolute path is a path. Where a script knows `forge`, it means the engine itself. The install steps for the tools named under "Needs" are on [Install what the forge needs](../start/install.md).

## Overview

| Script | What it is for | Command that runs it | What it needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save`, `/release` | Python, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | report the git state, read-only | none | Python, git; `gh` for the `github:` line |
| `forge-clone.py` | bring an existing project in | `/import-project` | Python, git |
| `forge-branch.py` | switch or create a branch, or report it | none | Python, git |
| `forge-config.py` | read and write the global git configuration | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | the history of one item as a timeline | `/history` | Python |
| `forge-report.py` | complete the unique name of a report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | make the ledger of a project | `/ledger`, every command that changes state | Python, git |
| `forge-migrate.py` | bring a project to the current shape of files | `/migrate` | Python, git |
| `forge-check.py` | the mechanical clauses of the light check as a program | none | Python, git |
| `forge-engine.py` | run one research packet on a model of another family | `/research` | Python; the engine's own tool |
| `forge-cite.py` | open the URLs of a research note | `/research` | Python |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | Markdown deck to PowerPoint | `/render`, `/publish` | Python; pandoc or the `claude` CLI |
| `md2docx.py` | Markdown render to Word | `/render`, `/publish` | Python; pandoc or the `claude` CLI |
| `md2video.py` | screenplay render to a video or a player file | `/render` | Python; Pillow and ffmpeg for video |
| `hook-walkthrough.py` | repeats the walkthrough rule at every prompt | a hook | Python |
| `hook-git.py` | the wall between reading git and writing it | a hook | Python |
| `docs-state.py` | state of every documentation page, writers' tasks | `/document` | Python |
| `docs-index.py` | the documentation index from the map | `/document` | Python |
| `docs-check.py` | mechanical check of the pages, one-file scan | `/document`, `/render` | Python |
| `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py` | shared modules, not commands | none | Python |

## The git scripts

### forge-save.py

Saves the engine and every project that is a repository of its own: commit and push. Run by `/save` and `/release`.

Synopsis:

    python scripts/forge-save.py [slug | path] [-m MESSAGE] [--tag NAME]

- Bare: visits the engine and every project repository, and gives each one with changes its own commit. With a slug or a path: that one repository only. A project directory without a repository is skipped with a note (bare) or refused (named).
- Per repository: stages everything, commits (the message from `-m`, else a generated one), then pushes when an origin is configured.
- The remote changes are integrated by rebase only where the histories diverged, that is, where the remote branch has moved on as well. A branch that is merely ahead is pushed as it stands, so a merge made by hand keeps its merge commit. A clean repository that is ahead of its upstream is pushed the same way. A branch with no upstream yet reaches the remote with its first commit.
- A rebase that conflicts is left standing, with the commit made and nothing lost. The script prints the files in conflict and the step that follows, then is run again to push the clean repository. See [Settle a conflict](../use/settle-a-conflict.md).
- A repository with a rebase or a merge already in progress is refused before anything is staged, so that conflict markers are never committed.
- Without an origin the commit is kept locally and reported.
- `--tag NAME` needs one repository, so a slug is required. The commit is tagged and the tag pushed with it. With nothing to commit, the current HEAD is tagged. An existing tag is refused.
- Where git resolves no commit identity for the repository, it commits nothing and says so.
- It never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never `git clean`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-pull.py

Pulls the latest state from the remotes: the engine (its upgrade channel) and every project with an origin. Run by `/pull`.

Synopsis:

    python scripts/forge-pull.py [slug | path]

- Fast-forward only. Bare: the engine, then every project with an origin. With a slug or a path: that repository only.
- A repository with unsaved changes is not touched: reported and skipped (bare) or refused (named).
- A project without a repository or without an origin is reported and skipped.
- A repository whose history diverged from its origin is refused and nothing is pulled. The script never merges on its own.
- After a pull it prints where the repository moved from and to (`before` and `after` with hash and subject) and the subjects of the commits between.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-status.py

Reports the git state of the engine and every project. Read-only: it changes nothing. It has no command of its own.

Synopsis:

    python scripts/forge-status.py [slug | path] [--remote]

- First it prints the global git configuration file git reads, and the registration of the merge driver `ours` in it: `ok`, or the keys that are missing.
- Per repository: unsaved changes (or `clean`), a rebase or a merge in progress with the number of files in conflict, the branch, the last commit and the origin (or `no origin`, or `not under git`).
- A `user.name` or `user.email` set in the repository itself is reported as a fact, because it wins over the per-host identity the global configuration gives.
- `--remote` fetches each origin and reports the branch against it: `up to date`, `behind N`, `ahead N` or `diverged (ahead N, behind M)`. Without the flag the script touches no network.
- With `--remote` it also tries to read what waits on GitHub outside git, through `gh`. Under the `remote:` line comes a `github:` line with the open pull requests and the discussions nobody of the repository has answered, one line each. Whatever keeps it from reading (no `gh`, an origin that is not GitHub, no login, no network) becomes one line saying why, and the script goes on.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it. `gh` on PATH and logged in for the `github:` line.

### forge-clone.py

Clones an existing project into `projects/`. Run by `/import-project`.

Synopsis:

    python scripts/forge-clone.py <url>

- Clones the repository at the URL into `projects/<repository name>`; the name is taken from the URL. An existing directory is never overwritten.
- It sets no identity and carries no identity and no URL.
- Afterwards it reports facts: the origin, the last commit, the commit identity git resolves for the fresh clone, and the project file (its kind and language).
- Where git resolves no identity, it prints a hint instead: run `/setup`, or `python scripts/forge-config.py --identity <host> <name> <email>`, or set one locally; until then `forge-save.py` commits nothing.
- A project with neither a project file nor a ledger was not scaffolded by the forge; the script says so as a fact. A project of the shape before the migration is reported with its kind and language from the old ledger and the advice to run `/migrate`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-branch.py

Switches one repository to a branch, creating it when needed, or reports the branch. It has no command of its own.

Synopsis:

    python scripts/forge-branch.py <slug | path> [branch]

- With a branch name: switches to that branch, creating it from the current state when it does not exist; `main` switches back.
- Without a name: reports the current branch and lists the branches.
- There is no bare form. The repository is named by its slug or path (`forge` for the engine).
- Unsaved changes stop the switch: save first.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote with the first save made on it.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-config.py

The one door of the forge to the user's global git configuration. Every read and write goes through `git config --global`, so it lands in the file git itself reads. Run by `/setup`.

Synopsis:

    python scripts/forge-config.py
    python scripts/forge-config.py --register [--zdiff3]
    python scripts/forge-config.py --guard [--unset-identity]
    python scripts/forge-config.py --identity <host> <name> <email> [--replace]

- Bare: shows what is there (the file git reads, the registration of the merge driver `ours`, the guard, a global identity and the per-host stanzas) and changes nothing.
- `--register`: sets `merge.ours.driver true`, `merge.renormalize true`, `rebase.backend merge` and `rerere.enabled true`. `--zdiff3` adds `merge.conflictStyle zdiff3`.
- `--guard`: sets `user.useConfigOnly true`. It bites only once no global `user.name` or `user.email` is left; `--unset-identity` removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf` stanzas of one host (the `https://<host>/**` form and the `git@<host>:*/**` form), each with a path `.gitconfig-<host>` relative to the global file, and that file with `[user]` name and email where it is missing.
- A key that already carries the value asked is reported and left. A key that carries another value is reported and left, never overwritten, unless `--replace` is given for an identity.

Example:

    python scripts/forge-config.py --identity github.com "<name>" <email>

Needs: Python 3.8 or newer, git 2.36 or newer on PATH (`hasconfig` in `includeIf`), `forge_repos.py` and `forge_tools.py` beside it.

## The state scripts

### forge-history.py

Prints the history of one item of a project by its ID, from the history logs, their archives and the places that cite it. Read-only, no model. Run by `/history`; see [Read the history of an item](../use/read-the-history-of-an-item.md).

Synopsis:

    python scripts/forge-history.py <ID> <slug | path> [--full]

- The ID is `PREFIX.NNNN`; a short form such as `pos580` is read as `POS.0580`.
- It prints three parts: Today (the file that holds the item and its wording), Timeline (one line per event, oldest first: `born`, `changed`, `closed`, `removed`, `approved`, `mentioned by <ID>`, `archive`) and Cited today (every other place in the project that names the ID).
- `--full` prints every `Was` in full; otherwise it is shortened to its first sentences.
- Long texts are wrapped at 78 columns. An ID with no item and no record is said so.
- The pages of `docs/`, the documentation map, the renders, the resources and `tmp/` are never searched.

Needs: Python 3.8 or newer, `forge_repos.py` and `docs_map.py` beside it.

### forge-report.py

Completes the unique name of a reviewer's report: the local time to the minute and four hex characters of a content hash, appended in place. No model, no git. Run by `/critique`, `/challenge` and `/check` after they file a report.

Synopsis:

    python scripts/forge-report.py <path>

- Renames `YYYY-MM-DD-<kind>-<name>.md` to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md` and prints the new path.
- It refuses, with exit 1 and the reason printed: a path that is not a file; a name that already carries the tail; a name that ends in a run number; a file that is not Markdown; a target name that exists.
- It changes no name but the one it was given.

Needs: Python 3.8 or newer.

### forge-ledger.py

Makes the ledger of a project at read time from its documents. Run by `/ledger` and by every command that changes state.

Synopsis:

    python scripts/forge-ledger.py <slug | path> [--out PATH]

- It reads the project file, the headers of the artefacts, the histories, the decisions, the resource indexes, the reviews and challenges, the provenance of the renders and of the documentation index, the published companions, the work specifications, the threads and the ledger archive, and builds `ledger.md` in the shape of `templates/ledger.md`. Dependencies are the citations of another project's documents.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header, never a crash. The exit code is 0.
- It writes `ledger.md` only on a project of the current shape whose ledger is out of git's index. On a project of the shape before the migration, or where the ledger is tracked, it prints to stdout, or to `--out PATH`; a dry run of a real project goes to `tmp/`.
- The slug `forge` is the engine's own project.

Needs: Python 3.8 or newer, git on PATH, `forge_docs.py`, `forge_repos.py` and `forge_tools.py` beside it, and `templates/ledger.md`.

### forge-migrate.py

Brings one project to the current shape of files. Run by `/migrate`; see [Migrate a project](../use/migrate-a-project.md).

Synopsis:

    python scripts/forge-migrate.py <slug | path>            # dry run
    python scripts/forge-migrate.py <slug | path> --apply    # perform
    python scripts/forge-migrate.py <slug | path> --undo     # take back

- The shape of a project is a set of marks, one per step, never a version stored in the project:
  - `A`: no header carries a field that changes with a round.
  - `B0`: the project file exists.
  - `B`: `ledger.md` is out of git's index and what only the ledger knew lives in records.
  - `C1`: `threads/` exists, or the project has no threads file.
  - `D`: `.gitattributes` exists.
- The dry run, the default, prints the marks and, for every step still missing, what it would change.
- `--apply` runs the missing steps in the order A, B0, B, C1, D, each verifying its own mark afterwards. A library takes A, B0, B and D. It commits nothing: `/save` follows.
- `--apply` refuses, where the project is a repository of its own, a working tree with unsaved changes to tracked files, a branch behind or diverged from its origin, and any branch but `main`.
- `--undo` takes back the last `--apply` from the script's manifest, `tmp/forge-migrate-<slug>.json` at the engine root. It refuses on a project outside git.
- A project outside git gets none of the refusals, because the forge runs no git on it. The way back is the backup its user takes before `--apply`, and a run that stops midway is finished by running it again, the marks being the memory.
- The author of every record it writes is the handle of the instance file; without it the script refuses.
- Lines it cannot place (a Waiting line without an ID, a guessed thread origin, text after the last thread) are printed for the principal.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` and `forge_tools.py` beside it, and the templates `project.md`, `thread.md` and `gitattributes`.

### forge-check.py

Runs the mechanical clauses of the light check as a program instead of a model. No command runs it: it is run by hand, beside the check.

Synopsis:

    python scripts/forge-check.py light <slug | path> [--out PATH]

- `light <slug>` checks the bookkeeping of one project against the rules of `CLAUDE.md` and the templates: front-matter and history of the versioned documents, the ledger's own reports, records and companions, dependencies and resource indexes.
- The report is in the shape of the check contract: a verdict line, the findings ranked by severity, each with where, the rule and one fix. A closing section, "Left to reading", names the clauses of the check the script does not verify.
- No ID is given. It reads only. The exit code is 0 always; the report is the result. Without `--out` it prints.

Needs: Python 3.8 or newer, git on PATH, `forge_check.py`, `forge_docs.py`, `forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it, and `templates/`.

## The research scripts

### forge-engine.py

Runs one packet on a model of another family and brings its answer back as a note. Run by `/research`; see [Research a topic](../use/research-a-topic.md).

Synopsis:

    python scripts/forge-engine.py <engine> --packet <dir> --out <file>
        [--model <word>] [--effort low|medium|high|xhigh|max]
        [--timeout <seconds>] [--schema <file.json>] [--allow-all]
        [--sandbox] [--no-profile] [--prompt <text>]

- The engine table has one row, `antigravity`, whose tool is `agy`. A new engine is a row of the table and its pair in `COMMANDS` (the command builder and the envelope reader); see [Add an engine](../extend/add-an-engine.md). Further rows are to be added when wanted.
- The script finds the tool on PATH and checks its version against the floor where a bug is known; below it, it refuses.
- The packet folder must hold `packet.md`. The engine is given that folder as its workspace and runs in it, under the project's `tmp/`, never in the engine root.
- Per-run profile: the script gives the engine a profile of its own in `<run>/.home`, a copy of the user's settings with permission rules added (reading URLs allowed; commands, writing and reading of every entry of the engine root but `tmp/` denied). The engine is started with `HOME` and `USERPROFILE` pointing at it. The profile stays in the run folder. The user's global settings are not touched. `--no-profile` runs without it, as a trial of the engine alone.
- Verified read-only: it fingerprints every file of the packet folder (earlier envelopes and logs left out), runs the engine once, non-interactively, and compares afterwards. A run that changed or added anything is refused and nothing is filed.
- The envelope: `status` must say success and `response` must be non-empty. It is saved beside the packet as `envelope.json`. The run folder is kept.
- The answer is written to `--out` as a note, with `engine`, `model`, `usage`, `run` and `status: immutable` in its front-matter. The caller files and indexes it.

Flags:

- `--model`: the model word, recorded in the note.
- `--effort`: `low`, `medium`, `high`, `xhigh` or `max`.
- `--timeout`: seconds for the run, default 1800. Passed to the engine, and enforced by the script a minute later.
- `--schema`: a JSON schema file the final answer must follow. Off by default.
- `--allow-all`: passes the engine's flag that approves every tool call, which a headless run needs when the engine's web tools would otherwise wait for a permission nobody can give.
- `--sandbox`: passes the engine's sandbox flag where it has one.
- `--no-profile`: no per-run profile.
- `--prompt`: the one sentence the engine is started with. Default: read `packet.md` and do what it says.

Exit codes: 0 the note written; 1 a refusal with the reason on stderr (tool missing, version below the floor, packet without `packet.md`, the folder changed by the run, the envelope unreadable or the answer empty). The engine's own non-zero exit is reported with its stderr.

Needs: Python 3.8 or newer, `forge_tools.py` beside it, and the engine's own tool on PATH, with its login made once outside the forge.

### forge-cite.py

Verifies the citations of a research note before it is filed. Run by `/research`.

Synopsis:

    python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]
    python scripts/forge-cite.py --independence <bundle-dir>

- It collects every `http` and `https` URL of the note (or of every `*.md` of a bundle directory) with its line, opens each once (GET, redirects followed, the time limit per URL) and gives it one of four states:
  - `ok`: 2xx.
  - `dead`: 404 or 410.
  - `unverifiable`: 401, 403, 429, a timeout or a network error. The page refused or did not answer; this is not counted as a failure.
  - `mismatch`: an arXiv abstract page whose title shares too few words with the note's entry.
- It prints one line per URL and a count. `--out` writes the same as a Markdown report. `--timeout` is the time limit per URL in seconds (the synopsis gives 20).
- Exit codes: 0 when nothing is dead or mismatched, 1 otherwise, 2 on a usage error.
- `--independence <bundle-dir>`: for every card with notes from more than one engine, prints the URLs the notes share and the long sentences they have in common, as counts, with a verdict. A second note that shares most of its sources or a third of its sentences with the first was written from it. No network is touched.
- It does not judge content, open paywalls or check a quote against its page. Nothing is written into the note.

Needs: Python 3.8 or newer, `forge_tools.py` beside it.

## The conversion scripts

### doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel and others) to Markdown. Run by `/ingest`.

Synopsis:

    python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
        [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
        [--dry-run] [--list-tools]

- Inputs: a file name, a glob, a list file (one path or glob per line, `#` or `;` starts a comment) or a directory with `--recurse`. They can be mixed.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the extension. A name collision within one run gets `_1`, `_2`.
- `--dry-run` lists what would be converted. `--list-tools` checks that markitdown is reachable and exits.
- Handled: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported and are to be resaved as `.docx`, `.pptx` or `.xlsx`.

Needs: Python 3.8 or newer and markitdown, resolved from PATH or named by `--markitdown-path`. The script installs nothing; the install line is `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

Synopsis:

    python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
        [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
        [--model <model>]

- `--engine claude` (the default): a model does the conversion, through headless Claude Code and Anthropic's official pptx skill. It is expensive and never the same twice. It is the engine of `/publish`.
- `--engine pandoc`: deterministic, one slide per second-level heading, nothing interpreted by a model. It is the engine of `/render`.
- `--template` names a `.potx` or `.pptx` by path. Without it, the claude engine designs the style itself and pandoc uses its built-in one.
- `--recipe` is the recipe the definition was rendered from; the claude engine reads its Format section.
- `--model` is the model of the headless run (default `opus`); the claude engine only.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python 3.8 or newer, `forge_tools.py` beside it. What pandoc and the claude engine need is in the next section. See [Render an output](../use/render-an-output.md).

### md2docx.py

Converts a Markdown render into a Word document.

Synopsis:

    python scripts/md2docx.py <render.md> [--engine pandoc|claude]
        [--reference <styles.docx>] [--page-size A4|Letter]
        [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]

- `--engine pandoc` (the default): deterministic. It is the engine of `/render`. The front-matter of the render is read as metadata and does not appear in the document. Mermaid fences land as blocks of code.
- `--engine claude`: a model does the conversion through headless Claude Code and the official docx skill, the recipe's Format section giving it its instructions. It is the engine of `/publish`.
- `--reference` names a `.docx`, `.dotx` or `.dotm` whose styles pandoc takes (its content is ignored). Without it, pandoc's built-in styles apply.
- `--page-size A4|Letter`: A4 when absent. Applied only without `--reference`; a reference document decides its own paper. The claude engine takes the reference as the template it starts from, and A4 where none is given.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python 3.8 or newer, `forge_tools.py` beside it.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser. See [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

Synopsis:

    python scripts/md2video.py <render.md> --format video|html-player
        [--pace 4,8,16] [--date "<date>"] [--section <name>]
        [--name <name>] [-o <file>] [--frame <seconds> <file.png>]

- It reads a screenplay render: the front-matter for the language, a title card, a card of what the viewer will see, scenes with a caption of two parts (Now, Why) and a fenced block of what the terminal shows, and an end card.
- `--format video`: every frame painted with Pillow as a simulated terminal (1280x890) and piped into ffmpeg (H.264, 30 fps). Deterministic.
- `--format html-player`: the timeline as JSON of events, wrapped as a script (`forgeVideo({...})` in `<name>.html-player.js`) so that the player page can load it from disk as well as from GitHub Pages.
- `--pace`: three reading rates in words a second: the principal's lines, Claude's answers and the lines that only report a file. Default `4,8,16`.
- `--date`: the date shown in the tab bar. The pace, the date and the look come from the recipe's Format section, as arguments; the render carries none of them.
- `--section`: the section of the course on the player page that the video belongs to. `--name`: the name the list shows, in the render's language, in place of the title card's title. Both go into the player file's data. The page groups videos by section, sections and videos alike in the order of the file names. A file without them is listed under its title, after the sections.
- `--frame <seconds> <file.png>`: paints one frame of the video at that second to a PNG and stops.
- The output lands next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path.
- Where the output lands under the engine's `docs/videos/`, the player page `docs/videos/index.html` is written anew from `templates/html-player.html`, with the folder's files listed and loaded.

Needs: Python 3.8 or newer, `forge_tools.py` beside it. For video: Pillow (`pip install pillow`) and ffmpeg on PATH. Fonts are taken from the system where they exist (Cascadia Mono or Consolas, Segoe UI; Menlo and Helvetica; DejaVu) and Pillow's built-in font otherwise. The script installs nothing.

### What the conversions need

Every tool is resolved from PATH and never installed by a script. `forge_tools.py` is the one owner of this text.

- pandoc, the engine of `/render`: installed by the user, once.
- The claude engine, behind `/publish`: the `claude` CLI on PATH and the official document skill of the format (pptx or docx) under either of its names, `anthropic-skills:<format>` or `document-skills:<format>`. Where neither is there, the plugin is installed from an interactive Claude Code session.

The steps are on [Install what the forge needs](../start/install.md).

## The hooks

### hook-walkthrough.py

A hook that runs at every prompt and repeats the rule of the one-item walkthrough. It is configured in `.claude/settings.json`.

- Claude Code runs it on every user prompt and adds its standard output to the context of that turn.
- It prints the walkthrough rule with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, the pointer to the walkthrough skill, and lines of conduct: use the forge's scripts; say what an own command does and wait for the principal's yes; change nothing that was not agreed; every question that asks the principal to decide is a proposition closed by the verdict line.
- It reads nothing, writes nothing and takes no arguments. It does not depend on the working directory: the settings invoke it in exec form with its own path from the `${CLAUDE_PROJECT_DIR}` placeholder.

Needs: Python 3.8 or newer on PATH as `python`.

### hook-git.py

A hook that runs before every Bash command Claude sends, and holds the wall between reading git and writing it. It is configured in `.claude/settings.json`; the PowerShell tool is closed to git whole by a deny rule.

Synopsis:

    python scripts/hook-git.py                                # as a hook: JSON on stdin
    echo 'git status' | python scripts/hook-git.py --judge    # one command, the verdict printed

- It reads the command from the hook's JSON, splits it at the shell's separators and judges every part that calls git:
  - allow: a reading verb with reading flags (`status`, `log`, `diff`, `show`, `fetch` and the like).
  - ask: the commands that finish a conflict, named one by one: `add` without `--force` and without interactive flags, `rebase --continue` and `--abort`, `merge --continue` and `--abort`, `merge <branch>` with one name and no flag, `checkout --ours` or `--theirs` on a file. The command is put to the principal and runs on his yes.
  - deny: everything else, with the script of the forge to use instead where one exists. That covers the writing verbs, a verb the script does not know (an alias among them), a reading verb with a writing flag, a global option that changes how git runs (`-c`, `--git-dir`, `--work-tree`, `--exec-path`), git inside another command and a part the script cannot read.
- A part that is not git is left to Claude Code. The answer is deny where any part is a git it refuses, ask where none is refused and one asks, allow where every part is a reading git, and nothing otherwise.
- It reads no file and writes nothing. It is for Claude's tools alone; the principal's own git from the shell is his.
- Its cases, every command with the verdict expected of it, are a test of the suite.

Needs: Python 3.8 or newer on PATH as `python`.

## The documentation scripts

The three run in the order below inside `/document`; see [Generate the documentation](../use/generate-the-documentation.md).

### docs-state.py

Computes the state of every page from the content of its inputs and prepares the writers' tasks. It runs before the writers.

Synopsis:

    python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
    python scripts/docs-state.py <map> --previous <path>

- For every entry of the documentation map, it hashes the entry's text (its `state` line excepted) with the content of every input: a whole file, or the part named after `#` (a section by its heading, an item by its ID), hashed as that part.
- The generator is hashed with the inputs: the writer's definition and the documentation contract, with their whitespace normalised. A change of the rule regenerates every page; a re-wrap of the rule regenerates nothing.
- The page at the entry's path carries `inputs-hash` in its front-matter. The two are compared and the entry's `state` is set in the map: `new` (no page), `regenerate` (the hash differs), `keep` (the same hash).
- A page under `<docs-dir>` that no entry names, and the page of an entry the planner marked `remove`, are listed as `remove`. The index `README.md` is excepted.
- For every `new` or `regenerate` entry it writes one task file to `<tmp-dir>`: the engine root, the page's path, the date, the version, the hash the page is to carry, the entry verbatim and the titles of the pages it links to.
- `--previous <path>` prints the map as last committed, for the planner.
- An input the map names and the disk does not have is reported and hashed as missing.
- It rewrites only the `- state:` line of each entry; the rest of the map stays byte for byte.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

### docs-index.py

Derives the documentation index from the map. No model.

Synopsis:

    python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]

- Writes `<docs-dir>/README.md`: before the sections, the reader paths of the map with each page a link; then one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its path and the entry's `line`.
- The same map gives the same index. The index is never edited by hand.
- Its front-matter names the map as its one input and carries the version of the owning project's intent.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

### docs-check.py

Mechanical check of the generated documentation. It runs after the pages are written, and its one-file form runs on a render.

Synopsis:

    python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
    python scripts/docs-check.py --file <path> [--fact PATTERN ...]

- It verifies: every entry not in state `remove` has its page and no unnamed page lies in `<docs-dir>`; every relative link to a `.md` file resolves; no long dash in prose (a code span and a fenced block are exempt); every page opens with front-matter; no instance fact (the values of the instance file, an e-mail address but a placeholder at `example.*`, an absolute path of a machine, every `--fact` pattern).
- `--file <path>` scans one file for instance facts only: the values of the instance file, an absolute path of a machine and the `--fact` patterns. No map, no link, no dash and no e-mail rule. This is the scan `/render` runs on a render it has just written; see [Render an output](../use/render-an-output.md).
- Every failure is printed with its file and line. Exit code 0 when everything holds, 1 when anything fails.
- It mends nothing: a page that fails is regenerated, never edited by hand.

Needs: Python 3.8 or newer, `docs_map.py` beside it.

## The shared modules

Not commands; each is imported by the scripts.

- `forge_repos.py`: what the git scripts share: the engine root, the list of repositories to visit, running git, the state of a repository against its origin, what waits on GitHub through `gh`, the global git configuration files, the registration of the merge driver `ours`, and coloured output.
- `forge_tools.py`: what the conversion scripts share: finding an external tool on PATH, resolving paths, running a tool, the headless Claude Code run, and the console set to UTF-8.
- `forge_docs.py`: what the scripts that read a project's documents share: front-matter, history records, ledger tables, resource index entries and threads. A reader never raises on a malformed file; it lists what it could not read.
- `docs_map.py`: the one reader of the documentation map, shared by the documentation scripts and by `forge-history.py`; it also reads the part of a file an input names after `#`.
- `forge_check.py`: what the mechanical checks of `forge-check.py` share: a finding and its report in the shape of the check contract, and the front-matter keys and comments a template owns.

To write a script of one's own, see [Add a script](../extend/add-a-script.md). The tests the scripts are changed with are on [Run the tests](../use/run-the-tests.md).

## Portability

`scripts/` is the only platform-bound layer. Its scripts are written to run unchanged on Linux and macOS as well as Windows: Python 3.8 or newer, run as `python scripts/<name>.py`, paths composed with `pathlib`, external tools resolved from PATH.

The tests run in CI on Linux and Windows at every push. Two kinds of script are still a writing rule rather than a verified claim: the conversions are tested for their failure without the tool alone, and the per-prompt hook is a writing rule. Nothing has run on macOS.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the conversions and the one-file scan.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job `md2video.py` serves.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Migrate a project](../use/migrate-a-project.md): the command behind the migration script.
- [Settle a conflict](../use/settle-a-conflict.md): the step the save script leaves standing.
- [Research a topic](../use/research-a-topic.md): the command behind the engine and the citation scripts.
- [Run the tests](../use/run-the-tests.md): the tests the scripts are changed with.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Add an engine](../extend/add-an-engine.md): adding a row to the engine table.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
