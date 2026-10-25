---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 3b01f5f9fd0ad746
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

This page lists every script in `scripts/` with its synopsis, its
options, what it needs and the command that runs it. It is for the
user who runs a script by hand and for the extender who reads one
before writing another. The scripts are the forge's door to git, to
the ledger, to file conversion and to the documentation: Claude
reaches git writes only through them. In this page the principal is
whoever's thinking is being forged, the ledger is the state report
made from a project's documents, and a harness is the program that
runs Claude and calls its hooks.

Every script is run as `python scripts/<name>.py` and carries its own
help in its module docstring. Installing what the conversions need is
described in [Install what the forge needs](../start/install.md).

## The scripts at a glance

| Script | What it is for | Command that runs it | What it needs |
|---|---|---|---|
| `forge-save.py` | commit and push the engine and the projects | `/save`, `/release` | Python 3.8+, git |
| `forge-pull.py` | fast-forward from the remotes | `/pull` | Python 3.8+, git |
| `forge-status.py` | report the git state, read-only | none named in the inputs | Python 3.8+, git |
| `forge-clone.py` | clone an existing project into `projects/` | `/import-project` | Python 3.8+, git |
| `forge-branch.py` | switch to a branch, creating it, or report it | none named in the inputs | Python 3.8+, git |
| `forge-config.py` | read and write the global git configuration | `/setup` | Python 3.8+, git 2.36+ |
| `forge-history.py` | the history of one item as a timeline | `/history` | Python 3.8+ |
| `forge-report.py` | complete the unique name of a report | `/critique`, `/challenge`, `/check` | Python 3.8+ |
| `forge-ledger.py` | make a project's ledger at read time | remade by every command that changes state | Python 3.8+, git |
| `forge-migrate.py` | bring a project to the current shape | `/migrate` | Python 3.8+, git |
| `forge-check.py` | the mechanical clauses of the light check | none: run by hand | Python 3.8+, git |
| `forge-engine.py` | run one packet on a model of another family | `/research` | Python 3.8+, the engine's CLI |
| `forge-cite.py` | open every URL of a research note | `/research` | Python 3.8+ |
| `doc2md.py` | convert documents to Markdown | `/ingest` | Python 3.8+, markitdown |
| `md2pptx.py` | Markdown deck to PowerPoint | `/render`, `/publish` | Python 3.8+, pandoc or the claude CLI |
| `md2docx.py` | Markdown render to Word | `/render`, `/publish` | Python 3.8+, pandoc or the claude CLI |
| `md2video.py` | screenplay render to video or player events | `/render` | Python 3.8+; Pillow and ffmpeg for video |
| `hook-walkthrough.py` | the per-prompt hook that repeats the conduct rules | called by the harness at every prompt | Python 3.8+ as `python` |
| `hook-git.py` | the hook that separates reading git from writing it | called by the harness before every Bash command | Python 3.8+ as `python` |
| `docs-state.py` | the state of every documentation page and the writers' tasks | `/document` | Python 3.8+ |
| `docs-index.py` | the documentation index, from the map | `/document` | Python 3.8+ |
| `docs-check.py` | the mechanical check of the documentation, and the one-file scan | `/document`, `/render` | Python 3.8+ |

Five modules are shared by the scripts and are not commands. They are
listed at the end of the page.

## Git: save, pull, status, clone, branch, config

These six are the door to git. The engine is one repository and every
project under `projects/` is a repository of its own, which a script
recognises by asking git whether the project's directory is the top
of a repository. A project that is not one is a project outside git,
on which no script runs git.

### forge-save.py

Commits and pushes the engine and every project that has changes.

- **Synopsis:** `python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]`
- **Forms:** without arguments it visits the engine and every
  project repository and gives each one with changes its own commit.
  With a slug it saves that one repository (`forge` means the
  engine). A project directory without a repository is skipped with a
  note when bare and refused when named.
- **Options:** `-m` gives the commit message, otherwise one is
  generated. `--tag NAME` tags the commit and pushes the tag with it;
  it needs a slug. When there is nothing to commit it tags the
  current HEAD. An existing tag is refused.
- **Per repository:** it stages everything, commits, and when an
  origin is configured integrates remote changes by rebase and pushes.
  A clean repository that is ahead of its upstream is pushed the same
  way. A branch with no upstream reaches the remote with its first
  commit. Without an origin the commit stays local and is reported.
- **A conflict is left standing:** when the rebase conflicts, the
  commit is made, nothing is lost, and the script prints the files in
  conflict and the step that follows. The step is described in
  [Settle a conflict](../use/settle-a-conflict.md). Running the script
  again afterwards pushes the clean repository that is ahead.
- **A standing rebase or merge is refused:** a repository with a
  rebase or a merge already in progress is refused before anything is
  staged, so that conflict markers are never committed.
- **It never** sets an identity or a remote, initialises a
  repository, uses `git add -f` or runs `git clean`.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py`.

### forge-pull.py

Fast-forwards the engine (its upgrade channel) and every project that
has an origin.

- **Synopsis:** `python scripts/forge-pull.py [slug]`
- **Forms:** bare pulls the engine, then every project with an
  origin. With a slug it pulls that one repository.
- **Refusals:** a repository with unsaved changes is skipped when
  bare and refused when named. A repository whose history has
  diverged from its origin is refused and nothing is pulled. Projects
  without a repository or an origin are reported and skipped. The
  script never merges.
- **Output:** after a pull it prints where the repository moved from
  and to, with the hash and subject of each end, and the subjects of
  the commits between, so that the releases crossed can be read off
  and their Action required lines looked up in `RELEASE-NOTES.md`.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py`.

### forge-status.py

Reports the git state of the engine and every project. It is
read-only.

- **Synopsis:** `python scripts/forge-status.py [--remote]`
- **First it reports** the global configuration file git actually
  reads and the registration of the merge driver `ours` in it. The
  merge driver is the git setting that lets the derived files merge
  without a conflict. The report says `ok`, or names the missing keys
  (the required keys are those of `forge-config.py --register`).
  Without the registration a clone silently falls back to a conflict
  on the derived files.
- **Then, for the engine and each project:** unsaved changes or
  `clean`; a rebase or a merge in progress with the number of files in
  conflict; the branch; the last commit; the origin, or `no origin`
  or `not under git`. A `user.name` or `user.email` set in the
  repository itself is reported, since it wins over the per-host
  identity and the forge never sets it.
- **With `--remote`** it fetches each origin and reports the branch
  against it: `up to date`, `behind N`, `ahead N` or `diverged (ahead
  N, behind M)`. The fetch changes nothing in the working tree.
  Without the flag the script touches no network.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py`.

### forge-clone.py

Brings an existing project in by cloning its repository into
`projects/`.

- **Synopsis:** `python scripts/forge-clone.py <url>`
- **Where it lands:** `projects/<repository name>`, the name taken
  from the URL. An existing directory is never overwritten.
- **Facts it reports afterwards:**
  - the last commit and the origin;
  - the commit identity git resolves for the fresh clone;
  - the project file, that is its kind and language, or what a
    project without the file is. A project with neither the file nor a
    ledger was not scaffolded by the forge, which is a fact and not a
    defect.
- **The hint:** where git resolves no `user.name` and `user.email` for
  the clone, it prints that `forge-save` commits nothing until then,
  and names the three ways out: `/setup`, `forge-config.py
  --identity <host> <name> <email>`, or a local identity set in the
  repository.
- **It sets** no identity and carries no URL.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py`.

### forge-branch.py

Switches one repository to a branch, creating it if needed, or
reports the branch it is on.

- **Synopsis:** `python scripts/forge-branch.py <slug> [branch]`
- **Forms:** with a branch name it switches, creating the branch from
  the current state when it does not exist (`main` switches back).
  Without a name it reports the current branch and lists the others.
  There is no bare form: the slug is always required (`forge` means
  the engine).
- **Refusal:** unsaved changes stop the switch. Save first, then
  switch.
- **Left to git:** merging, deleting and pushing branches. A new
  branch reaches the remote by the first `forge-save` made on it.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py`.

### forge-config.py

Reads and writes the global git configuration the forge needs, through
`git config --global` alone, so that it lands in the file git itself
reads, wherever that lies.

- **Synopsis:**
  - `python scripts/forge-config.py`
  - `python scripts/forge-config.py --register [--zdiff3]`
  - `python scripts/forge-config.py --guard [--unset-identity]`
  - `python scripts/forge-config.py --identity <host> <name> <email> [--replace]`
- **Bare form:** shows what is there and changes nothing: the file git
  reads, the registration of the merge driver `ours`, the guard, a
  global identity and the per-host identity stanzas.
- **`--register`:** writes `merge.ours.driver true`,
  `merge.renormalize true`, `rebase.backend merge` and
  `rerere.enabled true`. With `--zdiff3` it adds
  `merge.conflictStyle zdiff3`.
- **`--guard`:** writes `user.useConfigOnly true`. It bites only once
  no global `user.name` or `user.email` is left. `--unset-identity`
  removes them.
- **`--identity <host> <name> <email>`:** writes the two
  `includeIf` stanzas of one host (the `https` and the `git@` form of
  the remote URL), each with a path `.gitconfig-<host>` relative to the
  global file, and then that file with the `user` name and e-mail where
  it is missing. A stanza with another path, or an identity file with
  another name or e-mail, is reported and left. `--replace` rewrites
  them.
- **Rule for every key:** a key that already carries the value asked
  is reported and left. A key that carries another value is reported
  and left too, never overwritten, unless `--replace` is given for an
  identity. Values are compared as git stores them.
- **Needs:** Python 3.8 or newer; git 2.36 or newer on PATH (for
  `hasconfig` in `includeIf`); `forge_repos.py` and `forge_tools.py`.

## The record: history, report, ledger, migrate, check

### forge-history.py

Prints the history of one item by its ID, gathered from the history
logs, their archives and the places that cite it. It is read-only, and
no model is involved. The command behind it is described in
[Read the history of an item](../use/read-the-history-of-an-item.md).

- **Synopsis:** `python scripts/forge-history.py <ID> <slug> [--full]`
- **The ID:** `PREFIX.NNNN`; a short form such as `pos580` is read as
  `POS.0580`. `forge` as the slug is the engine's own project.
- **Output, in three parts:**
  - Today: the file that holds the item and its wording;
  - Timeline: one line per event, oldest first (`born`, `changed`,
    `closed`, `removed`, `approved`, `mentioned by <ID>`, `archive`),
    each with its version and date, followed by the reason and the
    Action and Was lines of the record;
  - Cited today: every other place in the project that names the ID,
    as file and line.
- **`--full`:** prints each Was in full instead of its first
  sentences.
- **Not searched:** the pages of `docs/`, the documentation map, the
  renders, the published files, the resources and `tmp/`.
- **Needs:** Python 3.8 or newer; `forge_repos.py` and `docs_map.py`.

### forge-report.py

Completes the unique name of a reviewer's report, in place.

- **Synopsis:** `python scripts/forge-report.py <path>`
- **The name it completes:** the command that files a report writes it
  as `YYYY-MM-DD-<kind>-<name>.md`. The script renames it to
  `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`, where `HHMM` is the local
  time to the minute and `<hash>` the first four hex characters of the
  SHA-256 of the file. It prints the new path.
- **Refusals (exit 1, with the reason printed):** a path that is not a
  file; a name that already carries the tail; a name that ends in a run
  number (`-2.md`); a target name that exists. Wrong usage exits 2.
- **Needs:** Python 3.8 or newer. No model and no git.

### forge-ledger.py

Makes the ledger of a project at read time from its documents.

- **Synopsis:** `python scripts/forge-ledger.py <slug> [--out PATH]`
- **What it writes:** `ledger.md` in the shape of the ledger template,
  its tables made from the project file, the headers of the
  artefacts, the histories, the decisions, the resource indexes, the
  reviews and challenges, the provenance of the renders, the published
  companions, the work specifications, the threads and the archive of
  an older hand-kept ledger. It also holds the rule of what waits on
  the principal and the reports of what the merged files cannot say.
- **Unreadable files:** an unparsable file becomes a line
  `unparsed: <file>:<line>` in the header. The script never crashes
  on it, and the exit code is 0.
- **Where the output lands:** it writes `ledger.md` only on a project
  of the current shape whose ledger is out of git's index. On a
  project of the shape before the migration, and where the ledger is
  tracked, `ledger.md` is the hand-kept one and is never written; the
  script prints to stdout, or to `--out PATH` (a dry run of a real
  project goes to `tmp/`).
- **Slug `forge`:** the engine's own project.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_docs.py`,
  `forge_repos.py` and `forge_tools.py`; the ledger template.

### forge-migrate.py

Brings one project to the current shape of files. The command behind
it is described in [Migrate a project](../use/migrate-a-project.md).

- **Synopsis:**
  - `python scripts/forge-migrate.py <slug>` (dry run)
  - `python scripts/forge-migrate.py <slug> --apply`
  - `python scripts/forge-migrate.py <slug> --undo`
- **The marks:** the shape of a project is a set of marks, one per
  step, and never an engine version written in the project.
  - `A`: no header of an artefact, specification, recipe, index or map
    carries a field that changes with a round.
  - `B0`: the project file exists.
  - `B`: `ledger.md` is out of git's index; what only the ledger knew
    has become records.
  - `C1`: `threads/` exists, or the project has no threads file.
  - `D`: `.gitattributes` exists.
- **Dry run:** the default. It prints the marks and, for every step
  still missing, what it would change.
- **`--apply`:** runs the missing steps in the order A, B0, B, C1, D,
  each verifying its own mark afterwards. A library takes A, B0, B and
  D. It commits nothing; `/save` follows. The author of every record it
  writes is the handle of the instance file; without it the script
  refuses.
- **`--undo`:** takes back the last `--apply` from the script's own
  manifest in `tmp/`: changed and deleted tracked files are restored,
  created files removed, the ledger put back into the index and the
  `.gitignore` line taken out.
- **Refusals of `--apply`,** where the project is a repository of its
  own: a working tree with unsaved changes to tracked files, a branch
  behind or diverged from its origin, and any branch but `main`.
  Untracked files are no risk.
- **A project outside git:** it gets none of these refusals, since no
  git is run on it. The way back is the backup its user takes before
  `--apply`, and `--undo` refuses there. A run that stops midway is
  finished by running it again, the marks being the memory.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_repos.py` and
  `forge_tools.py`; the project, thread and gitattributes templates.

### forge-check.py

Runs the mechanical clauses of the light check as a program instead of
a model.

- **Synopsis:** `python scripts/forge-check.py light <slug> [--out PATH]`
- **What it verifies for one project:**
  - front-matter and history: header keys against the skeleton,
    version and status, the companion beside each document, the shape
    and order of every record;
  - the ledger's own reports, composed in memory (nothing is written);
  - records and companions: the published companions, work files
    against their specification's inputs, the thread files, the
    Verdict words of the decisions;
  - dependencies: every path of the ledger's Dependencies table on
    disk;
  - resource indexes: header, registration of every file, bundles and
    their inner indexes, the fields of each entry.
- **Report:** printed in the shape of the check contract: a verdict
  line, the findings ranked by severity, each with where, the rule
  with its owner and one fix (marked immediate where it is pure
  bookkeeping). No ID is given. A closing section, Left to reading,
  names the clauses of the check that the script does not verify.
- **Run:** by hand, beside the check. No command runs it. It reads
  only, and the exit code is always 0; the report is the result.
- **Needs:** Python 3.8 or newer; git on PATH; `forge_check.py`,
  `forge_docs.py`, `forge_repos.py`, `forge_tools.py` and
  `forge-ledger.py`; the templates.

## Research: engine and citations

Both scripts are run by `/research`, described in
[Research a topic](../use/research-a-topic.md).

### forge-engine.py

Runs one packet on a model of another family and brings its answer
back as a note. It is the forge's adapter to the engine's command-line
tool; the login is the user's, made once outside the forge, and the
forge carries no key, account or configuration.

- **Synopsis:** `python scripts/forge-engine.py <engine> --packet <dir> --out <file>`
  with the flags `[--model <word>] [--effort low|medium|high|xhigh|max]
  [--timeout <seconds>] [--schema <file.json>] [--allow-all]
  [--sandbox] [--no-profile] [--prompt <text>]`.
- **The engine table:** one row per engine in `ENGINES`. The table has
  one row, `antigravity`, whose tool is `agy` with a version floor of
  1.1.1. A new engine is a row in the table and its pair in
  `COMMANDS` (the function that builds its command and the function
  that reads its envelope). Adding one is described in
  [Add an engine](../extend/add-an-engine.md). Further rows
  (codex, claude, copilot) are named in the header as to be added when
  wanted.
- **The packet folder:** it must hold `packet.md`, the whole context of
  the run. The engine is given that folder as its workspace, under the
  project's `tmp/`, and never the forge root.
- **The per-run profile:** the place alone locks nothing, so the script
  gives the engine a profile of its own for the run, in the run folder.
  It is a copy of the user's settings with permissions added: reading
  URLs is allowed; the shell, writing files and reading every entry of
  the engine root but `tmp/` are denied, and so is the folder where
  the first engine's notes wait. The engine is started with its home
  pointing at that profile. The user's global settings are not touched,
  and the profile stays in the run folder as the record.
  `--no-profile` runs without it, as a trial of the engine alone and
  never as a research.
- **The verified read-only folder:** the script records a fingerprint
  of every file in the packet folder, runs the engine once,
  non-interactively with stdin closed, and compares the folder
  afterwards. A run that changed or added anything is refused and
  nothing is filed.
- **The envelope:** the engine's JSON answer. Its `status` must say
  success and its `response` must be non-empty; an exit 0 with an
  empty answer is a failure. The envelope is saved beside the packet
  as `envelope.json`, and the run folder is kept.
- **The note:** the answer is written to `--out` with `engine`,
  `model` (from the envelope, else the `--model` word, else
  "engine default"), `usage`, `run` and `status: immutable` in its
  front-matter. The caller files, indexes and remakes the ledger.
- **Flags:**
  - `--model` and `--effort`: passed to the engine where it has them;
  - `--timeout`: seconds for the run, 1800 by default; passed to the
    engine where it has a flag and enforced by the script a minute
    later;
  - `--schema`: a JSON schema file the engine must shape its final
    answer by; off by default;
  - `--allow-all`: passes the engine's "approve every tool call" flag,
    needed when its web tools would otherwise wait for a permission
    nobody can give in a headless run;
  - `--sandbox`: passes the engine's sandbox flag where it has one;
  - `--no-profile`: see above;
  - `--prompt`: the one sentence the engine is started with; by
    default it reads `packet.md` and does exactly what it says.
- **Exit codes:** 0 when the note is written; 1 for a refusal with the
  reason on stderr (tool missing, version below the floor, a packet
  without `packet.md`, the folder changed by the run, an unreadable
  envelope or an empty answer). The engine's own non-zero exit is
  reported with its stderr.
- **Needs:** Python 3.8 or newer; the engine's tool on PATH (`agy` for
  the one row).

### forge-cite.py

Opens every URL of a research note before the note is filed, and
reports its state.

- **Synopsis:**
  - `python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20] [--out <report.md>]`
  - `python scripts/forge-cite.py --independence <bundle-dir>`
- **The four states of a URL:**
  - `ok`: the answer is 2xx;
  - `dead`: 404 or 410, the page is gone or never existed;
  - `unverifiable`: 401, 403, 429, a timeout or a network error; the
    page refused or did not answer, which is not wrong and is said so;
  - `mismatch`: an arXiv abstract page whose title shares too few words
    with the note's entry, the mark of a fabricated citation.
- **How it works:** it collects every http(s) URL with its line, opens
  each once (GET, redirects followed, a time limit per URL) and prints
  one line per URL and a count.
- **`--out`:** writes the same report as Markdown to the file given;
  the run folder under `tmp/` is the place.
- **`--timeout`:** seconds per URL, 20 in the synopsis.
- **`--independence <bundle-dir>`:** for every card of a research
  bundle with a note from more than one engine, it prints the URLs the
  notes share and the longer sentences (over sixty characters) they
  have in common, as counts, with a verdict. A second engine's note
  that shares most of its sources or a third of its sentences with the
  first engine's was written from it and not from the web. No network
  is touched.
- **Exit codes:** 0 when nothing is dead or mismatched, 1 otherwise,
  2 on a usage error.
- **It does not** judge content, open paywalls, or check a quote
  against its page, and it writes nothing into the note.
- **Needs:** Python 3.8 or newer.

## Conversions

The three conversion scripts share `forge_tools.py`, whose header says
what pandoc and the claude engine need and how each is installed.
Their install steps are described in
[Install what the forge needs](../start/install.md). None of them
installs anything. The job that runs them is described in
[Render an output](../use/render-an-output.md).

### doc2md.py

Converts Word, PowerPoint, PDF and Excel documents to Markdown.

- **Synopsis:** `python scripts/doc2md.py <input> [<input> ...] [-o <dir>]
  [--suffix <text>] [--recurse] [--force] [--as-list]
  [--markitdown-path <exe>] [--dry-run] [--list-tools]`
- **Input forms, mixable and repeatable:** a file name, a glob such as
  `"*.pdf"`, a list file (plain text, one path or glob per line,
  `#` or `;` starting a comment, relative paths read against the list
  file's own directory) and a directory with `--recurse`.
- **Output:** each document becomes `<name>.md` next to it, or in the
  directory `-o` names. An existing `.md` is skipped unless `--force`.
  `--suffix` inserts text before the extension. A name collision
  within one run gets `_1`, `_2`. `--dry-run` lists and writes
  nothing. `--list-tools` checks that markitdown is reachable and
  exits.
- **Handled:** `.pdf`, `.docx`, `.docm`, `.pptx`, `.pptm`, `.xlsx`,
  `.xlsm`, `.xls`, `.epub`, `.html`, `.htm`, `.csv`, `.json`, `.xml`
  and `.msg`. The legacy `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and
  `.ods` are reported as unsupported and are resaved first as
  `.docx`, `.pptx` or `.xlsx`.
- **Needs:** Python 3.8 or newer; markitdown, resolved from PATH or
  named by `--markitdown-path`.

### md2pptx.py

Generates a PowerPoint deck from a Markdown deck definition.

- **Synopsis:** `python scripts/md2pptx.py <definition.md>
  [--engine pandoc|claude] [--template <file.potx>] [--recipe <recipe.md>]
  [-o <file.pptx>] [--model <model>]`
- **The two engines:**
  - `claude` (the default): a model converts the free-form definition,
    following the instructions of the recipe's Format section.
    Expensive and never the same twice. It is the engine of
    `/publish`.
  - `pandoc`: a deterministic conversion, one slide per second-level
    heading, nothing interpreted by a model. It is the engine of
    `/render`.
- **Template:** `--template` names a `.potx` or `.pptx` by path. Without
  it the claude engine designs the style and pandoc uses its built-in
  one.
- **`--model`:** the model of the headless run, `opus` by default; the
  claude engine only.
- **Output:** next to the input with the same basename, unless `-o`
  names a path.
- **Needs:** Python 3.8 or newer; `forge_tools.py`; pandoc, or the
  claude CLI with the document skill of the format.

### md2docx.py

Converts a Markdown render into a Word document.

- **Synopsis:** `python scripts/md2docx.py <render.md>
  [--engine pandoc|claude] [--reference <styles.docx>]
  [--page-size A4|Letter] [--recipe <recipe.md>] [-o <file.docx>]
  [--model <model>]`
- **The two engines:**
  - `pandoc` (the default): deterministic, nothing interpreted by a
    model. It is the engine of `/render`.
  - `claude`: a model converts, the recipe's Format section giving its
    instructions (`--recipe`). Expensive and never the same twice. It
    is the engine of `/publish`.
- **Front-matter and diagrams:** the render's YAML front-matter is read
  as metadata and does not appear in the document. Mermaid diagrams are
  not rendered and land as blocks of code.
- **Styles and page:** `--reference` names a `.docx`, `.dotx` or
  `.dotm` whose styles the output takes; the page setup is then the
  reference's own and `--page-size` is not applied. Without a
  reference the page is A4, or Letter with `--page-size Letter`. The
  claude engine takes the reference as the template it starts from,
  and A4 where none is given.
- **`--model`:** `opus` by default; the claude engine only.
- **Output:** next to the input with the same basename, unless `-o`
  names a path.
- **Needs:** Python 3.8 or newer; `forge_tools.py`; pandoc, or the
  claude CLI with the document skill of the format.

### md2video.py

Makes the format file of a screenplay render. The job is described in
[Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

- **Synopsis:** `python scripts/md2video.py <render.md> --format video|html-player
  [--pace 4,8,16] [--date "<date>"] [--section <name>] [--name <name>]
  [-o <file>] [--frame <seconds> <file.png>]`
- **Input:** a render of the screenplay genre: a title card, a card of
  what the viewer will see, scenes each with a caption of two parts
  (Now, Why) and a fenced block of what the terminal shows, and an end
  card.
- **The two formats:**
  - `video`: every frame painted with Pillow as a simulated terminal
    (1280x890) and piped into ffmpeg (H.264, 30 fps). The same file
    comes from the same render every time.
  - `html-player`: the timeline as JSON of events, wrapped as a script
    (`forgeVideo({...})` in `<name>.html-player.js`) so that the player
    page can load it from a file on disk as well as from GitHub
    Pages.
- **The pace:** three reading rates in words a second, for the
  principal's lines, Claude's answers and the lines that only report
  a file. The default is `4,8,16`. The pace, the date shown in the tab
  bar and the look come from the recipe's Format section as
  arguments; the render carries none of it.
- **The section and the name:** `--section` names the section of the
  course the video belongs to and `--name` the name the list shows,
  in place of the title card's title. Both go into the player file's
  data. The page groups the videos by section, sections and videos
  alike in the order of the file names. A file without them is listed
  under its title, after the sections.
- **`--frame <seconds> <file.png>`:** paints one frame of the video at
  that second to a PNG and stops, as a check of the look.
- **Where the file lands:** next to the input with the render's
  basename (`<name>.mp4` or `<name>.html-player.js`) unless `-o` names
  a path. Where the output lands under the engine's `docs/videos/`,
  the player page `docs/videos/index.html` is written anew from the
  template with the folder's files listed and loaded.
- **Needs:** Python 3.8 or newer; `forge_tools.py`. For `video`:
  Pillow and ffmpeg on PATH. Fonts are taken from the system where
  they exist, and Pillow's built-in font otherwise.

## Hooks

Both hooks are configured in `.claude/settings.json` and are called by
the harness, which here means the program that runs Claude. Neither
takes the principal's arguments in normal use.

### hook-walkthrough.py

A hook that runs at every prompt the principal sends. The harness adds
its standard output to the context of that turn.

- **What it answers:** it prints lines that repeat the one-item
  walkthrough rule with the verdict line that closes every
  proposition, the pointer to the walkthrough skill, and the conduct
  rules: use the forge's scripts and never the raw tool, explain and
  ask before running a command of one's own, change nothing that was
  not agreed and approved, and close every step needing consent with
  the verdict line (a yes with a question in it counts as a question).
- **It reads and writes nothing,** takes no arguments, and is
  independent of the working directory: the settings file invokes it
  with its own path through the `${CLAUDE_PROJECT_DIR}` placeholder.
- **Needs:** Python 3.8 or newer on PATH as `python`.

### hook-git.py

A hook that runs before every Bash command Claude sends. It separates
reading git from writing it. The PowerShell tool is closed to git
whole by a deny rule, so that there is one parser and one door.

- **What it does:** it reads the command from the hook's JSON on
  stdin, splits it at the shell's separators, and judges every part
  that calls git.
- **What it answers, per part:**
  - `allow`: a reading verb (status, log, diff, show, fetch and the
    like) with reading flags.
  - `ask`: the commands that finish a conflict and its step, so that
    the harness puts the command to the principal and runs it on his
    yes. They are `add` without `--force` and without the interactive
    flags, `rebase --continue` and `--abort`, `merge --continue` and
    `--abort`, `merge <branch>` with one name and no flag, and
    `checkout --ours` or `--theirs` on a file. An ask holds in the
    automatic permission mode.
  - `deny`: everything else, with the script of the forge to use
    instead where one exists. Denied are the writing verbs, a verb the
    script does not know (an alias among them), a reading verb with a
    writing flag, a global option that changes how git runs (`-c`,
    `--git-dir`, `--work-tree`, `--exec-path`), git inside another
    command and a part the script cannot read.
- **Across a whole command:** a part that is not git is left to the
  harness. The answer is deny where any part is a git it refuses, ask
  where none is refused and one asks, allow where every part is a
  reading git, and nothing otherwise.
- **Reach:** it reads no file and writes nothing. It is for Claude's
  tools alone; the principal's own git from the shell is his.
- **Forms:**
  - `python scripts/hook-git.py` as a hook, with JSON on stdin;
  - `python scripts/hook-git.py --test` runs the built-in cases and
    exits 1 on a failure;
  - `echo 'git status' | python scripts/hook-git.py --judge` judges one
    command and prints the verdict.
- **Needs:** Python 3.8 or newer on PATH as `python`.

## Documentation

The three documentation scripts are steps of the run of `/document`,
described in [Generate the documentation](../use/generate-the-documentation.md).
They read the documentation map through `docs_map.py` and need Python
3.8 or newer and nothing else.

### docs-state.py

Computes the state of every page from the content of its inputs and
prepares the writers' tasks. It runs first in the run.

- **Synopsis:**
  - `python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]`
  - `python scripts/docs-state.py <map> --previous <path>`
- **The state:** for each entry it hashes the entry's text (its
  `state` line excepted) with the content of every input, a part of a
  file hashed as that part. The generator is hashed with the inputs:
  the writer's definition and the contract. The hash is compared with
  the `inputs-hash` in the front-matter of the page at the entry's
  path, and the entry's `state` is set in the map:
  - `new`: no page at the path;
  - `regenerate`: a page exists and its hash differs;
  - `keep`: a page exists with the same hash.
- **Removal:** a page under the documentation directory that no entry
  names, and the page of an entry marked `remove`, are listed as
  `remove`. The index `README.md` is excepted.
- **Tasks:** for every `new` or `regenerate` entry one task file is
  written to the folder given: the engine root, the page's path, the
  date, the version the page is made for, the hash it is to carry, the
  entry verbatim and the titles of the pages it links to. A task is a
  writer agent's whole prompt.
- **Missing inputs:** an input the map names and the disk does not
  have is reported and hashed as missing. The page is regenerated and
  its writer reports the gap.
- **The `--previous` form:** prints the map as last committed, for the
  planner.
- **It rewrites** only the `- state:` line of each entry.

### docs-index.py

Derives the documentation index from the map.

- **Synopsis:** `python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]`
- **Output:** writes `<docs-dir>/README.md`: before the sections, the
  reader paths of the map with each page a link; then one line per
  page grouped by section in the order start, use, about, extend,
  reference, each line the page's title linked to its path and the
  entry's `line`.
- **Deterministic:** no model is involved; the same map gives the same
  index. The index is never edited by hand.

### docs-check.py

Checks the generated documentation mechanically.

- **Synopsis:**
  - `python scripts/docs-check.py <map> <docs-dir> [--fact PATTERN ...]`
  - `python scripts/docs-check.py --file <path> [--fact PATTERN ...]`
- **What it verifies, printing each failure with file and line:**
  - every entry not in state `remove` has its page, and no page lies
    in the directory that the map does not name;
  - every relative link to a `.md` file resolves;
  - no long dash in the prose of a page (a code span and a fenced
    block are exempt);
  - every page opens with a front-matter;
  - no instance fact: the values of `CLAUDE.local.md`, any e-mail
    address but a placeholder at `example.*`, any absolute path of a
    machine, and every `--fact` pattern given.
- **The one-file scan:** with `--file <path>` in place of a map and a
  directory, one file is scanned for instance facts only (the values
  of `CLAUDE.local.md`, an absolute path of a machine and the `--fact`
  patterns). This is the scan `/render` runs on a render it has just
  written.
- **Exit codes:** 0 when everything holds, 1 when anything fails. The
  check mends nothing: a page that fails is regenerated, never edited
  by hand.

## Shared modules

These five modules are imported by the scripts and are not commands.

- `forge_repos.py`: what the git scripts share, that is the engine
  root, the list of repositories to visit, running git, the state of a
  repository against its origin, the global git configuration files,
  the registration of the merge driver and coloured output.
- `forge_tools.py`: what the conversion scripts share, that is finding
  a tool on PATH, running it, the headless Claude Code run and the
  console set to UTF-8; it owns the text of what the conversions need.
- `forge_docs.py`: what the scripts that read a project's documents
  share, that is front-matter, history records, ledger tables, resource
  index entries and threads; it never raises on a malformed file.
- `docs_map.py`: the one reader of the documentation map, shared by the
  three documentation scripts and by `forge-history.py`.
- `forge_check.py`: what the mechanical checks share, that is a
  finding and its report in the shape of the check contract, the keys
  and comments a template owns, and the kinds of the versioned
  documents.

## Portability

The scripts are the only platform-bound layer of the forge, and each
is written to run unchanged on Linux and macOS: Python 3.8 or newer
run as `python scripts/<name>.py`, paths composed with `pathlib`,
external tools resolved from PATH and nothing Windows-only. This is a
writing rule. The inputs do not record which scripts have run on
Linux. To write a script of one's own under the same rule, see
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
- [Add a script](../extend/add-a-script.md): writing a script of one's own.
- [Add an engine](../extend/add-an-engine.md): adding a row to the engine table.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
