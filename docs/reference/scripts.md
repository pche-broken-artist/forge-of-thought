---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 7edb8087e6ac4243
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

This page lists every file in `scripts/`: what it does, how it is called, what it needs installed and where its output lands. It is for the user who runs a script by hand and for the extender who writes one. Each script carries its own help in its module docstring, and this page restates it.

All scripts run as `python scripts/<name>.py` with Python 3.8 or newer. External tools (`git`, `markitdown`, `pandoc`, `claude`) are resolved from PATH, and no script installs anything. The scripts are the only part of the forge tied to a platform, and they are written to run unchanged on Linux, macOS and Windows. Installing what they need is described in [Install what the forge needs](../start/install.md). Writing a new one is described in [Add a script](../extend/add-a-script.md). Terms used here are defined in the [Glossary](glossary.md).

A project here is a directory `projects/<slug>`. The slug `forge` stands for the engine itself. The principal is the person whose thinking is forged. The ledger is the state table of a project, made at read time from its documents.

## Overview

| Script | What it is for | Command that runs it | What it needs |
|---|---|---|---|
| `forge-save.py` | Commit and push the engine and the projects | `/save`, `/release` | Python, git |
| `forge-pull.py` | Fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | Report the git state, read-only | none named; run by hand | Python, git |
| `forge-clone.py` | Clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | Switch to a branch, creating it, or report the branch | none named; run by hand | Python, git |
| `forge-config.py` | Read and write the global git configuration the forge needs | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | Print the history of one item by its ID | `/history` | Python |
| `forge-report.py` | Complete the unique name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | Make the ledger of a project | none named; run by hand | Python, git, `templates/ledger.md` |
| `forge-migrate.py` | Bring a project to the current shape of files | `/migrate` | Python, git, three templates |
| `forge-check.py` | Run the mechanical clauses of the light check as a program | none; run by hand | Python, git, `templates/` |
| `doc2md.py` | Convert documents to Markdown | none named; run by hand | Python, `markitdown` |
| `md2pptx.py` | Make a PowerPoint deck from a deck render | `/render` (pandoc engine), `/publish` (claude engine) | Python, pandoc or the `claude` CLI |
| `md2docx.py` | Make a Word document from a render | `/render` (pandoc engine), `/publish` (claude engine) | Python, pandoc or the `claude` CLI |
| `md2video.py` | Make a video or player events from a screenplay render | none named; run by hand | Python; for video, Pillow and ffmpeg |
| `hook-walkthrough.py` | Repeat the walkthrough rule at every prompt | a hook of Claude Code | Python on PATH as `python` |
| `hook-git.py` | Keep Claude's git to reading | a hook of Claude Code | Python on PATH as `python` |
| `docs-state.py` | Compute the state of every documentation page and prepare the writers' tasks | `/document` | Python |
| `docs-index.py` | Derive the documentation index from the documentation map | `/document` | Python |
| `docs-check.py` | Check the generated documentation mechanically | `/document`; its one-file form by `/render` | Python |

The shared modules are not commands:

- `forge_repos.py`: what the git scripts share (the engine root, the list of repositories, running git, the state against an origin, the registration of the merge driver, coloured output).
- `forge_tools.py`: what the conversion scripts share (finding tools on PATH, running them, the headless Claude Code run, the console set to UTF-8).
- `forge_docs.py`: what the scripts that read a project's documents share (front-matter, history records, ledger tables, resource index entries, threads).
- `docs_map.py`: the one reader of the documentation map, shared by the three documentation scripts.

`forge_check.py` is the module of `forge-check.py` and is described under it.

## The git scripts

The engine and every project under `projects/` are separate git repositories. A project that is not the top of a repository is outside git, and the forge runs no git on it. The scripts carry no URL and no identity.

### forge-save.py

Commits and pushes the engine and every project that is a repository of its own.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

- Without arguments it visits the engine and every project repository, and gives each one with changes its own commit.
- With a slug it saves that repository only. A project directory without a repository is skipped with a note (bare) or refused (slug).
- Per repository it stages everything, commits (the message from `-m`, or a generated one) and, when an origin is configured, integrates remote changes by rebase and pushes.
- A clean repository that is ahead of its upstream is pushed the same way. A branch with no upstream yet reaches the remote with its first commit.
- Without an origin the commit is kept locally and reported.
- `--tag <name>` needs a slug. The commit is tagged and the tag pushed with it. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.
- It never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never uses `git clean`.
- Where git resolves no commit identity for the repository, it commits nothing and says so.

A rebase that conflicts is left standing, with the commit made and nothing lost. The script prints the files in conflict and the step that follows: each file is settled, then `git add <file>` and `git rebase --continue` are run (both on the hook's ask), then the script is run again and pushes the clean repository. A repository with a rebase or a merge already in progress is refused before anything is staged, so that conflict markers are never committed. The step is described in [Settle a conflict](../use/settle-a-conflict.md).

Needs: Python, git, `forge_repos.py` and `forge_tools.py` beside it. Output: commits and pushes in git, and a report on the console.

### forge-pull.py

Pulls the engine (its upgrade channel) and every project that has an origin.

```
python scripts/forge-pull.py [slug]
```

- Fast-forward only. With a slug it pulls that repository ('forge' means the engine).
- A repository with unsaved changes is reported and skipped (bare) or refused (slug). Run `forge-save.py` first.
- A project without a repository or without an origin is reported and skipped.
- A repository whose history has diverged from its origin is refused and nothing is pulled. The script never merges on its own.
- After a pull it prints where the repository moved from and to (hash and subject, before and after) and the subjects of the commits between, so that the releases crossed can be read off and their Action required lines looked up in `RELEASE-NOTES.md`.

Needs: Python, git, `forge_repos.py` beside it.

### forge-status.py

Reports the git state of the engine and of every project. It is read-only.

```
python scripts/forge-status.py [--remote]
```

- First it prints the global configuration file git actually reads. Then it prints the registration of the merge driver `ours` in it: "ok", or the keys that are missing (`merge.ours.driver`, `rebase.backend`, `merge.renormalize`). Without the registration a clone silently falls back to a conflict on the derived files.
- Then, per repository: unsaved changes (or "clean"), the branch, the last commit and the origin, or "no origin" or "not under git".
- A rebase or a merge in progress is shown with the number of files in conflict, as a pointer to the step of a conflict.
- `--remote` also fetches each origin and reports the branch against it: "up to date", "behind N", "ahead N" or "diverged (ahead N, behind M)". The fetch changes nothing in the working tree. Without the flag the script touches no network.

Needs: Python, git, `forge_repos.py` beside it.

### forge-clone.py

Brings an existing project in by cloning its repository into `projects/`.

```
python scripts/forge-clone.py <url>
```

- The directory is `projects/<repository name>`, taken from the URL. An existing directory is never overwritten.
- It sets no identity and carries no URL.
- Afterwards it reports these facts:
  - the last commit
  - the origin
  - the commit identity git resolves for the fresh clone
  - the project file: kind and language, or the shape before the migration, or that there is no project file (a fact, not a defect)
- Where git resolves no `user.name` and `user.email`, it prints a hint: run `/setup`, or `python scripts/forge-config.py --identity <host> <name> <email>`, or set a local identity. `forge-save.py` commits nothing until then.

Needs: Python, git, `forge_repos.py` beside it.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports the branch it is on.

```
python scripts/forge-branch.py <slug> [branch]
```

- With a branch name it switches to that branch, creating it from the current state when it does not exist ('main' switches back).
- Without a name it reports the current branch and lists the branches.
- There is no bare form. Unsaved changes stop the switch: save first.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote with the first `forge-save.py` made on it.

Needs: Python, git, `forge_repos.py` beside it.

### forge-config.py

Reads and writes the global git configuration the forge needs, through `git config --global` alone. It names no path, because git decides where the file lies.

```
python scripts/forge-config.py
python scripts/forge-config.py --register [--zdiff3]
python scripts/forge-config.py --guard [--unset-identity]
python scripts/forge-config.py --identity <host> <name> <email> [--replace]
```

- Bare: prints what is there (the file git reads, the registration of the merge driver `ours`, the guard, a global identity and the per-host identity stanzas) and changes nothing.
- `--register`: writes the merge driver `ours` and the settings it needs: `merge.ours.driver true`, `merge.renormalize true`, `rebase.backend merge` and `rerere.enabled true`. `--zdiff3` adds `merge.conflictStyle zdiff3`.
- `--guard`: writes `user.useConfigOnly true`, so that a repository on a host with no identity stanza fails aloud. It bites only once no global `user.name` or `user.email` is left, and `--unset-identity` removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf` stanzas of one host (HTTPS and SSH remotes), each with a path `.gitconfig-<host>` relative to the global file. It then writes that file with `[user] name` and `email` where it is missing. `--replace` rewrites a stanza that carries another path and an identity file that carries another name or e-mail.
- A key that already carries the value asked is reported and left. A key that carries another value is reported and left as well, unless `--replace` is given for an identity.

Example: `python scripts/forge-config.py --identity github.com "<name>" <email>`.

Needs: Python, git 2.36 or newer (`hasconfig` in `includeIf`), `forge_repos.py` and `forge_tools.py` beside it.

## The record scripts

### forge-history.py

Prints the history of one item of a project, by its ID, as one timeline. It is read-only and involves no model. It is the one way Claude reads an item's history. The job is described in [Read the history of an item](../use/read-the-history-of-an-item.md).

```
python scripts/forge-history.py <ID> <slug> [--full]
```

- The ID is `PREFIX.NNNN`. A short form such as `pos580` is read as `POS.0580`.
- It prints three parts:
  - Today: the file that holds the item and its wording.
  - Timeline: one line per event, oldest first, from the history logs and their archives and from records of other items that name the ID.
  - Cited today: every other place in the project that names the ID, as file and line.
- A record's reason follows its line, with its Action and Was as marked lines. Was is shortened unless `--full` is given.
- An ID with no item and no record is said so. The pages of `docs/`, the map, the renders, the resources and `tmp/` are never searched.

Needs: Python, `forge_repos.py` and `docs_map.py` beside it.

### forge-report.py

Completes the unique name of a reviewer's report. No model and no git are involved.

```
python scripts/forge-report.py <path>
```

- The command that files a report writes it under `YYYY-MM-DD-<kind>-<name>.md`, then calls this script with the path.
- The script renames the file in place to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md` (the local time to the minute and the first four hex characters of the SHA-256 of the file) and prints the new path.
- It refuses, with exit 1 and the reason printed, in these cases:
  - the path is not a file
  - the name already carries the tail `-HHMM-<hash>`
  - the name ends in a run number such as `-2.md`
  - the target name exists
- It changes no name but the one it was given.

Needs: Python.

### forge-ledger.py

Makes the ledger of a project at read time from its documents.

```
python scripts/forge-ledger.py <slug> [--out PATH]
```

- It reads the project file, the headers of the artefacts, the history logs, the decisions, the resource indexes, the reviews and challenges, the provenance of the renders and of the documentation index, the published companions, the work specifications, the threads and `ledger.archive.md`. It builds `ledger.md` in the shape of `templates/ledger.md`, with the Waiting rule and the Reports section.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header, never a crash. The exit code is 0.
- It writes `ledger.md` only on a project of the current shape whose ledger is out of git's index.
- On a project of the shape before the migration, and where the ledger is tracked, it writes nothing into the project: it prints to standard output, or to the path `--out` names. The dry run of a real project goes to `tmp/`.

Needs: Python, git, `forge_docs.py`, `forge_repos.py` and `forge_tools.py` beside it, and `templates/ledger.md`.

### forge-migrate.py

Brings one project to the current shape of files. The job is described in [Migrate a project](../use/migrate-a-project.md).

```
python scripts/forge-migrate.py <slug>            # dry run
python scripts/forge-migrate.py <slug> --apply    # perform
python scripts/forge-migrate.py <slug> --undo     # take back
```

- The shape of a project is a set of marks, one per step, never an engine version in the project:
  - B0: the project file exists
  - A: no header carries a field that changes with a round
  - C1: `threads/` exists, or the project has no threads file
  - D: `.gitattributes` exists
  - B: `ledger.md` is out of git's index
- The dry run is the default. It prints the marks and, for each missing step, what it would change.
- `--apply` runs the missing steps, each verifying its own mark afterwards. The order is A, B0, B, C1, D. A library takes A, B0, B and D. It commits nothing: `/save` follows.
- `--undo` takes back the last `--apply` from the script's own manifest, `tmp/forge-migrate-<slug>.json` at the engine root.
- The author of every record it writes is the handle of the instance file. Without it the script refuses.
- Where the project is a repository of its own, `--apply` refuses a working tree with unsaved changes to tracked files, a branch behind or diverged from its origin, and any branch but main.
- A project outside git gets none of these refusals, because the forge runs no git on it. The way back is the backup its user takes before `--apply`, `--undo` refuses there, and a run that stops midway is finished by running it again.

Needs: Python, git, `forge_repos.py`, `forge_docs.py` and `forge_tools.py` beside it, and the templates `project.md`, `thread.md` and `gitattributes`.

### forge-check.py

Runs the mechanical clauses of a check as a program instead of a model. It is run by hand beside the check agent, and no command runs it. Its module is `forge_check.py`.

```
python scripts/forge-check.py light <slug> [--out PATH]
```

- It runs the clauses of the light check that are a comparison of files, with the rules read from `CLAUDE.md` and the templates. The clauses fall in five groups:
  - front-matter and history of every versioned document
  - the ledger's own reports (the ledger is composed in memory, nothing written)
  - records and companions (published companions, work files, thread files, Verdict words)
  - dependencies on disk
  - resource indexes
- It prints a report in the shape of the check contract: the verdict line, the findings ranked by severity, each with Where, the rule with its owner and one fix. No ID is given, because the `/check` procedure numbers and files a report.
- A section "Left to reading" closes the report. It names the clauses of the check that the script does not verify, so that the script and the agent can be compared clause by clause.
- It reads only. The exit code is always 0, and the report is the result.

`forge_check.py` holds what the mechanical checks share: a finding and its report in the contract's shape, the front-matter keys and comments a template owns, and the line numbers of a file. It is not a command.

Needs: Python, git, `forge_check.py`, `forge_docs.py`, `forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it, and `templates/`.

### doc2md.py

Converts Word, PowerPoint, PDF and Excel documents to Markdown with markitdown.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- Inputs may be a file name, a glob, a list file (one path or glob per line, `#` or `;` starts a comment) or a directory with `--recurse`.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the `.md`. A name collision within one run gets `_1`, `_2`.
- `--dry-run` lists what would be converted. `--list-tools` checks that markitdown is reachable and exits.
- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported.

Needs: Python and markitdown on PATH or named by `--markitdown-path`. Install it with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

## The conversion scripts

The tools they need are described in the docstring of `forge_tools.py`: pandoc (install it once, from pandoc.org or a package manager), and for the claude engine the `claude` CLI on PATH with the official pptx or docx skill of Claude Code or of the `document-skills` plugin. The claude engine is told to install and download nothing. The render that runs the pandoc conversions is described in [Render an output](../use/render-an-output.md).

### md2pptx.py

Makes a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

- `claude` (the default): a model does the conversion through headless Claude Code with the official pptx skill. It is expensive and never the same twice. It is the engine of `/publish`. `--recipe` hands the model the recipe's Format section. `--model` sets the model (default `opus`).
- `pandoc`: deterministic, one slide per second-level heading, nothing interpreted by a model. It makes a deck for reading, not for showing. It is the engine of `/render`.
- `--template` names a `.potx` or `.pptx` by path. Without it, the claude engine designs its own style and pandoc uses its built-in one.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python, `forge_tools.py` beside it, and pandoc or the claude engine's requirements.

### md2docx.py

Makes a Word document from a Markdown render.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

- `pandoc` (the default): deterministic, nothing interpreted by a model. It is the engine of `/render`.
- `claude`: a model does the conversion through headless Claude Code with the official docx skill, the recipe's Format section giving the instructions (`--recipe`). It is expensive and never the same twice. It is the engine of `/publish`.
- The Markdown render stays the source of truth. The YAML front-matter is read as metadata and does not appear in the document. Mermaid diagrams are not rendered: they land as blocks of code.
- `--reference` names a `.docx`, `.dotx` or `.dotm` whose styles the output takes. Without it pandoc's built-in styles apply and the page is A4 unless `--page-size Letter`. With `--reference` the template decides its own paper and `--page-size` is not applied.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python, `forge_tools.py` beside it, and pandoc or the claude engine's requirements.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser. The job is described in [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date "28. 9. 2026"] [-o <file>]
    [--frame <seconds> <file.png>]
```

- It reads a screenplay render: the language in the front-matter, a title card, a card of what the viewer will see, scenes each with a caption of two parts (Now, Why) and a block of what the terminal shows, and an end card.
- `--format video`: every frame is painted with Pillow as a simulated terminal (1280x890) and piped into ffmpeg (H.264, 30 fps). It is deterministic.
- `--format html-player`: the timeline as JSON events, wrapped as a script (`forgeVideo({...})` in `<name>.html-player.js`) so that the player page can load it from disk and from GitHub Pages. Where the output lands under the engine's `docs/videos/`, the player page `index.html` is written anew from `templates/html-player.html` with the folder's files listed and loaded.
- `--pace` is three reading rates in words a second: the principal's lines, Claude's answers, and the lines that only report a file. The default is `4,8,16`. The pace, the date shown in the tab bar and the look come from the recipe's Format section, as arguments.
- `--frame <seconds> <file.png>` paints one frame of the video at that second and stops, as a check of the look.
- The output lands next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path.

Needs: Python and `forge_tools.py` beside it. For video, Pillow (`pip install pillow`) and ffmpeg on PATH. Fonts are taken from the system where they exist, and Pillow's built-in font is the fallback.

## The hooks

A hook is a script that Claude Code runs at a fixed moment and that is configured in `.claude/settings.json`. Both need only Python on PATH as `python`.

### hook-walkthrough.py

The hook that runs on every prompt of the principal. A walkthrough is the forge's way of working a list of decisions one item per message.

- Claude Code adds its standard output to the context of that turn.
- It prints the walkthrough rule (one item per reply, closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`), a pointer to the walkthrough skill, and three lines of conduct: use the forge's scripts, say what an own command does and wait for a yes, and change nothing that was not agreed.
- It reads nothing, writes nothing, takes no arguments and does not depend on the working directory. `.claude/settings.json` invokes it by the path `${CLAUDE_PROJECT_DIR}` gives.

### hook-git.py

The hook that runs before every Bash command Claude sends. It keeps Claude's git to reading, so that the scripts are the only door to a write of git. The PowerShell tool is closed to git whole by a deny rule, so that there is one parser and one door. The harness, that is Claude Code, which runs Claude and its tools, acts on the answer.

- It reads the command from the hook's JSON on standard input, splits it at the shell's separators and judges every part that calls git. It answers one of three ways:
  - allow: a reading verb (`status`, `log`, `diff`, `show`, `fetch` and others) with reading flags
  - ask: the commands that finish a conflict, put to the principal and run on his yes. They are `add` without `--force` and without interactive flags, `rebase --continue`, `rebase --abort`, `merge --continue`, `merge --abort`, `merge <branch>` with one name and no flag, and `checkout --ours` or `--theirs` on a file. An ask holds in the automatic permission mode.
  - deny: everything else, with the script of the forge to use instead where one exists. Denied are the writing verbs, a verb the script does not know, a reading verb with a writing flag (`branch -d`, `tag v1`, `config` with a value, `log --output`, `fetch --prune`), a global option that changes how git runs (`-c`, `--git-dir`, `--work-tree`, `--exec-path`), git inside another command (`xargs`, `sh -c`, a substitution) and a part it cannot read.
- A part that is not git is left to the harness. Across parts, any refused git gives deny, else any asking git gives ask, else all reading gives allow.
- It reads no file and writes nothing. It is for Claude's tools alone: the principal's own git from the shell is his.

```
python scripts/hook-git.py            # as a hook: JSON on stdin
python scripts/hook-git.py --test     # the built-in cases, exit 1 on a failure
echo 'git status' | python scripts/hook-git.py --judge   # one command, the verdict printed
```

## The documentation scripts

The three scripts serve the run of `/document`, described in [Generate the documentation](../use/generate-the-documentation.md). Each reads the documentation map through `docs_map.py`, and none involves a model.

### docs-state.py

Computes the state of every page from the content of its inputs and prepares the writers' tasks.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
python scripts/docs-state.py <map> --previous <path>
```

- For every entry it hashes the entry's text (its `state` line excepted) together with the content of every input it names: a whole file, or the part after `#` (a section by its heading, an item by its ID), hashed as that part. The writer's definition and the contract are hashed in too.
- The page at the entry's path carries the hash it was made from as `inputs-hash`. The two are compared and the entry's `state` is set in the map:
  - `new`: no page at the path
  - `regenerate`: a page exists and its hash differs
  - `keep`: a page exists with the same hash
- A page under the docs directory that no entry names, and the page of an entry marked `remove`, are listed as `remove`. The index `README.md` is excepted.
- For every `new` or `regenerate` entry it writes one task file to `<tmp-dir>`: the engine root, the page's path, the date, the version the page is made for, the hash it is to carry, the entry verbatim and the titles of the pages it links to. The task is a writer agent's whole prompt.
- An input that the map names and the disk does not have is reported and hashed as missing.
- `--previous <path>` is the other form: it gives the map as last committed, for the planner.
- The script rewrites only the `- state:` line of each entry.

Needs: Python, `docs_map.py` beside it.

### docs-index.py

Derives the documentation index from the map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

- It writes `<docs-dir>/README.md`: before the sections, the reader paths of the map's Paths section. Then one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its path and the entry's `line`.
- It is deterministic: the same map gives the same index. The index is never edited by hand.

Needs: Python, `docs_map.py` beside it.

### docs-check.py

Checks the generated documentation mechanically.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

- It verifies the pages against the map and the rules of a page, and prints every failure with its file and line:
  - every entry not in state `remove` has its page, and no page lies in the docs directory that the map does not name
  - every relative link to a `.md` file resolves
  - no long dash in prose (code spans and fenced blocks are exempt)
  - every page opens with front-matter
  - no instance fact: the values of `CLAUDE.local.md`, any e-mail address but a placeholder at `example.*`, any absolute path of a machine, and every `--fact` pattern
- The one-file form `--file <path>` scans one file for instance facts only: the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns. There is no map, no link, no dash and no e-mail rule. It is the scan `/render` runs on a render it has just written.
- The exit code is 0 when everything holds and 1 when anything fails. It mends nothing: a page that fails is regenerated.

Needs: Python, `docs_map.py` beside it.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
- [Generate the documentation](../use/generate-the-documentation.md): the run the documentation scripts serve.
- [Render an output](../use/render-an-output.md): the render that runs the conversions and the one-file scan.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job `md2video.py` serves.
- [Read the history of an item](../use/read-the-history-of-an-item.md): the command behind the history script.
- [Migrate a project](../use/migrate-a-project.md): the command behind the migration script.
- [Settle a conflict](../use/settle-a-conflict.md): the step the save script leaves standing.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
