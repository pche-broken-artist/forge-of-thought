---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 0b14ed2906e2a3b6
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how you have a challenger persona attack the substance
of your work with `/challenge`. It is for the principal (the person
whose thinking is being forged) who wants the thinking tested, not the
writing. A persona is an isolated agent (a subagent, which never sees
your conversation with Claude) that hunts one kind of blind spot.

## When to use it

Use it when an artefact of your project is about to become the ground
for the next layer. Run it before the next layer is first derived from
the target: for the intent, before the first layer below it. An accepted
challenge is cheap to absorb at that point. Run it again after any major
shift of direction. Running it on a nearly final artefact is late but
not useless.

The command judges substance only. It never judges the quality of the
document; that is a different command.

## The command

```
/challenge <persona> [artefact|path] [slug]
```

- `persona`: the persona to run. Leave it out and the command lists the
  roster instead.
- `artefact|path`: the target. It is an artefact named as `/forge`
  names it, or any file of the project by its path. Leave it out and
  the whole chain is the target.
- `slug`: the project. Claude infers it from context and asks if it is
  ambiguous.

To see the roster with a recommended fit for your project, type it bare:

```
/challenge
```

The recommendation is advice, never a gate. The personas of today are
listed on [Challenger personas](../reference/challenger-personas.md).

## What happens

1. Claude makes the project's ledger first, so that the agent reads a
   current file. The ledger is the file that holds the state of the
   project. You should now see the ledger remade before the agent
   starts.
2. Claude invokes the persona's agent on the project and names the
   target. The agent gets the project path and the target, nothing
   else. You should now see the agent at work on the target alone.
3. The agent returns a report of three to seven challenges, ordered by
   severity. The report also says what is strong and which questions the
   agent cannot answer from the documents. The agent writes no file.
4. Claude gives each challenge its identifier and files the report
   word for word in the project's `challenges/` folder under a unique
   dated name. Only the identifiers are added. You should now see a new
   file in `challenges/`.
5. Claude presents the result to you: the overall read first, then
   each challenge compressed to two or three sentences. If Claude
   disagrees with a challenge, it says so plainly and separately, marked
   as its own view. You should now see the overall read, the compressed
   challenges and any disagreement of Claude marked as its own.
6. Where the answer to one of the agent's open questions exists in your
   conversation but not in the documents, Claude answers it and flags it
   to you. It usually means something true is missing from the intent.
7. Claude offers a walkthrough of the challenges. A walkthrough settles
   a list one item per message. You should now see the offer. If you
   decline it, the challenges wait.

## What you have afterwards

- A report in `challenges/`, unchanged from what the agent wrote, and
  every challenge entered in the ledger.
- Your verdicts, once you walk through the challenges. The verdict
  `accept` means the challenge is mended through `/forge`, in the
  artefact it concerns. The other verdicts are described on
  [Walk through a list](walk-through-a-list.md).

A rejected challenge is a healthy outcome. So is a challenge that
survives three rounds unresolved: park it and move on. To read why the
agent may be wrong, see [The challenger](../about/the-challenger.md).

## A worked example

Your project `my-project` has an intent you consider finished, and no
layer below it yet.

```
/challenge <persona> intent my-project
```

Claude remakes the ledger, runs the agent on the intent, files the
report in `challenges/` and shows you the overall read with, say, five
challenges, the most severe first. It offers a walkthrough. You accept
the first, so Claude mends the intent through `/forge`. You reject the
second because you know something the documents do not say, and it
stays rejected. The rest you park.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
