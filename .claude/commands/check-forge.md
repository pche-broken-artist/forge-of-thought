---
description: Careful consistency check of the Forge system itself (core + projects/forge)
---

Cross-check the universal core and `projects/forge/` against each other
and report in the conversation language (`CLAUDE.local.md`), compactly.
Read-only: report findings and proposed
fixes and apply only what the principal approves. Pure ledger
bookkeeping (stale versions, dates, counts) may be offered as an
immediate fix.

0. **Run in isolation** exactly as `/check` does
   (`.claude/commands/check.md`, opening paragraph); the prompt names
   the engine root and the files changed per
   `scripts/forge-status.ps1`. Back in the session: walk the findings
   through with the principal.
1. **Core internal consistency**
   - CLAUDE.md commands table ↔ actual files in `.claude/commands/`;
     described agents ↔ `.claude/agents/`.
   - Scripts on disk ↔ CLAUDE.md: every file in `scripts/` is
     described in CLAUDE.md (layout comment and its governing rule)
     and nothing described there is missing on disk.
   - README ↔ CLAUDE.md: same chain, same conventions, same command
     set, no contradictions.
   - README and release notes are renders: `/release` regenerates them
     from the settled sources after this check, so their currency is
     not checked here — a claim in the README that CLAUDE.md or the
     intent no longer supports is a recipe defect, fixed in the
     recipe and re-rendered, never by editing the file.
   - `templates/` agree with the conventions (front-matter fields
     including `last_change`, the history companion
     `templates/history.md`, prefixes, numbering, statuses; no
     template carries a Version History table in its body; the recipe
     templates carry no status).
2. **Core ↔ forge intent** (`projects/forge/10-intent.md`)
   - Every POS is honoured by the core documents; nothing withdrawn or
     rejected (REJ items, closed THR items) is still advertised
     anywhere in the core.
   - Decisions referenced from the intent exist in `decisions.md` and
     every DEC record is reflected in the intent where it applies.
3. **One mechanism in one place** (POS.1070) — over the
   operating-layer files (`.claude/`, `templates/`, `scripts/`,
   CLAUDE.md) changed in the scope; the full sweep of every command,
   agent and template only on an explicit bare `/check-forge`.
   - Every command, agent and template describes only its own job; a
     procedure, rule set or file shape that another file owns is
     cited by path, never restated. A restatement — the same steps or
     rules in two places, whatever the wording — is a finding; the
     fix is a reference to the owner.
   - Every challenger persona (`.claude/agents/challenger-*.md`)
     carries the fixed sections of `templates/challenger.md`
     verbatim; only its Lens section is its own. Every critic lens
     (`.claude/agents/critic-*.md`) likewise carries the fixed sections
     of `templates/critic.md`.
   - No command performs directly what a script, command or agent
     exists for (git outside the scripts in `scripts/`, a conversion outside
     `doc2md.ps1`, a render outside `/render`, a review outside the
     agents).
4. **Forge project** — run the `/check` procedure
   (`.claude/commands/check.md`) on `projects/forge` exactly as on any
   thought project; its findings join this report. Nothing of that
   procedure is restated here (POS.1070).
5. **Rename/removal sweep** — grep for the old names recorded in DEC
   records (e.g. a renamed command) and for terms the principal has
   explicitly dropped; only historical records (changelogs, DEC, REJ)
   may still contain them.
6. **Report** — findings ranked by severity, each with `file:line` and
   a proposed fix. If everything is consistent, say so in one line.
   Findings only, as `/check` says: what conforms is not reported.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. This command checks consistency only.
