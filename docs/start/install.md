---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.ps1
  - scripts/forge-save.ps1
  - scripts/doc2md.ps1
  - scripts/md2pptx.ps1
  - scripts/md2docx.ps1
  - projects/forge/recipes/readme.md
---

# Install what the forge needs

This page is for someone about to use the forge for the first time.
It lists what must be on the machine before the forge runs and how
each piece is installed, in the order you first need it. It was put
together from what the forge's scripts refuse to run without, from
the hook configuration in `.claude/settings.json`, from `CLAUDE.md`
and from the Setup section of the readme recipe
(`projects/forge/recipes/readme.md`), which owns the Claude Code
install commands.

No script of the forge installs anything. Every tool below is
installed by you, once, and the forge finds it on your PATH.

## 1. git

The forge keeps everything in git repositories, and its scripts are
the only way it touches git. `scripts/forge-save.ps1` stops with
"git is not installed." when git is missing. Install git the usual
way for your system.

## 2. PowerShell 7

Install PowerShell 7, the command `pwsh`, on every platform,
including macOS and Linux. It is needed before anything else
because:

- Every script in `scripts/` is PowerShell 7; each opens with a
  `#Requires -Version 7` line.
- Claude Code runs `scripts/hook-walkthrough.ps1` through `pwsh` on
  every prompt you send, as configured in `.claude/settings.json`.

The scripts are written to run unchanged beyond Windows: plain
cross-platform PowerShell 7 with nothing Windows-only.

## 3. Claude Code and a subscription

You need a paid Claude subscription. Install Claude Code with one of
these commands:

- Windows (PowerShell):

  ```
  irm https://claude.ai/install.ps1 | iex
  ```

- macOS or Linux:

  ```
  curl -fsSL https://claude.ai/install.sh | bash
  ```

- or, through npm:

  ```
  npm install -g @anthropic-ai/claude-code
  ```

Sign in when you first run it. Usage draws from the same pool as
Claude chat.

## 4. Optional tools, by what they are for

Each of these is needed only for the command named with it. Each is
resolved from PATH.

| Tool | Needed for | How to install |
|---|---|---|
| markitdown (needs Python 3) | converting Word, PowerPoint, PDF or Excel files to Markdown at `/ingest` (`scripts/doc2md.ps1`) | `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"` |
| pandoc | the plain Word and PowerPoint files made by `/render` (the `pandoc` engine of `scripts/md2docx.ps1` and `scripts/md2pptx.ps1`) | from https://pandoc.org/installing.html; for example `winget install JohnMacFarlane.Pandoc` on Windows, `brew install pandoc` on macOS, your package manager on Linux |
| Anthropic's document-skills plugin | the designed Word and PowerPoint files made by `/publish` (the `claude` engine of the same two scripts) | once, from an interactive Claude Code session (below) |

The plugin is installed with two commands typed inside Claude Code:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Where Claude Code already brings the Word and PowerPoint skills
itself, the plugin is not needed.

The git scripts need nothing beyond git.

## 5. Get the forge and start it

Clone this repository, the one you are looking at:

```
git clone <address of this repository>
```

Clone it rather than copying it: `scripts/forge-save.ps1` refuses to
work on an engine that is not a git repository.

Then always start `claude` from the root of the cloned repository,
so that `CLAUDE.md` and `CLAUDE.local.md` load.

## Next

Run the first setup, `/setup`, once, from that same session.

## See also

- [Set up the forge](setup.md): the first run, `/setup`, which fills the instance facts and sets the model.
- [Scripts](../reference/scripts.md): every script with what it needs and its parameters.
