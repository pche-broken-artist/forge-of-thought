---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 6292bf1c304f1d52
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

This page is for the extender who wants a new critic lens. A lens is one
agent file that reads the project's documents through one angle of
quality. The page shows how to write that file and prove it works.

## Before you start

A new lens is added only by the principal's decision (the principal is
whoever's thinking is being forged), and only where what it finds
genuinely differs from what the existing lenses find. Read the list of
lenses that exist first: [Critic lenses](../reference/critic-lenses.md).
A lens judges the quality of the documents, never the substance of the
thinking; the substance belongs to the challenger. What the shared part
of every lens does is described in [The critic](../about/the-critic.md).

The addition is recorded and released as any change of the forge. How a
change is made is in [Make a change to the forge](how-a-change-is-made.md).
Terms of the forge are in the [Glossary](../reference/glossary.md).

## The files

One file is added:

- `.claude/agents/critic-<lens>.md`

Start it from the template `templates/critic-definition.md`. The template
holds the front-matter and the Lens section and nothing else. The command
`/critique` does not change: it finds a lens by scanning the agent files,
so the new file is on the roster as soon as it exists.

The behaviour every lens shares (the subject, the way of working, the
shape of the report) is owned by the contract, which is preloaded into the
lens through its front-matter. The lens file never restates any of it.

## Steps

1. Copy the template to `.claude/agents/critic-<lens>.md`. The lens name
   is the suffix of the agent name.

2. Fill the front-matter. It has these keys:

   - `name`: `critic-<lens>`
   - `description`: the roster line (see step 3)
   - `tools`: `Read, Glob, Grep`
   - `model`: `inherit`
   - `skills`: a list with one entry, `critic-contract`

3. Write the description. It is the line the bare `/critique` roster
   shows, and the fit that Claude recommends from. It says what this lens
   reads, in one line, that it reviews the quality of the documents, and
   that it is not a challenger of the thinking.

   If the description holds a colon followed by a space, put the whole
   description in single quotes. An apostrophe inside the quotes is
   doubled. Without the quotes the agent does not register.

4. Write the Lens section, in four parts:

   - What you read: each artefact on its own, or the chain as a whole,
     and how a target narrows the run.
   - What to go after: the defects this lens exists to find, as a list of
     concrete angles.
   - Categories: the vocabulary of the category field of a finding.
   - Own report sections: what the lens adds to the shared report shape,
     if anything.

5. Delete the comment that the template carries. Leave nothing in the file
   that the contract already says. A Lens section specialises the
   contract: it may narrow what is read or make a shared rule stricter,
   and it never renames, drops or duplicates a shared rule or field.

You should now see the file in `.claude/agents/` holding only the
front-matter and the Lens section.

## A worked example

The shape of a lens file, with `<lens>` as the placeholder. The angles
here are generic and stand for whatever the new lens is about.

```markdown
---
name: critic-<lens>
description: 'Critic lens "<lens>": reads <what it reads>. Reviews the quality of the documents. Not a challenger of the thinking.'
tools: Read, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

### What you read
<The artefacts or the chain; how a named target narrows the run.>

### What to go after
- <a concrete angle of defect>
- <another concrete angle>

### Categories
<the words allowed in the category field of a finding>

### Own report sections
<a section appended to the report, or "none">
```

The description is quoted whole because it holds a colon followed by a
space.

## Prove it

Run the check of the engine:

```
/check engine
```

You should now see no finding about the new agent file. Then run the lens
on a project:

```
/critique <lens> [artefact] [slug]
```

The lens returns its report, and the command files it in the project's
`reviews/` and offers a walkthrough of the findings. You should now see
the lens on the bare `/critique` roster, its report filed, and the
delta summary presented.

## Record and release

Record the new lens and release it as any other change, as described in
[Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
