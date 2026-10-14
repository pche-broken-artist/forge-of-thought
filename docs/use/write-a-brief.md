---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: d78323aedd1dae4f
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how to compose or finish a brief with `/forge brief`, for the principal (the person whose thinking is being forged). A brief is the idea put together in free form, before it is sifted into the intent.

## When to use it

Use it when you have an idea to put together, however far it has got: written whole elsewhere, begun and left unfinished, or only a rough thought. Use it again later for a new whole of thinking that arises during a project's life. For what a brief is and why it is rough on purpose, see [The brief](../about/the-brief.md).

## The command

```
/forge brief [name] [slug]
```

Without a name the command works `00-brief.md`. With a name it works `00-brief-<name>.md`, a later whole of thinking. The slug names the project; leave it out where the project is clear. For example, `/forge brief pricing my-project` works `00-brief-pricing.md` of the project `my-project`.

## What happens

Claude first finds the project and the file. If the brief does not exist, Claude creates it from the template, with its history companion and its row in the ledger's Briefs table (Mined: pending). The ledger is the file that holds the state of the project. The template fixes only a short header: project, title, date, author, version, status and the last change. Everything below the header is free form.

What happens next depends on how the text arrives.

1. **The text is pasted whole.** Claude stores it as it came, word for word, and asks whether it is finished. If you say it is, the brief is approved at once.
   You should now see the brief stored unchanged, and a question whether it is finished.

2. **The text was begun outside.** Claude stores what came and then works from where it stops.
   You should now see your text stored as it was, and Claude taking up the conversation at its end.

3. **The brief is born here from a rough idea.** You open with the idea and Claude is active from the first word. It inspires, brings how the same thing is done elsewhere and how original the idea is, and verifies what can be verified. It proposes research with [Research a topic](research-a-topic.md) and ingest of outside material with [Register a source](register-a-source.md). Both run only on your word.
   You should now see a proposal of a research step against a named need, and after it a note of what it changed in the thought, what stays uncertain and whether more research is likely to change anything. Whether to go on is yours to say.

   Then the brief is written. Claude moves you to say what you want, why and what you do not want. On your word to write, it takes what the talk arrived at and writes it down so that it is understood. It may translate, mend the grammar and word an idea of its own that you have accepted, and it reflects that wording back before writing. A summary or a structured proposal that you ask it to record is stored as shown, never retold.
   You should now see the restated text before it is written, and then the file written once for the round.

Throughout, what goes into the brief and what stays out is your decision. Claude says at once, in one sentence, what does not fit: a wrong assumption, a contradiction or a risk. If the talk turns to taking the idea apart piece by piece (definitions, blocks, wording), Claude says that this is the intent's work and offers once to go on there. You decide whether that stays in the brief as one open line or is let go.

At the closing, before the approval is offered, the brief is checked against a short list of areas. Each is asked whether it has been considered, and an area may leave nothing in the brief. The check asks and does not mend: a tension or a vague boundary may stay as it is. Claude then ends by naming the state of the brief and proposing `/forge intent` if you want it mined.
You should now see the state named: draft or approved.

## What you can ask for

- **A structure.** At any time you may ask Claude to give the brief a structure: the text gathered under headings in a logical order, what repeats pointed out, the grammar mended. Claude adds nothing, drops nothing and rewords no thought. It shows the structure before it is written, and the headings are yours to rename. The step is never a condition of the approval.
- **Claude's opinion.** `??` alone at the end of your message, or as the whole message, asks for Claude's honest opinion of what you have just written. It gives three points at most, marked as its own, and writes nothing.

## What you have afterwards

- A file `00-brief.md`, or `00-brief-<name>.md`, in free form with no IDs and none of the conventions of the chain.
- Its history companion and its row in the ledger, updated with every version.
- Research notes and registered sources beside it, where the finding produced them. What stayed out of the brief lives there where it is a finding or a source, and otherwise nowhere.

The brief stays a draft until you say it is complete and approve it, in so many words. Approval is on your explicit word only. An approved brief is changed like any other artefact (a document of the chain), and a new whole is a new brief. The brief is mined into the intent when you say so with `/forge intent`, approved or not. Nothing in a brief is yet a position, so its thoughts may be changed, reworked or dropped when mined.

In the brief, `(source: <path>)` marks a thought that a source supports, limits or contradicts. A short `(remark: ...)` keeps a reservation or an uncertainty visible. Nothing marks who said what.

## A worked example

A generic exchange, with a placeholder project `my-project`.

```
You:     /forge brief my-project
You:     I want to replace our weekly status meeting with a short
         written update. People spend an hour and learn little.
Claude:  Teams that moved to written updates often report ... Shall I
         research what is known about it, against the question
         "does it lose the discussion"?
You:     yes
Claude:  (runs /research; then) It showed that discussion moves to
         comments. It is still uncertain for large teams. More
         research is unlikely to change that.
You:     ??
Claude:  Three points, my own: ...
You:     write
Claude:  Here is what I will write: ... Confirm?
You:     write
Claude:  Written: 00-brief.md, version 0.1, draft. Say when it is
         complete and approved. /forge intent mines it when you want.
```

## If something goes wrong

The inputs record no error messages of the command. What they set as limits is this:

- The brief is never approved without your explicit word.
- Nothing is written before you confirm, and one write is made per round.
- A walkthrough never runs over the text of a brief.

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
