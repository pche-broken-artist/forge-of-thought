---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: db41d22110d42860
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how you compose or finish a brief with `/forge brief`.
A brief is your own rough text of what you want and why, the
starting point of a project (see [The brief](../about/the-brief.md)).
It is for the principal, the person whose thinking is being forged.

## When to use it

- You have an idea and no brief yet: you begin one.
- You have a brief that is not finished: you continue it.
- You have a brief that is approved and a new whole of thinking
  arises during the project: you start a later brief beside it.

## The command

```
/forge brief [name] [slug]
```

Bare, the command works on `00-brief.md`. With a name, it works on
`00-brief-<name>.md`, a later whole of thinking born during the
project's life. The slug names the project; it can be left out
where the project is clear.

For example, a later brief on a new topic in a project called
`my-idea`:

```
/forge brief pricing my-idea
```

## What happens

Claude first finds the project and the file. If the brief does not
exist, Claude creates it from the template: a short header (project,
title, author, version, status) and nothing else, with a history
companion beside it. The text below the header is free. After that,
what happens depends on how your text arrives.

1. **You paste the whole text.** Claude stores it verbatim and asks
   whether it is finished. If it is, the brief can be approved at
   once.
   You should now see the pasted text in the brief file, unchanged.
2. **You began the text outside.** Claude stores what came, then works
   with you from where it stops.
   You should now see your text in the brief file, with the talk
   continuing at its last line.
3. **The brief is born here.** You open with a rough idea. Claude is
   active from the first word. It inspires, says how the same thing
   is done elsewhere and how original the idea is, checks what can
   be checked, and confronts and draws out what you have not yet
   said. It also proposes research (see
   [Research a topic](research-a-topic.md)) and ingest of outside
   material (see [Register a source](register-a-source.md)), each
   against a named need, and runs it on your word. After a research
   step, Claude says what it changed in the thought, what stays
   uncertain and whether more research is likely to change anything.
   Going on is yours to decide.
   You should now see research notes or registered sources that the
   brief can cite.
4. **Claude writes the talk down.** It does so once per round, on
   your confirmation. It condenses where the talk was long and
   reflects the wording back to you before it is written. A summary
   or a structured proposal that you ask to record is stored as
   shown.
   You should now see the new text in the brief file and a new
   version in its history.
5. **You decide what goes in.** What you take from the finding into
   the brief is your choice. Claude does not decide it. What stays
   out lives in the research notes and sources where it is a finding
   or a source, and otherwise nowhere.
6. **You approve.** Before the approval is offered, Claude walks
   once through the areas the finding looked at and asks whether
   each was considered. An area may leave nothing in the brief, and
   a tension or an open boundary may stay as it is. The brief is
   approved only on your explicit word.
   You should now see the state named by Claude and, if you want the
   brief mined, the proposal to run `/forge intent`.

### What you can ask for

- **A structure.** At any time you can have Claude gather the text
  under headings in a logical order, point out what repeats and mend
  the grammar. Claude adds nothing, drops nothing and rewords no
  thought. It shows the structure before writing it, and the
  headings are yours to rename. The step is never a condition of the
  approval.
- **Claude's opinion.** Put `??` alone at the end of your message,
  or as the whole message. Claude gives its honest opinion of what
  you have just written, in three points at most, marked as its own.
  Nothing is written or filed.

Apart from this, Claude says at once and unasked, in one sentence,
what does not fit: a wrong assumption, a contradiction, a risk.

## What you have afterwards

- The brief file, `00-brief.md` or `00-brief-<name>.md`, in free
  form: any headings, tables or lists you find useful, and no IDs.
- A history companion beside it that records each version.
- Where a source supports, limits or contradicts a thought, the mark
  `(source: <path>)`; where a reservation must stay visible, a short
  `(remark: ...)`. Nothing in a brief marks authorship.
- A brief kept in the language it is written in.

The brief is not a set of decisions. Its thoughts are still to be
processed and may be changed or dropped when mined. It is mined into
the intent only when you say so, approved or not, by
`/forge intent`. The ledger (the table of the state of every
document, made from the documents when it is read) shows in its
Briefs table how far each brief is mined; a brief not yet mined is
shown as pending.

## If something goes wrong

- **The talk turns to taking the idea apart piece by piece**
  (definitions, blocks, wording). Claude says in one sentence that
  this is the work of the intent and does not develop it. It offers
  once to go on in the intent. That is a recommendation, not a gate.
  You decide whether it stays in the brief as one open line or is
  let go.
- **The brief is already approved and you want to change it.** It is
  changed like any other artefact. A new whole of thinking is a new
  brief, started with a name.
- **You think the brief is too rough.** It is rough on purpose. A
  brief polished until the intent has nothing left to do has gone
  too far.

## A worked example

You type:

```
/forge brief my-idea
```

Claude creates `00-brief.md` for the project `my-idea` and asks you
to open with the idea. You answer in a few rough sentences: you want
a shared calendar for a small team, because meetings keep colliding.
Claude says that shared calendars already exist and asks what yours
would do differently. It proposes a short research step on what
exists, naming the need: a comparison. You say yes, and the note is
filed. Claude says the research shows two close existing tools, that
your idea differs in one respect, and that more research is unlikely
to change that.

You add what you do not want. You end your message with `??`, and
Claude gives three points of opinion, marked as its own, and writes
nothing. You say `write`. Claude reflects the wording back, you
confirm, and it writes the text and a new version. Later you ask for
a structure: Claude shows the text under four headings, you rename
one, and it writes them. When you are content, Claude walks once
through the areas and offers the approval. You approve explicitly,
and Claude names the state, approved and not yet mined, and proposes
`/forge intent` for when you want it mined.

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
