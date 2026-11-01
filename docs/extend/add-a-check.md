---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 694e8dadff752d2a
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a check

A check is one agent file that verifies one concern of conformance with the conventions, and this page is for the extender who wants to add one. The file is `.claude/agents/check-<name>.md`, made from the template `templates/check-definition.md`. Nothing else of the engine changes when a check is added.

## Before you start

- A new check is added only on the decision of the principal (the person whose thinking is forged). It is added only where what it finds genuinely differs from what the existing checks find. The list of the checks that exist is on [Checks](../reference/checks.md).
- One check owns one concern and none another's. If your rule belongs to the concern of an existing check, it belongs in that check's file, not in a new one.
- A check judges conformance only. Substance is the challenger's and document quality is the critic's, so a rule that asks for either is not a check.
- The shared behaviour of every check (the subject, the way of working, the shape of the report) belongs to the contract that the file names in its front-matter. What the contract owns is on [The check](../about/the-check.md). You do not write that behaviour again in your file.
- The addition is recorded and released as any change of the forge. How that goes is on [Make a change to the forge](how-a-change-is-made.md).
- Terms of the forge are in the [Glossary](../reference/glossary.md).

## The files

- `.claude/agents/check-<name>.md` is the one file you create. `<name>` is a short word for the concern.
- `templates/check-definition.md` is the skeleton you copy from. You do not change it.

The `/check` command and the contract stay as they are. The roster is a scan of the agent files, so the new check appears in it once the file exists.

## Steps

1. Copy `templates/check-definition.md` to `.claude/agents/check-<name>.md`.
   You should now see a file with a front-matter and a section headed `Lens`.
2. Fill the front-matter.
   - `name` is `check-<name>`.
   - `description` says in one line what the check verifies and when it fits. The roster shows this line, and the recommendation of which check fits a moment is made from it. Keep the closing sentences of the template, which say that the check verifies conformance and is neither a critic of the documents nor a challenger of the thinking.
   - `tools` stays `Read, Glob, Grep`. A check is read-only.
   - `model` stays `inherit`, so that the check runs on the session model.
   - `skills` lists `check-contract`.

   If the description contains a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside it. Otherwise the agent does not register.

   You should now see a front-matter that names the agent, says when it fits and preloads the contract.
3. Delete the comment that stands under the front-matter. It belongs to the template, not to the check file.
4. Write the Lens section in three parts, and only these.
   - What you read. Say whether the target is a project, every project or the engine, how a given target narrows the reading, and what a library reduces it to. The check says which of project or engine it takes, and what a missing or an added slug means, because the `/check` command reads that from here.
   - What you verify. List the rules. Each rule names its owner (a section of `CLAUDE.md`, a template or a position of the intent) and is never restated. Say which states are a fact to report in one line and not a finding.
   - Cost. Say the scope you read: named files, or the whole, honestly.

   You should now see a Lens section that points to the rules of other owners and holds none of its own.
5. Leave out everything the contract already says: the read-only conduct, the findings-only rule, the report shape and the handling of known and rejected findings. The Lens section is a specialisation of the contract. It may narrow what is read or make a shared rule stricter. It may not rename, drop or repeat a shared rule or field.

The check writes nothing. It returns its report, and the `/check` command files it in the `reviews/` folder of the target project and gives each finding its number. Whether a save or a release runs your check is for the definition of that command to say. Adding the file does not add the check to either.

## A worked example

A check for a concern called `<name>` has this shape. The words in angle brackets are yours to fill.

```markdown
---
name: check-<name>
description: Check "<name>" — <what this check verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

<What you read: the target, how it narrows, what a library reduces it to.>

What you verify:

1. <A rule, with its owner cited>
2. <A rule, with its owner cited>

<What is a fact and not a finding.>

Cost: <the scope you read.>
```

## Prove it

Run the check on the engine and on a project, and read what it returns.

```
/check <name>
/check <name> <slug>
```

The first form passes the engine root and no slug. The second passes the project with the slug you give it. Use the form your Lens section says the check takes. To prove the engine itself, run `/check engine` as well, since the new file is part of the engine.

- You should see the check in the roster that bare `/check` prints, with your description.
- You should see the check run as a read-only agent and return either one line that says it conforms or a ranked list of findings with a place, a rule and a fix each.
- You should see no file written by the agent itself. A report with findings is filed by the command, and a report that conforms is filed nowhere.

If the check does not appear in the roster, look at the front-matter first, and at the quoting of the description.

## Record and release

Record the addition and release it as any change of the forge. The steps are on [Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
