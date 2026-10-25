---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 92a1852266042a0e
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
---

# Scripts

This page lists every script in `scripts/`: what it is for, how it is called, which options it takes, what it needs installed and which command runs it. It is for the user who wants to run a script by hand and for the extender who wants to know what exists before writing another.

Every script carries its own help in its module docstring. The principal is whoever's thinking is being forged. The ledger is the file that holds a project's state, made from the project's documents each time it is read.

## Overview

| Script | What it is for | Run by | What it needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save`, `/release` | Python, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | report the git state, read-only | by hand | Python, git |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | switch to a branch, creating it, or report the branch | by hand | Python, git |
| `forge-config.py` | read and write the global git configuration the forge needs | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | print the history of one item by its ID | `/history` | Python |
| `forge-report.py` | complete the unique name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | make a project's ledger from its documents | `/ledger` and every command that changes state | Python, git |
| `forge-migrate.py` | bring a project to the shape of a release | `/migrate` | Python, git |
| `forge-check.py` | run the mechanical clauses of the light check as a program | by hand | Python, git |
| `forge-engine.py` | run one packet on a model of another family | `/research` | Python, the engine's CLI |
| `forge-cite.py` | open every URL of a research note | `/research` | Python, network |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | make a PowerPoint deck from a Markdown deck | `/render`, `/publish` | Python, pandoc or the claude engine |
| `md2docx.py` | make a Word document from a Markdown render | `/render`, `/publish` | Python, pandoc or the claude engine |
| `md2video.py` | make a video or a player file from a screenplay render | `/render` | Python, Pillow and ffmpeg for video |
| `hook-walkthrough.py` | repeat the walkthrough rule and the conduct lines at every prompt | hook of `.claude/settings.json` | Python |
| `hook-git.py` | hold the wall between reading git and writing it | hook of `.claude/settings.json` | Python |
| `docs-state.py` | compute the state of every page and prepare the writers' tasks | `/document` | Python |
| `docs-index.py` | write the documentation index from the map | `/document` | Python |
| `docs-check.py` | check the generated pages mechanically | `/document`, `/render` | Python |
| `forge_repos.py`, `forge_docs.py`, `forge_tools.py`, `docs_map.py`, `forge_check.py` | modules the scripts share; not commands | the scripts | Python |

Installing what the scripts need is described in [Install what the forge needs](../start/install.md).

## The git scripts

These scripts are the door to every write of git. The engine and each project under `projects/` are separate repositories. The slug `forge` means the engine. A project that is not a repository of its own is reported or refused, never touched.

### forge-save.py

Commits and pushes the engine and every project that has changes. Run by `/save` and `/release`.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

- Without a slug it visits the engine and every project repository, and gives each one with changes its own commit. With a slug it saves that repository only. A project directory without a repository is skipped with a note (bare) or refused (slug).
- Per repository it stages everything, commits (the message from `-m`, or a generated one) and, when an origin is configured, integrates remote changes by rebase and pushes. Without an origin the commit is kept locally and reported.
- A clean repository that is ahead of its upstream is pushed the same way. A branch with no upstream yet reaches the remote with its first commit.
- `--tag NAME` tags the commit and pushes the tag with it. It needs a slug, because it works on one repository. When there is nothing to commit, the current state is tagged. An existing tag is refused.
- A rebase that conflicts is left standing. The commit is made and nothing is lost. The script prints the files in conflict and the step that follows, then you run it again, and it pushes the clean repository that is ahead. The step itself is described in [Settle a conflict](../use/settle-a-conflict.md).
- A repository with a rebase or a merge already in progress is refused before anything is staged, so that conflict markers are never committed.
- It never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never runs `git clean`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-pull.py

Pulls the latest state from the remotes. Run by `/pull`.

```
python scripts/forge-pull.py [slug]
```

- Fast-forward only. Without a slug it pulls the engine, then every project that has an origin. With a slug it pulls that repository.
- A repository with unsaved changes is not touched: it is reported and skipped (bare) or refused (slug). A project without a repository or without an origin is reported and skipped.
- A repository whose history has diverged from its origin is refused and nothing is pulled. The script never merges on its own.
- After a pull it prints where the repository moved from and to (hash and subject, before and after) and the subjects of the commits between, so that the releases crossed can be read off and their "Action required" lines looked up in `RELEASE-NOTES.md`.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-status.py

Reports the git state of the engine and every project. Read-only. Run by hand.

```
python scripts/forge-status.py [--remote]
```

- First it prints the global git configuration file git actually reads and the registration of the merge driver `ours` in it: "ok", or the keys that are missing (the required keys are those of `forge-config.py --register`). An unregistered clone silently falls back to a conflict on the derived files.
- Then, for the engine and each project: unsaved changes (or "clean"), the branch, the last commit and the origin, or "no origin" or "not under git". A rebase or a merge in progress is shown with the number of files in conflict. A `user.name` or `user.email` set in the repository itself is shown, because it wins over the per-host identity and the forge never sets it.
- `--remote` also fetches each origin and reports the branch against it: "up to date", "behind N", "ahead N" or "diverged (ahead N, behind M)". The fetch changes nothing in the working tree. Without the flag the script touches no network.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-clone.py

Brings an existing project in by cloning its repository into `projects/`. Run by `/import-project`.

```
python scripts/forge-clone.py <url>
```

- The directory is `projects/<repository name>`, taken from the URL. An existing directory is never overwritten. The script carries no URL and no identity.
- Afterwards it reports facts: the last commit, the origin, the commit identity git resolves for the fresh clone, and the project file (its kind and language, or what a project without the file is). A project with neither a project file nor a ledger was not scaffolded by the forge. That is a fact, not a defect.
- Where git resolves no `user.name` or `user.email`, it prints a hint: run `/setup`, or `forge-config.py --identity <host> <name> <email>`, or set a local identity in the repository. `forge-save.py` commits nothing until then.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-branch.py

Switches one repository to a branch, or reports the branch. Run by hand.

```
python scripts/forge-branch.py <slug> [branch]
```

- With a branch name it switches to that branch and creates it from the current state when it does not exist. `main` switches back.
- Without a name it reports the current branch and lists the branches.
- There is no bare form. Unsaved changes stop the switch: save first, then switch.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote with the first save made on it. A release is made from `main` only.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` beside it.

### forge-config.py

Reads and writes the global git configuration the forge needs, through `git config --global` alone, so that it lands in the file git itself reads. Run by `/setup`.

```
python scripts/forge-config.py
python scripts/forge-config.py --register [--zdiff3]
python scripts/forge-config.py --guard [--unset-identity]
python scripts/forge-config.py --identity <host> <name> <email> [--replace]
```

- Bare: shows what is there (the file git reads, the registration of the merge driver `ours`, the guard, a global identity and the per-host identity stanzas) and changes nothing.
- `--register`: writes the merge driver `ours` and the settings it needs, once per place: `merge.ours.driver true`, `merge.renormalize true`, `rebase.backend merge` and `rerere.enabled true`. `--zdiff3` adds `merge.conflictStyle zdiff3`.
- `--guard`: writes `user.useConfigOnly true`. It bites only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf` stanzas of one host, for the `https://` and the `git@` form of its URLs, each with a path `.gitconfig-<host>` relative to the global file. It then writes that file with `[user] name` and `email` where it is missing.
- A key that already carries the value asked is reported and left. A key that carries another value is reported and left, never overwritten. `--replace` rewrites a stanza or an identity file that carries another path, name or e-mail.

Needs: Python 3.8 or newer, git 2.36 or newer on PATH (`hasconfig` in `includeIf`), `forge_repos.py` and `forge_tools.py` beside it.

## The record and state scripts

### forge-history.py

Prints the history of one item of a project as one timeline. Read-only, no model involved. Run by `/history`. How to read the result is described in [Read the history of an item](../use/read-the-history-of-an-item.md).

```
python scripts/forge-history.py <ID> <slug> [--full]
```

- The ID is `PREFIX.NNNN`. A short form such as `pos580` is read as `POS.0580`. The slug `forge` is the engine's own project.
- Output in three parts: Today (the file that holds the item and its wording), Timeline (one line per event, oldest first, from the history logs and their archives, with the records of other items that mention it) and Cited today (every other place in the project that names the ID, as file and line).
- A record's reason follows its line. Its "Action" and "Was" follow as marked lines. `--full` prints each "Was" in full, otherwise it is shortened.
- The pages of `docs/`, the documentation map, the renders, the resources and `tmp/` are never searched. An ID with no item and no record is said so.

Needs: Python 3.8 or newer, `forge_repos.py` and `docs_map.py` beside it.

### forge-report.py

Completes the unique name of a reviewer's report. No model, no git. Run by `/critique`, `/challenge` and `/check` after they file a report.

```
python scripts/forge-report.py <path>
```

- It renames the file `YYYY-MM-DD-<kind>-<name>.md` in place to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`, with the local time to the minute and the first four hex characters of the SHA-256 of the file, and prints the new path.
- It refuses with exit code 1 and the reason: a path that is not a file; a name that already carries the tail; a name that ends in a run number such as `-2.md`; a target name that exists.

Needs: Python 3.8 or newer.

### forge-ledger.py

Makes the ledger of a project from its documents. Run by `/ledger` and by every command that changes state.

```
python scripts/forge-ledger.py <slug> [--out PATH]
```

- It reads the project file, the headers of the artefacts, the histories, the decisions, the resource indexes, the reviews and challenges, the provenance of the renders and of the documentation index, the published companions, the work specifications, the threads and `ledger.archive.md`. It builds `ledger.md` in the shape of `templates/ledger.md`.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header, never a crash. The exit code is 0.
- It writes `ledger.md` only on a project of the current shape whose ledger is out of git's index. On a project of the shape before the migration, or where the ledger is tracked, the file is never written: the script prints to standard output, or to the path `--out` names.
- The slug `forge` is the engine's own project.

Needs: Python 3.8 or newer, git on PATH, `forge_docs.py`, `forge_repos.py` and `forge_tools.py` beside it, and `templates/ledger.md`.

### forge-migrate.py

Brings one project to the shape of a release. Run by `/migrate`. The job is described in [Migrate a project](../use/migrate-a-project.md).

```
python scripts/forge-migrate.py <slug>            # dry run
python scripts/forge-migrate.py <slug> --apply    # perform
python scripts/forge-migrate.py <slug> --undo     # take back
```

- The shape of a project is a set of marks, one per step, never an engine version in the project:
  - B0: the project file exists.
  - A: no header of an artefact, specification, recipe, index or map carries a field that changes with a round.
  - C1: `threads/` exists, or the project has no threads file.
  - D: `.gitattributes` exists.
  - B: `ledger.md` is out of git's index.
- The dry run is the default. It prints the marks and, for every step still missing, what it would change.
- `--apply` runs the missing steps in the order A, B0, B, C1, D, each verifying its own mark afterwards. A library takes A, B0, B and D. It commits nothing; `/save` follows.
- `--undo` takes back the last `--apply` from the script's own manifest in `tmp/forge-migrate-<slug>.json` at the engine root.
- The author of every record it writes is the handle in the instance file (`Author:`). Without it the script refuses.
- Where the project is a repository of its own, `--apply` refuses a working tree with unsaved changes to tracked files, a branch behind or diverged from its origin, and any branch but `main`. The migration is one large change, run once, on one clone.
- A project outside git gets none of these refusals, because the forge runs no git on it. The way back is the backup its user takes before `--apply`, and `--undo` refuses there. A run that stops midway is finished by running it again, the marks being the memory.
- Items it cannot place are printed for the principal: a Waiting line without an ID, the guessed origin of a thread, text after the last thread.

Needs: Python 3.8 or newer, git on PATH, `forge_repos.py` and `forge_tools.py` beside it, and the templates `project.md`, `thread.md` and `gitattributes`.

### forge-check.py

Runs the mechanical clauses of a check as a program instead of a model. Run by hand beside the check, and by no command.

```
python scripts/forge-check.py light <slug> [--out PATH]
```

- It runs the clauses of the light check that are a comparison of files, and prints a report in the shape of the check contract: the verdict line, the findings ranked by severity, each with its place (file and line, relative to the project), the rule with its owner and one fix. Pure bookkeeping is marked "immediate fix:". No ID is given, because the check command numbers and files a report.
- The clauses it verifies:
  - front-matter and history: the header keys of every versioned document, version and status, the companion beside it, every record in the shape of the log, no Version History table left;
  - the ledger's own reports, composed in memory by `forge-ledger.py` and written nowhere;
  - records and companions: the published companions, the work files against their specifications, the thread files, the Verdict words of the decisions;
  - dependencies: every path of the ledger's Dependencies table on disk;
  - resource indexes: the header, the registration of every file, the bundle indexes and the fields of each entry.
- A section "Left to reading" closes the report. It names the clauses of the check that the script does not verify, so that the script and the check can be compared clause by clause.
- It reads only. The exit code is always 0; the report is the result. `--out` writes the report to a path.

Needs: Python 3.8 or newer, git on PATH, `forge_check.py`, `forge_docs.py`, `forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it, and `templates/`.

## The research scripts

Both are run by `/research`. The job is described in [Research a topic](../use/research-a-topic.md).

### forge-engine.py

Runs one packet on a model of another family and brings its answer back as a note. It is the forge's adapter to such an engine's command-line tool. The login is the user's, made once outside the forge, and the forge carries no key, account or configuration.

```
python scripts/forge-engine.py <engine> --packet <dir> --out <file>
    [--model <word>] [--effort low|medium|high|xhigh|max]
    [--timeout <seconds>] [--schema <file.json>] [--allow-all]
    [--sandbox] [--prompt <text>] [--no-profile]
```

- The engine table has one row, `antigravity`, whose tool is `agy`, with a minimum version of 1.1.1. Other rows (codex, claude, copilot) are to be added when wanted. A row is added, never a branch. Adding one is described in [Add an engine](../extend/add-an-engine.md).
- The packet folder must hold `packet.md`, the whole context of the run. The engine is given that folder as its workspace and runs in it, under the project's `tmp/`, never the forge root.
- The per-run profile: the script writes a settings file under `<run>/.home/`, a copy of the user's settings with permission rules added. Web reading is allowed. The shell and file writing are denied. Reading is denied for every entry of the engine root except `tmp/`, and for the folder where the first engine's notes wait. The engine is started with its home pointing at that profile. The profile stays in the run folder as its record. The user's global settings are not touched. `--no-profile` runs under the user's own settings, for a trial of the engine alone.
- The verified read-only folder: the script records a fingerprint of every file in the packet folder (the envelopes and logs of earlier runs left out), runs the engine once, non-interactively, and compares the folder afterwards. A run that changed or added anything in it is refused and nothing is filed.
- The envelope: the engine's JSON answer. Its `status` must say success and its `response` must be non-empty. It is saved beside the packet as `envelope.json`. The run folder is kept, never cleaned.
- The note: the answer is written to `--out` with `engine`, `model`, `usage`, `run` and `status: immutable` in its front-matter. The caller files and indexes it.
- Flags:
  - `--model`: the model word, recorded in the note.
  - `--effort`: the effort level.
  - `--timeout`: seconds for the run, 1800 by default; passed to the engine where it has a flag and enforced here a minute later.
  - `--schema`: a JSON schema file the final answer must follow; off by default.
  - `--allow-all`: passes the engine's flag that approves every tool call. It is needed when the engine's web tools would otherwise wait for a permission nobody can give in a headless run.
  - `--sandbox`: passes the engine's sandbox flag where it has one.
  - `--no-profile`: see above.
  - `--prompt`: the one sentence the engine is started with. By default it says to read `packet.md` in the workspace and do exactly what it says.
- Exit codes: 0 when the note is written; 1 for a refusal, with the reason on standard error (tool missing, version below the minimum, packet without `packet.md`, folder changed by the run, envelope unreadable, empty answer). The engine's own non-zero exit is reported with its standard error.

Needs: Python 3.8 or newer, the engine's command-line tool on PATH, `forge_tools.py` beside it.

### forge-cite.py

Verifies the citations of a research note before it is filed.

```
python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]
python scripts/forge-cite.py --independence <bundle-dir>
```

- It collects every http(s) URL of the note, or of every `.md` of a bundle directory, with its line, opens each once (redirects followed, the time limit per URL) and classifies it into one of four states:
  - `ok`: a 2xx answer.
  - `dead`: 404 or 410, the page is gone or never existed.
  - `unverifiable`: 401, 403, 429, a timeout or a network error. The page refused or did not answer. This is not counted as wrong.
  - `mismatch`: a preprint abstract page whose title shares too few words with the note's entry, the mark of a fabricated citation.
- It prints one line per URL and a count. `--out` also writes a Markdown report. `--timeout` is the limit per URL.
- Exit codes: 0 when nothing is dead or mismatched, 1 otherwise, 2 on a usage error.
- `--independence <bundle-dir>` compares, for every card that has notes from more than one engine, the URLs the notes share and the longer sentences (over sixty characters) they have in common, as counts, with a verdict. A second engine's note that shares most of its sources or a third of its sentences with the first's was written from it, not from the web. No network is touched.
- It does not judge content, does not open paywalls and does not check a quote against its page. Nothing is written into the note.

Needs: Python 3.8 or newer, network access, `forge_tools.py` beside it.

## The conversion scripts

Each is run by `/render` for the plain file and by `/publish` for the designed one. The conversions are described in [Render an output](../use/render-an-output.md). Each installs nothing: the tools are resolved from PATH, and `forge_tools.py` says what pandoc and the claude engine need and how each is installed.

### doc2md.py

Converts documents (Word, PowerPoint, PDF, Excel) to Markdown using markitdown. Run by `/ingest`.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- An input is a file name, a glob, a list file (one path or glob per line, `#` or `;` starts a comment) or a directory with `--recurse`. The notations can be mixed.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the extension. A name collision within one run gets `_1`, `_2`.
- `--dry-run` lists what would be converted. `--list-tools` checks that markitdown is reachable and exits.
- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported; resave them as `.docx`, `.pptx` or `.xlsx` first.

Needs: Python 3.8 or newer, markitdown on PATH or named by `--markitdown-path`; installed with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

- Two engines. `claude` (the default) has a model do the conversion through headless Claude Code with the official pptx skill; it is expensive and never the same twice, and it is the engine of `/publish`. `pandoc` converts deterministically, one slide per second-level heading; it is cheap, plain, and the engine of `/render`.
- `--template` names a `.potx` or `.pptx` by path, typically a file in a library project. Without it the claude engine designs the style itself and pandoc uses its built-in one.
- `--recipe` names the recipe; the claude engine reads its Format section. `--model` names the model of the headless run; the claude engine only.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python 3.8 or newer, `forge_tools.py` beside it, pandoc or the claude engine.

### md2docx.py

Converts a Markdown render into a Word document.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

- Two engines. `pandoc` (the default) converts deterministically; it is the engine of `/render`. `claude` has a model do the conversion through headless Claude Code with the official docx skill, the recipe's Format section giving the instructions; it is the engine of `/publish`.
- The YAML front-matter of the render is read as metadata and does not appear. Mermaid diagrams are not rendered; they land as blocks of code.
- `--reference` names a `.docx`, `.dotx` or `.dotm` whose styles the output takes. Without it pandoc's built-in styles apply.
- The page is A4 by default. Without `--reference` the script writes the page size into pandoc's built-in reference (`--page-size A4|Letter`). With `--reference` the page setup is the reference document's own and `--page-size` is not applied.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python 3.8 or newer, `forge_tools.py` beside it, pandoc or the claude engine.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser. The job is described in [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date <date>] [--section <name>]
    [--name <name>] [-o <file>] [--frame <seconds> <file.png>]
```

- It reads a screenplay render: the language from the front-matter, a title card, a card of what the viewer will see, scenes with a time of day, each with a caption of two parts (Now, Why) and a fenced block of what the terminal shows, and an end card. It computes the timeline from the pace and writes one of two formats.
- `video`: every frame painted as a simulated terminal and piped into ffmpeg (H.264, 30 frames a second). Deterministic.
- `html-player`: the timeline as JSON of events, wrapped as a script in `<name>.html-player.js`, so that the player page loads it from a file on disk as well as from a hosted page. Where the output lands under the engine's `docs/videos/`, the player page `docs/videos/index.html` is written anew from `templates/html-player.html`, with the folder's files listed and loaded.
- The pace is three reading rates in words a second: the principal's lines, Claude's answers, and the lines that only report a file. The default is 4,8,16. The pace, the date shown in the tab bar and the look come from the recipe's Format section, as arguments.
- `--section` names the section of the course on the player page that the video belongs to. `--name` names the video in the list, in the render's language, in place of the title card's title. Both go into the player file's data. The page groups the videos by section, sections and videos alike in the order of the file names. A file without them is listed under its title, after the sections.
- `--frame <seconds> <file.png>` paints one frame of the video at that second to a PNG and stops, as a check of the look.
- The output lands next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path.

Needs: Python 3.8 or newer, `forge_tools.py` beside it. For video also Pillow (`pip install pillow`) and ffmpeg on PATH. Fonts come from the system where they exist, and from Pillow's built-in font otherwise.

## The hooks

A hook is a script that Claude Code runs at a fixed moment. Both are configured in `.claude/settings.json`. Both need Python 3.8 or newer on PATH as `python`, and nothing else.

### hook-walkthrough.py

The hook that runs at every prompt of the principal. Claude Code adds its standard output to the context of that turn. It reads nothing, writes nothing and takes no arguments. It is independent of the working directory: `.claude/settings.json` invokes it in exec form and hands it its own path.

It prints:

- the walkthrough rule: one item per reply, a proposition closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, a question from the principal keeping the item open;
- the pointer to the walkthrough skill, to work by when a walkthrough or an interview runs;
- three lines of conduct: use the forge's scripts rather than the raw tool; say what an own command does and why, and wait for the principal's yes before running it; write, run and change nothing that was not agreed and approved.

### hook-git.py

The hook that runs before every Bash command Claude sends. It is the wall between reading git and writing it. The PowerShell tool stays closed to git whole by a deny rule, so that there is one parser and one door. The script reads the command from the hook's JSON on standard input, splits it at the shell's separators and judges every part that calls git.

It answers:

- allow: a reading verb with reading flags (status, log, diff, show, fetch and the like).
- ask, so that Claude Code puts the command to the principal and runs it on his yes: the commands that finish a conflict and its step, namely `add` without `--force` and the interactive flags, `rebase --continue` and `--abort`, `merge --continue` and `--abort`, `merge <branch>` with one name and no flag, and `checkout --ours` or `--theirs` on a file.
- deny: everything else. That is the writing verbs, a verb the script does not know (an alias among them), a reading verb with a writing flag, a global option that changes how git runs (`-c`, `--git-dir`, `--work-tree`, `--exec-path`), git inside another command (`xargs`, `sh -c`, a substitution) and a part the script cannot read. The reason names the rule and the script of the forge to use instead, where one exists.

A part that is not git is left to Claude Code. Over the whole command, deny wins, then ask, then allow. The hook is for Claude's tools alone; the principal's own git from the shell is his. It reads no file and writes nothing.

Forms:

```
python scripts/hook-git.py            # as a hook: JSON on standard input
python scripts/hook-git.py --test     # the built-in cases, exit 1 on a failure
echo 'git status' | python scripts/hook-git.py --judge   # one command, the verdict printed
```

## The documentation scripts

The three scripts serve `/document`, which is described in [Generate the documentation](../use/generate-the-documentation.md). Each needs Python 3.8 or newer and `docs_map.py` beside it, and nothing else. The map is the documentation map, one entry per page.

### docs-state.py

Computes the state of every page from the content of its inputs and prepares the writers' tasks. It runs before the writers.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
python scripts/docs-state.py <map> --previous <path>
```

- For every entry it hashes the entry's text (its `state` line excepted) together with the content of every input the entry names: a whole file, or the part named after `#` (a section by its heading, an item by its ID), hashed as that part. The writer's definition and the documentation contract are hashed with the inputs.
- The page at the entry's path carries the hash it was made from in its front-matter as `inputs-hash`. The two are compared and the entry's `state` is set in the map to `new` (no page), `regenerate` (the hash differs) or `keep` (the same hash).
- A page under the documentation directory that no entry names, and the page of an entry marked `remove`, are listed as `remove`. The index `README.md` is excepted.
- For every `new` or `regenerate` entry it writes one task file to the `--tasks` directory: the engine root, the page's path, the date, the version the page is made for, the hash the page is to carry, the entry verbatim and the titles of the pages it links to. The task is the whole prompt of a writer.
- An input the map names and the disk does not have is reported and hashed as missing. The page is regenerated and its writer reports the gap.
- `--previous <path>` prints the map as last committed, for the planner.
- The script rewrites only the `- state:` line of each entry.

### docs-index.py

Derives the documentation index from the map. Deterministic, no model.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

- It writes `<docs-dir>/README.md`: before the sections, the reader paths of the map, each page a link. Then one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its relative path and the entry's `line` (the first sentence of its `says` where an entry has no `line`).
- The front-matter names the map as its one input and carries the version of the owning project's intent. The opening paragraph is fixed text of this script.
- The index is never edited by hand: change the map and run the script again.

### docs-check.py

Checks the generated documentation mechanically. It runs after the pages are written.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

- With a map and a directory it verifies, and prints every failure with its file and line:
  - every entry of the map not marked `remove` has its page, and no page lies in the directory that the map does not name (the index excepted);
  - every relative link to a `.md` file resolves;
  - no long dash in the prose of any page (a code span and a fenced block are exempt);
  - every page opens with a front-matter;
  - no instance fact: the values of the instance file `CLAUDE.local.md` (every word of four letters or more in a value, looked for outside URLs), any e-mail address but a placeholder at `example.*`, any absolute path of a machine, and every `--fact` pattern given.
- With `--file <path>` one file is scanned for instance facts only: the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns. There is no map, no link check, no dash rule and no e-mail rule. This is the scan that `/render` runs on a render it has just written.
- The exit code is 0 when everything holds and 1 when anything fails. The script mends nothing: a page that fails is regenerated, never edited by hand.
- The script carries no name, address or host of its own. The instance facts are read from `CLAUDE.local.md` at run time.

## The shared modules

These are not commands. They are used by the scripts above and live beside them, never twice.

- `forge_repos.py`: what the git scripts share. The engine root, the git check, the list of repositories to visit, running git, the state of a repository against its origin, the files of the global git configuration, the registration of the merge driver `ours` and coloured output.
- `forge_docs.py`: what the scripts that read a project's documents share. Front-matter, the records of a history companion, the tables of a ledger, the entries of a resource index and the threads. Used by `forge-ledger.py`, `forge-migrate.py` and `forge-history.py`. A reader never raises on a malformed file: it lists what it could not read.
- `forge_tools.py`: what the conversion scripts share. Finding an external tool on PATH, resolving paths, running a tool, the headless Claude Code run, and the console set to UTF-8. It is the one owner of the text on what pandoc and the claude engine need.
- `docs_map.py`: the one reader of the documentation map, shared by the three documentation scripts and by `forge-history.py`. An input is a file, a section named after `#` by its heading, an item by its ID, or a block by its bold label.
- `forge_check.py`: what the mechanical checks of `forge-check.py` share. A finding and its report in the shape of the check contract, the front-matter keys and the comment a template owns, and the kinds of the versioned documents. A check there raises on nothing: what a file does not give is a finding or is left unread, named in the report.

## Portability

The scripts are the only platform-bound layer. They are written to run unchanged on Linux, macOS and Windows: Python 3.8 or newer, run as `python scripts/<name>.py`, paths composed with `pathlib`, external tools resolved from PATH.

Writing a script of your own is described in [Add a script](../extend/add-a-script.md).

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the conversions and the one-file scan.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job `md2video.py` serves.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Migrate a project](../use/migrate-a-project.md): the command behind the migration script.
- [Settle a conflict](../use/settle-a-conflict.md): the step the save script leaves standing.
- [Research a topic](../use/research-a-topic.md): the command behind the engine and the citation scripts.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Add an engine](../extend/add-an-engine.md): adding a row to the engine table.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
