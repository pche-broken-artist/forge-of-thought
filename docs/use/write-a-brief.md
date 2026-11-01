---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 6ef72802e3ef79bb
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
---

# Write a brief

This page shows how you compose or finish a brief with `/forge brief`. A brief is your own rough text of what you want and why, the first document of a project's chain. It is written for the principal, the person whose thinking is being forged. For what a brief is and why it stays rough, see [The brief](../about/the-brief.md).

## When to use it

Use it when a project has no brief yet, when a brief is unfinished, or when a new whole of thinking is born during the project's life and should not land in the intent as a batch of unproven positions. A later whole gets a brief of its own.

## The command

```
/forge brief [name] [slug]
```

Bare, the command works on `00-brief.md`. With a name, it works on `00-brief-<name>.md`, the brief of a later whole. The slug names the project; without it Claude resolves the project itself. If the brief does not exist, Claude creates it from the template together with its history companion.

The file opens with a small header (project, title, author, version, status). Below it the text is free form: any headings, tables or lists you find useful, and no IDs. A brief is kept in the language it is written in.

## What happens

The text reaches the brief in one of three ways.

1. **Pasted whole.** You hand Claude a finished text. Claude stores it verbatim and asks whether it is finished. If you say it is, the brief is approved at once.
   You should now see the brief stored as you gave it, and a question whether it is finished.

2. **Begun outside.** You hand Claude what you have written elsewhere. Claude stores what came and then works with you from where the text stops.
   You should now see your text stored unchanged, and the conversation continuing from its last point.

3. **Born in the forge.** You open with a rough idea. Claude is active from the first word: it inspires, brings how the same thing is done elsewhere, verifies what can be verified, confronts and draws out what you want, why and what you do not want. Claude may propose research ([Research a topic](research-a-topic.md)) or ingest of outside material ([Register a source](register-a-source.md)). Each runs only on your word. After a research step Claude says what it changed in the thought, what stays uncertain and whether more research is likely to change anything. Whether to go on is yours to say.
   You should now see proposals that you accept or decline, and findings filed in `research/` and `sources/`.

   What goes into the brief and what stays out is your decision. A proposal of Claude's serves the finding and is not the brief. Once you say to write, Claude writes down what the talk arrived at, condensed where the talk was long, and reflects it back before it is written. It writes once per round, on your confirmation.
   You should now see the brief written, with a new version in its history.

Whichever way the text arrived, two things hold afterwards. The brief is approved only on your explicit word. When it is done, Claude names the state of the brief and proposes `/forge intent` if you want it mined.

Before offering the approval, Claude goes once through what the finding looked at, to see that each area was consciously considered. An area may leave nothing in the brief, and a tension or an open question may stay as it is, because resolving them is the intent's work.

## What you can ask for

- **A structure.** At any time you can have Claude give the text a structure: it gathers the text under headings in a logical order, points out what repeats and mends the grammar. It adds nothing, drops nothing and rewords no thought. It shows the structure before it is written, and you may rename the headings. The step is never a condition of the approval.
- **Claude's opinion.** `??` alone at the end of your message, or as the whole message, asks for Claude's honest opinion of what you have just written: three points at most, marked as its own, nothing written.

Claude also tells you, unasked and in one sentence, what does not fit: a wrong assumption, a contradiction, a risk. If the talk turns to taking the idea apart piece by piece (definitions, blocks, wording), Claude says in one sentence that this is the intent's work and offers once to go on there. You decide whether that stays in the brief as one open line or is let go.

## What you have afterwards

- `00-brief.md` or `00-brief-<name>.md`, in draft until you approve it, with its history companion.
- A text where a source that supports, limits or contradicts a thought is marked `(source: <path>)`, and a reservation that must stay visible is marked `(remark: ...)`. Nothing marks who said what.
- Research notes and sources, indexed, for whatever you took from the finding.

The brief is mined into the intent by `/forge intent` when you say so, approved or not. How far each brief is mined is shown in the ledger (the state file made at read time) in its Briefs table, which reads the brief's header and the mining record in the intent's history. A brief not yet mined shows as pending. Terms of the forge are in the [Glossary](../reference/glossary.md).

## A worked example

You open with a rough idea. The slug is a placeholder.

```
/forge brief example-project
```

You: "I want a shorter onboarding for new colleagues, because the current one takes weeks and half of it is waiting."

Claude: asks what prompted it, brings two ways onboarding is shortened elsewhere, and notes in one sentence that "weeks" and "half of it is waiting" are two different claims. It proposes a research step on how others measure waiting time in onboarding, and waits.

You: "Yes, run the research."

Claude runs it, then says what it changed (the waiting time is common elsewhere), what stays uncertain (whether it applies to your size of team) and that more research is unlikely to change the idea.

You: "Write."

Claude reflects back the text it will write, the topics with a few sentences each, the research cited beside them and one open line. You confirm. The brief is written as draft 0.1 or its next version.

You: "Structure it."

Claude shows the text gathered under headings, with the repeats pointed out. You rename one heading and confirm.

You: "Approve."

Claude approves the brief and names its state: approved, not yet mined. It proposes `/forge intent` for when you want it mined.

## See also

- [The brief](../about/the-brief.md): what a brief is and why it is rough on purpose.
- [Research a topic](research-a-topic.md): the research step the brief's finding uses.
- [Register a source](register-a-source.md): the ingest step the brief's finding uses.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
