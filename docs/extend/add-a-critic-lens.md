---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 18ee4ad5b24ff659
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a critic lens

A critic lens is one agent file that reads the documents of a project
through one angle and reports on their quality. This page is for the
extender who wants to add a lens. A lens is added as one file and
nothing else changes.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). The lens is
recorded and released as any change of the forge is.

A new lens is added only by the decision of the principal (the person
whose thinking is being forged). It is added only where what it finds
genuinely differs from what the existing lenses find. The lenses that
exist are listed in [Critic lenses](../reference/critic-lenses.md).

What every lens shares is owned by the critic's contract, described in
[The critic](../about/the-critic.md). The contract covers the subject,
the way of working and the shape of the report. A lens file never
restates it. A lens may narrow what is read or make a shared rule
stricter. It never renames, drops or duplicates a shared rule or field.

Terms of the forge are glossed in the [Glossary](../reference/glossary.md).

## The files

- `.claude/agents/critic-<lens>.md`: the one new file. It is made from
  the skeleton `templates/critic-definition.md`.

The command `/critique` does not change. It finds lenses by scanning
`.claude/agents/critic-*.md`, so the new file is on the roster as soon
as it exists. The roster line of a lens is its `description`.

## Steps

1. Copy `templates/critic-definition.md` to
   `.claude/agents/critic-<lens>.md`. The suffix is the name of the lens.
2. Fill the front-matter:
   - `name`: `critic-<lens>`.
   - `description`: one line that says what this lens reads. It is the
     roster line, and `/critique` uses it to recommend a lens that
     fits the project. The skeleton's shape is `Critic lens "<lens>" -`
     followed by what the lens reads, then that it reviews the quality
     of the documents and is not a challenger of the thinking.
   - `tools`: `Read, Glob, Grep`, as the skeleton has them.
   - `model`: `inherit`.
   - `skills`: a list holding `critic-contract`.
3. Quote the description if it needs it. A description that carries a
   colon followed by a space is put whole in single quotes, with an
   apostrophe inside doubled. Otherwise the agent does not register.
4. Delete the comments of the skeleton from the file.
5. Write the section `## Lens` in four parts:
   - What you read: each artefact on its own, or the chain as a whole,
     and how a target narrows it.
   - What to go after: the defects this lens exists to find, as a list
     of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what the lens appends to the shared report
     shape, if anything.
6. Check that the section restates nothing of the contract and takes no
   angle from an existing lens as its own.

## A worked example

The shape of a lens file, with `<lens>` standing for the name and the
bracketed words for what the extender writes:

```markdown
---
name: critic-<lens>
description: Critic lens "<lens>" - <what this lens reads, in one line>. Reviews the quality of the documents. Not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

<What you read: ...>

<What to go after: a list of concrete angles>

<Categories: the words of the [category] field>

<Own report sections: what the lens appends, if anything>
```

## Prove it

Run the check on the engine, so that the new file is verified against
the conventions. Among other things it verifies that every skill an
agent names in its front-matter exists, because Claude Code skips a
missing one without a word.

```
/check engine
```

Then run the lens on a project, so that you see it work. Replace
`<lens>` with the name of the lens and `<slug>` with the slug of the
project. The target and the slug are optional.

```
/critique <lens> <slug>
```

You should now see the report of the lens, filed in the `reviews/`
folder of the project, and its delta summary.

## Record and release

Record the change and release it as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) says.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
