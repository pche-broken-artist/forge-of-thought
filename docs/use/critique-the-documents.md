---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a16f210f646571a4
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

`/critique` runs a critic lens, one isolated reviewer, over the
documents of a project and judges their quality, never their
substance. This page is for you, the principal (the person whose
thinking is being forged), when you want an independent reading of how
well your documents are written. For the list of lenses, see
[Critic lenses](../reference/critic-lenses.md).

## When to use it

Use it when you want a reader who has seen none of your conversation
to judge the documents as they stand. The critic judges quality and
leaves the thinking to you. Why it is blind to substance is explained
in [The critic](../about/the-critic.md).

No lens runs at a save. A release may offer one lens, `essence`; that
is described on [Release a version](release-a-version.md). Every other
run happens only on your word.

## The command

```
/critique [lens] [artefact|path] [slug]
```

All three arguments are optional.

- `lens` names the lens to run. Without it, the command only lists the
  lenses.
- `artefact|path` narrows the run to one artefact, named as `/forge`
  names it, or to any file of the project by its path. The file is read
  with the chain around it. Without a target, the whole chain is read.
- `slug` names the project. Claude infers it from the context and asks
  you when it is ambiguous.

A line you can type as it stands:

```
/critique essence
```

## What happens

1. **Bare `/critique` lists the lenses.** Claude scans the lenses
   available and recommends the one that fits the state of your
   project, by the fit each lens states about itself. The
   recommendation is never a gate.

   You should now see the roster with one lens recommended.

2. **With a lens, Claude first makes the ledger.** The ledger is the
   single record of the project's state, made from its documents at
   read time. Making it first means the reviewer reads current files.

   You should now see Claude start the run on the project, and the
   target if you named one.

3. **One isolated agent reads and judges.** The agent is a subagent,
   that is, a reviewer that sees nothing of your conversation and
   reads every input from disk. It reads the project's documents and
   judges their quality through the lens. It writes no file and returns
   a report.

   You should now see the run finish and Claude take over the report.

4. **Claude files the report.** The findings come back without
   numbers. Claude gives each new finding its `FND` number and files
   the report in `reviews/` under a dated name that a script completes.
   A finding the report marks as newly obsolete is settled later, at
   the walkthrough.

   You should now see a new report in the `reviews/` folder of the
   project.

5. **Claude presents the delta summary.** It does so in the language
   of your conversation. It names the new findings, the ones verified
   as resolved, the ones still open, the ones newly obsolete, and what
   waits for your verdict. Findings carry a severity and a category;
   the reviewer assigns both. For the lens `essence`, the
   distillations come first, because the findings rest on them.

   You should now see the delta summary.

6. **Claude offers a walkthrough.** A walkthrough settles the open
   findings one by one; see [Walk through a list](walk-through-a-list.md).
   Answering `accept` to a finding means an iteration of the artefact
   concerned through `/forge`, and the finding is then resolved. The
   other verdicts are explained on the walkthrough page.

   You should now see the offer of a walkthrough.

## What you have afterwards

- A report in `reviews/` of the project, dated and not edited
  afterwards.
- Every new finding numbered.
- If you took the walkthrough, each finding settled by your verdict.
  If you declined it, the findings wait.

## If something goes wrong

The owning definition names no stop condition and no error message for
this command, so none is listed here. If the project is ambiguous,
Claude asks which one you mean. If you decline the walkthrough,
nothing is lost: the findings stay open until you take it up.

## A worked example

You have a project `my-project` and want its intent read for quality.

```
/critique
```

Claude lists the lenses and recommends one. You pick `essence` and
narrow it to the intent:

```
/critique essence intent my-project
```

Claude makes the ledger of `my-project`, the critic reads the intent
with the chain around it, and the report is filed in `reviews/`. Claude
shows the delta summary and offers the walkthrough. You answer
`accept` to one finding, and Claude iterates the intent through
`/forge` to resolve it.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings
  one by one.
- [Release a version](release-a-version.md): the release, which offers
  the lens `essence` once.
- [The critic](../about/the-critic.md): what the critic judges and why
  it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
