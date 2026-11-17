---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a9197a50b5aaed39
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how to have a challenger persona attack the substance
of your thinking with `/challenge`. It is for the principal (the person
whose thinking is being forged) who wants a hard, isolated reading of an
artefact before building on it. A persona is one isolated agent, a
reviewer that sees nothing of your conversation with Claude. It judges
what is claimed, never how the document is written.

## When to use it

Run it before the next layer is first derived from the target. For the
intent, that means before the first layer below it. An accepted
challenge is still cheap to absorb at that point.

Run it again after any major shift of direction. Running it on a
near-final artefact is late, but not useless.

## The command

```
/challenge [persona] [artefact|path] [slug]
```

A real example that can be typed as it stands, with a placeholder
project slug:

```
/challenge architect intent my-project
```

The target is optional. It is an artefact (named as `/forge` names it) or
any file of the project by its path. Without a target, the persona reads
the whole chain. The slug is the project; where it is ambiguous, Claude
asks.

Bare `/challenge` prints the roster of personas and recommends which
fits the project's subject. The recommendation is never a gate. The
personas of today are listed in [Challenger
personas](../reference/challenger-personas.md).

## What happens

1. Claude remakes the project's ledger (the state file built from the
   documents at read time), so that the agent reads a current file.
   You should now see no output of your own to act on; the run goes on to
   the agent.
2. Claude invokes the persona's agent on the project, passing only the
   project path and the target. You should now see the agent at work; it
   writes no file.
3. The agent returns a report with three to seven challenges ordered by
   severity, what is strong, and the questions it cannot answer from the
   documents. You should now see Claude file the report in `challenges/`
   under a dated name, which a script completes.
4. Claude gives each challenge its own CHL number at its head. You should
   now see each challenge carrying its number.
5. Claude presents the report. You should now see the overall read first,
   then each challenge compressed to two or three sentences. If Claude
   disagrees with a challenge, it says so separately and marks that as its
   own view. It does not defend earlier drafting choices.
6. Where the answer to one of the agent's open questions exists in your
   conversation but not in the documents, Claude answers it and flags it
   to you. You should now see those flags; they usually mean something
   true is missing from the intent.
7. Claude offers a walkthrough of the challenges. You should now see that
   offer, closed with the verdict line.

## What you have afterwards

- A filed report in `challenges/`, dated and not edited afterwards.
- Every challenge numbered and open, waiting for your verdict.

If you decline the walkthrough, the challenges wait.

## Settling the challenges

The challenges are settled one by one in a walkthrough, described in
[Walk through a list](walk-through-a-list.md). Here `accept` means the
challenge is mended through `/forge` in the artefact it concerns, and its
state becomes `accepted`. The other verdicts are those of the
walkthrough.

A rejected challenge is a normal, healthy outcome. So is a challenge
that survives three rounds unresolved: park it and move on. Why a
challenger can be wrong, and what it judges, is in [The
challenger](../about/the-challenger.md).

## If something goes wrong

- The slug cannot be inferred from context: Claude asks which project is
  meant.
- No persona named: you get the roster, not a run.

The owner records no other stop conditions or messages for this command.

## A worked example

You have an intent at version 0.3 and have not yet derived anything from
it. You type:

```
/challenge cto intent my-project
```

Claude remakes the ledger, runs the persona, and files the report. It
then tells you the overall read in a few sentences, followed by, say,
four challenges, the most severe first, each in two or three sentences.
One of them Claude disagrees with, and says so, marked as its own view.
The agent's question about a constraint is one you answered earlier in
conversation; Claude answers it and flags that the intent does not yet
say it. Claude offers a walkthrough. You accept the first challenge, so
it is mended through `/forge intent`. You reject the second as not
relevant to your aim. You park the third. The rejection is a healthy
outcome, and nothing more is asked of it.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
