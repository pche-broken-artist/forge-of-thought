---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: f0a4f8be9f8948be
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

The step of a conflict is what you do when a save stops because the
remote has changes that collide with yours, or when a merge you made
with git leaves files in conflict. This page is for you as the
principal (the person whose thinking is being forged) working with
Claude on a project that lives in git. It tells you what you see,
what Claude does, which commands you are asked to confirm and how
you save again once the files are clean.

## When to use it

Two situations bring you here.

- `/save` ([Save your work](save-your-work.md)) has committed your
  work and tried to put your commits on top of the remote's by a
  rebase. The rebase met a conflict. The save script leaves it
  standing and prints the files in conflict.
- You merged a branch with git yourself, by hand on your own clone,
  and git left files in conflict. The merge is git's, made outside
  the forge's scripts. A merge request that needs no hand never
  reaches this page.

In both cases nothing is lost: your commit is made and the rebase or
the merge waits where it stopped.

## What you do

Ask for the state of the repository with one line:

```
python scripts/forge-status.py
```

Then work the conflicts with Claude as a walkthrough (one item per
message, each closed with a verdict), confirm the finishing commands
the hook puts to you, and save again:

```
python scripts/forge-save.py <slug>
```

## What happens

1. **The save stops.** The save script makes your commit, then
   integrates the remote's changes by a rebase. When the rebase
   conflicts, the script leaves it standing and prints the files in
   conflict and the step that follows: settle each file, then
   `git add <file>` and `git rebase --continue`, then the save
   script again. You should now see a message that remote changes
   conflict with yours, that the commit is made and nothing was
   lost, and a list of the files in conflict.

2. **You read the state.** `python scripts/forge-status.py` reads
   git and changes nothing. You should now see, under the
   repository's name, a line saying that a rebase or a merge is in
   progress and how many files are in conflict, followed by "the
   step of a conflict, then forge-save".

3. **A further save is refused.** Until the step is finished, the
   save script refuses the repository before it stages anything.
   This is so that conflict markers are never committed. You should
   now see, if you try, a message that a rebase or a merge is in
   progress, that nothing was staged or committed, and the files
   still in conflict.

4. **Claude lays both sides out.** Claude reads both sides of each
   conflict through the reading commands of git the hook allows.
   It puts one conflict per message in front of you, with the
   situation, what would change and its proposition, and closes
   with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`
   ([Walk through a list](walk-through-a-list.md)). You give the
   verdict; a question keeps the item open. You should now see one
   conflict at a time, never a table asking for every verdict at
   once.

5. **Claude writes the chosen wording.** At the round's end, on your
   word, Claude writes the wording you chose into each file. For an
   artefact (a document of the chain, such as the intent) it also
   writes a `changed` record into the artefact's history, as for any
   change. A conflict in a history, in `decisions.md` or in a
   resource index is two tails appended after one last line: it is
   settled by keeping both, in the order you choose. You should now
   see the files without conflict markers and the histories with
   both sides' records.

6. **The finishing commands run on your yes.** Claude's git is
   walled by a hook: every write is denied and the script to use
   is named. The few commands that finish a conflict are the
   exception: the hook puts each to you and runs it on your yes.
   They are:
   - `git add <file>`, without `--force` and without the
     interactive flags;
   - `git rebase --continue`, again after each conflict until the
     rebase ends, or `git rebase --abort` to give it up;
   - `git merge --continue` or `git merge --abort` after a merge;
   - `git merge <branch>` with one name and no flag, for a merge
     Claude is asked to start;
   - `git checkout --ours <file>` or `git checkout --theirs <file>`,
     to take one side of a file whole.
   You should now see each command as a question before it runs,
   and the rebase or the merge ending.

7. **You save again.** `python scripts/forge-save.py <slug>` finds
   nothing to commit and the repository ahead of its origin, and
   pushes it. You should now see "nothing to commit", the number of
   commits ahead, and then "saved and pushed".

### Where both sides raised one document to the same version

Two people may each have raised the same document, say from 0.4 to
0.5, before the merge. Git finds this itself. Both sides appended
their records to the end of the document's history, so the history
conflicts as text whenever both raised it. The header's `version:`
line conflicts only where the two numbers differ. Where both wrote
the same number, that line merges silently, and the clash shows at
the end of the history alone. The merged document takes the next
number, 0.6 in the example, with one `changed` record naming the
merge and what was joined. The records of both sides keep their
numbers. An item number that both sides took is renumbered, the
younger with a record, as [Stable IDs](../about/stable-ids.md) says.

## What you have afterwards

- A repository with no rebase or merge in progress and no conflict
  markers, pushed to its origin.
- Every settled file holding the wording you chose, each artefact
  with a `changed` record in its history for the change.
- Every record file (a history, `decisions.md`, a resource index)
  holding both tails.
- Where a version was given twice, the document at the next number
  with one record naming the merge.

## If something goes wrong

- **"A rebase is in progress in ... nothing was staged or
  committed."** The step is not finished. Settle the files the
  message lists, confirm `git add <file>` and
  `git rebase --continue` (or `merge --continue` after a merge),
  then save again.
- **"The pull with rebase failed ... and left no rebase to
  finish."** This is not a conflict: the commit is made, nothing was
  lost. Check the network and the access to the remote and save
  again.
- **"Push failed."** The files are clean and the commits are made.
  Check the network and the access to the remote and save again.
- **The hook denies a git command Claude tries.** Only the finishing
  commands above are asked; every other write of git is denied and
  the reason names the script of the forge to use instead. Claude
  runs the step through those commands and the save script, nothing
  else.
- **You want to give the rebase or the merge up.** Confirm
  `git rebase --abort` or `git merge --abort` when the hook puts it
  to you. Your commit stays in the repository; the remote's changes
  are not integrated.

## A worked example

You and a colleague both work on `projects/<slug>`. Each of you
reworded the same passage of the intent, `10-intent.md`, and each
recorded the change in `10-intent.history.md`.

You run `/save`. The save script commits your work, tries the
rebase and stops:

```
Remote changes in <slug> conflict with yours. The rebase stands
where it stopped, the commit is made and nothing was lost. The step
of a conflict follows, one file at a time:
  10-intent.md
  10-intent.history.md
  settle each file (both sides laid out, the principal deciding),
  then: git -C '<path>' add <file>
  git -C '<path>' rebase --continue   (again after each conflict,
  until it ends; --abort gives it up)
  python scripts/forge-save.py <slug>   (pushes the clean
  repository that is ahead)
```

`python scripts/forge-status.py` shows, under `<slug>`, "rebase in
progress - 2 file(s) in conflict; the step of a conflict, then
forge-save".

Claude reads both sides of `10-intent.md` and puts the one conflict
in front of you: what your wording says, what your colleague's
says, what would change for the reader of the intent, and its
proposition to keep your colleague's sentence with one clause of
yours added, the merged text shown in full. It closes with the
verdict line. You answer `a`.

Claude then puts the history in front of you. Both of you appended
a record after the same last line, so the conflict is two tails. The
proposition is to keep both records, the colleague's first since it
reached the remote first. You answer `a`.

The round looks finished, and Claude offers `write`. On your word it
writes the merged passage into `10-intent.md`, keeps both records in
`10-intent.history.md` and adds a `changed` record for the merged
wording. It then asks, one at a time, for `git add 10-intent.md`,
`git add 10-intent.history.md` and `git rebase --continue`; you
say yes to each. The rebase ends.

Had both of you also raised the intent from 0.4 to 0.5, the
`version:` line would have merged silently and the history's tail
would have shown the clash. The intent would then take 0.6, with one
`changed` record naming the merge.

You run `/save` once more. The save script reports nothing to
commit, one commit ahead of origin, and pushes. The repository is
clean and shared.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the one-item-per-
  message shape the step runs in.
- [Working together on one project](../about/working-together.md):
  what the forge promises two people on one project and how each
  kind of file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken
  twice is settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
