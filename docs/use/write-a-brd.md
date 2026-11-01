---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 94703e7092df16c8
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

This page shows how you break an assignment, an intent or a document
someone gave you into business requirements with `/forge brd`. It is
for you as the principal, the person whose thinking is being forged and
who has the final word on content. Claude is the forge's assistant: it
proposes the structure and the wording, and you decide. What a BRD is
and why it names what the forge cannot know is on
[The BRD](../about/the-brd.md).

## When to use it

Use it when the stakeholders need to review the ask on their own, the
delivery teams need to estimate it and the solution design needs a
place to start. The business requirements break the parent into rules,
behaviour and qualities, and each one traces back to it.

You can also use it when someone else gave you a transcript, an offer
or a document and you want its asks as business requirements. That
case ends in a different place, described below.

## The command

```
/forge brd <slug>
```

The slug names your project. When you ask, you also name the parent of
the BRD:

- the assignment, which Claude reads together with the intent and its
  threads for the reasons the assignment does not carry;
- the intent with its threads, where the project has no assignment.
  Claude invents no assignment for it.

Claude says whether the parent is stable enough to derive from,
meaning approved or your word that it is. This is advice and never a
gate.

A file someone else gave you is not a parent. Register it first, as
[Register a source](register-a-source.md) describes, and then ask for
the BRD from it.

## What happens

The way in decides what you see. Each way below ends with the sign
that it worked.

1. **Found together.** Use this when there is no BRD yet and you want
   to work it out with Claude. It asks its questions up front, one per
   message, on the stakeholders, the scope of the document and the
   phasing, because the parent does not answer them. It then shows the
   whole draft with its provenance map, which lists every item of the
   parent and the items that carry it. A walkthrough follows. A
   walkthrough takes one item per message and closes each with the
   verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
   It goes by group, and the touched areas of the enterprise come one
   per item. You should now see a draft whose every parent item is
   carried or knowingly left out, and your verdicts on each group.

2. **On your word, drafted automatically.** Say so when you ask. Claude
   asks nothing. It builds the provenance map from the parent, walks
   the whole BRD alone and returns three things:
   - the draft with the provenance map;
   - the list of what it assumed;
   - the list of what must be supplied from outside the forge, in two
     parts: what the forge already holds, by path, and what must be
     fetched.

   What the parent does not answer is left as an open question or an
   assumption. A step of a use case, a guarantee or the phasing that no
   place of the parent gives is marked as Claude's reading. An open
   question whose owner the parent does not name carries
   `owner: unassigned`. That is a valid open state until you name a
   role. You should now see the draft, the three lists and nothing
   derived from the draft until you have judged it.

3. **A file someone else gave you.** The automatic way runs on it. Every
   turn of the principal's side in the file is listed as an ask, a
   question or an agreement, and each item cites its place in the file.
   The draft is always a work product in `work/`, never `30-brd.md`,
   because what someone said is never silently promoted to your
   position. See [Work a work product](work-a-work-product.md) for how
   to work such a file. To have the BRD in the chain, an intent is first
   handed over from the same file. The BRD is then given that intent as
   its parent. You should now see the draft in `work/`.

4. **A parent that moved.** The pass runs on what changed and not on the
   whole BRD again. You should now see the changed items and what they
   touched.

5. **A wording fix.** Claude makes it directly. You should now see the
   corrected wording.

For the first two ways, you say when you ask where the draft lands: in
the chain as `30-brd.md`, or as a quick look in `work/`.

Claude writes nothing from imagination about what lies outside the
forge. That covers a value of a quality the stakeholders have not given,
the behaviour of a system it has not read and a rule of a standard it
has not been shown. In their place stands a dependency or an open
question with an owner. The owner is a role wherever one fits, and
`unassigned` only where none does. The forge also reads the indexes of
the project's resources and of the libraries it depends on, so that a
standard or a report it already holds is cited and not declared
unknown.

The round ends with Claude naming what changed, what stays open and
what must come from outside.

## What you have afterwards

- A BRD in the chain as `30-brd.md` with its history beside it, or a
  draft in `work/` where it came from a file or where you wanted a quick
  look.
- The list of what must be supplied from outside, each entry pointing
  at its dependency or open question. Collecting it is the analyst's
  work, which is yours.
- An offer to approve, once nothing of the parent is left out in
  silence, every matter from outside has an owner and no open question
  that blocks estimation remains. Approval is yours.

The stakeholders' sign-off is your organisation's act. It is recorded
outside the forge, or as a decision where you want it kept.

The item wording is explained on
[Requirement style](../reference/requirement-style.md).

## Review it

Claude offers these reviewers for a BRD. Each runs on your command.

- `/critique essence` finds drift from the parent.
- `/critique clarity` checks the wording against the requirement style.
- `/challenge business-analyst` finds what was written from the parent
  though it belongs to the world outside it. See
  [Challenge the thinking](challenge-the-thinking.md).
- `/check brd` checks the mechanics. See
  [Check conformance](check-conformance.md).

## If something goes wrong

- The parent is not yet stable: Claude says so and goes on if you say
  so. Nothing blocks.
- The draft contains a value or a behaviour you did not expect: it
  should not. A value no stakeholder gave stands as an open question
  with an owner. Where you find an invented one, reject it in the
  walkthrough.
- Something is missing in the parent: Claude raises it as a question.
  A change of substance goes to the intent first, and the BRD follows.
- An open question shows `owner: unassigned`: name the role, and the
  mark is replaced.

## A worked example

You have a project `<slug>` with an approved assignment and want the
BRD found together.

```
/forge brd <slug>
```

Claude asks which parent to use. You answer: the assignment. Claude
asks, one per message, who is responsible, who approves and who
reviews, what this BRD does not cover that a reader would expect, and
what each phase delivers. You answer. It shows the whole draft with the
provenance map and then walks the groups. Under the touched areas it
raises each area of the enterprise in turn, and you say which apply.
At the end Claude names what changed, what stays open and what must
come from outside, and offers the approval. You approve, and you record
the stakeholders' sign-off where your organisation keeps it.

## See also

- [The BRD](../about/the-brd.md): what a BRD is, what it holds and why
  the forge names what it cannot know.
- [Work a work product](work-a-work-product.md): the work product a BRD
  from someone else's file becomes.
- [Register a source](register-a-source.md): registering the file put
  in.
- [Challenge the thinking](challenge-the-thinking.md): running the
  business-analyst persona.
- [Check conformance](check-conformance.md): running the `brd` check.
- [Requirement style](../reference/requirement-style.md): the rule set
  of a BRD's items.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
