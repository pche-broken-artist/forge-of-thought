---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f57bcae8e7a44228
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a check

A check is one agent file that verifies whether the files of a target
follow the conventions of the forge. This page is for the extender who
wants to add one, and it shows the file, the steps and the proof that
it works.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first. The
addition is recorded and released as any change of the forge is.

Two things decide whether a new check is worth adding:

- A new check is added only on the decision of the principal (the
  person whose thinking is forged).
- It is added only where what it finds genuinely differs from what
  the existing checks find. The checks that exist are listed in
  [Checks](../reference/checks.md).

A check owns one concern and no other. If your idea mixes two
concerns, it is two checks.

A check verifies mechanical conformance only. It does not judge the
quality of documents, and it does not judge the substance of the
thinking. What the contract that every check shares owns is explained
in [The check](../about/the-check.md). Terms of the forge that this
page uses without a gloss are in [Glossary](../reference/glossary.md).

## The files

You add one file and change no other:

- `.claude/agents/check-<name>.md`, made from the skeleton
  `templates/check-definition.md`.

The command `/check` does not change. It finds checks by scanning the
agent files, and it reads each check's `description` to say when the
check fits.

The file has two parts.

The front-matter carries these fields:

- `name`: `check-<name>`.
- `description`: what the check verifies and when it fits.
- `tools`: read-only tools, `Read, Glob, Grep`.
- `model`: `inherit`.
- `skills`: the list holding `check-contract`.

The Lens section is the check's own text, in three parts:

1. What it reads. This is a project, every project or the engine, how
   the target narrows the reading, and what a library reduces it to.
2. What it verifies. Each rule is cited with its owner (a section of
   `CLAUDE.md`, a template or a position) and never restated. The part
   also says what is a fact and not a finding.
3. Cost. This is the scope it reads, as named files or as the whole,
   said honestly.

Everything else about how a check behaves comes from the contract that
the `skills` field loads. The check file does not repeat it.

## Steps

1. Copy `templates/check-definition.md` to
   `.claude/agents/check-<name>.md`.
2. Fill in `name` with `check-<name>`. Keep `tools`, `model` and
   `skills` as the skeleton has them.
3. Write the `description`: one line saying what the check verifies,
   then when it fits. If the description holds a colon followed by a
   space, put the whole description in single quotes, and double any
   apostrophe inside it. Otherwise the agent does not register.
4. Delete the skeleton's comments from the file. They are guidance for
   writing, not part of the check.
5. Write the Lens section in its three parts. Cite the owner of every
   rule, and do not restate the rule.
6. Do not make the check write a file. A check returns its report and
   writes nothing, and the `/check` procedure files the report.
7. Decide nothing about who runs the check. Whether a save or a
   release runs it is said by the definition of the caller (the save
   or the release), not by the check. Add the check there only if the
   principal decides so, as a change of its own.

## Prove it

Run the check on the engine. This works for a check whose Lens takes
the engine root:

```
/check <name>
```

Then run it on a project. A project is named by its slug, and the
engine's own project is `forge`:

```
/check <name> <project-slug>
```

You should now see the report of an isolated run. It has a one-line
verdict, either `conforms` or the number of findings. Each finding
carries a place, the rule with its owner, and one proposed fix.

A report that has findings is filed in the target project's `reviews/`
folder, and one that says `conforms` is filed nowhere. Check that the
findings are about conformance with the conventions your Lens names,
and that none is about quality or substance.

To see how an existing check reads, run the one for the engine with
`/check engine`.

## Record and release

Record the addition and release it as any change of the forge, by the
steps of [Make a change to the forge](how-a-change-is-made.md).

## A worked example

You want a check named `<name>`, which verifies one convention in one
kind of file.

1. Copy the skeleton to `.claude/agents/check-<name>.md`.
2. Set the front-matter:

```
---
name: check-<name>
description: Check "<name>" — <what it verifies>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---
```

3. Write `## Lens` with three parts: the files it reads, the rules it
   verifies with the owner of each cited, and the cost.
4. Run `/check <name>` and then `/check <name> <project-slug>`.
5. Record and release the change.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
