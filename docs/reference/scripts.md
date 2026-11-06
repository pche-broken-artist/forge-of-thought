---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: dc0e4683390b4773
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

This page lists every script in `scripts/`: what it is for, its
synopsis and options, the command that runs it and what it needs. It is
for the user who runs a script by hand and for the extender who reads
one before changing it. Every script is run as `python scripts/<name>.py`
and carries its own help in its module docstring. What the scripts need
installed is described in [Install what the forge needs](../start/install.md).

Terms used below:

- **Principal**: the person whose thinking is being forged.
- **Ledger**: the file `ledger.md` of a project, the state of its
  documents, made from them at read time and never kept in git.
- **Slug**: the short name of a project, the name of its directory under
  `projects/`; the slug `forge` means the engine itself.

## Overview

| Script | What it is for | Run by | Needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and every project | `/save`, `/release` | Python, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python, git |
| `forge-status.py` | report the git state of every repository | by hand | Python, git |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python, git |
| `forge-branch.py` | switch a repository to a branch, or report the branch | by hand | Python, git |
| `forge-config.py` | read and write the global git configuration | `/setup` | Python, git 2.36 or newer |
| `forge-history.py` | print the history of one item by its ID | `/history` | Python |
| `forge-report.py` | complete the unique name of a reviewer's report | `/critique`, `/challenge`, `/check` | Python |
| `forge-ledger.py` | make the ledger of a project | every command that changes state | Python, git |
| `forge-migrate.py` | bring a project to the shape of a release | `/migrate` | Python, git |
| `forge-check.py` | run the mechanical clauses of the light check | by hand, no command | Python, git |
| `forge-engine.py` | run one packet on a model of another family | `/research` | Python, the engine's CLI |
| `forge-cite.py` | open every URL of a research note | `/research` | Python |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python, markitdown |
| `md2pptx.py` | make a PowerPoint deck from a Markdown deck | `/render`, `/publish` | Python, pandoc or `claude` |
| `md2docx.py` | make a Word document from a Markdown render | `/render`, `/publish` | Python, pandoc or `claude` |
| `md2video.py` | make a video or a player file from a screenplay render | `/render` | Python, Pillow and ffmpeg for video |
| `hook-walkthrough.py` | repeat the walkthrough rule at every prompt | Claude Code, per prompt | Python |
| `hook-git.py` | hold the wall between reading git and writing it | Claude Code, per Bash command | Python |
| `docs-state.py` | compute the state of every page and prepare the tasks | `/document` | Python |
| `docs-index.py` | derive the documentation index from the map | `/document` | Python |
| `docs-check.py` | check the generated pages mechanically | `/document`, `/render` | Python |

The five shared modules, `forge_repos.py`, `forge_tools.py`,
`forge_docs.py`, `docs_map.py` and `forge_check.py`, are not commands;
they are described after the entries.

Where a script says "Python", it means Python 3.8 or newer. Where it
says "git", it means git on `PATH`.

## forge-save.py

- **What it does**: saves the engine and every project that is a
  repository of its own. Per repository it stages everything, commits
  (the message from `-m`, or a generated one) and, where an origin is
  configured, integrates remote changes by rebase and pushes.
- **Synopsis**: `python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]`
- **Forms**:
  - Without a slug: the engine and every `projects/<slug>` that is a
    repository, each one with changes getting its own commit. A project
    without a repository is skipped with a note.
  - With a slug: that repository only. A project without a repository is
    refused.
- **Options**:
  - `-m MESSAGE`: the commit message.
  - `--tag NAME`: tags the commit and pushes the tag with it. It takes
    one repository, so a slug is required. When there is nothing to
    commit, the current `HEAD` is tagged. An existing tag is refused.
- **Standing conflict**: a rebase that conflicts is left standing with
  the commit made and nothing lost. The script prints the files in
  conflict and the step that follows; run the script again afterwards,
  and it pushes the clean repository that is ahead.
- **Refusal**: a repository with a rebase or a merge already in progress
  is refused before anything is staged, so that conflict markers are
  never committed. See [Settle a conflict](../use/settle-a-conflict.md).
- **Other cases**: a clean repository ahead of its upstream is pushed
  the same way. A branch with no upstream reaches the remote with its
  first commit. Without an origin the commit is kept locally and
  reported.
- **Never**: it sets no identity or remote, initialises no repository,
  and uses neither `git add -f` nor `git clean`.
- **Needs**: Python, git; `forge_repos.py` beside it.

## forge-pull.py

- **What it does**: fast-forwards the engine (its upgrade channel) and
  every project that has an origin. It never merges.
- **Synopsis**: `python scripts/forge-pull.py [slug]`
- **Forms**:
  - Without a slug: the engine, then every project with an origin.
  - With a slug: that repository.
- **Refusals**: a repository with unsaved changes is reported and
  skipped (bare form) or refused (slug form). A repository whose history
  has diverged from its origin is refused and nothing is pulled.
  Projects without a repository or an origin are reported and skipped.
- **Output**: after a pull it prints where the repository moved from and
  to, and the subjects of the commits between, so that the releases
  crossed can be read off and their required actions looked up in
  `RELEASE-NOTES.md`.
- **Needs**: Python, git; `forge_repos.py` beside it.

## forge-status.py

- **What it does**: reports the git state of the engine and every
  project, and changes nothing.
- **Synopsis**: `python scripts/forge-status.py [--remote]`
- **Reported first**: the global configuration file git actually reads,
  and the registration of the merge driver `ours` in it: "ok", or the
  keys that are missing (the required keys of `forge-config.py
  --register`). An unregistered clone falls back to a conflict on the
  derived files without saying so.
- **Reported per repository**:
  - unsaved changes, or "clean";
  - a rebase or a merge in progress, with the number of files in
    conflict;
  - the branch and the last commit;
  - the origin, or "no origin", or "not under git";
  - a `user.name` or `user.email` set in the repository itself, as a
    fact: it wins over the per-host identity and the forge never sets it.
- **Option**: `--remote` fetches each origin and reports the branch
  against it: "up to date", "behind N", "ahead N" or "diverged (ahead N,
  behind M)". The fetch changes nothing in the working tree. Without the
  flag the script touches no network.
- **Needs**: Python, git; `forge_repos.py` beside it.

## forge-clone.py

- **What it does**: clones the repository at a URL into
  `projects/<repository name>`. The directory name falls out of the URL
  and an existing directory is never overwritten. It sets no identity
  and carries no URL.
- **Synopsis**: `python scripts/forge-clone.py <url>`
- **Facts it reports afterwards**: the last commit, the origin, the
  commit identity git resolves for the clone, and the project file: its
  kind and language, or what a project without the file is. A project
  with neither project file nor ledger was not scaffolded by the forge,
  which is a fact and not a defect.
- **Hint**: where git resolves no `user.name` and `user.email`, it
  prints the ways to set one: `/setup`, `forge-config.py --identity
  <host> <name> <email>`, or a local setting. `forge-save.py` commits
  nothing until then.
- **Needs**: Python, git; `forge_repos.py` beside it.

## forge-branch.py

- **What it does**: switches one repository to a branch, creating it
  from the current state if it does not exist, or reports the branch the
  repository is on. Branches are voluntary: whoever does not want one
  works on `main`.
- **Synopsis**: `python scripts/forge-branch.py <slug> [branch]`
- **Forms**:
  - With a branch name: switches, creating the branch when missing;
    `main` switches back.
  - Without a name: reports the current branch and lists the branches.
- **Rules**: there is no bare form, since switching every repository at
  once is never wanted. Unsaved changes stop the switch: save first.
  Merging, deleting and pushing branches stay with git; a new branch
  reaches the remote by the first `forge-save.py` made on it, and a
  release is made from `main` only.
- **Needs**: Python, git; `forge_repos.py` beside it.

## forge-config.py

- **What it does**: the one door to the user's global git configuration.
  Every read and write goes through `git config --global`, so it lands
  in the file git itself reads. A key that already carries the asked
  value is reported and left; a key that carries another value is
  reported and left, never overwritten, unless `--replace` is given for
  an identity.
- **Synopsis**:
  - `python scripts/forge-config.py`
  - `python scripts/forge-config.py --register [--zdiff3]`
  - `python scripts/forge-config.py --guard [--unset-identity]`
  - `python scripts/forge-config.py --identity <host> <name> <email> [--replace]`
- **Forms**:
  - Bare: shows the file git reads, the registration of the merge driver
    `ours`, the guard, a global identity and the per-host identity
    stanzas. Changes nothing.
  - `--register`: writes the merge driver `ours` and the settings it
    needs: `merge.ours.driver true`, `merge.renormalize true`,
    `rebase.backend merge` and `rerere.enabled true`. With `--zdiff3` it
    adds `merge.conflictStyle zdiff3`. They hold for every repository the
    configuration serves.
  - `--guard`: writes `user.useConfigOnly true`. It bites only once no
    global `user.name` or `user.email` is left; `--unset-identity`
    removes them.
  - `--identity <host> <name> <email>`: writes the two `includeIf`
    stanzas of one host (one for `https://<host>/**`, one for
    `git@<host>:*/**`), each with a path `.gitconfig-<host>` relative to
    the global file, and the identity file with `[user]` name and email
    where it is missing. A stanza with another path, or an identity file
    with another name or e-mail, is reported and left; `--replace`
    rewrites them.
- **Output**: the global git configuration file, wherever git reads it.
  On a machine with more than one such place, the configuration is made
  once in each.
- **Needs**: Python; git 2.36 or newer (`hasconfig` in `includeIf`);
  `forge_repos.py` and `forge_tools.py` beside it.
- **Example**: `python scripts/forge-config.py --identity github.com "<name>" <email>`

## forge-history.py

- **What it does**: prints the history of one item of a project by its
  ID, gathered from the history logs, their archives and the places that
  cite it. Read-only, no model involved. See
  [Read the history of an item](../use/read-the-history-of-an-item.md).
- **Synopsis**: `python scripts/forge-history.py <ID> <slug> [--full]`
- **Option**: `--full` prints every `Was` in full; otherwise each is
  shortened to its first sentences.
- **Output**:
  - Today: the file that holds the item and its wording.
  - Timeline: one line per event, oldest first (`born`, `changed`,
    `closed`, `removed`, `approved`, `mentioned by <ID>`, `archive`),
    each with its version, its date where the log has one, and the
    reason, with `Action` and `Was` as marked lines.
  - Cited today: every other place in the project that names the ID, as
    file and line.
- **Input forms**: a short form such as `pos580` is read as `POS.0580`.
  An ID with no item and no record is said so.
- **Not searched**: the pages of `docs/`, the map, the renders, the
  resources and `tmp/`.
- **Needs**: Python; `forge_repos.py` and `docs_map.py` beside it.

## forge-report.py

- **What it does**: completes the unique name of a reviewer's report. A
  file filed as `YYYY-MM-DD-<kind>-<name>.md` is renamed in place to
  `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`, the time being the local
  time to the minute and the hash the first four hex characters of the
  SHA-256 of the file's bytes. It prints the new path. No model, no git.
- **Synopsis**: `python scripts/forge-report.py <path>`
- **Refuses** (exit 1, the reason printed):
  - a path that is not a file;
  - a name that already carries the tail `-HHMM-<hash>`;
  - a name that ends in a run number such as `-2.md`;
  - a target name that exists.
- **Needs**: Python.

## forge-ledger.py

- **What it does**: makes the ledger of a project at read time from its
  documents: the tables of `templates/ledger.md`, the Waiting rule, the
  reports of what the merged files cannot say, and the archive for what
  has no record of the new shape.
- **Synopsis**: `python scripts/forge-ledger.py <slug> [--out PATH]`
- **Reads**: the project file, the artefacts' headers, the history
  logs, the decisions, the resource indexes, the reviews and the
  challenges, the provenance of the renders and of the documentation
  index, the published companions, the work specifications, the threads
  and `ledger.archive.md`. Dependencies are the citations of another
  project's documents.
- **Output**: writes `ledger.md` only on a project of the current shape
  whose ledger is out of git's index. On a project of the shape before
  the migration, or where the ledger is tracked, `ledger.md` is the
  hand-kept ledger and is never written: the script prints to standard
  output, or to the path of `--out`, where the dry run of a real project
  goes under `tmp/`.
- **Failure mode**: an unparsable file becomes a line `unparsed:
  <file>:<line>` in the header, never a crash. The exit code is 0.
- **Needs**: Python, git; `forge_docs.py`, `forge_repos.py` and
  `forge_tools.py` beside it; `templates/ledger.md`.

## forge-migrate.py

- **What it does**: brings one project to the shape of a release. The
  shape is a set of marks, one per step, never an engine version kept in
  the project. See [Migrate a project](../use/migrate-a-project.md).
- **Synopsis**:
  - `python scripts/forge-migrate.py <slug>` (dry run)
  - `python scripts/forge-migrate.py <slug> --apply`
  - `python scripts/forge-migrate.py <slug> --undo`
- **Marks and steps**, in the order of one run (A, B0, B, C1, D):
  - A: no header of an artefact, a specification, a recipe, an index or
    the map carries a field that changes with a round.
  - B0: the project file exists.
  - B: what only the ledger knew becomes records, and the hand-kept
    ledger moves to `ledger.archive.md` and out of git's index.
  - C1: `threads/` exists, or the project has no threads file.
  - D: `.gitattributes` exists.
  A library takes A, B0, B and D.
- **Forms**:
  - Dry run (the default): prints the marks and, for every missing step,
    what it would change.
  - `--apply`: runs the missing steps, each verifying its own mark
    afterwards. It commits nothing; `/save` follows.
  - `--undo`: takes back the last `--apply` from the script's manifest,
    `tmp/forge-migrate-<slug>.json` at the engine root.
- **Refusals**: without an `Author:` handle in the instance file, the
  script refuses. Where the project is a repository of its own,
  `--apply` refuses a working tree with unsaved changes to tracked
  files, a branch behind or diverged from its origin, and any branch but
  `main`.
- **Project outside git**: none of those refusals apply, because the
  forge runs no git on it. The way back is the backup the user takes
  before `--apply`, and `--undo` refuses. A run that stops midway is
  finished by running it again.
- **Needs**: Python, git; `forge_repos.py` and `forge_tools.py` beside
  it; the templates `project.md`, `thread.md` and `gitattributes`.

## forge-check.py

- **What it does**: runs the mechanical clauses of the light check as a
  program instead of a model: what the files fully determine, verified
  by reading them. It is run by hand beside the check and by no command.
- **Synopsis**: `python scripts/forge-check.py light <slug> [--out PATH]`
- **Form**: `light <slug>` checks the bookkeeping of one project:
  - front-matter and history of every versioned document;
  - the ledger's own reports, the ledger composed in memory and nothing
    written;
  - records and companions: the published companions, the threads, the
    verdict words of the decisions;
  - dependencies: every path of the ledger's Dependencies table on disk;
  - resource indexes against their directories.
- **Output**: a report in the shape of the check contract: a verdict
  line, the findings ranked by severity, each with its place, the rule
  and one fix. No ID is given. A closing section, "Left to reading",
  names the clauses of the check that the script does not verify. With
  `--out` the report goes to the path; otherwise to standard output.
- **Exit code**: 0 always; the report is the result.
- **Needs**: Python, git; `forge_check.py`, `forge_docs.py`,
  `forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it;
  `templates/`.

## forge-engine.py

- **What it does**: runs one packet on a model of another family and
  brings its answer back as a note. The login is the user's, made once
  outside the forge in the engine's own tool; the forge carries no key,
  account or configuration. Run by `/research`. See
  [Research a topic](../use/research-a-topic.md).
- **Synopsis**: `python scripts/forge-engine.py <engine> --packet <dir> --out <file> [--model <word>] [--effort low|medium|high|xhigh|max] [--timeout <seconds>] [--schema <file.json>] [--allow-all] [--sandbox] [--prompt <text>] [--no-profile]`
- **Engine table**: one row per engine. The only row is `antigravity`,
  whose tool is `agy` (version floor 1.1.1). A new engine is a row in the
  table and its pair of functions in `COMMANDS`: the command builder and
  the envelope reader. See [Add an engine](../extend/add-an-engine.md).
- **Steps**:
  1. Finds the engine's CLI on `PATH` and refuses a version below the
     floor.
  2. Reads the packet folder, which must hold `packet.md`. The engine
     is given that folder as its workspace, under the project's `tmp/`,
     never the forge root.
  3. Gives the engine a per-run profile: a copy of the user's settings
     with permissions added that allow reading URLs and deny commands,
     writing files and reading any entry of the engine root but `tmp/`.
     The engine is started with its home pointing at that profile, which
     stays in the run folder as its record. The user's global settings
     are not touched.
  4. Fingerprints every file of the packet folder, runs the engine once,
     non-interactively, and compares the folder afterwards. A run that
     changed or added anything in it is refused and nothing is filed:
     read-only is verified, not trusted.
  5. Reads the envelope: `status` must say success and `response` must
     be non-empty. The envelope is saved beside the packet as
     `envelope.json`; the run folder is kept.
  6. Writes the answer to `--out` as a note, with `engine`, `model`,
     `usage`, `run` and `status: immutable` in its front-matter. The
     caller files, indexes and remakes the ledger.
- **Flags**:
  - `--model`: the model word, recorded in the note; "engine default"
    where none is given.
  - `--effort`: the effort level, one of `low`, `medium`, `high`,
    `xhigh`, `max`.
  - `--timeout`: seconds for the run; default 1800. Passed to the
    engine where it has a flag, and enforced by the script a minute
    later.
  - `--schema`: a JSON schema file the final answer must follow; off by
    default.
  - `--allow-all`: passes the engine's flag to approve every tool call;
    needed when its web tools would otherwise wait for a permission
    nobody can give in a headless run.
  - `--sandbox`: passes the engine's sandbox flag where it has one.
  - `--no-profile`: runs under the user's own settings, with no per-run
    profile; a trial, never a research.
  - `--prompt`: the one sentence the engine is started with; the default
    tells it to read `packet.md` and do what it says.
- **Exit codes**: 0 the note was written. 1 a refusal with the reason on
  standard error: tool missing, version below the floor, a packet
  without `packet.md`, the folder changed by the run, an unreadable
  envelope or an empty answer. The engine's own non-zero exit is
  reported with its standard error.
- **Needs**: Python; the engine's CLI on `PATH`; `forge_tools.py` beside
  it.

## forge-cite.py

- **What it does**: opens every URL of a research note before it is
  filed and reports its state. It judges no content, opens no paywalls
  and writes nothing into the note. Run by `/research`. See
  [Research a topic](../use/research-a-topic.md).
- **Synopsis**:
  - `python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]`
  - `python scripts/forge-cite.py --independence <bundle-dir>`
- **The four states of a URL**:
  - `ok`: a 2xx answer.
  - `dead`: 404 or 410, the page is gone or never existed.
  - `unverifiable`: 401, 403, 429, a timeout or a network error; the page
    refused or did not answer, which is not wrong.
  - `mismatch`: an arXiv abstract page whose title shares too few words
    with the note's entry.
- **Options**:
  - `--timeout`: seconds per URL.
  - `--out`: also writes the report as Markdown to the path.
  - `--independence <bundle-dir>`: for every card with notes from more
    than one engine, prints the URLs the notes share and the sentences
    they have in common as counts, and a verdict. Sentences counted are
    those over sixty characters. No network is touched.
- **Output**: one line per URL and a count.
- **Exit codes**: 0 when nothing is dead or mismatched, 1 otherwise, 2 on
  a usage error.
- **Needs**: Python; `forge_tools.py` beside it.

## doc2md.py

- **What it does**: converts documents to Markdown through markitdown.
  Each document becomes `<name>.md` next to it, or in the directory `-o`
  names.
- **Synopsis**: `python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>] [--recurse] [--force] [--as-list] [--markitdown-path <exe>] [--dry-run] [--list-tools]`
- **Inputs**: a file name, a glob, a list file (one path or glob per
  line, `#` or `;` starting a comment) or a directory with `--recurse`.
- **Options**:
  - `-o <dir>`: the output directory.
  - `--suffix <text>`: inserted before the `.md` extension.
  - `--force`: overwrites an existing `.md`, which is skipped otherwise.
  - `--dry-run`: lists what would be converted, writes nothing.
  - `--list-tools`: checks that markitdown is reachable and exits.
  - `--markitdown-path <exe>`: names the markitdown executable.
- **Handled extensions**: `.pdf`, `.docx`, `.docm`, `.pptx`, `.pptm`,
  `.xlsx`, `.xlsm`, `.xls`, `.epub`, `.html`, `.htm`, `.csv`, `.json`,
  `.xml`, `.msg`. Legacy `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp`, `.ods`
  are reported as unsupported.
- **Needs**: Python; markitdown on `PATH`, installed by the user with
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`. The script
  installs nothing.

## md2pptx.py

- **What it does**: generates a PowerPoint deck from a Markdown deck
  definition.
- **Synopsis**: `python scripts/md2pptx.py <definition.md> [--engine pandoc|claude] [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>] [--model <model>]`
- **Two engines**:
  - `claude` (the default): a model does the conversion, through
    headless Claude Code with the official pptx skill. Expensive, never
    the same twice. It is the engine of `/publish`.
  - `pandoc`: deterministic, one slide per second-level heading, nothing
    interpreted by a model. It is the engine of `/render`.
- **Options**:
  - `--template`: a `.potx` or `.pptx` named by path. Without it, the
    `claude` engine designs its own style and `pandoc` uses its
    built-in one.
  - `--recipe`: the recipe the definition was rendered from; the
    `claude` engine reads its Format section.
  - `-o`: the output path. By default the output lands next to the input
    with the same basename.
  - `--model`: the model of the headless run; default `opus`; the
    `claude` engine only.
- **Needs**: Python; `forge_tools.py` beside it, which says what pandoc
  and the `claude` engine need. Nothing is installed by the script.

## md2docx.py

- **What it does**: converts a Markdown render into a Word document.
- **Synopsis**: `python scripts/md2docx.py <render.md> [--engine pandoc|claude] [--reference <styles.docx>] [--page-size A4|Letter] [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]`
- **Two engines**:
  - `pandoc` (the default): deterministic, nothing interpreted by a
    model. It is the engine of `/render`.
  - `claude`: a model does the conversion through headless Claude Code
    with the official docx skill, the recipe's Format section giving it
    instructions. Expensive, never the same twice. It is the engine of
    `/publish`.
- **Options**:
  - `--reference`: a `.docx`, `.dotx` or `.dotm` whose styles pandoc
    takes, its content ignored. The `claude` engine starts from it as a
    template.
  - `--page-size`: `A4` (the default) or `Letter`. It is not applied
    when `--reference` is given, since a template decides its own paper.
  - `--recipe`, `-o` and `--model` as for `md2pptx.py`; the default
    output lands next to the input with the same basename.
- **Behaviour of the pandoc engine**: the front-matter block at the top
  of a render is read as metadata and does not appear in the document.
  Mermaid diagrams are not rendered; they land as blocks of code.
- **Needs**: Python; `forge_tools.py` beside it. Nothing is installed by
  the script.

## md2video.py

- **What it does**: makes the format file of a screenplay render: a
  video, or the timed events its player plays in the browser. It reads a
  screenplay render (a title card, a card of what the viewer will see,
  scenes each with a caption of two parts, Now and Why, and a block of
  what the terminal shows, and an end card) and computes the timeline
  from the pace. See
  [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).
- **Synopsis**: `python scripts/md2video.py <render.md> --format video|html-player [--pace 4,8,16] [--date "<date>"] [--section <name>] [--name <name>] [-o <file>] [--frame <seconds> <file.png>]`
- **The two formats**:
  - `video`: every frame painted with Pillow as a simulated terminal
    (1280x890) and piped into ffmpeg (H.264, 30 fps). Deterministic.
  - `html-player`: the timeline as JSON of events, wrapped as a script
    `forgeVideo({...})` in `<name>.html-player.js`, so that the player
    page can load it from disk as well as from GitHub Pages.
- **Options**:
  - `--pace`: three reading rates in words a second: the principal's
    lines, Claude's answers, the lines that only report a file. Default
    `4,8,16`.
  - `--date`: the date shown in the tab bar.
  - `--section`: the section of the course the video belongs to on the
    player page.
  - `--name`: the name the list shows, in the render's language, in
    place of the title card's title.
  - `-o`: the output path.
  - `--frame <seconds> <file.png>`: paints one frame of the video at the
    given second to a PNG and stops, as a check of the look.
- **Player page**: sections and videos are grouped in the order of the
  file names. A file without a section or a name is listed under its
  title, after the sections. Where the output lands under the engine's
  `docs/videos/`, the page `docs/videos/index.html` is written anew from
  `templates/html-player.html`, with the folder's files listed and
  loaded.
- **Output**: next to the input with the render's basename (`<name>.mp4`
  or `<name>.html-player.js`) unless `-o` names a path.
- **Needs**: Python; `forge_tools.py` beside it. For `video`: Pillow
  (`pip install pillow`) and ffmpeg on `PATH`. Fonts come from the
  system where they exist and Pillow's built-in font otherwise. The
  script installs nothing.

## hook-walkthrough.py

- **What it does**: is the hook that Claude Code runs on every prompt,
  configured in `.claude/settings.json`. Its standard output is added to
  the context of that turn. A walkthrough is the way a list of items is
  worked, one item per message.
- **What it answers**: lines that repeat the one-item walkthrough rule
  with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject /
  (p)ark`, the pointer to the walkthrough skill, and four lines of
  conduct: use the forge's scripts, say what a command of one's own does
  and wait for a yes, change nothing that was not agreed, and close
  every decision question with the verdict line.
- **Behaviour**: it reads nothing, writes nothing, takes no arguments
  and is independent of the working directory; the settings invoke it in
  exec form with its own path from `${CLAUDE_PROJECT_DIR}`.
- **Needs**: Python as `python` on `PATH`. Nothing else.

## hook-git.py

- **What it does**: is the hook that Claude Code runs before every Bash
  command Claude sends. It holds the wall between reading git and
  writing it. The PowerShell tool is closed to git whole by a deny rule.
- **Synopsis**:
  - `python scripts/hook-git.py` (as a hook, JSON on standard input)
  - `python scripts/hook-git.py --test`
  - `echo 'git status' | python scripts/hook-git.py --judge`
- **What it answers**: the command is split at the shell's separators
  and every part that calls git is judged:
  - allow: a reading verb with reading flags.
  - ask: the commands that finish a conflict, so that Claude Code puts
    the command to the principal and runs it on his yes: `add` without
    `--force` and the interactive flags, `rebase --continue` and
    `--abort`, `merge --continue` and `--abort`, `merge <branch>` with
    one name and no flag, and `checkout --ours` or `--theirs` on a file.
  - deny: everything else, naming the script of the forge to use where
    one exists. Denied are writing verbs, an unknown verb (an alias
    among them), a reading verb with a writing flag, a global option
    that changes how git runs, git inside another command, and a part
    the script cannot read.
  The overall answer is deny where any part is refused, ask where none
  is refused and one asks, allow where every part reads, and nothing
  otherwise. A part that is not git is left to Claude Code.
- **Options**:
  - `--test`: runs the built-in cases; exit 1 on a failure.
  - `--judge`: reads one command from standard input and prints the
    verdict.
- **Reach**: it reads no file and writes nothing. It is for Claude's
  tools alone; the principal's own git from the shell is his.
- **Needs**: Python as `python` on `PATH`. Nothing else.

## docs-state.py

- **What it does**: computes the state of every page of the
  documentation from the content of its inputs and prepares the writers'
  tasks. It is the first script of the run of `/document`. See
  [Generate the documentation](../use/generate-the-documentation.md).
- **Synopsis**:
  - `python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]`
  - `python scripts/docs-state.py <map> --previous <path>`
- **State**: for every entry, it hashes the entry's text (its `state`
  line excepted) with the content of every input the entry names, a file
  whole or the part named after `#`. The generator is hashed with them:
  the writer's definition and the documentation contract, with their
  whitespace normalised, so that a change of a sentence regenerates
  every page and a re-wrap regenerates nothing. The hash is compared
  with the page's `inputs-hash`, and the entry's `state` is set in the
  map:
  - `new`: no page at the path.
  - `regenerate`: a page exists and its hash differs.
  - `keep`: a page exists with the same hash.
  A page that no entry names, and the page of an entry marked `remove`,
  are listed as `remove`; the index `README.md` is excepted.
- **Tasks**: for every `new` or `regenerate` entry one task file is
  written to `<tmp-dir>`: the engine root, the page's path, the date,
  the version, the hash the page is to carry, the entry verbatim and the
  titles of the pages it links to.
- **Form `--previous <path>`**: prints the map as last committed, for the
  planner.
- **Missing input**: an input the map names and the disk does not have
  is reported and hashed as missing.
- **Needs**: Python; `docs_map.py` beside it. It rewrites only the
  `- state:` line of each entry.

## docs-index.py

- **What it does**: derives the documentation index, `README.md` of the
  documentation directory, from the documentation map. One line per
  page, grouped by section in the order start, use, about, extend,
  reference, each the page's title linked to its path and the entry's
  `line`; before the sections, the reader paths of the map. It is
  deterministic and uses no model. Run by `/document` after the pages
  are written. See
  [Generate the documentation](../use/generate-the-documentation.md).
- **Synopsis**: `python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]`
- **Needs**: Python; `docs_map.py` beside it.

## docs-check.py

- **What it does**: checks the generated pages mechanically and prints
  every failure with its file and line. It mends nothing; a page that
  fails is regenerated.
- **Synopsis**:
  - `python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]`
  - `python scripts/docs-check.py --file <path> [--fact PATTERN ...]`
- **Checks of the first form**:
  - every entry of the map not in state `remove` has its page, and no
    page lies in the directory that the map does not name;
  - every relative link to a `.md` file resolves;
  - no long dash in the prose of a page; code spans and fenced blocks
    are exempt;
  - every page opens with a front-matter;
  - no instance fact: the values of `CLAUDE.local.md` (every word of
    four letters or more, looked for outside URLs), any e-mail address
    but a placeholder at `example.*`, any absolute path of a machine,
    and every `--fact` pattern.
- **Form `--file <path>`**: scans one file for instance facts only: the
  values of `CLAUDE.local.md`, an absolute path of a machine and the
  `--fact` patterns. No map, no link, no dash and no e-mail rule. This
  is the scan that `/render` runs on a render it has just written. See
  [Render an output](../use/render-an-output.md).
- **Exit codes**: 0 when everything holds, 1 when anything fails.
- **Needs**: Python; `docs_map.py` beside it.

## Shared modules

None of these is a command.

- `forge_repos.py`: what the git scripts share: the engine root, the git
  check, the list of repositories to visit, running git, the state of a
  repository against its origin, the files of the global git
  configuration as git reads them, the registration of the merge driver
  `ours`, and coloured output.
- `forge_tools.py`: what the conversion scripts share: finding an
  external tool on `PATH`, resolving paths, running a tool, the headless
  Claude Code run, and the console set to UTF-8. Its docstring owns the
  text of what pandoc and the `claude` engine need installed.
- `forge_docs.py`: what the scripts that read a project's documents
  share: front-matter, history records, ledger tables, resource index
  entries and threads. Used by `forge-ledger.py`, `forge-migrate.py` and
  `forge-history.py`. A reader never raises on a malformed file; it
  lists what it could not read.
- `docs_map.py`: the one reader of the documentation map, shared by
  `docs-state.py`, `docs-index.py` and `docs-check.py`; it also reads a
  part of a file named after `#`.
- `forge_check.py`: what the mechanical checks of `forge-check.py`
  share: a finding and its report in the shape of the check contract,
  the front-matter keys and comments a template owns, and the kinds of
  the versioned documents.

## Portability

The scripts are the only platform-bound layer of the forge, and each is
written to run unchanged on Linux and macOS. They run as `python
scripts/<name>.py` on Python 3.8 or newer, with `python` on `PATH` as
the one prerequisite (a system that has only `python3` gives it that
name), paths composed with `pathlib` and external tools resolved from
`PATH`.

- Run on Linux: the git scripts, the ledger script and `docs-state.py`.
- A writing rule until a run says otherwise: the conversions and the two
  hooks.
- Run on macOS: nothing. For macOS the whole set is the writing rule
  alone.

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

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
