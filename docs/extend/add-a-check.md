---
generated: 2026-10-10
made: mirrored
inputs-hash: 6acb0140ca06e25f
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md
---

# Add a check

This page is for the extender who wants a new check: a reviewer that
verifies one kind of mechanical conformance of a project or of the
engine. It says what the file is, what goes into it and how to see that
it works.

## What a check is

A check is one agent file, `.claude/agents/check-<name>.md`, made from
the skeleton `templates/check-definition.md`. The file holds two things
and nothing else: a front-matter and a section called Lens. Everything
the checks have in common, such as the subject, the way of working and
the shape of the report, is not in your file. It lives in one contract
skill that the front-matter names, and it is loaded into your check when
it runs. Your Lens section may narrow what is read or make a shared rule
stricter. It never renames, drops or repeats a shared rule.

A check verifies conformance with the conventions and nothing else. It
does not judge whether a document is good (that is the critic's work) or
whether the thinking is sound (that is the challenger's). The engine
adds a check only on the principal's decision, and only where what the
new check finds genuinely differs from what the existing ones find. Each
check owns one concern and none another's.

## The front-matter

Copy the skeleton and fill in these fields.

| Field | What it holds |
|---|---|
| `name` | `check-<name>`. Your check's name is the part after `check-`. |
| `description` | One line saying what the check verifies and when it fits. The bare `/check` roster is made from these descriptions, so a reader choosing a check relies on this line. |
| `tools` | Read-only: `Read, Glob, Grep`. |
| `model` | `inherit`, so the check runs on the session's model. |
| `skills` | `check-contract`, the shared behaviour. |

If the description contains a colon followed by a space, put the whole
description in single quotes, and double any apostrophe inside it.
Otherwise the agent does not register.

Delete the comment block of the skeleton in your file.

## The Lens section

The Lens section is yours alone and has three parts.

1. **What you read.** Say whether the target is one project, every
   project or the engine. Say how the target narrows the reading: what a
   project slug means to this check, what a missing or an added slug
   means, and what a library, which has no chain, reduces the reading
   to. The `/check` command reads this part to know which targets your
   check takes.
2. **What you verify.** List the rules the check goes after. For each
   rule, cite its owner (a section of `CLAUDE.md`, a template or a
   position of the forge intent) and never restate the rule. The owner
   stays the single place where the rule is written, so that the check
   follows it when it changes. Say here too what is a fact rather than a
   finding: a state that is deliberate, such as a project that is not
   under git, is reported once in one line and not as a defect.
3. **Cost.** Say honestly what the check reads: named files, or the
   whole target. A check that names a scope reads that scope and nothing
   more. A check that names the whole reads the whole, however long it
   takes.

Do not describe the report format, the way findings are ranked or the
handling of findings already filed. Those belong to the contract, and
writing them again in a Lens section would give the same rule two
places.

## What the check does not do

The check writes nothing. It returns its report as its final message,
and the `/check` command does the rest. When there are findings, the
command files the report in the target project under `reviews/` as
`YYYY-MM-DD-check-<name>.md`, gives each new finding its number and adds
a row for it to the project's ledger. A report that says the target
conforms is filed nowhere. The command then presents the findings and
offers a walkthrough of them. Nothing a check finds blocks anything:
what becomes of a finding is decided at the walkthrough.

The command itself does not change when you add a check. It finds the
check by scanning the agent files.

A check also does not decide when it runs. Whether `/save` or `/release`
runs it is for the definition of that command to say. A check never
calls another check, and none runs on Claude's own judgement.

## See that it works

1. Run `/check` with no arguments. Your check should appear in the
   roster with its description.
2. Run `/check <name> engine`, or use the engine's own project slug if
   the check takes a slug, and read the report. Each finding should show
   a place in a file, the rule it breaks with that rule's owner, and one
   proposed fix.
3. Run the check on a project, `/check <name> <project-slug>`, and
   compare. If your Lens section says a state is a fact, confirm it
   appears once as a fact and not as a finding.

If the report names a rule without an owner, or restates a rule, the
fault is in the Lens section. Mend it there.

## See also

- [About the check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
