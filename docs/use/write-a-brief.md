---
generated: 2026-10-10
made: mirrored
inputs-hash: e66d9690d28e6ff7
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - CLAUDE.md
---

# Write a brief

This page is for the person who has an idea and wants to put it
together as a brief: the first document of a project, in which the
idea is stated as what he wants, why, and what he does not want. It
says how to start the command, how the text can arrive and what you
can ask for along the way.

## Start

Run `/forge brief [name] [slug]`.

- Without a name, the command works on `00-brief.md`, the brief of
  the project.
- With a name, it works on `00-brief-<name>.md`: a later whole of
  thinking born during the life of the project, under the same
  rules. A new whole is a new brief; it does not reopen the first.
- If the brief does not exist yet, the command creates it from the
  template, with its history companion and its row in the ledger.
  An approved brief is changed like any other document of the
  chain.

## How the text arrives

There are three ways, and each is handled differently.

**Pasted whole.** You paste a finished text. It is stored exactly
as you gave it, and you are asked whether it is finished. If you say
it is, the brief is approved at once.

**Begun outside.** You began the text elsewhere. What you bring is
stored as it came, and the work goes on from where it stops.

**Born in the forge.** You open with a rough idea. At the opening
Claude is the active one: he inspires, tells you how the same thing
is done elsewhere and how original the idea is, and verifies what
can be verified. He may propose research or the registration of
outside material. Nothing of that runs on his own: each step runs
on your word, as [Research a topic](research-a-topic.md) and
[Register a source](register-a-source.md) describe. After a
research step he says what it changed in the thought, what stays
uncertain and whether more research is likely to change anything;
whether to go on is yours to say.

Then the brief is written. Claude moves you to say what you want,
why and what you do not want. When you tell him to write, he takes
what the talk arrived at and writes it down so that it is
understood: condensed where the talk was long, reflected back to
you before it is written. A summary or a structured proposal you
ask him to record is stored as shown, not told again in other
words. The writing happens once per round, on your confirmation.

## What you can ask for

- **A structure.** At any time you can have the text gathered under
  headings in a logical order, with what repeats pointed out and
  the grammar mended. Nothing is added, nothing dropped and no
  thought reworded. You see the structure before it is written, and
  the headings are yours to rename. It is never a condition of
  approval.
- **Claude's opinion.** `??` alone at the end of your message, or as
  the whole message, asks what he honestly thinks of what you have
  just written: three points at most, marked as his own, nothing
  written.

What does not fit he says at once and unasked, in one sentence: a
wrong assumption, a contradiction, a risk. What goes into the
brief and what stays out is yours to decide. If the talk turns to
taking the idea apart piece by piece, he says in one sentence that
this belongs to the next step and offers once to go on there; you
decide whether it stays in the brief as one open line or is let go.

## What the brief is

The brief is free form: a short header, then whatever headings,
tables or lists you find useful. It carries no IDs and none of the
conventions of the later documents, and it is kept in the language
it is written in. It is rough on purpose: its usual shape is the
topics of the whole, each with a few sentences of what you want of
it, the research that verifies or limits it beside it, and what is
still open. Where a source supports, limits or contradicts a
thought, it is cited beside it as `(source: <path>)`; a short
`(remark: ...)` keeps a reservation visible.

## Approve, then mine

Before the approval is offered, the areas the finding looked at are
walked once, as questions, to see that each was considered. The
walk does not mend anything: a tension or an open question may stay
in the brief.

The brief is approved only on your explicit word. The command ends
by naming the state of the brief and proposing `/forge intent` when
you want it mined. Mining happens when you say so, whether the
brief is approved or not.

## See also

- [About the brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
