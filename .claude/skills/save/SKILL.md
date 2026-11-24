---
description: Save the forge to git — the light check, then commit and push; no renders; --quick leaves the check out
argument-hint: '[project-slug] [-m "message"] [-F file] [--tag name] [--quick]'
---

Save the forge to git: the light check, then commit and push on whatever
branch is checked out, nothing more (POS.1100). The `project` and
`engine` checks and the renders belong to `/release`
(`.claude/skills/release/SKILL.md`, POS.0570). The engine and every
project are repositories of their own (POS.0940), the engine's own
project one of them, beside the engine, and `forge` saves both
(POS.1980); what the save does per
repository is stated in the help header of `scripts/forge-save.py`
(POS.1070).
Arguments (`[slug]`, `-m "message"`, `-F <file>`, `--tag <name>`) are passed through
to the script; `--quick` is this skill's alone, leaves the check out and
nothing else (POS.1100), and is never passed on; a project without a
repository is a property, not a defect (POS.0940) — relay
the script's note in the report. Saves made directly from the shell,
`python scripts/forge-save.py`, are unaffected.

1. Determine scope from `python scripts/forge-status.py` (the forge
   reads state by its script). It reports the
   engine and each project
   separately, with the branch each is on. A project "not under git"
   with changes is named in the report and otherwise left alone.
1a. Unless `--quick` was given, run the `light` check on every
   repository in scope and settle
   its report through the `/check` procedure
   (`.claude/skills/check/SKILL.md`; the engine's project is
   `forge`); a save never waits on a finding the principal has not
   asked to fix (POS.0430). When the ledger script fails or names
   files it could not parse, the check reads the ledger as it lies,
   the save goes on and says so: the save is what does not lose work
   (SOL.0530).
2. Unless `-m` was supplied, draft an English commit message for the
   round, a subject and a body (POS.2050, SOL.0990), from the records
   the round appended to the touched documents' histories, the
   primary record of every round (POS.0310), and propose it to the
   principal; commit with the confirmed or adjusted wording. The
   subject says the one thing the commit does: one clause in the
   imperative, opening in lower case, with no full stop, no prefix,
   no type and no scope, of at most about 72 characters, where the
   lists of commits cut it. The body follows a blank line: sentences
   wrapped at about 72 columns, a paragraph for each thing it says,
   what changed and why with the items and their versions, what was
   built and what the tests said, where the matter came from; a
   commit whose subject says all has none. A message with a body is
   written to a file in the engine's `tmp/` and handed to the script
   with `-F <file>`, one short command; a subject alone goes through
   `-m`. When more than
   one repository has changes, one message per repository is drafted,
   or the save is run per slug. With `forge`, the one message serves
   both commits. The message the script makes from the files is used
   only if the principal says so.
3. A tag is set only on the principal's word: `--tag <name>` given, or
   asked for in words. A tag needs one repository, so a slug. When he
   asks for a tag without naming it, propose `v<intent version>` of
   that repository's intent and take his word or his own name — any
   name git accepts (`pre-save-release-split` as readily as a
   number). The one fixed name, `v<major>` at an approved major, is
   `/release`'s rule; it runs this command with it (POS.1100).
4. Only then run `python scripts/forge-save.py $ARGUMENTS`, `--quick`
   left out, and report the
   outcome — the script itself prints the commit's file summary and
   the tag; no direct git verification afterwards. Where the script
   leaves a conflicting rebase standing, the session goes on with the
   step of a conflict as CLAUDE.md, Persistence, has it (POS.1710) and
   saves again; where it refuses because a rebase or merge is already
   standing, report that refusal and the step it names.
