---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: fe82b47154a3cedd
inputs:
  - .claude/skills/forge/states/user-stories.md
  - templates/user-stories.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - templates/recipe-user-stories-export.md
---

# Write user stories

This page shows how you break a BRD, or a small change of the intent,
into user stories with `/forge user-stories`, and how you hand the
stakeholders their export. It is for you, the principal: the person
whose thinking is being forged and who has the last word on all
content. What a story is and why the layer exists is on
[The user stories](../about/the-user-stories.md).

## When to use it

Use it when the requirements are settled enough to be broken into
behaviour seen from outside, so that the stakeholders can approve
them as a whole, the delivery can build from them and the testers can
test from them. Claude asks whether the parent is stable enough to be
derived from, approved or your word for it. It is never a gate.

The stories have one parent, and you name it when you ask:

- The BRD, read with the layers above it for the reasons it does not
  carry. See [Write a BRD](write-a-brd.md). Each story cites the
  items of the BRD it serves.
- The intent, where the change is small, the ask is precise and it has
  no further impact, and you say so. Each story then cites the
  positions of the intent it serves.

Whether the ask suffices is your word. Claude may say why it thinks
it does not.

A requirements document of someone else works differently. You
register it first with `/ingest`. The stories made from it are a work
product in `work/` and never `35-user-stories.md`, each story citing
its place in the source. See
[Work a work product](work-a-work-product.md).

## The command

```
/forge user-stories <slug>
```

Without a slug it takes the project it resolves. The command iterates
`35-user-stories.md`.

## What happens

The default way is handing over: Claude works alone from what you
gave it and returns a proposal.

1. Claude walks the Map of the definition alone. The Map is the list
   of what the stories look for: the coverage, the behaviour, the
   edge cases, the qualities, the dependencies, the risks, the
   references outward, the contradictions and what stays open.

   You should now see the cut: the name of every story with a short
   description of what it covers, and the items of the parent that no
   story serves, each named by what it says.

2. You give your word on the cut. Claude drafts the whole stories
   only once the cut is agreed.

   You should now see the draft, returned without any question put to
   you on the way.

3. The draft is walked story by story: one story per message, closed
   with the verdict line `(a)ccept / (m)odify / (q)uestion /
   (r)eject / (p)ark`. See
   [Walk through a list](walk-through-a-list.md). Nothing is derived
   from the draft before you have judged it.

   You should now see each story with a verdict of yours behind it.

4. Where a story's parent does not suffice, the walk turns into an
   interview on that story, one question at a time.

   You should now see a question, not a guess, in the place the
   parent was silent.

5. The round ends with Claude naming what changed and what stays
   open. When the stories are complete it offers the approval.

   You should now see the list of changes, the open questions and
   the offer.

Two other ways in:

- A parent that moved: the pass runs on what changed.
- A wording fix: it is made directly, without a round.

The approval Claude offers is yours. The stakeholders' approval of the
whole is your organisation's act, recorded in the decisions where you
want it kept.

## What you have afterwards

`35-user-stories.md` with its history beside it, a draft at version
0.1 at the first round. Each story has its name, a sentence, its
acceptance criteria and a `Reference` to the parent. The other parts
(`Edge cases`, `Risks`, `Note`, `Questions`) appear only where a story
has something for them. What each part must say is in
[Requirement style and Story style](../reference/requirement-style.md).

## The reviewers

Three reviewers are offered, each on your word:

- `/check user-stories` for the mechanics. See
  [Check conformance](check-conformance.md).
- `/critique clarity`, which reads the stories against the Story style.
- `/critique essence`, which looks for drift from the parent.

## The export for the stakeholders

The export is a render, never the artefact. It is made in two steps.

1. `/recipe user-stories-export` composes its recipe through a short
   interview. It asks for the input (`35-user-stories.md`, or the work
   product in `work/` where the stories came from a source) and for
   the section heading and the purpose line, in your words. The
   language question closes it, as with every recipe. See
   [Compose a recipe](compose-a-recipe.md).
2. `/render user-stories-export` writes `renders/user-stories-export.md`.
   See [Render an output](render-an-output.md).

You should now see one heading per story and its parts on lines of
their own. There is no table, because a table cannot break a line
inside a cell and a paste would run a story into one paragraph. No
line is wrapped. Every reference to the intent is left out, since the
stakeholders never see the intent, so a story whose reference held
only those has no `Reference` in the export. The file is ready to be
pasted into a wiki or a tracker. Nothing of a story is reworded,
shortened or added.

## If something goes wrong

- The parent is not stable. Claude says so and goes on if you say so;
  it does not stop the work.
- A story's parent does not answer a question. The walk of that story
  becomes an interview and the question stays open with an owner.
- The stories came from someone else's document and landed in
  `35-user-stories.md`. They belong in `work/`.
- The export shows a story you did not expect. The export is made
  from the input as it stands, so change the stories first and render
  again; the render is never edited by hand.

## A worked example

The parent is the BRD of a project `<slug>`. You run
`/forge user-stories <slug>` and name the BRD as the parent.

Claude returns the cut:

- Request a password reset: a registered visitor asks for a link to
  choose a new password.
- Sign in: a registered visitor enters credentials and reaches the
  start page.
- Not served by any story: the rule that accounts are kept for a
  period after closing.

You agree the cut and ask for the draft. In the walk, one story
arrives with its verdict line:

```
### US.0010 — Request a password reset
A visitor who has forgotten the password asks for a reset link, so
that the visitor can sign in again.
- The page for a reset asks for the e-mail address of the account.
- A link to choose a new password is sent to that address.

**Edge cases:**
- The address belongs to no account → the page shows the same
  confirmation as for a known address.

**Questions:**
1. How long does the link stay valid? → the owner of the BRD

**Reference:** BR.0010

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You accept it. After `/recipe user-stories-export` and
`/render user-stories-export`, the export holds that story as:

```
### US.0010 — Request a password reset

A visitor who has forgotten the password asks for a reset link, so that the visitor can sign in again.
- The page for a reset asks for the e-mail address of the account.
- A link to choose a new password is sent to that address.

**Edge cases:**
- The address belongs to no account → the page shows the same confirmation as for a known address.

**Questions:**
1. How long does the link stay valid? → the owner of the BRD

**Reference:** BR.0010
```

## See also

- [The user stories](../about/the-user-stories.md): what the stories are, what a story holds and why the export leaves the intent out.
- [Write a BRD](write-a-brd.md): the usual parent of the stories.
- [Work a work product](work-a-work-product.md): the work product stories from someone else's document become.
- [Walk through a list](walk-through-a-list.md): the walk of the draft, one story per message.
- [Compose a recipe](compose-a-recipe.md): the genre interview every recipe runs through.
- [Render an output](render-an-output.md): the render that makes the export.
- [Check conformance](check-conformance.md): running the `user-stories` check.
- [Requirement style and Story style](../reference/requirement-style.md): the Story style of a story's parts.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
