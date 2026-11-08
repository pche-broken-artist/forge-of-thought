---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 9c45991b96491167
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

This page lists every script in `scripts/` with its synopsis, options, forms, what it needs installed and the command that runs it. It is for the user who runs a script by hand and for the extender who changes one.

Every script is Python, run as `python scripts/<name>.py`. Each carries its own help in its module docstring. The words below follow the glossary: the ledger is the file that records the state of a project, made from its documents each time it is read (see [Glossary](glossary.md)). The principal is the person whose thinking is forged.

Two rules hold for the scripts that name a project:

- A project is named by its slug or by the path of its directory. A bare word is a slug and anything with a separator, or an absolute path, is a path.
- In the git scripts the word `forge` names the whole: the engine and the forge's own project where it is cloned beside it.

What each tool needs installed is explained in [Install what the forge needs](../start/install.md).

## Overview

| Script | What it is for | Run by | Needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save`, `/release` | Python, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | report git state without changing it | `/forge`, `/pull`, `/setup` | Python, git; `gh` for the `github:` line |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | switch to a branch or report the branch | by hand | Python, git |
| `forge-config.py` | read and write the global git configuration | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | the history of one item by its ID | `/history` | Python |
| `forge-report.py` | complete the name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | make the ledger of a project | `/ledger` and every command that changes state | Python, git |
| `forge-migrate.py` | bring a project to a new shape of files | `/migrate` | Python, git |
| `forge-check.py` | the mechanical clauses of the light check as a program | by hand | Python, git |
| `forge-engine.py` | run one packet on a model of another family | `/research` | Python, the engine's CLI |
| `forge-cite.py` | open every URL of a research note | `/research` | Python |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | Markdown deck to PowerPoint | `/render`, `/publish` | Python, pandoc or `claude` |
| `md2docx.py` | Markdown render to Word | `/render`, `/publish` | Python, pandoc or `claude` |
| `md2video.py` | screenplay render to a video or a player file | `/render` | Python; Pillow and ffmpeg for video |
| `hook-walkthrough.py` | the per-prompt hook | Claude Code, from `.claude/settings.json` | Python |
| `hook-git.py` | the hook between reading git and writing it | Claude Code, from `.claude/settings.json` | Python |
| `docs-state.py` | state of every page, the writers' tasks | `/document` | Python |
| `docs-index.py` | the documentation index from the map | `/document` | Python |
| `docs-check.py` | mechanical check of the pages; one-file scan | `/document`, `/render` | Python |

Python means 3.8 or newer. The shared modules `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py` and `forge_check.py` are not commands and are described at the end.

## The git scripts

### forge-save.py

Saves the engine and every project that is a repository of its own: stage, commit, push.

```
python scripts/forge-save.py [slug | path] [-m MESSAGE] [--tag NAME]
```

- Bare, it visits the engine and every project repository and gives each one with changes its own commit.
- With a slug or a path it saves that repository only. A project directory without a repository is skipped with a note when bare and refused when named.
- With `forge` it saves the engine and the forge's own project, each its own commit, both prefixed `forge:`.
- The message comes from `-m`, or is generated.
- Where an origin is configured it pushes. The remote changes are integrated by rebase only where the histories diverged, that is, where the remote's branch has moved on as well. A branch that is merely ahead is pushed as it stands, so that a merge made by hand keeps its merge commit. A clean repository ahead of its upstream is pushed the same way. A branch with no upstream reaches the remote with its first commit.
- A rebase that conflicts is left standing, with the commit made and nothing lost. The script prints the files in conflict and the step that follows (see [Settle a conflict](../use/settle-a-conflict.md)), then it is run again.
- A repository with a rebase or a merge already in progress is refused before anything is staged.
- Without an origin the commit is kept locally and reported.
- `--tag NAME` tags the commit and pushes the tag with it. It needs one repository, so a slug is required. When there is nothing to commit, the current state is tagged. With `forge` the tag goes on the engine alone. An existing tag is refused.
- The script sets no identity or remote and initialises no repository. It never uses `git add -f` and never `git clean`. Where git resolves no commit identity for a repository it commits nothing there and says so.

Needs: Python, git, `forge_repos.py`. Run by `/save` and `/release`.

### forge-pull.py

Pulls the latest state from the remotes: the engine, which is the upgrade channel, and every project with an origin.

```
python scripts/forge-pull.py [slug | path]
```

- Fast-forward only. The script never merges.
- A repository with unsaved changes is reported and skipped when bare, refused when named.
- A project without a repository or without an origin is reported and skipped.
- A repository whose history diverged from its origin is refused and nothing is pulled.
- After a pull it prints where the repository moved from and to, and the subjects of the commits between, so that the releases crossed can be read off and looked up in the release notes.
- `forge` means the engine and the forge's own project beside it.

Needs: Python, git, `forge_repos.py`. Run by `/pull`.

### forge-status.py

Reports the git state of the engine and every project. It is read-only.

```
python scripts/forge-status.py [slug | path] [--remote]
```

- First it names the global git configuration file git reads, and the registration of the merge driver `ours` in it: "ok", or the keys that are missing. Without the registration an unregistered clone silently falls back to a conflict on the derived files.
- Then, per repository: unsaved changes or "clean", a rebase or merge in progress with the number of files in conflict, the branch, the last commit and the origin (or "no origin" or "not under git").
- A `user.name` or `user.email` set in the repository itself is reported as a fact, since it wins over the per-host configuration and the forge never sets it.
- `--remote` fetches each origin and reports the branch against it: "up to date", "behind N", "ahead N" or "diverged (ahead N, behind M)". The fetch changes nothing in the working tree. Without the flag the script touches no network.
- With `--remote` it also tries to read what waits on GitHub outside git, through `gh`: a `github:` line under the `remote:` line, with the open pull requests and the discussions nobody of the repository has answered, one line each. Whatever keeps it from reading (no `gh`, an origin that is not GitHub, no login, no network) is one line saying so, and the script goes on.
- `forge` means the engine and the forge's own project beside it.

Needs: Python, git, `forge_repos.py`; `gh` on PATH and logged in for the `github:` line. Run by `/forge`, `/pull` and `/setup`.

### forge-clone.py

Brings an existing project into the forge by cloning its repository into `projects/`.

```
python scripts/forge-clone.py <url>
```

- The directory name falls out of the URL: `projects/<repository name>`. An existing directory is never overwritten.
- The script sets no identity and carries no identity and no URL.
- Afterwards it reports facts: the last commit, the origin, the commit identity git resolves for the fresh clone, and the project file (kind and language, or what a project without the file is). A project with neither file nor ledger was not scaffolded by the forge, which is a fact and not a defect.
- Where git resolves no identity, it prints a hint: run `/setup`, or `forge-config.py --identity <host> <name> <email>`, or set a local identity. `forge-save.py` commits nothing until then.

Example: `python scripts/forge-clone.py https://example.com/team/my-idea.git`

Needs: Python, git, `forge_repos.py`. Run by `/import-project`.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or reports the branch it is on.

```
python scripts/forge-branch.py <slug | path> [branch]
```

- With a branch name it switches, creating the branch from the current state when it does not exist. `main` switches back.
- Without a name it reports the current branch and lists the branches.
- There is no bare form.
- `forge` switches the engine and the forge's own project together, and every repository is checked before any is switched.
- Unsaved changes stop the switch: save first.
- Merging, deleting and pushing branches stay with git. A new branch reaches the remote by the first `forge-save.py` made on it.

Needs: Python, git, `forge_repos.py`. No command runs it: it is run by hand.

### forge-config.py

The one door to the user's global git configuration, through `git config --global`, so that it lands in the file git itself reads.

```
python scripts/forge-config.py
python scripts/forge-config.py --register [--zdiff3]
python scripts/forge-config.py --guard [--unset-identity]
python scripts/forge-config.py --identity <host> <name> <email> [--replace]
```

- Bare: shows the file git reads, the registration of the merge driver `ours`, the guard, a global identity and the per-host stanzas. Changes nothing.
- `--register`: writes the merge driver `ours` and the settings it needs (`merge.ours.driver true`, `merge.renormalize true`, `rebase.backend merge`, `rerere.enabled true`). `--zdiff3` adds `merge.conflictStyle zdiff3`.
- `--guard`: writes `user.useConfigOnly true`. It bites only once no global `user.name` or `user.email` is left; `--unset-identity` removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf` stanzas of one host and its identity file `.gitconfig-<host>`, beside the global file.
- A key that already carries the value is reported and left. A key that carries another value is reported and left, never overwritten, unless `--replace` is given for an identity.
- Where the configuration lies in several places (a network home and a local profile), it is made once in each place.

Example: `python scripts/forge-config.py --identity github.com "<name>" <email>`

Needs: Python, git 2.36 or newer (for `hasconfig` in `includeIf`), `forge_repos.py`, `forge_tools.py`. Run by `/setup`.

## The scripts of records and state

### forge-history.py

Prints the history of one item of a project by its ID, as one timeline. Read-only, no model.

```
python scripts/forge-history.py <ID> <slug | path> [--full]
```

- It prints the item's wording today, a timeline of its records and archive rows, and every other place that cites it.
- A short form such as `pos580` is read as the full ID.
- `--full` prints every `Was` in full instead of shortened.
- `forge` is the engine's own project.

Needs: Python, `forge_repos.py`, `docs_map.py`. Run by `/history`; see [Read the history of an item](../use/read-the-history-of-an-item.md).

### forge-report.py

Completes the name of a reviewer's report so that it is unique.

```
python scripts/forge-report.py <path>
```

- It renames the file in place from `YYYY-MM-DD-<kind>-<name>.md` to `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`, with the local time to the minute and four hex characters of a content hash, and prints the new path.
- It refuses, exit 1, a path that is not a file, a name that already has the tail, a name that ends in a run number and a target name that exists.

Needs: Python. Run by `/critique`, `/challenge` and `/check`.

### forge-ledger.py

Makes the ledger of a project from its documents.

```
python scripts/forge-ledger.py <slug | path> [--out PATH]
```

- It reads the project file, the artefacts' headers, the histories, the decisions, the resource indexes, the reviews and challenges, the provenance of renders and of the documentation index, the published companions, the work specifications, the threads and the ledger archive, and builds `ledger.md` in the shape of the ledger template.
- An unparsable file becomes a line `unparsed: <file>:<line>` in the header, never a crash. The exit code is 0.
- It writes `ledger.md` only for a project of the current shape whose ledger is out of git's index. Otherwise (a project before the migration, or a tracked ledger) it prints to stdout or to the `--out` path.
- The slug `forge` is the engine's own project.

Needs: Python, git, `forge_docs.py`, `forge_repos.py`, `forge_tools.py`, `docs_map.py` and the ledger template. Run by `/ledger` and by every command that changes state.

### forge-migrate.py

Brings one project to the shape of a release that changed the shape of files.

```
python scripts/forge-migrate.py <slug | path>            # dry run
python scripts/forge-migrate.py <slug | path> --apply    # perform
python scripts/forge-migrate.py <slug | path> --undo     # take back
```

- The shape is a set of marks, one per step: the project file exists, no header carries a field that changes with a round, the threads are files, `.gitattributes` exists, the ledger is out of git's index. The dry run, the default, prints the marks and what each missing step would change.
- `--apply` runs the missing steps, each verifying its mark afterwards. A library takes only some of them.
- It refuses, where the project is a repository of its own, a working tree with unsaved changes to tracked files, a branch behind or diverged from its origin and any branch but `main`.
- A project outside git gets none of these refusals, because the forge runs no git on it. Its way back is the backup its user takes before `--apply`, and `--undo` refuses there. A run that stops midway is finished by running it again, the marks being the memory.
- The author of every record it writes is the handle in the instance file; without it the script refuses.
- It commits nothing; `/save` follows.
- `--undo` takes back the last `--apply` from the script's own manifest, `tmp/forge-migrate-<slug>.json` at the engine root.
- Some facts are printed for the principal to judge (a line of the old waiting list without an ID, the guessed origin of a thread).

Needs: Python, git, `forge_repos.py`, `forge_tools.py`, `forge_docs.py` and the project, thread and gitattributes templates. Run by `/migrate`; see [Migrate a project](../use/migrate-a-project.md).

### forge-check.py

Runs the mechanical clauses of the light check as a program instead of a model, and prints a report.

```
python scripts/forge-check.py light <slug | path> [--out PATH]
```

- It verifies what the files fully determine: front-matter and history against the skeletons, the ledger's own reports, records and companions, the dependencies, and the resource indexes.
- The report is in the shape of the check contract: a verdict line, the findings ranked by severity, each with its place, rule and fix. No ID is given, because the `/check` procedure numbers and files a report.
- A closing section, "Left to reading", names the clauses of the check the script does not verify.
- It reads only. The exit code is always 0; the report is the result.
- It is run by hand beside the check and by no command.

Needs: Python, git, `forge_check.py`, `forge_docs.py`, `forge_repos.py`, `forge_tools.py`, `forge-ledger.py` and the templates.

## Research scripts

### forge-engine.py

Runs one packet on a model of another family and brings the answer back as a note. The login is the user's, made once in the engine's own tool; the forge carries no key or account.

```
python scripts/forge-engine.py <engine> --packet <dir> --out <file>
    [--model <word>] [--effort low|medium|high|xhigh|max]
    [--timeout <seconds>] [--schema <file.json>] [--allow-all]
    [--sandbox] [--no-profile] [--prompt <text>]
```

The engine table has one row today, `antigravity`, whose tool is `agy`. A version floor is checked and the run is refused below it. A new engine is a row of the table and its pair in `COMMANDS` (see [Add an engine](../extend/add-an-engine.md)). Rows for `codex`, `claude` and `copilot` are named as to be added.

What a run does:

1. It finds the engine's CLI on PATH and checks its version.
2. It reads the packet folder, which must hold `packet.md`. The engine is given that folder as its workspace, under the project's `tmp/`, never the engine root.
3. It gives the engine a profile of its own for the run: a copy of the user's settings with permissions added that allow reading URLs and deny commands, writing files and reading every part of the engine root but `tmp/`. The engine starts with its home pointed at that profile. The profile stays in the run folder as its record, and the user's global settings are not touched.
4. It records a fingerprint of the packet folder, runs the engine once, non-interactively, and compares the folder afterwards. A run that changed or added anything in it is refused and nothing is filed: read-only is verified, never trusted.
5. It reads the JSON envelope, saved beside the packet as `envelope.json`. Its status must say success and its response must be non-empty.
6. It writes the answer to `--out` as a note, with `engine`, `model`, `usage`, `run` and `status: immutable` in its front-matter. The caller files and indexes it.

Flags:

- `--model`: the model word, recorded in the note.
- `--effort`: the effort level passed to the engine.
- `--timeout`: seconds for the run, default 1800.
- `--schema`: a JSON schema file the final answer must follow.
- `--allow-all`: passes the engine's "approve every tool call" flag, needed when its web tools would otherwise wait for a permission nobody can give.
- `--sandbox`: passes the engine's sandbox flag.
- `--no-profile`: runs under the user's own settings, a trial and never a research.
- `--prompt`: the one sentence the engine is started with. The default tells it to read `packet.md` and do what it says.

Exit codes: 0 the note written; 1 a refusal with the reason on stderr (tool missing, version below the floor, packet without `packet.md`, the folder changed by the run, the envelope unreadable, the answer empty).

Needs: Python, `forge_tools.py`, the engine's CLI on PATH. Run by `/research`; see [Research a topic](../use/research-a-topic.md).

### forge-cite.py

Verifies the citations of a research note before it is filed.

```
python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]
python scripts/forge-cite.py --independence <bundle-dir>
```

Every http(s) URL is opened once and has one of four states:

- `ok`: a 2xx answer.
- `dead`: 404 or 410.
- `unverifiable`: 401, 403, 429, a timeout or a network error. It is not wrong, and it is never counted as a failure.
- `mismatch`: an arXiv abstract page whose title shares too few words with the note's entry.

It prints one line per URL and a count, and writes the same as Markdown to `--out`. `--timeout` is the limit per URL. Exit 0 when nothing is dead or mismatched, 1 otherwise, 2 on a usage error.

`--independence <bundle-dir>` touches no network. For every card with notes from more than one engine it prints the URLs and the longer sentences the notes share, as counts, and a verdict: a note that shares most of its sources or a third of its sentences with another was written from it, not from the web.

The script does not judge content, open paywalls or check a quote against its page, and it writes nothing into the note.

Needs: Python, `forge_tools.py`. Run by `/research`.

## The conversion scripts

### doc2md.py

Converts Word, PowerPoint, PDF, Excel and other documents to Markdown through markitdown.

```
python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
    [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
    [--dry-run] [--list-tools]
```

- Inputs are a file name, a glob, a list file (one path or glob per line) or a directory with `--recurse`; they may be mixed.
- Each document becomes `<name>.md` next to it, or in the directory `-o` names. An existing `.md` is skipped unless `--force`. `--suffix` inserts text before the extension.
- `--dry-run` lists what would be converted. `--list-tools` checks that markitdown is reachable.
- Legacy `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported and must be resaved first.

Needs: Python, markitdown on PATH or named by `--markitdown-path`. The script installs nothing. Run by `/ingest`.

### md2pptx.py

Makes a PowerPoint deck from a Markdown deck definition.

```
python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
    [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>] [--model <model>]
```

- `claude`, the default: a model does the conversion through headless Claude Code and the official pptx skill. Expensive, never the same twice. It is the engine of `/publish`. `--model` sets its model.
- `pandoc`: deterministic, one slide per second-level heading. It is the engine of `/render`.
- `--template` names a `.potx` or `.pptx` by path. `--recipe` hands the claude engine the recipe's Format section.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python, `forge_tools.py`; pandoc or the `claude` CLI with the document skill. The script installs nothing. See [Render an output](../use/render-an-output.md).

### md2docx.py

Makes a Word document from a Markdown render.

```
python scripts/md2docx.py <render.md> [--engine pandoc|claude]
    [--reference <styles.docx>] [--page-size A4|Letter]
    [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]
```

- `pandoc`, the default: deterministic, the engine of `/render`.
- `claude`: a model through headless Claude Code and the official docx skill, the engine of `/publish`.
- The front-matter of the render is read as metadata and does not appear. Mermaid diagrams are not rendered and land as blocks of code.
- `--reference` takes the styles of a `.docx`, `.dotx` or `.dotm`. Without it the page is A4, or Letter with `--page-size Letter`. With a reference the page setup is the reference's own.
- The output lands next to the input with the same basename unless `-o` names a path.

Needs: Python, `forge_tools.py`; pandoc or the `claude` CLI with the document skill. The script installs nothing.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed events its player plays in the browser.

```
python scripts/md2video.py <render.md> --format video|html-player
    [--pace 4,8,16] [--date "<date>"] [--section <name>]
    [--name <name>] [-o <file>] [--frame <seconds> <file.png>]
```

- `video`: every frame is painted with Pillow as a simulated terminal and piped into ffmpeg (H.264, 30 fps). The same render gives the same file.
- `html-player`: the timeline as JSON, wrapped as a script in `<name>.html-player.js`.
- `--pace` gives three reading rates in words a second: the principal's lines, Claude's answers, and the lines that only report a file. The default is 4,8,16.
- `--date` is the date shown in the tab bar.
- `--section` names the section of the course the video belongs to, and `--name` the name the list shows. A file without them is listed under its title, after the sections.
- `--frame <seconds> <file.png>` paints one frame of the video to a PNG and stops, as a check of the look.
- The output lands next to the input with the render's basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path. Where it lands under the engine's `docs/videos/`, the player page is written anew there, with the folder's files listed and loaded.

Needs: Python, `forge_tools.py`. For video also Pillow and ffmpeg on PATH. Fonts come from the system where they exist. See [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

## The hooks

Both hooks are configured in `.claude/settings.json` and run by Claude Code. Neither takes arguments in normal use, and both need only Python on PATH as `python`.

### hook-walkthrough.py

Runs on every prompt and adds its output to the context of that turn. It prints the one-item walkthrough rule with its verdict line, the pointer to the walkthrough skill, and the lines of conduct: use the forge's scripts, say and ask before a command of one's own, change nothing that was not agreed, and close every question that asks the principal to decide with the verdict line. It reads and writes nothing and does not depend on the working directory.

### hook-git.py

Runs before every Bash command Claude sends and judges every part that calls git. It reads the command from the hook's JSON on stdin and answers:

- `allow` where every part is a reading git.
- `ask` where none is refused and one finishes the step of a conflict: `add` without `--force`, `rebase --continue` or `--abort`, `merge --continue` or `--abort`, `merge <branch>` with one name, and `checkout --ours` or `--theirs` on a file. The command is put to the principal and runs on his yes.
- `deny` for everything else: writing verbs, an unknown verb, a reading verb with a writing flag, a global option that changes how git runs, git inside another command, and a part the script cannot read. The reason names the script of the forge to use instead.
- Nothing, for a part that is not git.

`--judge` takes one command on stdin and prints the verdict:

```
echo 'git status' | python scripts/hook-git.py --judge
```

The PowerShell tool is closed to git by a deny rule. The hook is for Claude's tools alone, and the principal's own git from the shell is his. Its cases, every command with the verdict expected, are a test of the suite (see [Run the tests](../use/run-the-tests.md)).

## The documentation scripts

The three scripts serve one run of `/document`; see [Generate the documentation](../use/generate-the-documentation.md). They need Python and `docs_map.py` beside them.

### docs-state.py

Computes the state of every page from the content of its inputs and prepares the writers' tasks.

```
python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
python scripts/docs-state.py <map> --previous <path>
```

- It hashes each entry's text and the content of every input it names (a whole file, or a part named after `#`) together with the writer's definition and the documentation contract, with their whitespace normalised. A re-wrap of the rule regenerates nothing and a change of the rule regenerates every page.
- It compares the hash with the `inputs-hash` in the page's front-matter and sets the entry's `state` line: `new` (no page), `regenerate` (the hash differs), `keep` (the same hash). A page that no entry names, or whose entry is marked `remove`, is listed as `remove`.
- It writes one task file per `new` or `regenerate` entry to the `--tasks` folder. An input the disk does not have is reported and hashed as missing.
- `--previous <path>` prints the map as last committed, for the planner.
- It rewrites only the `- state:` lines of the map.

### docs-index.py

Derives the documentation index from the map.

```
python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]
```

It writes `<docs-dir>/README.md`: the reading paths of the map, then one line per page grouped by section in the order start, use, about, extend, reference. It is deterministic and uses no model.

### docs-check.py

Checks the pages mechanically.

```
python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
python scripts/docs-check.py --file <path> [--fact PATTERN ...]
```

- Against the map: every entry not in state `remove` has its page and no page lies unnamed. Relative links to `.md` files resolve, no long dash stands in prose, and every page opens with front-matter.
- Instance facts: the values of the instance file, any e-mail address but a placeholder at `example.*`, any absolute path of a machine, and every `--fact` pattern.
- `--file <path>` scans one file for instance facts only: no map, links, dash or e-mail rule. It is the scan `/render` runs on a render it has just written (see [Render an output](../use/render-an-output.md)).
- Exit 0 when everything holds, 1 when anything fails. It mends nothing.

## The shared modules

None of these is a command.

- `forge_repos.py`: what the git scripts share: the engine root, the list of repositories to visit, running git, the state against the origin, what waits on GitHub, the global configuration files and the registration of the merge driver `ours`.
- `forge_tools.py`: what the conversion scripts share: finding a tool on PATH, running it, the headless Claude Code run and the console set to UTF-8. It is the one place that says what the conversions need installed.
- `forge_docs.py`: what the scripts that read project documents share: front-matter, history records, ledger tables, resource index entries and threads. A reader never raises on a malformed file.
- `docs_map.py`: the one reader of the documentation map, shared by the three documentation scripts and by `forge-history.py`.
- `forge_check.py`: what the mechanical checks share: a finding, its report in the shape of the check contract, and the front-matter keys and comments a template owns.

## Portability

- The scripts are the only platform-bound layer. They are written to run unchanged on Linux and macOS, with `python` on PATH as the one prerequisite (a system with only `python3` gives it that name).
- The tests run in CI on Linux and Windows at every push, the git scripts, the ledger, the light check and the git hook's judgement among them. The conversions are tested for their failure without the tool alone.
- The per-prompt hook is a writing rule until a run says otherwise.
- Nothing has run on macOS. For it the whole set is the writing rule alone.

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

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
