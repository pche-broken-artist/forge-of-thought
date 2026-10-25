---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: f44d13af973b43cd
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

The step of a conflict is how a repository of the forge gets past a
conflict that git cannot resolve alone: Claude lays both sides out,
you decide, and Claude writes the wording. This page is for the
principal (the person whose thinking is forged, who has the final
word on all content). It covers a conflict left by `/save` and one
left by a merge.

## When to use it

Use it in either of these cases:

- a save whose rebase of your commits onto the remote conflicts;
- a merge of a branch that git leaves in conflict.

Nothing is lost in either case. The save script has already made
your commit before the rebase stopped.

## What you do

Ask Claude to settle the conflict, then save again:

```
/save <slug>
```

Between the two, you give one verdict per conflict and say yes to
each finishing command of git that is put to you.

## What happens

1. **The save stops on the conflict.** The save script makes the
   commit, leaves the rebase standing where it stopped and prints
   the files in conflict. Under them it prints the step that
   follows: settle each file, `git add <file>`, `git rebase
   --continue` until the rebase ends, then the save again.
   You should now see "Remote changes in <slug> conflict with
   yours. The rebase stands where it stopped, the commit is made and
   nothing was lost." followed by the list of files.

2. **The state shows the step is open.** `python
   scripts/forge-status.py` says, for that repository, that a rebase
   (or a merge) is in progress and how many files are in conflict.
   Until the step is finished, a further save is refused before
   anything is staged. This is so that conflict markers are never
   committed.
   You should now see the repository's line saying a rebase in
   progress and the number of files in conflict.

3. **Claude puts the conflicts to you one at a time.** The step runs
   as a walkthrough: one item per message, each closed with a
   proposition and the verdict line `(a)ccept / (m)odify /
   (q)uestion / (r)eject / (p)ark`. Claude reads both sides of each
   conflict. One message carries one conflict: what each side says,
   what would change, and the wording Claude recommends. You give
   your verdict, and Claude moves to the next conflict.
   You should now see one conflict in front of you, ending in the
   verdict line.

4. **Claude writes the chosen wording.** At the round's end Claude
   writes the wording you chose into the file. For an artefact (a
   document of the chain) it also writes a `changed` record into the
   artefact's history, as for any change. A history or
   `decisions.md` in conflict holds two tails: both sides appended
   records after the same last line. Such a file is settled by
   keeping both tails.
   You should now see the files free of conflict markers, and a new
   `changed` record in the history of each artefact that was
   settled.

5. **You say yes to the finishing commands.** The commands that
   finish the step are put to you by the hook (a check that runs
   before every shell command Claude sends) through the harness (the
   program Claude runs in, which asks you before it runs a command).
   Each runs on your yes:
   - `git add <file>` for each settled file;
   - `git rebase --continue`, again after each conflict until the
     rebase ends;
   - `git rebase --abort`, if you give the rebase up;
   - `git merge --continue` or `git merge --abort`, after a merge.

   You should now see the harness asking you to allow each command,
   and git reporting that the rebase or the merge has finished.

6. **You save again.** `/save <slug>` pushes the clean repository
   that is ahead of the remote.
   You should now see "saved and pushed to" followed by the remote.

## What you have afterwards

Your commits and the remote's side joined in one history, every
conflict settled by your verdict, and the repository pushed. Each
artefact that was settled carries a `changed` record of the
settlement in its history.

### A version given twice

Both sides may have raised one document to the same version. Git
shows this itself: the header's `version:` line conflicts. The
merged document then takes the next number. It gets one `changed`
record naming the merge and what was joined. The records of both
sides keep their numbers.

An item number taken by both sides is renumbered as
[Stable IDs](../about/stable-ids.md) says.

## If something goes wrong

- **A save is refused with "A rebase is in progress in <slug> -
  nothing was staged or committed. Finish the step of a conflict
  first, then save again".** The step is still open. The message
  lists the files left in conflict and the commands that finish the
  step. Settle the files, run the finishing commands on the hook's
  ask, then save again. The same holds for a merge in progress.
- **"The pull with rebase failed in <slug> and left no rebase to
  finish".** There is no conflict to settle. The commit is made and
  nothing was lost. Check the network or your access to the remote
  and save again.
- **"Push failed in <slug>".** The rebase has finished but the push
  did not reach the remote. Check the network or your access to the
  remote and save again. The save pushes a clean repository that is
  ahead.
- **You want to give the rebase up.** Say so. `git rebase --abort`
  is put to you by the hook and runs on your yes. After a merge the
  command is `git merge --abort`.

## A worked example

You run `/save <slug>`. The remote holds a change by someone else to
`10-intent.md`, and the rebase stops. The save script lists two
files in conflict:

```
  10-intent.md
  10-intent.history.md
```

In `10-intent.md` both sides raised the version and both rewrote
one sentence:

```
<<<<<<<
version: 0.5
=======
version: 0.5
>>>>>>>
...
<<<<<<<
The pilot runs in one team first.
=======
The pilot runs in two teams at once.
>>>>>>>
```

Claude puts the sentence to you as one item: both wordings, what
each would change, and a recommended wording. You answer `a`. Claude
then puts the version to you as the next item. Both sides gave the
document 0.5, so it proposes 0.6 for the merged document, with one
`changed` record naming the merge. You answer `a`.

In `10-intent.history.md` both sides appended their records after
the same last line:

```
<<<<<<<
<the records of your side>
=======
<the records of the other side>
>>>>>>>
```

Claude proposes to keep both tails. You answer `a`.

At the round's end Claude writes the chosen sentence and `version:
0.6` into `10-intent.md`. It writes both tails into the history,
followed by the `changed` record of the merge. The hook then puts
`git add 10-intent.md`, `git add 10-intent.history.md` and `git
rebase --continue` to you one by one, and each runs on your yes. You
run `/save <slug>` again, and the repository is pushed.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the one-item-per-message
  shape the step runs in.
- [Working together on one project](../about/working-together.md):
  what the forge promises two people on one project and how each
  kind of file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken
  twice is settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
