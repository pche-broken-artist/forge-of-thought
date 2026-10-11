---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: d83d37552e5ff035
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how you compose or finish a brief with
`/forge brief`. A brief is the first document of a project: the
idea put together, rough on purpose. It is for the principal (the
person whose thinking is being forged) who has an idea, a draft or a
pasted text and wants it set down. What a brief is, and why it is
rough, is on [The brief](../about/the-brief.md); terms of the forge
are in the [Glossary](../reference/glossary.md).

## When to use it

- You have an idea and want to put it together with Claude.
- You have a text from elsewhere and want it kept as the brief.
- The project already has a brief and a new whole of thinking
  has been born during its life. That whole gets a brief of its own.

## The command

```
/forge brief example-project
```

With a name, the command makes a later brief for the same project:

```
/forge brief pricing example-project
```

The bare form works on `00-brief.md`. The named form works on
`00-brief-pricing.md`. The slug is optional in both forms, as in the
command's shape `/forge brief [name] [slug]`.

## What happens

The text arrives in one of three ways. Claude first finds or
creates the file, with its history companion and its row in the
ledger (the table that holds a project's state), if they do not
exist. Then it works the way that fits.

1. **You paste the whole text.** Claude stores it verbatim and asks
   whether it is finished. If you say yes, it approves the brief
   at once.
   You should now see the brief stored as you pasted it, and its
   state named.
2. **You began outside the forge.** Claude stores what came and
   works from where the text stops.
   You should now see your text stored, and Claude's questions
   starting at its end.
3. **The brief is born here, from a rough idea.** You open with
   the idea. At the opening Claude is the active one:
   - it inspires and brings how the same thing is done elsewhere
   - it says how original the idea is
   - it verifies what can be verified
   - it proposes research and ingest

   Research ([Research a topic](research-a-topic.md)) and ingest
   ([Register a source](register-a-source.md)) run only on your
   word. After a research step Claude says what it changed in the
   thought, what stays uncertain and whether more is likely to
   change anything. Whether to go on is yours to say.
   You should now see proposals from Claude, and notes in
   `research/` or `sources/` for each step you allowed.

   Then the brief is written. Claude moves you to say what you
   want, why and what you do not want. On your word to write, it
   sets down what the talk arrived at, condensed where the talk was
   long, and reflects back first any wording of its own. A summary
   or a structured proposal you ask it to record is stored as
   shown, never retold.
   You should now see the text written once for the round, and the
   version and the ledger row updated.

Claude does not decide what goes in. If the talk turns to taking
the idea apart piece by piece (definitions, blocks, wording), it
says in one sentence that this is work for the intent, and offers
once to go on there. You decide whether the matter stays in the
brief as one open line or is let go.

## What you can ask for

- **A structure.** At any time you can have Claude gather the text
  under headings in a logical order, point out what repeats and
  mend the grammar. It adds nothing, drops nothing and rewords no
  thought. It shows the structure before writing it, and the
  headings are yours to rename. You can ask for it, and it is never
  a condition of approval.
- **Its opinion.** Put `??` at the end of your message, or send it
  alone, and Claude gives its honest opinion of what you have just
  written, marked as its own. Nothing is written or filed.

Without being asked, Claude says in one sentence what does not fit:
a wrong assumption, a contradiction or a risk.

## What you have afterwards

- A brief in free form: a short header, then any headings, tables
  or lists you find useful. It has no IDs and none of the
  conventions of the chain.
- Where the identity of a source supports, limits or contradicts a
  thought, `(source: <path>)` stands beside it. Where a reservation
  or an uncertainty must stay visible, a short `(remark: ...)`
  stands.
- The brief is a draft until you approve it. Claude approves only on
  your explicit word, and before it offers the approval it walks the
  five areas of what was found once, so that each has been
  considered. An area may leave nothing in the brief.
- A history companion and a ledger row, both updated with every
  version.
- Nothing in it is yet a position. Its thoughts are mined into the
  intent by `/forge intent`, when you say so, whether the brief is
  approved or not.

Claude ends by naming the state of the brief and proposing
`/forge intent` if you want it mined.

## A worked example

A generic exchange for a brief born in the forge.

```
you:    /forge brief example-project
you:    I want one place where our teams record what they
        decided and why, so new people stop asking.
Claude: Two things exist for this elsewhere: decision logs and
        architecture decision records. I can run research on how
        they are kept up to date. Shall I?
you:    Yes.
Claude: (research filed in research/) It changed one thing: logs
        that are not tied to a review go stale. What stays
        uncertain is who owns them. More research is unlikely to
        settle that. Shall I go on?
you:    No. Write it down.
Claude: Here is what I will write: the want, the reason, what you
        do not want, one open line on ownership. Write it?
you:    write
Claude: Written as 00-brief.md, version 0.1, a draft. Say the
        word to approve it, and /forge intent when you want it
        mined.
```

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
