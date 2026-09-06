---
description: Save the forge to git — the light check, then commit and push; no renders
argument-hint: '[project-slug] [-m "message"] [-Tag name]'
disable-model-invocation: true
---

Save the forge to git: the light check, then commit and push on
whatever branch is checked out, nothing more (POS.1100). The full
checks and the renders belong to `/release`
(`.claude/skills/release/SKILL.md`, POS.0570). The engine and every project are repositories of their
own (POS.0940); what the save does per repository is stated in the
help header of `scripts/forge-save.ps1`, and CLAUDE.md (Persistence)
carries the one-line summary (POS.1070).
Arguments (`[slug]`, `-m "message"`, `-Tag <name>`) are passed
through to the script; a project without a repository is a property,
not a defect — relay the script's note in the report.

1. Determine scope from `./scripts/forge-status.ps1` (the scripts are
   the only door to git — CLAUDE.md, Persistence). It reports the
   engine and each project
   separately, with the branch each is on. A project "not under git"
   with changes is named in the report and otherwise left alone.
1a. Run the `light` check on every repository in scope through the
   `/check` procedure (`.claude/skills/check/SKILL.md`; the engine's
   project is `forge`) and settle what it finds: immediate fixes
   offered as one step, the rest by walkthrough or deferred — a save
   never waits on a finding the principal has not asked to fix
   (POS.0430).
2. Unless `-m` was supplied, draft a one-line English commit message
   summarising the round — from the newest rows of the touched
   documents' `.history.md` companions, the primary record of every
   round (CLAUDE.md, Versioning & status) — and propose it to the
   principal; commit with the confirmed or adjusted wording. When
   more than one repository has changes, one message per repository
   is drafted, or the save is run per slug. The script's
   auto-generated file list is used only if the principal says so.
3. A tag is set only on the principal's word: `-Tag <name>` given, or
   asked for in words. A tag needs one repository, so a slug. When he
   asks for a tag without naming it, propose `v<intent version>` of
   that repository's intent and take his word or his own name — any
   name git accepts (`pre-save-release-split` as readily as a
   number). The one fixed name, `v<major>` at an approved major, is
   `/release`'s rule; it runs this command with it (POS.1100).
4. Only then run `./scripts/forge-save.ps1 $ARGUMENTS` and report the
   outcome — the script itself prints the commit's file summary and
   the tag; no direct git verification afterwards.
