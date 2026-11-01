---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 383fcc004db72519
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

This page lists every file in `scripts/` with its synopsis, options, forms, what it needs installed and the command that runs it. It is for the user who wants to know what a command runs, and for the extender who writes or changes a script. Every script is run as `python scripts/<name>.py`, and each carries its own help in its module docstring.

## Overview

| Script | What it is for | Run by | Needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save`, `/release` | Python, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | report the git state, change nothing | Claude, when it reads state | Python, git |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | switch a repository to a branch, or report the branch | on request | Python, git |
| `forge-config.py` | read and write the global git configuration | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | the history of one item by its ID | `/history` | Python |
| `forge-report.py` | complete the name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | make the ledger of a project | every command that changes state | Python, git |
| `forge-migrate.py` | bring a project to the shape of a release | `/migrate` | Python, git |
| `forge-check.py` | the mechanical clauses of the light check as a program | by hand, no command | Python, git |
| `forge-engine.py` | run one packet on a model of another family | `/research` | Python, the engine's CLI |
| `forge-cite.py` | open the URLs of a research note | `/research` | Python |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | Markdown deck to PowerPoint | `/render`, `/publish` | Python, pandoc or the `claude` CLI |
| `md2docx.py` | Markdown render to Word | `/render`, `/publish` | Python, pandoc or the `claude` CLI |
| `md2video.py` | screenplay render to video or player events | `/render` | Python; Pillow and ffmpeg for video |
| `hook-walkthrough.py` | per-prompt hook that repeats the conduct rules | Claude Code, at every prompt | Python |
| `hook-git.py` | hook that separates reading git from writing it | Claude Code, before every Bash command | Python |
| `docs-state.py` | state of every documentation page, and the writers' tasks | `/document` | Python |
| `docs-index.py` | the documentation index from the documentation map | `/document` | Python |
| `docs-check.py` | mechanical check of the documentation, and the one-file scan | `/document`, `/render` | Python |

The modules `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py` and `forge_check.py` are shared code, not commands. They are listed at the end.

The git scripts are the door to every write of git. Reading git directly is open. Installing what the scripts need is described in [Install what the forge needs](../start/install.md). Writing a script of one's own is described in [Add a script](../extend/add-a-script.md). Every term of the forge is in the [Glossary](glossary.md).

## The git scripts

### forge-save.py

Commits and pushes the engine and every project that is a repository of its own.

```
python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]
```

- Without arguments it visits the engine and every repository under `projects/`, and gives each one with changes its own commit.
- With a slug it saves that one repository only. The slug `forge` means the engine.
- A project directory without a repository is skipped with a note (bare) or refused (with a slug).
- Per repository it stages everything, commits (the message from `-m`, or a generated one), then, when an origin is configured, integrates remote changes by rebase and pushes.
- A clean repository that is ahead of its upstream is pushed the same way. A branch with no upstream reaches the remote with its first commit.
- Without an origin the commit is kept locally and reported.
- `--tag NAME` tags the commit and pushes the tag with it. It needs a slug, since it works on one repository. When there is nothing to commit, the current HEAD is tagged. An existing tag is refused.
- If git resolves no commit identity for the repository, the script says so and commits nothing.

A rebase that conflicts is left standing. The commit is made and nothing is lost. The script prints the files in conflict and the step that follows (the step of a conflict, described in [Settle a conflict](../use/settle-a-conflict.md)), and then this script is run again to push the clean repository.

A repository with a rebase or a merge already in progress is refused before anything is staged, so that conflict markers are never committed.

The script never sets an identity or a remote, never initialises a repository, never uses `git add -f` and never uses `git clean`.

It needs Python 3.8 or newer, git on PATH, and `forge_repos.py` beside it.

### forge-pull.py

Fast-forwards the engine (its upgrade channel) and every project that has an origin.

```
python scripts/forge-pull.py [slug]
```

- Fast-forward only. The script never merges on its own.
- A repository with unsaved changes is reported and skipped (bare) or refused (with a slug).
- A project without a repository or without an origin is reported and skipped.
- A repository whose history has diverged from its origin is refused and nothing is pulled.
- After a pull it prints where the repository moved from and to (hash and subject), and the subjects of the commits between. The releases crossed can be read off them.

It needs Python 3.8 or newer, git on PATH, and `forge_repos.py`.

### forge-status.py

Reports the git state of the engine and every project. It is read-only.

```
python scripts/forge-status.py [--remote]
```

- First it reports the global configuration file git reads, and the registration of the merge driver `ours` in it: "ok", or the keys that are missing. Without the registration a clone silently falls back to a conflict on the derived files.
- For the engine and each project it reports unsaved changes (or "clean"), the branch, the last commit and the origin ("no origin" or "not under git" otherwise).
- It reports a rebase or a merge in progress, with the number of files in conflict.
- It reports a `user.name` or `user.email` set in the repository itself, which wins over the per-host identity.
- `--remote` also fetches each origin and reports the branch against it: "up to date", "behind N", "ahead N" or "diverged (ahead N, behind M)". Without the flag the script touches no network.

It needs Python 3.8 or newer, git on PATH, and `forge_repos.py`.

### forge-clone.py

Brings an existing project in by cloning its repository into `projects/`.

```
python scripts/forge-clone.py <url>
```

- The directory name falls out of the URL. An existing directory is never overwritten.
- The script sets no identity and carries no identity and no URL.
- Afterwards it reports facts: the origin, the last commit, the commit identity git resolves for the fresh clone, and the project file (kind and language, or what a project without the file is). A project with neither file nor ledger was not scaffolded by the forge. That is a fact, not a defect.
- Where git resolves no identity, it prints a hint: run `/setup`, or `python scripts/forge-config.py --identity <host> <name> <email>`, or set a local identity in the clone. It adds that `forge-save` commits nothing until then.

It needs Python 3.8 or newer, git on PATH, and `forge_repos.py`.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports the branch it is on.

```
python scripts/forge-branch.py <slug> [branch]
```

- With a branch name it switches to that branch and creates it from the current state when it does not exist. `main` switches back.
- Without a name it reports the current branch and lists the branches the repository has.
- There is no bare form. The slug `forge` means the engine.
- Unsaved changes stop the switch: save first, then switch.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote by the first save made on it. A release is made from `main` only.

It needs Python 3.8 or newer, git on PATH, and `forge_repos.py`.

### forge-config.py

Reads and writes the global git configuration the forge needs, through `git config --global` alone. It names no path to the file, because git decides where it lies.

```
python scripts/forge-config.py
python scripts/forge-config.py --register [--zdiff3]
python scripts/forge-config.py --guard [--unset-identity]
python scripts/forge-config.py --identity <host> <name> <email> [--replace]
```

- Bare: it shows what is there (the file git reads, the registration of the merge driver `ours`, the guard, a global identity and the per-host identity stanzas) and changes nothing.
- `--register`: writes the merge driver `ours` and the settings it needs, once per place: `merge.ours.driver true`, `merge.renormalize true`, `rebase.backend merge` and `rerere.enabled true`. `--zdiff3` adds `merge.conflictStyle zdiff3`.
- `--guard`: writes `user.useConfigOnly true`. It bites only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf` stanzas of one host (the `https://<host>/` form and the `git@<host>:` form), each with a path relative to the global file, then the identity file `.gitconfig-<host>` with the name and e-mail where it is missing.

A key that already carries the value asked is reported and left. A key that carries another value is reported and left as well, never overwritten, unless `--replace` is given for an identity. `--replace` also rewrites a stanza with another path and an identity file with another name or e-mail.

It needs Python 3.8 or newer, git 2.36 or newer on PATH (for `hasconfig` in `includeIf`), and `forge_repos.py` and `forge_tools.py`.

## The scripts that read a project

### forge-history.py

Prints the history of one item of a project by its ID, as one timeline. It is read-only and uses no model.

```
python scripts/forge-history.py <ID> <slug> [--full]
```

- The ID is `PREFIX.NNNN`. A short form such as `pos580` is read as `POS.0580`. The slug `forge` is the engine's own project.
- It prints three parts: today (the file that holds the item and its wording), the timeline (one line per event, oldest first, from the history logs, their archives and the records that mention the item), and where the item is cited today (file and line).
- Long texts are wrapped at 78 columns. `--full` prints every `Was` in full instead of shortened.
- Documentation pages, the documentation map, the renders, the resources and `tmp/` are never searched.

The command behind it is described in [Read the history of an item](../use/read-the-history-of-an-item.md). It needs Python 3.8 or newer, `forge_repos.py` and `docs_map.py`.

### forge-report.py

Completes the name of a reviewer's report so that two branches cannot make the same name.

```
python scripts/forge-report.py <path>
```

- The command that files a report writes it under `YYYY-MM-DD-<kind>-<name>.md`, then calls this script with the path.
- The script renames the file in place to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md` (the local time to the minute and the first four hex characters of the SHA-256 of the bytes) and prints the new path.
- It refuses, with exit code 1 and the reason printed: a path that is not a file; a name that already carries the time and hash; a name that ends in a run number such as `-2.md`; a file that is not Markdown; a target name that exists.
- It uses no model and no git, and changes no name but the one it was given.

It needs Python 3.8 or newer.

### forge-ledger.py

Makes the ledger of a project at read time from its documents, in the shape of `templates/ledger.md`.

```
python scripts/forge-ledger.py <slug> [--out PATH]
```

- It reads the project file, the headers of the artefacts, the histories, the decisions, the resource indexes, the reviews and challenges, the provenance of the renders and of the documentation index, the published companions, the work specifications, the threads and `ledger.archive.md`. Dependencies are the citations of another project's documents.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header, never a crash. The exit code is 0.
- It writes `ledger.md` only on a project of the current shape whose ledger is out of git's index. On a project of the shape before the migration, or where the ledger is tracked, `ledger.md` is the hand-kept ledger and is never written.
- `--out PATH` prints to that path instead of writing the ledger. Without it, a project that is not written to prints to stdout. A dry run of a real project goes to `tmp/`.
- The slug `forge` is the engine's own project.

It needs Python 3.8 or newer, git on PATH, `forge_docs.py`, `forge_repos.py` and `forge_tools.py`, and `templates/ledger.md`.

### forge-migrate.py

Brings one project to the shape of a release that changed the shape of files. The command behind it is described in [Migrate a project](../use/migrate-a-project.md).

```
python scripts/forge-migrate.py <slug>            # dry run
python scripts/forge-migrate.py <slug> --apply    # perform
python scripts/forge-migrate.py <slug> --undo     # take back
```

- The shape of a project is a set of marks, one per step: the project file exists (B0); no header carries a field that changes with a round (A); `threads/` exists or the project has no threads file (C1); `.gitattributes` exists (D); `ledger.md` is out of git's index (B).
- The dry run is the default. It prints the marks and, for every step still missing, what it would change.
- `--apply` runs the missing steps, each verifying its own mark afterwards. The order is A, B0, B, C1, D. A library takes A, B0, B and D.
- `--undo` takes back the last `--apply` from the script's own manifest in `tmp/`: tracked files are restored from the index, created files are removed, the ledger is put back into the index and the `.gitignore` line is taken out.
- The author of every record it writes is the handle in the instance file. Without it the script refuses.
- Where the project is a repository of its own, `--apply` refuses a working tree with unsaved changes to tracked files, a branch behind or diverged from its origin, and any branch but `main`. The migration is one large change, run once, on one clone.
- A project outside git gets none of these refusals. The forge runs no git on it, the way back is the backup its user takes before `--apply`, `--undo` refuses there, and a run that stops midway is finished by running it again.
- It commits nothing. `/save` follows.
- Lines the script cannot place (a Waiting line without an ID, the guessed origin of a thread, text after the last thread) are printed for the principal to judge.

It needs Python 3.8 or newer, git on PATH, `forge_repos.py` and `forge_tools.py`, and the templates `project.md`, `thread.md` and `gitattributes`.

### forge-check.py

Runs the mechanical clauses of a check as a program instead of a model: what the files fully determine, verified by reading them. No command runs it. It is run by hand beside the check.

```
python scripts/forge-check.py light <slug> [--out PATH]
```

- `light <slug>` is the bookkeeping of one project: front-matter and history; the ledger's own reports; records and companions; dependencies; resource indexes. The rules are read from `CLAUDE.md` (Versioning & status) and the templates.
- The report is in the shape of the check contract: the verdict line, the findings ranked by severity, each with where (file and line), the rule with its owner and one fix, marked "immediate fix:" where it is pure bookkeeping. No ID is given.
- A closing section "Left to reading" names the clauses of the check that the script does not verify, so that the script and the check can be compared clause by clause.
- It reads only. The exit code is always 0; the report is the result. `--out PATH` writes the report to a file.

It needs Python 3.8 or newer, git on PATH, `forge_check.py`, `forge_docs.py`, `forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it, and `templates/`.

## The scripts of research

### forge-engine.py

Runs one packet on a model of another family and brings its answer back as a note. The login is the user's, made once in the engine's own tool. The forge carries no key, account or configuration. It is run by `/research`, described in [Research a topic](../use/research-a-topic.md).

```
python scripts/forge-engine.py <engine> --packet <dir> --out <file>
    [--model <word>] [--effort low|medium|high|xhigh|max]
    [--timeout <seconds>] [--schema <file.json>] [--allow-all]
    [--sandbox] [--no-profile] [--prompt <text>]
```

What it does:

1. Finds the engine's CLI on PATH and checks its version against the floor where a bug is known (for `antigravity`, 1.1.1). It refuses below it.
2. Reads the packet folder, which must hold `packet.md`, the whole context of the run. The engine is given that folder as its workspace, under the project's `tmp/`, never the forge root.
3. Gives the engine a profile of its own for the run, in `<run>/.home/`: a copy of the user's settings with permissions added. It allows reading URLs, and denies commands, writing files and reading every entry of the engine root but `tmp/`. The engine is started with its home pointing at that profile. The profile stays in the run folder as its record, and the user's global settings are not touched.
4. Records a fingerprint of every file in the packet folder, runs the engine once, non-interactively, with its JSON envelope asked for and a time limit set, and compares the folder afterwards. A run that changed or added anything in it is refused and nothing is filed. Read-only is verified, not trusted.
5. Reads the envelope: `status` must say success and `response` must be non-empty. The envelope is saved beside the packet as `envelope.json`, and the run folder is kept.
6. Writes the answer to `--out` as a note, with `engine`, `model`, `usage`, `run` and `status: immutable` in its front-matter. The caller files and indexes it.

The engine table has one row, `antigravity`, whose tool is `agy`. A new engine is a row in the table and its pair in `COMMANDS`, as described in [Add an engine](../extend/add-an-engine.md). The header names `codex`, `claude` and `copilot` as rows to add when wanted.

| Flag | Meaning |
|---|---|
| `--model` | the model word, recorded in the note when the envelope names none |
| `--effort` | the effort level, passed on to the engine |
| `--timeout` | seconds for the run; default 1800. Passed to the engine where it has a flag, and enforced by the script a minute later |
| `--schema` | a JSON schema file the engine must shape its final answer by; off by default |
| `--allow-all` | passes the engine's "approve every tool call" flag; needed when its web tools would otherwise wait for a permission nobody can give in a headless run |
| `--sandbox` | passes the engine's sandbox flag where it has one |
| `--no-profile` | runs the engine under the user's own settings, with no per-run profile; a trial, never a research |
| `--prompt` | the one sentence the engine is started with; default: read `packet.md` in the workspace and do exactly what it says |

Exit codes:

- 0: the note was written.
- 1: a refusal, with the reason on stderr (tool missing, version below the floor, packet without `packet.md`, the folder changed by the run, the envelope unreadable or the answer empty). The engine's own non-zero exit is reported with its stderr.

It needs Python 3.8 or newer, `forge_tools.py`, and the engine's CLI on PATH.

### forge-cite.py

Verifies the citations of a research note before it is filed. Every URL in the note is opened and its state reported. It is run by `/research`, described in [Research a topic](../use/research-a-topic.md).

```
python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]
python scripts/forge-cite.py --independence <bundle-dir>
```

Each URL is opened once (GET, redirects followed, a time limit per URL) and classified in one of four states:

| State | Meaning |
|---|---|
| `ok` | a 2xx answer |
| `dead` | 404 or 410: the page is gone or never existed |
| `unverifiable` | 401, 403, 429, a timeout or a network error: the page refused or did not answer, which is not wrong |
| `mismatch` | an arXiv abstract page whose title shares too few words with the note's entry: the ID points to another paper |

- It prints one line per URL and a count. `--out` also writes the same as a Markdown report. `--timeout` sets the seconds per URL.
- Exit 0 when nothing is dead or mismatched, 1 otherwise, 2 on a usage error.
- `--independence <bundle-dir>` works on a research bundle. For every card with notes from more than one engine, it prints the URLs the notes share and the sentences they have in common, as counts, and a verdict. A second engine's note that shares most of its sources, or a third of its sentences, with the first engine's was written from it, not from the web. The sentences counted are the longer ones (over sixty characters). No network is touched.
- It does not judge content, does not open paywalls and does not check a quote against its page. A 403 is never counted as a failure. Nothing is written into the note.

It needs Python 3.8 or newer and `forge_tools.py`. The network is touched except in the `--independence` form.

## The conversion scripts

None of them installs anything. What pandoc and the `claude` engine need is described in the header of `forge_tools.py` and in [Install what the forge needs](../start/install.md).

### doc2md.py

Converts Word, PowerPoint, PDF and Excel documents to Markdown with markitdown.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- Inputs can be mixed: a file name, a glob, a list file (plain text, one path or glob per line, `#` or `;` starting a comment) and a directory with `--recurse`.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the extension. A name collision within a run gets `_1`, `_2` and so on.
- `--dry-run` lists what would be converted and writes nothing. `--list-tools` checks that markitdown is reachable and exits.
- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg`. The legacy `.doc .ppt .rtf .odt .odp .ods` are reported as unsupported.

It needs Python 3.8 or newer and markitdown, found on PATH or named by `--markitdown-path`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
    [--model <model>]
```

Two engines, chosen by `--engine`:

- `claude` (the default): a model converts the definition, through headless Claude Code with the official pptx skill. It is expensive and never the same twice. It is the engine of `/publish`. `--model` sets its model (default `opus`), and `--recipe` lets it read the recipe's Format section.
- `pandoc`: a deterministic conversion, one slide per second-level heading, nothing interpreted by a model. It is the engine of `/render`.

`--template` names a `.potx` or `.pptx` by path. Without it, the `claude` engine designs the style itself and pandoc uses its built-in one. The output lands next to the input with the same basename unless `-o` names a path.

It needs Python 3.8 or newer and `forge_tools.py`, with pandoc or the `claude` engine as above.

### md2docx.py

Converts a Markdown render into a Word document.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

Two engines, chosen by `--engine`:

- `pandoc` (the default): a deterministic conversion, nothing interpreted by a model. It is the engine of `/render`.
- `claude`: a model converts the render, through headless Claude Code with the official docx skill, following the recipe's Format section (`--recipe`). It is expensive and never the same twice. It is the engine of `/publish`.

Other facts of the pandoc engine:

- The front-matter of the render is read as metadata and does not appear in the document.
- Mermaid diagrams are not rendered. They land in the document as blocks of code.
- `--reference` names a `.docx`, or a `.dotx` or `.dotm` template, whose styles pandoc takes. Without it, pandoc's built-in styles apply.
- The page is A4 by default. `--page-size A4|Letter` applies only without `--reference`, since a reference document decides its own paper.

The output lands next to the input with the same basename unless `-o` names a path. It needs Python 3.8 or newer and `forge_tools.py`, with pandoc or the `claude` engine.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser. The job is described in [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date "28. 9. 2026"] [--section <name>]
    [--name <name>] [-o <file>] [--frame <seconds> <file.png>]
```

- `--format video`: every frame is painted with Pillow as a simulated terminal (1280x890) and piped into ffmpeg (H.264, 30 fps). It is deterministic.
- `--format html-player`: the timeline as JSON of events, wrapped as a script (`forgeVideo({...})` in `<name>.html-player.js`) so that the player page can load it from disk as well as from GitHub Pages.
- Where the output lands under the engine's `docs/videos/`, the player page `index.html` is written anew from `templates/html-player.html`, with the folder's files listed and loaded.
- `--pace` is three reading rates in words a second: the principal's lines, Claude's answers, the lines that only report a file. The default is `4,8,16`.
- `--date` is the date shown in the tab bar. The pace, the date and the look come from the recipe's Format section, as arguments.
- `--section` names the section of the course the video belongs to. `--name` is the name the list shows, in the render's language, in place of the title card's title. Both go into the player file. The page groups the videos by section, in the order of the file names.
- `-o` names the output. By default it lands next to the input as `<name>.mp4` or `<name>.html-player.js`.
- `--frame <seconds> <file.png>` paints one frame of the video at that second to a PNG and stops, as a check of the look.

It needs Python 3.8 or newer and `forge_tools.py`. For video it also needs Pillow and ffmpeg on PATH. Fonts are taken from the system where they exist, and Pillow's built-in font is used otherwise.

## The hooks

A hook is a script that Claude Code runs on its own at a fixed moment, as `.claude/settings.json` configures it. Both need Python 3.8 or newer as `python` on PATH and nothing else.

### hook-walkthrough.py

A hook run at every prompt of the principal. It prints the rule of the one-item walkthrough with its verdict line, the pointer to the walkthrough method, and lines of conduct: use the forge's scripts, explain and ask before running a command of one's own, change nothing that was not agreed and approved, and close every question that asks the principal to decide with the verdict line. Claude Code adds this output to the context of the turn. The script reads nothing, writes nothing, takes no arguments and does not depend on the working directory.

### hook-git.py

A hook run before every Bash command Claude sends. It separates reading git from writing it. The PowerShell tool is closed to git whole by a deny rule.

```
python scripts/hook-git.py            # as a hook: JSON on stdin
python scripts/hook-git.py --test     # the built-in cases, exit 1 on a failure
echo 'git status' | python scripts/hook-git.py --judge   # one command, the verdict printed
```

It splits the command at the shell's separators and judges every part that calls git:

- A reading verb with reading flags (status, log, diff, show and the like): allow.
- The commands that finish a conflict: ask, so that the principal is asked and the command runs on his yes. They are `add` without `--force` and without the interactive flags, `rebase --continue` and `--abort`, `merge --continue` and `--abort`, `merge <branch>` with one name and no flag, and `checkout --ours` or `--theirs` on a file.
- Everything else: deny, naming the script of the forge to use where one exists. Denied are the writing verbs, an unknown verb (an alias among them), a reading verb with a writing flag, a global option that changes how git runs (`-c`, `--git-dir`, `--work-tree`, `--exec-path`), git inside another command and a part the script cannot read.

A part that is not git is left to Claude Code. The overall answer is deny where any part is a git it refuses, ask where none is refused and one is an asking git, allow where every part is a reading git, and nothing otherwise. The hook reads no file and writes nothing. It is for Claude's tools alone: the principal's own git from the shell is his.

`--test` runs the built-in cases and exits 1 on a failure. `--judge` reads one command from stdin and prints the verdict.

## The documentation scripts

These three serve `/document`, described in [Generate the documentation](../use/generate-the-documentation.md). `docs_map.py` reads the documentation map for all of them.

### docs-state.py

Computes the state of every page from the content of its inputs, and prepares the writers' tasks. It runs first in the run.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
python scripts/docs-state.py <map> --previous <path>
```

- For each entry of the map it hashes the entry (its `state` line excepted) together with the content of every input: a whole file, or the part named after `#` (a section by its heading, an item by its ID). The writer's definition and the documentation contract are hashed with the inputs, so that a change of the rule regenerates every page.
- A page carries the hash it was made from as `inputs-hash`. The entry's `state` is set in the map: `new` (no page at the path), `regenerate` (a page exists and its hash differs) or `keep` (the same hash).
- A page that no entry names, and the page of an entry marked `remove`, are listed as `remove`. The index `README.md` is excepted.
- For every `new` or `regenerate` entry it writes one task file to `<tmp-dir>`: the engine root, the page's path, the date, the version, the hash, the entry verbatim and the titles of the pages it links to.
- An input the map names and the disk does not have is reported and hashed as missing.
- The `--previous <path>` form prints the map as last committed, for the planner.
- It rewrites only the `- state:` line of each entry.

It needs Python 3.8 or newer and `docs_map.py`.

### docs-index.py

Derives the documentation index from the documentation map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

It writes `<docs-dir>/README.md`: before the sections, the reader paths of the map, each page a link; then one line per page, grouped by section in the order start, use, about, extend, reference, each line the page's title linked to its path and the entry's `line`. It is deterministic and uses no model. The index is never edited by hand. It needs Python 3.8 or newer and `docs_map.py`.

### docs-check.py

A mechanical check of the generated documentation.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

The first form verifies the pages against the map and the rules of a page, and prints every failure with file and line:

- every entry not in state `remove` has its page, and no page lies in the directory that the map does not name;
- every relative link to a `.md` file resolves;
- no long dash in the prose of a page (a code span and a fenced block are exempt);
- every page opens with a front-matter;
- no instance fact: the values of `CLAUDE.local.md`, any e-mail address but a placeholder at `example.*`, any absolute path of a machine, and every `--fact` pattern given.

The `--file <path>` form scans one file for instance facts only: the values of `CLAUDE.local.md`, an absolute path of a machine and the `--fact` patterns. It has no map, no link, no dash and no e-mail rule. It is the scan that `/render` runs on a render it has just written, described in [Render an output](../use/render-an-output.md).

The exit code is 0 when everything holds and 1 when anything fails. The check mends nothing: a page that fails is regenerated by the documentation command. It needs Python 3.8 or newer and `docs_map.py`.

## The shared modules

None is a command.

- `forge_repos.py`: what the git scripts share (the engine root, the list of repositories to visit, running git, the state of a repository against its origin, the global configuration files, the registration of the merge driver `ours`, coloured output).
- `forge_tools.py`: what the conversion scripts share (finding a tool on PATH, running a tool, the headless Claude Code run, the console set to UTF-8). Its header is the one owner of what pandoc and the `claude` engine need.
- `forge_docs.py`: what the scripts that read a project's documents share (front-matter, history records, ledger tables, resource index entries, threads). Used by `forge-ledger.py`, `forge-migrate.py` and `forge-history.py`.
- `docs_map.py`: the one reader of the documentation map, shared by the three documentation scripts.
- `forge_check.py`: what the mechanical checks of `forge-check.py` share (a finding and its report in the shape of the check contract, the front-matter keys and comments a template owns, the kinds of the versioned documents).

## Portability

`scripts/` is the only platform-bound layer. It is written to run unchanged on Linux and macOS: Python 3.8 or newer, `python scripts/<name>.py`, paths composed with `pathlib`, and external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH. A system that has only `python3` gives it that name.

The git scripts, the ledger script and `docs-state.py` have run on Linux. The conversions and the two hooks are a writing rule until a run says otherwise.

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

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
