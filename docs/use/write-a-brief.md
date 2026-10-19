---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 224aeff7be1a4c5a
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how to compose or finish a brief with `/forge brief`, for the principal (the person whose thinking is being forged). A brief is your own text of what you want, why, and what you do not want. It is rough on purpose, and [The brief](../about/the-brief.md) says why.

## When to use it

Use it when an idea is to be put together as the start of a project, or when a later whole of thinking is born during a project's life. It also fits when you already hold a text and want it stored and approved as a brief.

## The command

```
/forge brief [name] [slug]
```

- Bare, it works on `00-brief.md`.
- With a name, it works on `00-brief-<name>.md`, a later whole of thinking. For example `/forge brief pricing my-project` works on `00-brief-pricing.md` of the project `my-project`.

A project may have more than one brief. A later whole is born as its own brief, under the same rules, so that it does not land in the intent as a batch of unproven positions.

## What happens

Claude creates the brief if it does not exist yet, with its history companion beside it. The file starts from the template: a short header (project, title, author, version, status) and free form below it. Then the text arrives in one of three ways.

1. **Pasted whole.** You paste the finished text. Claude stores it verbatim and asks whether it is finished. If you say yes, it is approved at once.
   You should now see the text stored unchanged in the brief file.

2. **Begun outside.** You bring what you have written elsewhere. Claude stores what came and works from where the text stops.
   You should now see your text in the brief file and Claude continuing at its end.

3. **Born in the forge.** You open with a rough idea. Claude is the active one at the opening: it inspires, brings how the same thing is done elsewhere and how original the idea is, verifies what can be verified, and proposes research and ingest.
   - A research step (see [Research a topic](research-a-topic.md)) is proposed against a named need: an uncertainty, a comparison or an inspiration. After it, Claude says what it changed in the thought, what stays uncertain and whether more research is likely to change anything.
   - An ingest step (see [Register a source](register-a-source.md)) brings outside material into the project's sources.
   - Both run only on your word. Whether to go on is yours to say.
   You should now see findings in the project's research and sources, kept apart from the brief.

   Then the brief is written. Claude moves you to say what you want, why and what you do not want. On your word to write, it takes what the talk arrived at and writes it down so that it is understood. It may translate, mend the grammar, and word an idea of its own that you accepted. What it formulated, it reflects back before it is written.
   You should now see a draft of the brief and the version bumped once for the whole round.

Whichever way the text arrived, these rules hold:

- What goes into the brief is your decision, and what stays out lives in the research and the sources, or nowhere. The brief is not the record of the finding.
- Claude writes once per round, on your confirmation.
- Claude does not decide what goes in, and it does not chisel the text into an intent. If the talk turns to taking the idea apart piece by piece (definitions, blocks, wording), Claude says in one sentence that this is the intent's work and offers once to go on there. You decide whether it stays in the brief as one open line or is let go.
- Before the approval is offered, Claude walks the areas of the finding once: the thought, the boundaries, the world around it, the material and what is still open. The walk asks and does not mend. An area may leave nothing in the brief, and a tension or an open point may stay as it is.
- The brief is approved only on your explicit word. The command ends by naming the state and proposing `/forge intent` if you want the brief mined.

## What you can ask for

- **A structure.** At any time you can have Claude give the text a structure: it gathers the text under headings in a logical order, points out what repeats and mends the grammar. It adds nothing, drops nothing and rewords no thought. It shows the structure before it is written, and the headings are yours to rename. It is never a condition of the approval.
- **Claude's opinion.** `??` alone at the end of your message, or as the whole message, asks for Claude's honest opinion of what you just wrote: three points at most, marked as Claude's own, nothing written.
- **A recorded summary.** A summary or a structured proposal you ask to record is stored as shown, never re-told in other words.

Without being asked, Claude says in one sentence what does not fit: a wrong assumption, a contradiction or a risk.

## What you have afterwards

- A brief file, `00-brief.md` or `00-brief-<name>.md`, with its history companion.
- A text in free form: any headings, tables or lists you find useful, and no IDs. A source is marked `(source: <path>)` only where its identity supports, limits or contradicts the thought. A short `(remark: ...)` marks a reservation or uncertainty that must stay visible. Nothing in the text marks who said what.
- A brief kept in the language it is written in.
- Status `draft` until you approve it, and then approved.
- Nothing in it is yet a position. Its thoughts are to be processed when mined, and may be changed, reworked or dropped.

The brief is mined into the intent by `/forge intent`, when you say so, approved or not. How far each brief has been mined is shown in the Briefs table of the ledger (the project's state report). It reads the header and the mining record in the intent's history, and says pending until one exists. Terms of the forge are in the [Glossary](../reference/glossary.md).

## If something goes wrong

The inputs name no stop conditions or messages for this job. Two things are stated:

- A brief that is already approved is changed like any other artefact. A new whole of thinking is a new brief, not a change of the old one.
- If the work seems to have drifted into the intent's work, Claude says so once. Take the offer or leave it, as you decide.

## A worked example

A generic exchange, with a placeholder slug `my-project`.

```
You:     /forge brief my-project
You:     I want a weekly digest of what changed across our
         teams' documents, so nobody has to read everything.
Claude:  Two things come to mind. Similar digests exist as
         newsletters built from change logs, and the hard part
         there is deciding what counts as a change worth
         reading. Shall I research how others filter, and
         register the one internal note you mentioned?
You:     Yes, research that. Skip the note for now.
Claude:  (runs the research) It found that most digests fail
         on volume, not on content. That sharpens your aim but
         does not settle what "worth reading" means.
You:     ??
Claude:  My own view, three points: the aim is clear; the
         boundary of "teams" is open; "weekly" may follow from
         the volume, not be a given.
You:     Write it down, and I will say when it is done.
Claude:  Here is what I understood: ... (reflected back)
You:     Good. write
Claude:  Written to 00-brief.md, version 0.1, draft. Give it a
         structure, approve it, or go on?
You:     Approved. Mine it later.
Claude:  The brief is approved. When you want it mined, run
         /forge intent.
```

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
