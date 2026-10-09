---
generated: 2026-10-09
made: mirrored
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md
---

# Add a check

This page is for someone extending the forge with a new check: one
more isolated reviewer that verifies mechanical conformance with the
conventions. It says what the file is, what goes into it and how to
see that it works.

A new check is added only by the principal's decision, and only where
what it finds genuinely differs from what the existing checks find.
Each check owns one concern and none another's.

## What a check is

A check is one agent file, `.claude/agents/check-<name>.md`, made from
the skeleton `templates/check-definition.md`. The file holds
front-matter and a Lens section, nothing else. Everything the checks
share (the subject, the way of working, the shape of the report) is
the contract skill that the front-matter names, so the file never
repeats it.

## Steps

1. **Copy the skeleton** to `.claude/agents/check-<name>.md` and
   replace `<name>` with the check's name. The name is the suffix of
   the agent's name.
2. **Fill the front-matter.**
   - `name`: `check-<name>`.
   - `description`: what the check verifies and when it fits. The
     roster printed by a bare `/check` is built from these
     descriptions, so this line is how the principal chooses the
     check. If it contains a colon followed by a space, put the whole
     description in single quotes (an apostrophe inside is doubled),
     or the agent does not register.
   - `tools`: read-only (`Read, Glob, Grep`, as the skeleton has
     them).
   - `model: inherit`.
   - `skills`: `check-contract`.
3. **Write the Lens section** in three parts (below).
4. **Delete the comment** at the top of the skeleton.

## The Lens section

The Lens is the only part of the file that is the check's own. It is
a specialisation of the contract: it may narrow what is read or make a
shared rule stricter, and it never renames, drops or duplicates a rule
or field of the contract. Its three parts:

1. **What you read.** A project, every project, or the engine; how the
   target narrows the reading (what a missing or an added project
   slug means to this check); what a library reduces it to.
2. **What you verify.** The rules, each with its owner (a section of
   `CLAUDE.md`, a template, a position of the intent) cited and never
   restated, so that a rule is stated in one place only. Also what is
   a fact rather than a finding: a state that is reported once, in
   one line, and not counted as a defect.
3. **Cost.** The scope the check reads: named files, or the whole,
   stated honestly. A check that names a scope reads that scope and
   nothing more; one that names the whole reads the whole.

## What a check does not do

- **It writes nothing.** It returns its report in its final message.
  The `/check` command files the report as
  `reviews/YYYY-MM-DD-check-<name>.md` in the target project, gives
  each new finding its number and adds it to the ledger. A report that
  says "conforms" is filed nowhere.
- **It judges neither substance nor quality.** A document that is
  wrong or unclear but conforms is not its business.
- **It does not decide whether a save or a release runs it.** That
  is the definition of the caller, `/save` or `/release`, to say.
  Checks never call each other.

You do not change the `/check` command to add a check: it scans
`.claude/agents/check-*.md` for the roster.

## Prove it

1. Run bare `/check`. The new check appears in the roster with its
   description.
2. Run `/check <name> engine`, a run on the engine. The check returns
   either "conforms" or a ranked list of findings, each with a place,
   the rule and its owner, and one proposed fix.
3. Run it on a project, `/check <name> <project-slug>`, and read
   the Lens to confirm that the target narrows the reading as you
   wrote it.

A finding is settled afterwards by walkthrough, and nothing blocks:
a release may go on with a finding parked.

## See also

- [About the check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
