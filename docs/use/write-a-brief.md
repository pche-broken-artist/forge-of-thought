---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - CLAUDE.md
---

# Write a brief

This page is for the person who has an idea and wants to put it into
a brief with the forge: to compose one from nothing, to finish one
begun elsewhere, or to store one already written.

## Start the command

```
/forge brief [name] [slug]
```

Without a name the command works on `00-brief.md`. With a name it
works on `00-brief-<name>.md`, a later brief for a new whole of
thinking that arises during the project's life. The slug names the
project. If the brief does not exist yet, the command creates it
from the template, with its history companion and a row in the
ledger's Briefs table (Mined: pending).

## The three ways the text arrives

- **Pasted whole.** You paste the finished text. It is stored
  verbatim, and you are asked whether it is finished. If you say so,
  the brief is approved at once.
- **Begun outside.** You bring what you have. It is stored as it
  came, and the work continues from where the text stops.
- **Born in the forge.** You open with a rough idea. Claude is
  active at the opening: he inspires, brings how the same thing is
  done elsewhere, says how original the idea is, and verifies what
  can be verified. He may propose research and the ingest of
  outside material. Both run only on your word: see
  [Research a topic](research-a-topic.md) and
  [Register a source](register-a-source.md). A proposal of his,
  however large, serves the finding and is not the brief. When the
  brief is being written, Claude moves you to say what you want, why
  and what you do not want, and on your word to write he sets down
  what the talk arrived at. A summary or structured proposal you ask
  him to record is stored as shown.

What goes into the brief and what stays out is your decision. What
stays out lives in `research/` and `sources/` where it is a finding
or a source, and otherwise nowhere.

## What you can ask for

- **A structure.** At any time you can have the text gathered under
  headings in a logical order, with repetitions pointed out and the
  grammar mended. Nothing is added, nothing dropped, no thought
  reworded. The structure is shown before it is written, and you
  rename the headings. It is never a condition of approval.
- **An opinion.** `??` alone at the end of your message, or as the
  whole message, asks for Claude's honest opinion of what you have
  just written: three points at most, marked as his own, nothing
  written.

If the talk turns to taking the idea apart piece by piece
(definitions, wording), Claude says in one sentence that this is the
intent's work and offers once to go on there. You decide whether it
stays in the brief as one open line or is let go. What does not fit
(a wrong assumption, a contradiction, a risk) he says at once, in
one sentence.

## What the brief looks like

The file has a short fixed header (project, title, date, author,
version, status, last change); the text under it is free form. Use
any headings, tables or lists you find useful. There are no IDs. The
brief is kept in whatever language it is written in.

Where the identity of a source supports, limits or contradicts the
thought, the text carries `(source: <path>)`. A short `(remark: …)`
keeps a reservation or uncertainty visible. Nothing marks who said
what.

## Writing, approving, mining

- Each round is written once, on your confirmation, and the brief's
  version and history are updated.
- Before approval is offered, the closing walk asks whether each
  area of the finding was consciously considered. It asks and does
  not mend; an area may leave nothing in the brief.
- The brief is approved only on your explicit word. An approved
  brief is changed like any artefact, and a new whole of thinking is
  a new brief.
- At the end Claude names the state of the brief and, if you want it
  mined, proposes `/forge intent`. The brief is mined into the
  intent when you say so, approved or not.

## See also

- [About the brief](../about/the-brief.md): what a brief is and why
  it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the
  brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the
  brief's finding uses.
