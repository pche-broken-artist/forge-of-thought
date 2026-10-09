---
generated: 2026-10-09
made: mirrored
inputs-hash: 21d5c3a46bb57db9
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - CLAUDE.md
---

# Write a brief

This page is for a user who has an idea and wants to put it into a
brief: the first document of a project, written in the user's own
words. It says which command to run, how the text can arrive and what
happens with each way.

## The command

```
/forge brief [name] [slug]
```

Bare, the command works on `00-brief.md`, the project's first brief.
With a name it works on `00-brief-<name>.md`, a later brief for a
whole of thinking that is born during the project's life. The slug
names the project; leave it out when the command can tell which one
you mean. If the brief does not exist yet, the command creates it
with its history file and a row in the ledger's Briefs table. If it
exists, even approved, it is changed like any other artefact. A new
whole of thinking is a new brief, not an edit of the old one.

## What a brief looks like

A new brief starts from a skeleton: a short header (project, title,
date, author, version, status, last change) and nothing else. Under
it the text is free form. Use any headings, tables or lists that
help. There are no IDs and no conventions of the chain. The brief
is kept in the language it is written in. It is rough on purpose: it
says what you want, why, and what you do not want. Polishing it is
the work of the next step.

## The three ways the text arrives

- **Pasted whole.** You paste a finished text. It is stored exactly
  as it came. You are asked whether it is finished. If you say it
  is, it is approved at once.
- **Begun outside.** You started the text elsewhere. What you bring
  is stored as it is, and the work goes on from where it stops.
- **Born in the forge.** You open with a rough idea. At the opening
  Claude is active: he inspires, tells you how the same thing is done
  elsewhere, checks what can be checked, and proposes research and
  ingest. Both run only on your word. Research stores a durable
  note (see [Research a topic](research-a-topic.md)). Ingest
  registers outside material as a source (see
  [Register a source](register-a-source.md)). After a research
  step Claude says what it changed in the thought, what stays
  uncertain and whether more research is likely to change anything.
  Whether to go on is yours to say. Once the finding is wide enough,
  the brief is written. Claude condenses a long talk into the text,
  and he reflects it back to you before it is written. A summary or
  structured proposal you ask him to record is stored as you showed
  it, not re-told.

The brief is written once per round of conversation, on your
confirmation, and each write is one new version with its history
record.

## What you can ask for

- **A structure.** At any time you can ask Claude to give the brief
  a structure: the text gathered under headings in a logical order,
  repetitions pointed out, grammar mended. He adds nothing, drops
  nothing and rewords no thought. He shows you the structure before
  it is written, and the headings are yours to rename. It is never a
  condition of approval.
- **His opinion.** Put `??` alone at the end of your message, or as
  the whole message, and Claude gives his honest opinion of what
  you wrote: three points at most, marked as his own. Nothing is
  written or filed.

Claude also speaks up unasked, in one sentence, when something does
not fit: a wrong assumption, a contradiction, a risk. If the talk
turns to taking the idea apart piece by piece, he says that this is
the intent's work and offers once to go on there. You decide whether
it stays in the brief as one open line or is let go.

## Marks in the text

Nothing in a brief says who wrote it. Two marks may appear.
`(source: <path>)` stands where the identity of a source supports,
limits or contradicts the thought. A short `(remark: ...)` stands
where a reservation or an uncertainty must stay visible. A
suggestion you did not take is gone, unless you say it stays.

## Approval and what follows

The brief is finished when you say so and approve it. Approval is
only on your explicit word. Before it is offered, Claude walks the
areas the finding looks at, once, and asks whether each was
considered. An area may leave nothing in the brief, and the walk
asks without mending. At the end Claude names the state of the brief
and proposes `/forge intent` if you want it mined. The brief is
mined into the intent only when you say so, approved or not. The
ledger's Briefs table tracks how far each brief has been mined.

## See also

- [About the brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
