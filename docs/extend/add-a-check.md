---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 54c97e62ab7b1055
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

This page is for the extender who wants a new check: a read-only
reviewer that verifies one kind of mechanical conformance with the
conventions of the forge. A check is one agent file,
`.claude/agents/check-<name>.md`, made from
`templates/check-definition.md`. A check runs as a subagent, that is a
reviewer that starts without the working conversation and sees only
the files it reads.

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md). It
  covers proving, recording and releasing a change, and this addition
  is recorded and released as any change of the forge.
- Decide the one concern the check owns. Each check owns one concern
  and none another's, and a new check is added only where what it
  finds genuinely differs from the checks that exist (see
  [Checks](../reference/checks.md)).
- Add a check only on the decision of the principal, the person whose
  thinking is being forged. New checks are not added on Claude's own
  judgement.
- Keep the boundary in mind. A check verifies conformance only. It
  never judges substance, which belongs to the challenger, and it
  never judges document quality, which belongs to the critic. What the
  contract gives every check is described in
  [The check](../about/the-check.md).

## The files

One file is added:

- `.claude/agents/check-<name>.md`: the agent, made from
  `templates/check-definition.md`. It holds the front-matter and the
  Lens section, and nothing else.

Nothing else changes. The `/check` command finds a check by scanning
`.claude/agents/check-*.md`, so the command itself is not edited. The
shared behaviour (the subject, the way of working, the shape of the
report) comes from the contract skill `check-contract`, which the
front-matter names. The check file does not restate it.

## Steps

1. Copy `templates/check-definition.md` to
   `.claude/agents/check-<name>.md`. The name is the suffix of the
   agent name.
2. Fill the front-matter:
   - `name`: `check-<name>`.
   - `description`: what the check verifies, in one line, and when it
     fits. The bare `/check` roster prints this line for each check.
     If the description holds a colon followed by a space, put the
     whole description in single quotes (an apostrophe inside is
     doubled). Otherwise the agent does not register.
   - `tools`: read-only, that is `Read, Glob, Grep`.
   - `model`: `inherit`, so that the check runs on the session model.
   - `skills`: a list with `check-contract`.
3. Delete the comment block of the skeleton.
4. Write the Lens section in three parts:
   1. What you read: a project, every project, or the engine; how the
      target narrows it; what a library reduces it to.
   2. What you verify: the rules, each with its owner cited (a section
      of `CLAUDE.md`, a template, a position of the intent) and never
      restated. Say which states are a fact and not a finding, so that
      the check reports them as one line of fact.
   3. Cost: the scope the check reads, as named files or as the whole,
      said honestly.
5. Keep the Lens section a specialisation of the contract. It may
   narrow what is read or make a shared rule stricter. It never
   renames, drops or duplicates a shared rule or field.
6. Leave writing to the command. The check returns its report and
   writes no file. The `/check` procedure numbers the findings and
   files the report.
7. Decide where the check runs. Whether `/save` or `/release` runs it
   is said by the definition of that command, not by the check file.
   If the new check is to be part of a save or a release, change that
   definition as a separate part of the same change.

You should now see one new file, `.claude/agents/check-<name>.md`,
with front-matter and a Lens section and no leftover comment.

### A worked example

The front-matter of a check with the placeholder name `<name>`. The
description has no colon followed by a space, so it needs no quotes.

```markdown
---
name: check-<name>
description: Check "<name>" - verifies <what it verifies, in one line>. Fits when <the moment>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

**What you read.** <the target: a project, every project or the
engine; how a slug narrows it; what a library reduces it to>

**What you verify.** <each rule with its owner cited, not restated;
the states that are a fact and not a finding>

**Cost.** <the files or the whole, said honestly>
```

## Prove it

Run the new check on the engine. The engine root is the target and no
slug is given:

```
/check engine
```

Replace `engine` with `<name>` for your check. Then run it on a
project, with a placeholder slug:

```
/check <name> <slug>
```

Which of the two targets the check takes, and what a slug means to it,
is said by its Lens section. Run the bare command, `/check`, to see
that the roster lists the new check with its description.

You should now see the report: a one-line verdict ("conforms" or a
count of findings) and, if there are findings, each with a place, the
rule and its owner, and one proposed fix. A report that says
"conforms" is filed nowhere. A report with findings is filed by
`/check` into the `reviews/` folder of the target project and is
offered for a walkthrough, which is the forge's way of settling a list
one item at a time. Nothing blocks: the findings are advisory.

## Record and release

Record the change and release it as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) describes. For
the full list of checks and the terms used here, see
[Checks](../reference/checks.md) and the
[Glossary](../reference/glossary.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
