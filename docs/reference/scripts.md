---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a3a2180a8f4e1e11
inputs:
  - scripts/forge-save.py
  - scripts/forge-pull.py
  - scripts/forge-status.py
  - scripts/forge-clone.py
  - scripts/forge-branch.py
  - scripts/forge-config.py
  - scripts/forge-history.py
  - scripts/forge-report.py
  - scripts/forge-record.py
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
  - CLAUDE.md#Portability
  - projects/forge/10-intent.md#POS.0830
---

# Scripts

This page lists every script in `scripts/` with its synopsis,
options, forms and what it needs installed. It is for the user who
runs a script and for the extender who changes or adds one. Each
script carries the same help in its own docstring. Where a script
needs a tool, it resolves the tool from `PATH` and installs nothing
(see [Install what the forge needs](../start/install.md)).

Three rules hold for the whole set:

- Every script that takes a project takes it by its slug or by the
  path of its directory. A bare word is a slug, anything with a
  separator or an absolute path is a path.
- In the git scripts the word `forge` names the whole: the engine and
  the forge's own project where it is cloned beside it.
- Run each script as `python scripts/<name>.py`.

Terms used below: the principal is the person whose thinking is
being forged. The ledger is the file that records a project's state,
made at read time. The instance file is `CLAUDE.local.md` at the
engine root, which holds facts of one installation. Every other term
of the forge is in the [Glossary](glossary.md).

## Overview

| Script | What it is for | What it needs |
|---|---|---|
| `forge-save.py` | Commit and push the engine and the projects | Python 3.8+, git |
| `forge-pull.py` | Fast-forward the engine and the projects from their origins | Python 3.8+, git |
| `forge-status.py` | Report the git state, read-only | Python 3.8+, git; `gh` for the `github:` line |
| `forge-clone.py` | Clone an existing project into `projects/` | Python 3.8+, git |
| `forge-branch.py` | Switch a repository to a branch, or report the branch | Python 3.8+, git |
| `forge-config.py` | Read and write the global git configuration the forge needs | Python 3.8+, git 2.36+ |
| `forge-history.py` | Print the history of one item as a timeline | Python 3.8+ |
| `forge-report.py` | Complete the unique name of a reviewer's report | Python 3.8+ |
| `forge-record.py` | Append one history record or one decision | Python 3.8+ |
| `forge-ledger.py` | Make a project's ledger from its documents | Python 3.8+, git |
| `forge-migrate.py` | Bring a project to the current shape | Python 3.8+, git |
| `forge-check.py` | Run the mechanical clauses of the light check | Python 3.8+, git |
| `forge-engine.py` | Run one packet on a model of another family | Python 3.8+, the engine's CLI |
| `forge-cite.py` | Verify the URLs of a research note | Python 3.8+ |
| `doc2md.py` | Convert documents to Markdown | Python 3.8+, markitdown |
| `md2pptx.py` | Make a PowerPoint deck from a Markdown deck | Python 3.8+, pandoc or the `claude` CLI |
| `md2docx.py` | Make a Word document from a Markdown render | Python 3.8+, pandoc or the `claude` CLI |
| `md2video.py` | Make a video or a player file from a screenplay render | Python 3.8+; Pillow and ffmpeg for video |
| `hook-walkthrough.py` | Per-prompt hook that repeats the walkthrough rule | Python 3.8+ |
| `hook-git.py` | Hook that judges every git command Claude sends | Python 3.8+ |
| `docs-state.py` | Compute the state of each documentation page and prepare tasks | Python 3.8+ |
| `docs-index.py` | Derive the documentation index from the documentation map | Python 3.8+ |
| `docs-check.py` | Check the generated documentation mechanically | Python 3.8+ |

The five shared modules are not commands:

| Module | What it holds |
|---|---|
| `forge_repos.py` | What the git scripts share |
| `forge_tools.py` | What the conversion scripts share |
| `forge_docs.py` | What the scripts that read a project's documents share |
| `docs_map.py` | The one reader of the documentation map |
| `forge_check.py` | What the mechanical checks share |

## The git scripts

### forge-save.py

Saves the engine and the projects to git: commit, then push.

Synopsis:

    python scripts/forge-save.py [slug | path] [-m MESSAGE] [--tag NAME]

Forms:

- Without arguments it visits the engine and every project that is a
  repository of its own, and gives each one with changes its own
  commit.
- With a slug or a path it saves that repository only. `forge` saves
  the engine and the forge's own project as two commits, each
  prefixed `forge:`.
- A project directory without a repository is skipped with a note
  (bare form) or refused (slug form). A directory the engine tracks is
  the engine's and is passed over.

Per repository it stages everything, commits (the message from `-m`,
or a generated one) and, where an origin is configured, pushes.

- The remote changes are integrated by rebase only where the histories
  diverged. A branch that is merely ahead is pushed as it stands, so a
  merge made by hand keeps its merge commit.
- A clean repository that is ahead of its upstream is pushed the same
  way. A branch with no upstream yet reaches the remote with its first
  commit.
- A rebase that conflicts is left standing, with the commit made and
  nothing lost. The script prints the files in conflict and the step
  that follows (see [Settle a conflict](../use/settle-a-conflict.md)),
  then this script again pushes the clean repository.
- A repository with a rebase or a merge already in progress is refused
  before anything is staged, so that conflict markers are never
  committed.
- Without an origin the commit is kept locally and reported.

Option `--tag <name>` needs one repository, so a slug is required. The
commit is tagged and the tag is pushed with it. When there is nothing
to commit, the current HEAD is tagged. With `forge` the tag goes on
the engine and on the project beside it, under the same name. An
existing tag is refused.

The script never sets an identity or a remote and never initialises a
repository. It never uses `git add -f` and never `git clean`.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` beside it.

### forge-pull.py

Pulls the latest state from the remotes: the engine, which is its
upgrade channel, and every project that has an origin.

Synopsis:

    python scripts/forge-pull.py [slug | path]

Forms:

- Without arguments it pulls the engine, then every project with an
  origin.
- With a slug or a path it pulls that repository. `forge` means the
  engine and the forge's own project beside it.

It is a fast-forward only and never merges.

- A repository with unsaved changes is reported and skipped (bare) or
  refused (slug), so a pull never creates a conflict in half-finished
  work.
- A project without a repository or without an origin is reported and
  skipped.
- A repository whose history diverged from its origin is refused and
  nothing is pulled. What to do then is offered by `/pull`.

After a pull it prints where the repository moved from and to (hash
and subject, before and after) and the subjects of the commits
between, so the releases crossed can be read off and their Action
required lines looked up in `RELEASE-NOTES.md`.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` beside it.

### forge-status.py

Reports the git state of the engine and every project. It is
read-only and changes nothing.

Synopsis:

    python scripts/forge-status.py [slug | path] [--remote]

It prints first the global git configuration file git actually reads
and the registration of the merge driver `ours` in it: `ok`, or the
keys that are missing (the required keys of `forge-config.py
--register`). `/setup` needs to know the file.

Then, for the engine and each project, or for one repository by slug
or path (`forge` means the engine and the forge's own project):

- unsaved changes, or `clean`
- a rebase or merge in progress, with the number of files in conflict
- the branch and the last commit
- the origin, or `no origin`, or `not under git`
- a `user.name` or `user.email` set in the repository itself, reported
  as a fact: it wins over the per-host identity and the forge never
  sets it

Option `--remote` fetches each origin and reports the branch against
it: `up to date`, `behind N`, `ahead N` or `diverged (ahead N, behind
M)`. The fetch changes nothing in the working tree. Without the flag
the script touches no network. With `--remote` it also reads, through
`gh`, what waits on GitHub outside git: a `github:` line under the
`remote:` line with the open pull requests and the discussions nobody
of the repository has answered, one line each. Whatever keeps it from
reading (no `gh`, an origin that is not GitHub, no login, no network)
is one line saying so, and the script goes on.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` beside it. `gh` on
`PATH` and logged in for the `github:` line.

### forge-clone.py

Brings an existing project into the forge by cloning its repository
into `projects/`.

Synopsis:

    python scripts/forge-clone.py <url>

The directory is `projects/<repository name>`, taken from the URL. An
existing directory is never overwritten. The script sets no identity
and carries no identity and no URL.

Afterwards it reports facts:

- the origin and the last commit
- the commit identity git resolves for the fresh clone; where git
  resolves none, it prints the hint to run `/setup`, to run
  `forge-config.py --identity <host> <name> <email>`, or to set a
  local one, and says that `forge-save.py` commits nothing until then
- the project file: its kind and language, or what a project without
  the file is. A project with neither file nor ledger was not
  scaffolded by the forge, a fact and not a defect.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` beside it.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or
reports which branch it is on.

Synopsis:

    python scripts/forge-branch.py <slug | path> [branch]

Forms:

- With a branch name it switches the repository to that branch,
  creating it from the current state when it does not exist. `main`
  switches back.
- Without a name it reports the current branch and lists the branches
  the repository has.

There is no bare form. `forge` names the engine and the forge's own
project, and switches both together. Unsaved changes stop the switch:
save first with `forge-save.py`.

Merging, deleting and pushing branches stay with git. A new branch
reaches the remote by the first save made on it. A release is made
from `main` only.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` beside it.

### forge-config.py

Reads and writes the global git configuration the forge needs, through
`git config --global` alone, so it lands in the file git itself reads.
The forge names no path to that file.

Synopsis:

    python scripts/forge-config.py
    python scripts/forge-config.py --register [--zdiff3]
    python scripts/forge-config.py --guard [--unset-identity]
    python scripts/forge-config.py --identity <host> <name> <email> [--replace]

Forms:

- Bare: reports what is there (the file git reads, the registration of
  the merge driver `ours`, the guard, a global identity and the
  per-host identity stanzas). It changes nothing.
- `--register`: writes the merge driver `ours` and the settings it
  needs, once per place: `merge.ours.driver true`,
  `merge.renormalize true`, `rebase.backend merge` and
  `rerere.enabled true`. With `--zdiff3` it adds
  `merge.conflictStyle zdiff3`.
- `--guard`: writes `user.useConfigOnly true`. It bites only once no
  global `user.name` or `user.email` is left; `--unset-identity`
  removes them.
- `--identity <host> <name> <email>`: writes the two `includeIf`
  stanzas of one host (an `https` and a `git@` remote) with a path
  `.gitconfig-<host>` relative to the global file, then that file with
  the name and e-mail where it is missing.

A key that already carries the value asked is reported and left. A key
that carries another value is reported and left as well, never
overwritten, unless `--replace` is given for an identity. `--replace`
rewrites a stanza that carries another path, an absolute one among
them, and an identity file that carries another name or e-mail. Values
are compared as git stores them, so a name differing in a diacritic
differs.

Needs: Python 3.8+, git 2.36 or newer on `PATH` (`hasconfig` in
`includeIf`), `forge_repos.py` and `forge_tools.py` beside it.

## The record scripts

### forge-history.py

Gathers the history of one item of a project by its ID from the
history logs, their archives and the places that cite it, and prints
it as one timeline. It is read-only, changes nothing and involves no
model. It is the script behind `/history` (see
[Read the history of an item](../use/read-the-history-of-an-item.md)).

Synopsis:

    python scripts/forge-history.py <ID> <slug | path> [--full]

The ID is `PREFIX.NNNN`; a short form such as `pos580` is read as
`POS.0580`. It prints three parts:

- Today: the file that holds the item and its wording.
- Timeline: one line per event, oldest first, with version, date where
  the log has one, and what happened (`born`, `changed`, `closed`,
  `removed`, `approved`, `mentioned by <ID>`, `archive`). A record's
  reason follows its line; its Action and its Was follow as marked
  lines. Was is shortened to its first sentences unless `--full` is
  given.
- Cited today: every other place in the project that names the ID, as
  file and line, shortened.

An ID with no item and no record is said so. The pages of `docs/`, the
map, the renders, the resources and `tmp/` are never searched.

Needs: Python 3.8+, `forge_repos.py` and `docs_map.py` beside it.

### forge-report.py

Completes the unique name of a reviewer's report: it appends the time
to the minute and four hex characters of a content hash to the name
the report was filed under, in place. It involves no model and no git.
The commands that file a report (`/critique`, `/challenge`, `/check`)
call it with the file's path.

Synopsis:

    python scripts/forge-report.py <path>

It renames `YYYY-MM-DD-<kind>-<name>.md` to
`YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md` and prints the new path. It
refuses, exit 1, with the reason printed:

- a path that is not a file
- a name that already carries the tail `-HHMM-<hash>`
- a name that ends in a run number (`-2.md`)
- a file that is not Markdown
- a target name that exists

Needs: Python 3.8+.

### forge-record.py

Appends one record to a history companion, or one decision to a
project's `decisions.md`, at the end of the file and nowhere else. It
involves no model and no git. A record is appended by this script and
never by an edit (see
[Versioning and history](../about/versioning-and-history.md)).

Synopsis:

    python scripts/forge-record.py history <project> <document>
        --subject <subject> --kind <kind> [--reason <text>]
        [--action <text>] [--was <text>] [--instance <path>] [--dry-run]
    python scripts/forge-record.py decision <project>
        --title <line> --decision <text> --reason <text>
        [--verdict "<ID> rejected"]... [--instance <path>] [--dry-run]

Forms:

- `history`: takes the versioned document by its path inside the
  project and writes to its companion `<file>.history.md`, which must
  exist. The record is one line: date, version, author, subject, kind,
  reason, `Action:` and `Was:`. The date is today, the version is the
  one the document's header carries now.
- `decision`: writes the next decision of the project's sequence, ten
  above the highest, in the shape of the decisions template, with the
  Decision and the Reason wrapped at 72 columns.

The author is read from the instance file, the `**Author:**` line of
`CLAUDE.local.md` at the engine root, or from the file `--instance`
names. Where it gives none, the script refuses and names `/setup`.

It refuses, exit 1, with the reason printed and the file untouched:

- a project, a document or a companion that does not exist
- a kind outside `created`, `changed`, `closed`, `removed`, `approved`
- a record other than `created` without a reason
- a line break in any field
- ` | `, `Action: ` or `Was: ` inside the subject, the kind, the reason
  or the action (`Was` comes last and may carry them; its paragraphs
  are divided by `<br>`)

The line endings of the file are kept, and a file that does not end in
a line break gets one first. After the write the script reads the last
record back and refuses if it is not the one it wrote. `--dry-run`
prints what would be written and writes nothing.

Needs: Python 3.8+, `forge_docs.py`, `forge_repos.py` and
`forge_tools.py` beside it.

### forge-ledger.py

Makes the ledger of a project at read time from its documents. It
reads the project file, the artefacts' headers, the histories, the
decisions, the resource indexes, the reviews and the challenges, the
provenance of the renders and of the documentation index, the
published companions, the work specifications, the threads and
`ledger.archive.md`, and builds `ledger.md` in the shape of the ledger
template.

Synopsis:

    python scripts/forge-ledger.py <slug | path> [--out PATH]

An unparsable file becomes a line `unparsed: <file>:<line>` in the
header and never a crash. The exit code is 0.

Where the output lands:

- It writes `ledger.md` only on a project of the current shape whose
  ledger is out of git's index.
- On a project of the shape before the migration, or where the ledger
  is tracked, the hand-kept `ledger.md` is never written. The script
  prints to stdout, or to the path `--out` names. A dry run of a real
  project goes to `tmp/`.

The slug `forge` is the engine's own project.

Needs: Python 3.8+, git on `PATH`, `forge_docs.py`, `forge_repos.py`
and `forge_tools.py` beside it, and `templates/ledger.md`.

### forge-migrate.py

Brings one project, or a library, to the shape the current release
expects: the project file, headers without fields that change with a
round, the state in records, threads as files, the attributes file and
the ledger out of git. See [Migrate a project](../use/migrate-a-project.md).

Synopsis:

    python scripts/forge-migrate.py <slug | path>            # dry run
    python scripts/forge-migrate.py <slug | path> --apply    # perform
    python scripts/forge-migrate.py <slug | path> --undo     # take back
    python scripts/forge-migrate.py <slug | path> --comments [--apply]

The shape of a project is a set of marks, one per step, never an
engine version. The marks are:

- the project file exists
- no header of an artefact, a specification, a recipe, an index or the
  documentation map carries a field that changes with a round
- `threads/` exists, or the project has no threads file
- `.gitattributes` exists
- `ledger.md` is out of git's index

Forms:

- The dry run, the default, prints the marks and, for every step still
  missing, what it would change.
- `--apply` runs the missing steps, each verifying its own mark
  afterwards. A library takes the headers, the project file, the
  records and the attributes.
- `--undo` takes back the last `--apply` from the script's own
  manifest, `tmp/forge-migrate-<slug>.json` at the engine root:
  changed and deleted tracked files are restored from the index,
  created files removed, the ledger put back into the index and the
  `.gitignore` line taken out.
- `--comments` is a step of its own, with no mark and never a
  condition of a write, run on the owner's word. In every file made
  from a template that is not immutable, the skeleton's comment is
  replaced by the line that names the skeleton,
  `<!-- Shape: templates/<name>.md -->`. A file without the comment
  gets the line where the skeleton has it. Closed threads, archives,
  research and sources are not read. A recipe whose genre the file
  does not tell is printed and left. It is dry without `--apply`, and
  with it the refusals and the manifest of `--apply` hold.

What the steps do: the hand-kept ledger is copied as it stands to
`ledger.archive.md`, `ledger.md` is taken out of the index (nothing is
deleted) and put into the project's `.gitignore`. Threads are cut into
`threads/THR.NNNN.md`. Where the script guesses (a thread's origin) or
cannot place a line (a Waiting line without an ID), it prints it for
the principal.

The author of every record it writes is the handle of the instance
file; without it the script refuses.

`--apply` refuses, where the project is a repository of its own:

- a working tree with unsaved changes to tracked files (an untracked
  file is no risk)
- a branch behind or diverged from its origin
- any branch but `main`

A project outside git gets none of these refusals. The forge runs no
git on it, the way back is the backup its user takes before `--apply`,
and `--undo` refuses there. A run that stops midway is finished by
running it again, the marks being the memory. The script commits
nothing; `/save` follows. The slug `forge` is the forge's own project.

Needs: Python 3.8+, git on `PATH`, `forge_repos.py` and
`forge_tools.py` beside it, and the templates `project.md`,
`thread.md` and `gitattributes`.

### forge-check.py

Runs the mechanical clauses of a check as a program instead of a
model: what the files fully determine, verified by reading them.
Today it runs the light check.

Synopsis:

    python scripts/forge-check.py light <slug | path> [--out PATH]

`light <slug>` runs the clauses of the light check's Lens that are a
comparison of files, on one project. It reads only and the exit code
is always 0; the report is the result. The report is in the shape of
the check contract: the verdict line, then the findings ranked by
severity, each with Where (file and line, relative to the project),
the rule with its owner and one fix, marked `immediate fix:` where it
is pure bookkeeping. No ID is given, because the `/check` procedure
numbers and files a report. A closing section, Left to reading, names
the clauses of the Lens the script does not verify. The report goes to
stdout, or to the path `--out` names.

Needs: Python 3.8+, git on `PATH`, `forge_check.py`, `forge_docs.py`,
`forge_repos.py`, `forge_tools.py` and `forge-ledger.py` beside it, and
`templates/`.

## The research scripts

### forge-engine.py

Runs one packet on a model of another family and brings its answer
back as a note. It is the one adapter of the forge to such a model's
command-line tool: one script and one table of engines. The login is
the user's, made once outside the forge in the engine's own tool, and
the forge carries no key, account or configuration. See
[Research a topic](../use/research-a-topic.md) and, for a new row of
the table, [Add an engine](../extend/add-an-engine.md).

Synopsis:

    python scripts/forge-engine.py <engine> --packet <dir> --out <file>
        [--model <word>] [--effort low|medium|high|xhigh|max]
        [--timeout <seconds>] [--schema <file.json>] [--allow-all]
        [--sandbox] [--no-profile] [--prompt <text>]

The engine table has one row today, `antigravity`, whose tool is
`agy`. A new engine is a row in the table and its pair in `COMMANDS`
(a function that builds the command and a function that reads the
envelope). Other rows are to be added when wanted.

What a run does, in order:

1. It finds the engine's tool on `PATH` and checks its version against
   the floor where a bug is known (for `agy`, 1.1.1). It refuses below
   the floor.
2. It reads the packet folder, which must hold `packet.md`, the whole
   context of the run. The engine gets that folder as its workspace
   and runs in it, under the project's `tmp/`, never in the forge
   root.
3. It gives the engine a per-run profile, kept in the run folder as its
   record: a copy of the user's settings with permissions added. These
   allow `read_url(*)` and deny `command(*)`, `write_file(*)` and
   `read_file(<path>)` for every entry of the engine root but `tmp/`
   and for the folder `hold/` of the run. The engine starts with
   `HOME` and `USERPROFILE` pointing at that profile. The user's
   global settings are not touched. `--no-profile` runs without it, for
   a trial of the engine alone.
4. It records a fingerprint of every file in the packet folder (the
   envelopes and logs of earlier runs left out), runs the engine once,
   non-interactively, with stdin closed, its JSON envelope asked for
   and a time limit set, and compares the folder afterwards. A run
   that changed or added anything in it is refused and nothing is
   filed: the read-only folder is verified, never trusted.
5. It reads the envelope. `status` must say success and `response`
   must be non-empty; exit 0 with an empty answer is a failure. The
   envelope is saved beside the packet as `envelope.json`, and the run
   folder is kept, never cleaned.
6. It writes the answer to `--out` as a note: the engine's text with
   `engine`, `model` (as the envelope or the `--model` word says, else
   `engine default`), `usage`, `run` and `status: immutable` in its
   front-matter, or a front-matter made when the answer has none. The
   caller files, indexes and remakes the ledger.

Flags:

| Flag | Meaning |
|---|---|
| `--model` | The model word passed to the engine and recorded in the note |
| `--effort` | The effort level, `low`, `medium`, `high`, `xhigh` or `max` |
| `--timeout` | Seconds for the run, default 1800; passed to the engine where it has a flag, and enforced by the script a minute later |
| `--schema` | A JSON schema file the engine must shape its final answer by; off by default |
| `--allow-all` | Passes the engine's "approve every tool call" flag, needed when its web tools would otherwise wait for a permission nobody can give in a headless run |
| `--sandbox` | Passes the engine's sandbox flag where it has one |
| `--no-profile` | Runs under the user's own settings, with no per-run profile; a trial, never a research |
| `--prompt` | The one sentence the engine is started with; by default it reads `packet.md` in the workspace and does exactly what it says |

Exit codes: 0 when the note is written. 1 for a refusal, with the
reason on stderr: tool missing, version below the floor, packet
without `packet.md`, the folder changed by the run, the envelope
unreadable or the answer empty. The engine's own non-zero exit is
reported with its stderr.

Needs: Python 3.8+, the engine's tool on `PATH` (`agy` for
`antigravity`), `forge_tools.py` beside it.

### forge-cite.py

Verifies the citations of a research note before it is filed. Every
URL in the note is opened and its state reported, and an arXiv
abstract page is read for its title, which must match the words the
note gives the source. See
[Research a topic](../use/research-a-topic.md).

Synopsis:

    python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20]
        [--out <report.md>]
    python scripts/forge-cite.py --independence <bundle-dir>

It reads the note, or every `*.md` of a bundle directory, collects
every http(s) URL with its line, opens each once (GET, a browser-like
User-Agent, redirects followed) and classifies it in one of four
states:

| State | Meaning |
|---|---|
| `ok` | 2xx |
| `dead` | 404 or 410: the page is gone or never existed |
| `unverifiable` | 401, 403, 429, a timeout or a network error: the page refused or did not answer; not wrong, and said so |
| `mismatch` | an arXiv abstract page whose title shares too few words with the note's entry: the ID points to another paper |

It prints one line per URL and a count. `--out` writes the same as a
Markdown report. `--timeout` is the time limit per URL.

Exit codes: 0 when nothing is dead or mismatched, 1 otherwise, 2 on a
usage error.

Form `--independence <bundle-dir>`: for every card of a research
bundle that has a note from more than one engine, it prints the URLs
the notes share and the sentences they have in common, as counts, and
a verdict. A second engine's note that shares most of its sources or a
third of its sentences with the first engine's was written from it,
not from the web. Only sentences over sixty characters are counted. No
network is touched.

The script does not judge content, does not open paywalls and does not
check a quote against its page. A 403 is never counted as a failure.
Nothing is written into the note.

Needs: Python 3.8+ and network access (not for `--independence`);
`forge_tools.py` beside it.

## The conversion scripts

### doc2md.py

Converts Word, PowerPoint, PDF and Excel documents to Markdown.

Synopsis:

    python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
        [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
        [--dry-run] [--list-tools]

Inputs, which can be mixed and repeated: a file name, a glob in
quotes, a list file (plain text, one path or glob per line, `#` or `;`
starts a comment, relative paths are resolved against the list file's
own directory), and a directory with `--recurse`.

Each document becomes `<name>.md` next to it, or in the directory
`-o` names.

- An existing `.md` is skipped unless `--force`.
- `--suffix` inserts text before the extension (`.text` gives
  `report.text.md`).
- A name collision within one run gets `_1`, `_2`.
- `--dry-run` lists what would be converted and writes nothing.
- `--list-tools` checks that markitdown is reachable and exits.

Formats handled: `.pdf`, `.docx`, `.docm`, `.pptx`, `.pptm`, `.xlsx`,
`.xlsm`, `.xls`, `.epub`, `.html`, `.htm`, `.csv`, `.json`, `.xml`,
`.msg`. The legacy binary `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and
`.ods` are reported as unsupported and are to be resaved as `.docx`,
`.pptx` or `.xlsx` first.

Needs: Python 3.8+ and markitdown, resolved from `PATH` or named by
`--markitdown-path`. The script installs nothing. Install it with
`pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

Synopsis:

    python scripts/md2pptx.py <definition.md> [--engine pandoc|claude]
        [--template <file.potx>] [--recipe <recipe.md>] [-o <file.pptx>]
        [--model <model>]

Two engines, chosen by `--engine`:

- `claude` (the default): a model converts the definition, through
  headless Claude Code with the official pptx skill. The recipe may
  carry instructions for the model. It is expensive and never the same
  twice. It is the engine of `/publish`.
- `pandoc`: deterministic, one slide per second-level heading, nothing
  interpreted by a model. It is cheap and a deck for reading, not for
  showing. It is the engine of `/render`.

`--template` names a `.potx` or `.pptx` by path. Without it, the
`claude` engine designs the style itself and `pandoc` uses its
built-in one. `--recipe` names the recipe the definition was rendered
from; the `claude` engine reads its Format section. `--model` applies
to the `claude` engine only. The output lands next to the input with
the same basename unless `-o` names a path.

Needs: Python 3.8+, `forge_tools.py` beside it. The `pandoc` engine
needs pandoc on `PATH`; the `claude` engine needs the `claude` CLI and
the official pptx skill. The script installs nothing; `forge_tools.py`
says how each is installed.

### md2docx.py

Converts a Markdown render into a Word document.

Synopsis:

    python scripts/md2docx.py <render.md> [--engine pandoc|claude]
        [--reference <styles.docx>] [--page-size A4|Letter]
        [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]

Two engines, chosen by `--engine`:

- `pandoc` (the default): deterministic, nothing interpreted by a
  model, cheap. It is the engine of `/render`.
- `claude`: a model converts it, through headless Claude Code with the
  official docx skill, the recipe's Format section giving the model
  its instructions (`--recipe`). It is expensive and never the same
  twice. It is the engine of `/publish`.

For the `pandoc` engine:

- A YAML front-matter block at the top of the render is read as
  metadata and does not appear in the document.
- Mermaid diagrams are not rendered; they land as blocks of code.
- `--reference` names a `.docx`, or a Word template `.dotx` or
  `.dotm`. pandoc takes its styles and ignores its content.
- The page is A4 by default. `--page-size A4|Letter` sets it without
  `--reference`; with `--reference` the document's own page setup
  holds and `--page-size` is not applied.

The `claude` engine takes the reference document as the template it
starts from, and A4 where none is given. The output lands next to the
input with the same basename unless `-o` names a path.

Needs: Python 3.8+, `forge_tools.py` beside it. The `pandoc` engine
needs pandoc on `PATH`; the `claude` engine needs the `claude` CLI and
the official docx skill. The script installs nothing.

### md2video.py

Makes the format file of a screenplay render: a video, or the timed
events its player plays in the browser. See
[Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

Synopsis:

    python scripts/md2video.py <render.md> --format video|html-player
        [--pace 4,8,16] [--date "28. 9. 2026"] [--section <name>]
        [--name <name>] [-o <file>] [--frame <seconds> <file.png>]

It reads a screenplay render (its front-matter language, a title card,
a card of what the viewer will see, scenes with a time of day, each
with a caption of two parts, Now and Why, and a fenced block of what
the terminal shows, and an end card), computes the timeline from the
pace, and writes one of two formats:

- `video`: every frame painted with Pillow as a simulated terminal
  (1280x890) and piped into ffmpeg (H.264, 30 fps). It is
  deterministic: the same file from the same render every time.
- `html-player`: the timeline as JSON of events, wrapped as a script
  (`forgeVideo({...})` in `<name>.html-player.js`) so the player page
  can load it from a file on disk as well as from GitHub Pages.

Options:

- `--pace`: three reading rates in words a second, for the
  principal's lines, Claude's answers, and the lines that only report
  a file. The default is `4,8,16`.
- `--date`: the date shown in the tab bar.
- `--section`: the section of the course the video belongs to on the
  player page.
- `--name`: the name the list shows, in place of the title card's
  title. Both go into the player file's data. The page groups the
  videos by section, sections and videos alike in the order of the file
  names. A file without them is listed under its title, after the
  sections.
- `-o`: the output path.
- `--frame <seconds> <file.png>`: paints one frame of the video at the
  given second to a PNG and stops, a check of the look without the
  whole render.

The pace, the date and the look come from the recipe's Format section
as arguments; the render carries none of it.

The output lands next to the input with the render's basename
(`<name>.mp4` or `<name>.html-player.js`) unless `-o` names a path.
Where the output lands under the engine's `docs/videos/`, the player
page `docs/videos/index.html` is written anew from
`templates/html-player.html`, with the folder's files listed and
loaded.

Needs: Python 3.8+, `forge_tools.py` beside it. For `video`: Pillow
(`pip install pillow`) and ffmpeg on `PATH`. Fonts are taken from the
system where they exist, and Pillow's built-in font otherwise. The
script installs nothing.

## The hooks

### hook-walkthrough.py

The hook that runs on every prompt of the principal. Claude Code runs
it (configured in `.claude/settings.json`) and adds its standard
output to the context of that turn.

It prints the one-item walkthrough rule with its verdict line, the
pointer to the walkthrough skill, and lines of conduct: use the
forge's scripts, run the forge's skill at once where one covers what is
asked, explain and ask before running a command of one's own, change
nothing that was not agreed and approved, and close every question
that asks the principal to decide with the verdict line.

It reads nothing, writes nothing, takes no arguments and is
independent of the working directory: `.claude/settings.json` invokes
it in exec form with its own path.

Needs: Python 3.8+ on `PATH` as `python`. Nothing else.

### hook-git.py

The hook that runs before every Bash command Claude sends, the wall
between reading git and writing it. It reads the command from the
hook's JSON on stdin, splits it at the shell's separators and judges
every part that calls git:

- A reading verb with reading flags (`status`, `log`, `diff`, `show`,
  `fetch` and the like): allow.
- The commands that finish a conflict, named one by one (`add`
  without `--force` and without interactive flags, `rebase --continue`
  and `--abort`, `merge --continue` and `--abort`, `merge <branch>`
  with one name and no flag, and `checkout --ours` or `--theirs` on a
  file): ask, so that Claude Code puts the command to the principal and
  runs it on a yes.
- Everything else: deny, with the script of the forge to use instead
  where one exists. Denied are the writing verbs, a verb the script
  does not know (an alias among them), a reading verb with a writing
  flag, a global option that changes how git runs (`-c`, `--git-dir`,
  `--work-tree`, `--exec-path`), git inside another command (`xargs`,
  `sh -c`, a substitution) and a part the script cannot read.

A part that is not git is left to Claude Code. The hook answers deny
where any part is a git it refuses, ask where none is refused and one
is an asking git, allow where every part is a reading git, and nothing
otherwise. The reason of a deny names the rule and the script to use.

It reads no file and writes nothing. It is for Claude's tools alone;
the principal's own git from the shell is the principal's.

Forms:

    python scripts/hook-git.py            # as a hook: JSON on stdin
    echo 'git status' | python scripts/hook-git.py --judge   # one command, the verdict printed

Its cases, every command with the verdict expected of it, are a test
of the suite.

Needs: Python 3.8+ on `PATH` as `python`. Nothing else.

## The documentation scripts

The three scripts serve the run of `/document` (see
[Generate the documentation](../use/generate-the-documentation.md)).
Each needs Python 3.8+ and `docs_map.py` beside it, and nothing else.

### docs-state.py

Computes the state of every page of the documentation from the content
of its inputs, and prepares the writers' tasks. It runs after the
planner has written the documentation map and before the writers.

Synopsis:

    python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]
    python scripts/docs-state.py <map> --previous <path>

For every entry of the map it hashes the entry's text (its `state`
line excepted) together with the content of every input the entry
names: a whole file, or the part of a file named after `#` (a section
by its heading, an item by its ID), hashed as that part, so that a
change elsewhere in the file leaves the page as it is. The generator
is hashed with the inputs: the writer's definition and the
documentation contract, with their whitespace normalised, so that a
change of the rule regenerates every page and a re-wrap of the rule
regenerates nothing.

The page at the entry's path carries the hash it was made from in its
front-matter, `inputs-hash`. The two are compared and the entry's
`state` is set in the map:

| State | Meaning |
|---|---|
| `new` | no page at the path |
| `regenerate` | a page exists and its hash differs |
| `keep` | a page exists with the same hash |
| `remove` | a page under the docs directory that no entry names, or the page of an entry the planner marked `remove` (the index `README.md` excepted); such an entry keeps its state and gets no task |

For every `new` or `regenerate` entry it writes one task file to
`<tmp-dir>`: the engine root, the page's path, the date, the version
the page is made for, the hash the page is to carry, the entry
verbatim and the titles of the pages it links to. The task is a
writer agent's whole prompt.

The form with `--previous <path>` prints the map as last committed, for
the planner. An input the map names and the disk does not have is
reported and hashed as missing; the page is regenerated and its writer
reports the gap. The script rewrites only the `- state:` line of each
entry and leaves the rest of the map byte for byte.

### docs-index.py

Derives the documentation index from the documentation map, and writes
`<docs-dir>/README.md`.

Synopsis:

    python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]

It writes one line per page, grouped by section in the order start,
use, about, extend, reference, each line the page's title linked to
its relative path and the entry's `line`. Before the sections stand
the reader paths of the map's `## Paths` section, each page a link. It
is deterministic and involves no model. The index is a derivation of
the map and is never edited by hand. The opening paragraph is fixed
text of the script.

### docs-check.py

Checks the generated documentation mechanically.

Synopsis:

    python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]
    python scripts/docs-check.py --file <path> [--fact PATTERN ...]

With a map and a directory it verifies the pages and prints every
failure with its file and line:

- every entry of the map not in state `remove` has its page, and no
  page lies in the directory that the map does not name
- every relative link to a `.md` file resolves
- no long dash in the prose of any page (a code span and a fenced
  block are exempt)
- every page opens with a front-matter
- no instance fact: the values of `CLAUDE.local.md` at the engine root
  (every word of four letters or more in a value, looked for outside
  URLs), any e-mail address but a placeholder at `example.*`, any
  absolute path of a machine, and every `--fact` pattern given

With `--file <path>` in place of a map and a directory, one file is
scanned for instance facts only: the values of `CLAUDE.local.md`, an
absolute path of a machine and the `--fact` patterns. There is no map,
link, dash or e-mail rule. This is the scan that `/render` runs on a
render it has just written (see
[Render an output](../use/render-an-output.md)).

Exit code 0 when everything holds, 1 when anything fails. The check
mends nothing: a page that fails is regenerated by the documentation
command. The script carries no name, address or host of its own; the
instance facts are read from `CLAUDE.local.md` at run time.

## The shared modules

None of these is a command.

- `forge_repos.py`: the engine root, the git check, the list of
  repositories to visit, running git, the state of a repository
  against its origin, what waits on GitHub through `gh`, the global
  git configuration files, the registration of the merge driver
  `ours`, and coloured output. The scripts carry no URL and no
  identity.
- `forge_tools.py`: finding an external tool on `PATH`, resolving
  paths, running a tool, the headless Claude Code run, and the console
  set to UTF-8. It is the one place that says what the conversions
  need.
- `forge_docs.py`: the front-matter of a file, the records of a history
  companion, the tables of a hand-kept ledger, the entries of a
  resource index and the threads. A reader here never raises on a
  malformed file; it lists what it could not read.
- `docs_map.py`: the one reader of the documentation map and of the
  inputs it names, a whole file or a part after `#`.
- `forge_check.py`: a finding and its report in the shape of the check
  contract, the front-matter keys a template owns, the line numbers of
  a file and the kinds of the versioned documents.

## Portability

The scripts are the only platform-bound layer and are written to run
unchanged on Linux and macOS: Python 3.8 or newer, run as `python
scripts/<name>.py`, paths composed with `pathlib`, external tools
resolved from `PATH`.

The tests run in CI at every push, on Linux and on Windows (see
[Run the tests](../use/run-the-tests.md)). They include the git
scripts, the ledger, the light check and the git hook's judgement. The
conversions are tested for their failure without the tool alone. The
per-prompt hook is a writing rule until a run says otherwise.

Nothing has run on macOS: for it the whole set is the writing rule
alone.

To write a script of one's own, see
[Add a script](../extend/add-a-script.md).

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
- [Versioning and history](../about/versioning-and-history.md): why a record is appended by a script and never by an edit.
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Add an engine](../extend/add-an-engine.md): adding a row to the engine table.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
