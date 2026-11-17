---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 4d4cd7adb15973b6
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how to compose or finish a brief with `/forge brief`.
A brief is the idea put together in free form, before it is sifted
into the intent. It is written for the principal, the person whose
thinking is being forged. For what a brief is and why it is rough on
purpose, see [The brief](../about/the-brief.md). Terms of the forge
are one line each in the [Glossary](../reference/glossary.md).

## When to use it

- You have an idea and want to put it together as a brief.
- You have text written elsewhere and want it kept as the brief.
- You have a brief that is begun and want to finish it.
- You have a new whole of thinking in a project that already has a
  brief, and you want it born as a brief of its own.

## The command

```
/forge brief [name] [slug]
```

Without a name the command works on `00-brief.md`. With a name it
works on `00-brief-<name>.md`, a later whole of thinking born during
the project's life. The slug names the project. For example:

```
/forge brief pricing my-project
```

## What happens

The text arrives in one of three ways. Claude resolves the project
and the file first, and creates the brief with its history companion
if it does not exist.

1. **Pasted whole.** You give the finished text. Claude stores it
   verbatim and asks whether it is finished. If you say so, it is
   approved at once.
   You should now see the text stored unchanged, and the question
   whether it is finished.

2. **Begun outside.** You give what you have. Claude stores what came
   and works from where it stops.
   You should now see your text stored as it came, and Claude's first
   question about what follows it.

3. **Born in the forge.** You open with a rough idea. Claude is the
   active one at the opening. It brings how the same thing is done
   elsewhere, says how original the idea is, verifies what can be
   verified and draws out what you want, why and what you do not
   want. It may propose [research](research-a-topic.md) or
   [ingest of a source](register-a-source.md), and each runs only on
   your word. After a research step Claude says what it changed in the
   thought, what stays uncertain and whether more research is likely
   to change anything. Whether to go on is yours to say.
   You should now see proposals for research or ingest, each waiting
   for your word.

4. **The write.** The brief is written once per round, on your
   confirmation. Claude takes what the talk arrived at and writes it
   down, condensed where the talk was long, and shows you any wording
   of its own before it is written. A summary or a structured proposal
   you ask to record is stored as shown.
   You should now see the brief file named, with its version raised
   and the change recorded in its history.

5. **The close.** Before the approval is offered, Claude looks once
   over what the finding covered. The brief is approved only on your
   explicit word. Claude then names the state and offers
   `/forge intent` when you want the brief mined.
   You should now see the state of the brief named.

## What you can ask for

- **A structure.** At any time you may ask Claude to give the brief a
  structure: the text gathered under headings in a logical order,
  what repeats pointed out, the grammar mended. Claude adds nothing,
  drops nothing and rewords no thought. It shows the structure before
  it is written, and the headings are yours to rename. The step is
  never a condition of the approval.
- **Claude's opinion.** `??` alone at the end of your message, or as
  the whole message, asks for Claude's honest opinion of what you have
  just written. It gives three points at most, marked as its own,
  and writes nothing.

Claude also says at once and unasked, in one sentence, what does not
fit: a wrong assumption, a contradiction or a risk. What goes into the
brief and what stays out is yours to say.

## What you have afterwards

- A `00-brief.md` or `00-brief-<name>.md` with a short header (project,
  title, author, version, status) and free text below it. It has no
  IDs and no conventions of the chain.
- A history companion that records each change.
- A text kept in the language it is written in.
- A brief that stays a draft until you approve it. An approved brief
  is changed like any artefact, and a new whole is a new brief.
- A brief mined by `/forge intent` only when you say so, approved or
  not. The ledger (the table of state, made when it is read) shows
  how far each brief is mined, in its Briefs table.

## If something goes wrong

- If the talk turns to taking the brief apart piece by piece, such as
  definitions, blocks or wording, Claude says in one sentence that
  this is the intent's work and offers once to go on there. This is a
  recommendation, not a gate. You decide whether it stays in the brief
  as one open line or is let go.
- If you want something recorded that Claude proposed but you did not
  take, say so. Otherwise it is left out.
- If the brief seems too rough, that is intended: it is composed in a
  round or two and then mined.

## A worked example

You type:

```
/forge brief my-project
```

You answer Claude's opening with a rough idea: a shared booking
calendar for three small teams, because they now trade e-mails, and
no new tool to be bought. Claude replies that tools of this kind
exist, names how they differ, and proposes one research step on
existing calendar sharing. You say yes, and the note is filed.
Claude says what it changed: one assumption does not hold, and one
question stays open. You say "write". Claude shows the condensed text,
with its own wording marked, and you confirm it. The file is written
as version 0.1. Later you ask for a structure, check the headings and
approve the brief. Claude names the state as approved and offers
`/forge intent`.

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is
  rough on purpose.
- [Research a topic](research-a-topic.md): the research step the
  brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the
  brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
