---
generated: 2026-10-09
made: mirrored
inputs:
  - scripts/forge-save.ps1
  - scripts/forge-pull.ps1
  - scripts/forge-status.ps1
  - scripts/forge-clone.ps1
  - scripts/forge-branch.ps1
  - scripts/doc2md.ps1
  - scripts/md2pptx.ps1
  - scripts/md2docx.ps1
  - scripts/hook-walkthrough.ps1
  - CLAUDE.md
---

# Scripts

This page lists the scripts in `scripts/`, one entry each, as their
help headers state them: what the script does, its parameters and
forms, what it needs installed, where its output lands and which
command of the forge runs it. It is for the user who runs them and
for the one who extends the forge. Every script needs PowerShell 7
(`#Requires -Version 7`).

The scripts are the only door to git: reading state included.

## forge-save.ps1

Commit and push: the engine and every project that is a repository
of its own.

- Run by: `/save` (and `/release`, which saves with the release
  message and tag).
- Forms:
  - bare: visits the engine and every `projects/<slug>/.git` and
    gives each one with changes its own commit; a project directory
    without a repository is skipped with a note.
  - `<slug>`: saves that repository only; `forge` means the engine. A
    project without a repository is refused.
- Parameters:

| Parameter | Meaning |
|---|---|
| `<slug>` (position 0) | the one repository to save |
| `-m`, `-Message` | the commit message; without it one is generated |
| `-Tag <name>` | tags the commit and pushes the tag; needs a slug; when there is nothing to commit the current HEAD is tagged; an existing tag is refused |

- Per repository: stage everything, commit, then, when an origin is
  configured, integrate remote changes by rebase and push. Without an
  origin the commit is kept locally and reported.
- Needs: git.
- Never: sets an identity or a remote, initialises a repository,
  uses `git add -f` or `git clean`.
- Output: commits and pushes in the repository; reported on screen.

```
./scripts/forge-save.ps1
./scripts/forge-save.ps1 <slug>
./scripts/forge-save.ps1 forge
./scripts/forge-save.ps1 -m "my message"
./scripts/forge-save.ps1 forge -Tag v3.33
```

## forge-pull.ps1

Pull the latest from the remotes: the engine (its upgrade channel)
and every project that has an origin.

- Run by: no command is named for it in `CLAUDE.md`; it is run
  directly.
- Forms:
  - bare: the engine, then every project with an origin.
  - `<slug>`: that one repository; `forge` means the engine.
- Fast-forward only. A repository with unsaved changes is not
  touched: reported and skipped (bare) or refused (slug); save first
  with `forge-save.ps1`. Projects without a repository or without an
  origin are reported and skipped.
- Needs: git.
- Output: updates the repositories; reported on screen.

```
./scripts/forge-pull.ps1
./scripts/forge-pull.ps1 forge
./scripts/forge-pull.ps1 <slug>
```

## forge-status.ps1

Report the git state of the engine and every project.

- Run by: no command is named for it in `CLAUDE.md`; its header says
  `/setup` needs the global configuration file it names.
- Form: bare only, no parameters.
- Read-only, changes nothing. It reports first the global
  configuration file git reads; then, for the engine and each
  `projects/<slug>`, the unsaved changes (or "clean"), the branch, the
  last commit and the origin, or "no origin" / "not under git".
- Needs: git.
- Output: on screen.

```
./scripts/forge-status.ps1
```

## forge-clone.ps1

Bring an existing project in: clone its repository into `projects/`.

- Run by: `/import-project`.
- Parameter: `<Url>` (mandatory, position 0), the repository URL.
- The directory is `projects/<repository name>`, derived from the
  URL; an existing directory is never overwritten. The script sets no
  identity and carries no URL.
- Afterwards it reports the last commit, the origin, the commit
  identity git resolves for the clone, and whether the project has a
  ledger with a `kind:` header (absence is a fact, not a defect).
- Needs: git.
- Output: the clone in `projects/<repository name>`; the report on
  screen.

```
./scripts/forge-clone.ps1 https://example.com/team/my-idea.git
./scripts/forge-clone.ps1 git@example.com:team/my-idea.git
```

## forge-branch.ps1

Switch one repository to a branch, creating it if needed, or report
the branch it is on.

- Run by: no command is named for it in `CLAUDE.md`; it is run
  directly.
- Forms: `<slug>` is mandatory, there is no bare form; `forge` means
  the engine.
  - `<slug>`: reports the current branch and lists the branches.
  - `<slug> <branch>`: switches to the branch, creating it from the
    current state when it does not exist; `main` switches back.
- Unsaved changes stop the switch: save first with `forge-save.ps1`.
- Merging, deleting and pushing branches stay with git: a new branch
  reaches the remote by the first save made on it; a release is made
  from `main` only.
- Needs: git.
- Output: the branch of the repository; reported on screen.

```
./scripts/forge-branch.ps1 forge
./scripts/forge-branch.ps1 forge work-release
./scripts/forge-branch.ps1 <slug> main
```

## doc2md.ps1

Convert Word, PowerPoint, PDF and Excel documents to Markdown.

- Run by: `/ingest`, on the principal's explicit word; the extract
  then is the source.
- Inputs, mixed and repeated freely, also from the pipeline: a file; a
  glob; a list file (plain text, one path or glob per line, `#` or
  `;` starts a comment, relative paths resolved against the list
  file's directory); a directory with `-Recurse`.
- Parameters:

| Parameter | Meaning |
|---|---|
| `-OutDir`, `-o <dir>` | where to write the `.md` files; default next to each source file |
| `-Suffix <text>` | inserted before the `.md` extension (`-Suffix '.text'` gives `report.text.md`) |
| `-MarkitdownPath <exe>` | explicit path to markitdown; otherwise from PATH |
| `-Recurse` | descend into directories and into globs without `**` |
| `-Force` | overwrite existing `.md` files; default is to skip them |
| `-AsList` | treat every input as a list file, whatever its extension |
| `-WhatIf` | show what would be converted, write nothing |
| `-ListTools` | check that the engine is available, then exit |
| `-Help`, `-h`, `-?` | usage summary |

- Handled extensions: `.pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls
  .epub .html .htm .csv .json .xml .msg`. Legacy `.doc .ppt .rtf .odt
  .odp` are reported as unsupported; resave them as `.docx` or
  `.pptx` first.
- Needs: markitdown (MIT), installed by the user, never by the script:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- Output: `.md` files, next to the source or in `-OutDir`.

```
./doc2md.ps1 presentation.pptx
./doc2md.ps1 report.pdf -Suffix '.text'
./doc2md.ps1 *.pdf, *.docx -OutDir md
./doc2md.ps1 files.txt -OutDir md -Force
```

## md2pptx.ps1

Generate a PowerPoint deck from a Markdown deck definition.

- Run by: `/render` (engine `pandoc`) and `/publish` (engine
  `claude`).
- Parameters:

| Parameter | Meaning |
|---|---|
| `<definition.md>` (`-Md`, position 0) | the Markdown deck definition; without it the usage is printed |
| `-Engine pandoc\|claude` | the engine; default `claude` |
| `-Template <path>` | a `.potx` or `.pptx` template, named by path, relative to the current directory or absolute |
| `-Recipe <path>` | the recipe the definition was rendered from; the `claude` engine reads its Format section, `pandoc` ignores it |
| `-Out`, `-o <file.pptx>` | output path; default next to the input, same basename |
| `-Model <model>` | model of the headless Claude Code run; default `opus`; `claude` engine only |
| `-Help`, `-h`, `-?` | usage summary |

- Engines:

| Engine | What it does | Needs |
|---|---|---|
| `claude` (default) | a model designs the deck, through headless Claude Code (`claude -p`) with the official pptx skill; expensive, never the same twice | the pptx skill, named `anthropic-skills:pptx` or `document-skills:pptx`; where missing, installed once from an interactive Claude Code session with `/plugin marketplace add anthropics/skills` and `/plugin install document-skills@anthropic-agent-skills` |
| `pandoc` | deterministic: one slide per second-level heading, nothing interpreted by a model; a plain deck for reading | pandoc on PATH, installed once from https://pandoc.org/installing.html |

- Template: named by path, typically a file in a library project's
  `sources/`. Without `-Template` the `claude` engine designs the
  visual style itself and `pandoc` uses its built-in one.
- The script installs nothing and tells the model to install and
  download nothing.
- Output: the `.pptx` next to the input, or at `-Out`.

```
./md2pptx.ps1 <path>/renders/<recipe>.md
./md2pptx.ps1 deck.md -Template <path>/<template>.potx
./md2pptx.ps1 deck.md -Engine pandoc
./md2pptx.ps1 deck.md -Recipe ../recipes/deck.md -Out ../published/deck.pptx
```

## md2docx.ps1

Convert a Markdown render into a Word document.

- Run by: `/render` (engine `pandoc`) and `/publish` (engine
  `claude`).
- Parameters:

| Parameter | Meaning |
|---|---|
| `<render.md>` (`-Md`, position 0) | the Markdown render; its YAML front-matter is metadata and does not appear in the document; without it the usage is printed |
| `-Engine pandoc\|claude` | the engine; default `pandoc` |
| `-Reference <path>` | a `.docx`, `.dotx` or `.dotm` whose styles the output takes (its content is ignored) |
| `-PageSize A4\|Letter` | the page when no `-Reference` is given; default `A4` |
| `-Recipe <path>` | the recipe the render was made from; the `claude` engine reads its Format section, `pandoc` ignores it |
| `-Model <model>` | model of the headless Claude Code run; default `opus`; `claude` engine only |
| `-Out`, `-o <file.docx>` | output path; default next to the input, same basename |
| `-Help`, `-h`, `-?` | usage summary |

- Engines:

| Engine | What it does | Needs |
|---|---|---|
| `pandoc` (default) | deterministic; nothing interpreted by a model | pandoc on PATH, installed once (https://pandoc.org/installing.html; Windows `winget install JohnMacFarlane.Pandoc`, macOS `brew install pandoc`, Linux the package manager) |
| `claude` | a model designs the document, through headless Claude Code (`claude -p`) with the official docx skill and the recipe's Format section; expensive, never the same twice | the docx skill, named `anthropic-skills:docx` or `document-skills:docx`; where missing, installed once as for `md2pptx.ps1` |

- Reference document: named by path with `-Reference`, typically a
  file in a library project's `sources/`; pandoc takes its styles and
  ignores its content. Without it pandoc's built-in styles apply. The
  `claude` engine takes it as the template it starts from.
- Page: A4 by default. Without `-Reference` the script hands pandoc
  its own built-in reference with the page size written in. With
  `-Reference` the page setup is the reference document's own and
  `-PageSize` is not applied. The `claude` engine uses A4 where no
  reference is given.
- Limit: Mermaid diagrams are not rendered by `pandoc`; they land as
  blocks of code.
- The script installs nothing.
- Output: the `.docx` next to the input, or at `-Out`.

```
./md2docx.ps1 <path>/renders/<recipe>.md
./md2docx.ps1 brd.md -Reference <path>/<reference>.docx
./md2docx.ps1 brd.md -Out out/brd.docx
./md2docx.ps1 brd.md -Engine claude -Recipe ../recipes/brd.md -Out ../published/brd.docx
```

## hook-walkthrough.ps1

The per-prompt hook of the engine.

- Run by: Claude Code, on every user prompt, as configured in
  `.claude/settings.json`; not by a command and not by hand.
- Form: no parameters; it reads nothing and writes nothing.
- It prints to standard output, which Claude Code adds to the context
  of that turn: the one-item walkthrough rule, the pointer to the
  walkthrough skill, and three lines of conduct (use the forge's
  scripts; explain and ask before running a command of one's own;
  change nothing that was not agreed and approved).
- Needs: PowerShell 7. It is independent of the working directory:
  `.claude/settings.json` invokes it in exec form with its own path
  through the `${CLAUDE_PROJECT_DIR}` placeholder.

## Portability

`scripts/` is the one platform-bound layer and is written to run
unchanged on Linux, macOS and Windows: cross-platform PowerShell 7,
nothing Windows-only.

## See also

- [Install what the forge needs](../start/install.md): installing what the scripts need.
