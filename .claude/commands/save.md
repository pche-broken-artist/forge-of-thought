---
description: Save the forge to git with the pre-save conformance check and render refresh
argument-hint: [project-slug] [-m "message"]
---

Save the forge to git with the pre-save conformance check
(POS.0570). The engine and every project are repositories of their
own (POS.0940); what the save does per repository is stated in the
help header of `scripts/forge-save.ps1`, and CLAUDE.md (Persistence)
carries the one-line summary (POS.1070).
Arguments (`[slug]`, `-m "message"`) are passed through to the
script; a project without a repository is a property, not a defect —
relay the script's note in the report.

1. Determine scope from `./scripts/forge-status.ps1` — never from
   direct git commands; the scripts are the only door to git, for
   reading state too. It reports the engine and each project
   separately. Engine files touched → run the `/check-forge`
   procedure; project files touched → run `/check` for each affected
   project; both → both. A project "not under git" with changes is
   named in the report and otherwise left alone.
2. For every repository in scope, first regenerate its README and
   release notes from their recipes — unconditionally, no staleness
   test, always through the `/render` procedure
   (`.claude/commands/render.md`), never through an ad-hoc subagent
   prompt (POS.1070). The README and release-notes renders of one
   repository are launched at once, each through the `/render`
   procedure, and awaited together. Report the steps, including a
   short summary of what materially changed in the regenerated files
   (POS.0810, POS.1000): the principal rules on the delta as part of
   the pre-save report. The engine (core or `projects/forge/`
   touched): `README.md` and `RELEASE-NOTES.md` at the repository
   root from `projects/forge/recipes/`. A project: its `README.md`
   from `recipes/readme.md` and, for a thought project,
   `RELEASE-NOTES.md` from `recipes/release-notes.md`. A project
   whose recipe is missing is reported (a `/check` finding) and saved
   without the render. Other renders are never regenerated here; their
   staleness is the principal's business, shown by the `/forge` map,
   never a check finding (POS.0570).
3. Report the result to the principal — always, even when clean.
4. Clean check: state that the check passed and run the script.
5. Findings: settle them by walkthrough (CLAUDE.md, Working
   methods); a finding may be accepted as a deferral, recorded in the
   affected project's ledger under "Waiting on principal", and the
   save proceeds. Never fix silently; never proceed with an unsettled
   finding.
6. Unless `-m` was supplied, draft a one-line English commit message
   summarising the round — from the newest rows of the touched
   documents' `.history.md` companions, the primary record of every
   round (CLAUDE.md, Versioning & status) — and propose it to the
   principal; commit
   with the confirmed or adjusted wording. When more than one
   repository has changes, one message per repository is drafted, or
   the save is run per slug. The script's auto-generated file list is
   used only if the principal says so.
7. Only then run `./scripts/forge-save.ps1 [slug] [-m "message"]`
   and report the outcome — the script itself prints the commit's
   file summary; no direct git verification afterwards.

The check is advisory (POS.0430): the principal may order the save
at any moment regardless of findings.
