---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: b674f050961782b4
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how to compose or finish a brief with `/forge brief`, for the principal (the person whose thinking is being forged). A brief is the principal's idea put together in free form, before it is sifted into an intent. For what a brief is and why it is rough on purpose, see [The brief](../about/the-brief.md).

## When to use it

Use it when you have an idea to put together, whether it is a text you already have, a text you began elsewhere, or only a rough thought. Use it again for a later whole of thinking born during the project's life, which gets a brief of its own.

## The command

```
/forge brief [name] [slug]
```

Bare, the command works on `00-brief.md`. With a name, it works on `00-brief-<name>.md`, a later whole of thinking. The slug names the project; leave it out when Claude can resolve the project itself. For example, `/forge brief pricing my-project` works on `00-brief-pricing.md` of the project `my-project`.

## What happens

The text of a brief arrives in one of three ways. Claude first resolves the project and the file. If the brief does not exist, Claude creates it with its history companion (the file beside it that records each change).

1. **Pasted whole.** Claude stores the text verbatim and asks whether it is finished. If it is, you can approve it at once.
   You should now see the brief stored as you gave it, with the question whether it is finished.
2. **Begun outside.** Claude stores what came and works from where the text stops.
   You should now see your text stored unchanged, and Claude's questions starting at its end.
3. **Born in the forge from a rough idea.** You open with the idea. At the opening Claude is the active one. It inspires, brings how the same thing is done elsewhere and how original the idea is, and verifies what can be verified. It proposes research and ingest, and runs each only on your word. A research step is [Research a topic](research-a-topic.md), and ingest is [Register a source](register-a-source.md). After a research step Claude says what it changed in the thought, what stays uncertain and whether more research is likely to change anything. You decide whether to go on.
   Then the brief is written. Claude moves you to say what you want, why and what you do not want. When you say to write, it takes what the talk arrived at and writes it down, condensed where the talk was long. It reflects back any wording of its own before it is written.
   You should now see the brief written once for the round, in wording you have confirmed.

Throughout, the brief stays yours. Claude does not decide what goes in and does not chisel it into an intent. A proposal of Claude's, however large, serves the finding and is not the brief. When something does not fit, such as a wrong assumption, a contradiction or a risk, Claude says so at once in one sentence. When the talk turns to taking the idea apart piece by piece (definitions, blocks, wording), Claude says in one sentence that this is the intent's work and offers once to go on there. You decide whether it stays in the brief as one open line or is let go.

When you think the brief is complete, Claude walks the areas of the finding once before it offers the approval:

- the thought
- the boundaries
- the world around it
- the material
- what is still open

An area may leave nothing in the brief. The walk asks and does not mend, so a tension or a vague boundary may stay as it is.

## What you can ask for

- **A structure.** At any time you can ask Claude to give the brief a structure. It gathers the text under headings in a logical order, points out what repeats and mends the grammar. It adds nothing, drops nothing and rewords no thought. It shows you the structure before writing it, and the headings are yours to rename. The step is never a condition of the approval.
- **Claude's opinion.** Put `??` alone at the end of your message, or as the whole message. Claude gives its honest opinion of what you have just written, marked as its own. Nothing is written.

## What you have afterwards

- A brief in free form: a short YAML header (project, title, author, version, status) and then any headings, tables or lists you find useful. It carries no IDs and no conventions of the chain, and it is kept in the language it is written in.
- Its history companion.
- Nothing in it marks authorship. `(source: <path>)` stands where the identity of a source supports, limits or contradicts the thought. A short `(remark: ...)` stands where a reservation or an uncertainty must stay visible.
- A draft until you approve it. Claude approves only on your explicit word.
- Mining into the intent only when you say so. The brief is mined by `/forge intent`, approved or not, and Claude ends by naming the state and proposing it when you want it. The ledger's Briefs table shows how far each brief has been mined, and reads "pending" until a mining is recorded.

An approved brief is changed like any other artefact. A new whole of thinking is a new brief.

## A worked example

The exchange is generic and runs in a project with the placeholder slug `my-project`.

```
You:     /forge brief my-project
You:     I want a lighter way to review the team's weekly
         reports. Too much time goes on them.
Claude:  Two questions before I propose anything: what is
         the report for, and who reads it?
You:     It keeps the group informed. The managers read it.
Claude:  Similar reviews are done elsewhere with a short
         monthly digest. Shall I run /research on that?
You:     Yes.
Claude:  (runs the research) It supports a digest for
         status, but not for risks. More research is
         unlikely to change that. Shall we go on?
You:     Enough. Write what we have.
Claude:  Here is what I will write: the thought, what you do
         not want, the research that limits it, one open
         line. Write it?
You:     Write.
Claude:  Written to 00-brief.md, version 0.1, draft. Say
         when you approve it, and /forge intent when you
         want it mined.
```

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
