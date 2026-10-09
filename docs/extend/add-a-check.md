---
generated: 2026-10-09
made: mirrored
inputs-hash: 4143c8e5197c4b83
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md
---

# Add a check

This page is for someone who extends the forge with a new check: an isolated reviewer that verifies one kind of mechanical conformance with the conventions. It says what the file is, what goes into it, and how to prove it works.

A new check is added only by the principal's decision, and only where what it finds genuinely differs from what the existing checks find. The roster of checks that exist is on the page [Checks](../reference/checks.md), so look there first.

## What a check is

A check is one agent file: `.claude/agents/check-<name>.md`. You start it from the skeleton `templates/check-definition.md`. The file holds two things and nothing else: the front-matter and a Lens section. Everything a check shares with every other check (what it is allowed to do, how it works, the shape of its report) lives in the contract skill that the front-matter names. You do not repeat any of that in your file. [About the check](../about/the-check.md) explains what the contract owns.

Each check owns one concern and none another's. A check verifies conformance only: it never judges substance (that is the challenger's) or document quality (that is the critic's).

## The front-matter

Fill in these fields:

- `name`: `check-<name>`.
- `description`: one line saying what the check verifies and when it fits. The bare `/check` command builds its roster from these descriptions, so the line is how a person chooses the check. If the description contains a colon followed by a space, put the whole description in single quotes (an apostrophe inside is doubled), or the agent does not register.
- `tools`: read-only tools only (the skeleton gives `Read, Glob, Grep`).
- `model`: `inherit`. The whole forge runs on the session model.
- `skills`: `check-contract`.

## The Lens section

The Lens section is the only part of the file that is yours. It has three parts.

1. **What you read.** Say whether the target is a project, every project or the engine, and how the target the caller names narrows the reading. Say what a library reduces it to, and what a missing or an added project slug means to this check. The `/check` command leaves exactly these questions to the Lens section.
2. **What you verify.** List the rules the check goes after. For each rule, cite its owner (a section of `CLAUDE.md`, a template, a position of the forge intent) and do not restate the rule. The check reads the rule there, so a change at the owner reaches the check without editing it. Also say which states are a fact rather than a finding (for example a project that is not under git). A fact is reported in one line and is not counted as a defect.
3. **Cost.** State the scope the check reads: named files, or the whole, honestly. A check that names a scope reads that scope and nothing more.

A Lens section specialises the contract. It may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field.

## What the check does not do

- **It writes nothing.** The check returns its report as its final message. The `/check` procedure files the report in the project's `reviews/` folder, gives each new finding its number and adds it to the ledger. Nothing in your file should say otherwise.
- **It does not decide when it runs.** Whether a save or a release runs the check is for the definition of that caller to say, not for the check. Checks never call each other, and none runs on Claude's own judgement.

## Prove it

1. Run `/check engine`. The new check should appear in the roster by its description, and a run on the engine shows how it reads its target.
2. Run the check on a project: `/check <name> <project-slug>`. If it finds something, the report is filed as a dated report in that project's `reviews/`, and each finding is settled by walkthrough. If it finds nothing, the report says it conforms and nothing is filed.

If the check cannot be started, look first at the front-matter: a description with an unquoted colon is the usual cause.

## See also

- [About the check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
