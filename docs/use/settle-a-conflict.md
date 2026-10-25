---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 21c1ebc7c373a930
inputs:
  - CLAUDE.md#Persistence (git)
  - scripts/forge-save.py
  - scripts/forge-status.py
  - scripts/hook-git.py
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/40-solution-design.md#SOL.0840
  - projects/forge/10-intent.md#POS.1790
---

# Settle a conflict

Settling a conflict is the step that finishes a save or a merge that
git could not finish on its own, because the same lines changed on
both sides. This page is for the principal (the person whose thinking
is forged and who decides every wording). It takes you from the
moment `/save` stops on a conflict, or a merge leaves one, to the
repository pushed clean. Terms of the forge used here are explained
in one line each in the [Glossary](../reference/glossary.md).

## When to use it

Use it in either of two situations:

- a save whose rebase of your commits onto the remote conflicts (the
  save that stops is described in [Save your work](save-your-work.md));
- a merge of a branch that git leaves in conflict, such as a branch
  of a contributor merged on your clone with `git merge <branch>`.

## The command

The step ends with the save that pushes the repository:

```
/save <slug>
```

Before it, the step runs as a conversation with Claude, and the git
commands that finish it are put to you one at a time.

## What happens

1. **The save stops.** The save script has made your commit and left
   the rebase standing where it stopped. Nothing is lost. It prints
   that remote changes conflict with yours, the files in conflict,
   and the step that follows:

   ```
   settle each file (both sides laid out, the principal deciding), then: git -C '<path>' add <file>
   git -C '<path>' rebase --continue   (again after each conflict, until it ends; --abort gives it up)
   python scripts/forge-save.py <slug>   (pushes the clean repository that is ahead)
   ```

   You should now see the list of files in conflict under the
   message "Remote changes in <slug> conflict with yours."

2. **The state is visible.** `python scripts/forge-status.py` says
   that a rebase or a merge is in progress and how many files are in
   conflict. A further save is refused before anything is staged
   until the step is finished. This is so that conflict markers are
   never committed.

   You should now see a line such as `rebase in progress - 2 file(s)
   in conflict` for the repository.

3. **Claude lays both sides out, one conflict per message.** The step
   runs as a walkthrough (a list of items put to you one item per
   message, each closed by your verdict; the shape is described in
   [Walk through a list](walk-through-a-list.md)). Claude reads both
   sides of each conflict and puts one conflict in front of you with
   its proposition: the wording it recommends and why. Each message
   closes with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. A message
   that says yes and asks a question counts as a question, not as
   consent.

   You should now see one conflict, its two sides and one
   proposition, and nothing else, in each message.

4. **Claude writes the chosen wording.** At the round's end Claude
   writes the wording you chose into the file. For an artefact (a
   document of the chain, such as the intent) it also appends a
   `changed` record to the artefact's history, as for any change.
   A conflict in a history, in `decisions.md` or in a resource index
   is different. It is two tails appended after one last line, and it
   is settled by keeping both.

   You should now see the files free of conflict markers, and a new
   `changed` record in the history of each artefact that conflicted.

5. **The finishing commands run on your yes.** Claude may not write
   to git directly. A hook (a script that Claude Code, the program
   Claude runs in, starts before each shell command) stops every git
   write but a few named commands, and puts those to you instead.
   The commands that finish the step are these:
   - `git add <file>`: marks a settled file;
   - `git rebase --continue`: carries on with the rebase, again after
     each conflict until it ends;
   - `git rebase --abort`: gives the rebase up;
   - `git merge --continue` or `git merge --abort`: the same after a
     merge.

   You should now see each command offered for your approval before
   it runs, and the rebase or merge ended once the last one has run.

6. **Save again.** Run `/save <slug>`. It pushes the clean repository
   that is ahead of the remote.

   You should now see that the repository is saved and pushed.

## What you have afterwards

The repository is clean and pushed, with both sides joined in the
wording you chose. Each artefact that conflicted carries a `changed`
record for the settlement. Each record file that conflicted keeps the
records of both sides.

What the forge promises two people on one project, and how each kind
of file merges, is described in
[Working together on one project](../about/working-together.md).

## If something goes wrong

- **Both sides raised one document to the same version.** Git shows
  it itself: the header's `version:` line conflicts. The merged
  document takes the next number, with one `changed` record naming
  the merge and what was joined. The records of both sides keep their
  numbers.
- **Both sides took the same item number.** The younger item is
  renumbered with a record, as [Stable IDs](../about/stable-ids.md)
  describes.
- **The save is refused with "A rebase is in progress" (or "A merge
  is in progress").** Nothing was staged or committed. The step is
  not finished yet: settle the files it lists, run the finishing
  commands, then save again.
- **The pull with rebase failed and left no rebase to finish.** This
  is not a conflict. The commit is made and nothing was lost. Check
  the network or your access to the remote, and save again.
- **You want to give the step up.** Approve `git rebase --abort`, or
  `git merge --abort` after a merge.

## A worked example

You run `/save <slug>`, and the save stops with two files in
conflict: the intent `10-intent.md` and its history
`10-intent.history.md`.

In the intent, you and the other side changed one sentence of the
same item:

```
<<<<<<< one side
The review runs once a month.
=======
The review runs after every release.
>>>>>>> the other side
```

Both sides had also raised the intent from version 0.3 to 0.4, so
the header's `version:` line conflicts as well.

Claude puts the sentence to you as one item: both wordings, and a
proposition such as "The review runs after every release and at
least once a month." You answer `a`. Claude puts the version to you
as the next item: the merged intent takes 0.5, with one `changed`
record naming the merge and what was joined. You answer `a`.

In the history, each side appended its own records after the same
last line:

```
<<<<<<< one side
<the records of one side, version 0.4>
=======
<the records of the other side, version 0.4>
>>>>>>> the other side
```

This is two tails, so both are kept, each with its own number.

At the round's end Claude writes the sentence and version 0.5 into
the intent, and the `changed` record into its history. It then
offers `git add 10-intent.md`, `git add 10-intent.history.md` and
`git rebase --continue`, each run on your yes. You run
`/save <slug>`, and the repository is pushed.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the
  one-item-per-message shape the step runs in.
- [Working together on one project](../about/working-together.md):
  what the forge promises two people on one project and how each kind
  of file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken
  twice is settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
