---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: a17007c9b9ad573d
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

Settling a conflict is the job you do when your changes and someone
else's touch the same lines and git cannot join them alone. This page
is for you if `/save` has stopped on a conflict with the remote, or a
merge of a branch has left files in conflict. It shows what you see,
how Claude puts each conflict in front of you, and which commands
finish the job.

On this page the principal is the person whose thinking is forged and
who decides: here, that is you. A walkthrough is the way a list of
decisions runs: one item per message, each closed by your verdict. A
hook is a small script that Claude Code runs before each command
Claude sends; this one guards every write of git.

## When to use it

Use it in one of two situations:

- `/save` stopped because the rebase of your commits onto the remote
  conflicts. A rebase replays your commits on top of the remote's.
- A merge of a branch was left by git in conflict.

The save that stops and the save that follows are described in
[Save your work](save-your-work.md).

## What you do

You answer one conflict at a time, then say yes to the commands that
finish the step, then save again:

```
/save <slug>
```

## What happens

1. **The save stops and says so.** The save script has already made
   your commit, so nothing is lost. It leaves the rebase standing
   where it stopped instead of aborting it. It prints the files in
   conflict and the step that follows, in this shape:

   ```
   Remote changes in <slug> conflict with yours. The rebase stands where it stopped, the commit is made and nothing was lost. The step of a conflict follows, one file at a time:
     <file>
     settle each file (both sides laid out, the principal deciding), then: git -C '<path>' add <file>
     git -C '<path>' rebase --continue   (again after each conflict, until it ends; --abort gives it up)
     python scripts/forge-save.py <slug>   (pushes the clean repository that is ahead)
   ```

   You should now see the list of files in conflict and the three
   lines of the step.

2. **The state can be checked at any time.** Run:

   ```
   python scripts/forge-status.py
   ```

   It says, for the repository concerned, that a rebase or a merge is
   in progress and how many files are in conflict.

   You should now see a line such as
   `rebase in progress - 2 file(s) in conflict` under the project.

3. **A further save is refused until the step is finished.** While a
   rebase or a merge is in progress, the save script refuses the
   repository before it stages anything. It prints the files still in
   conflict and the commands that finish the step. This happens so
   that conflict markers are never committed.

   You should now see "A rebase is in progress" (or "A merge is in
   progress") and "nothing was staged or committed".

4. **Claude lays out each conflict as a walkthrough.** Claude reads
   both sides of the file. It puts one conflict per message in front
   of you: what each side says, what would change, and its
   proposition for the joined wording. The message closes with the
   verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject /
   (p)ark`. You answer, and only then does the next conflict come.
   The shape of the walkthrough is described in
   [Walk through a list](walk-through-a-list.md).

   You should now see one conflict and one proposition at a time,
   never a table of all of them.

5. **Claude writes the chosen wording at the round's end.** When the
   conflicts are decided, Claude writes the wording you chose into
   the file. For an artefact (a versioned document of the chain), it
   also writes a `changed` record into the artefact's history, as for
   any change.

   A conflict in a record file is settled differently. A record file
   is a history, `decisions.md` or a resource index. There, the
   conflict is two tails appended after one last line, and it is
   settled by keeping both.

   You should now see the files without conflict markers.

6. **The finishing commands run on your yes.** The hook puts each of
   these commands to you, and it runs only when you say yes:

   - `git add <file>`: marks a settled file as ready.
   - `git rebase --continue`: carries the rebase on. Run again after
     each conflict, until the rebase ends.
   - `git rebase --abort`: gives the rebase up instead.
   - `git merge --continue` or `git merge --abort`: the same after a
     merge.

   You should now see each command offered to you for a yes before it
   runs.

7. **Save again.** Run `/save <slug>`. The repository is now clean
   and ahead of the remote, and the save pushes it.

   You should now see "saved and pushed to" followed by the remote.

## What you have afterwards

Your commits and the remote's are joined in one line and pushed. Every
conflict was decided by you, one at a time. Each artefact that was
joined carries a `changed` record in its history. Each record file
holds both tails.

## If something goes wrong

- **Two sides raised one document to the same version.** Git itself
  shows this: the header's `version:` line conflicts. Whoever merges
  settles it. The merged document takes the next number, with one
  `changed` record naming the merge and what was joined. The records
  of both sides keep their numbers.
- **One item number was taken on both sides.** It is renumbered as
  [Stable IDs](../about/stable-ids.md) says.
- **The save says the pull with rebase failed and left no rebase to
  finish.** The commit is made and nothing was lost. The save script
  says to check the network and remote access, then save again.
- **You want to give the step up.** Say yes to `git rebase --abort`
  (or `git merge --abort` after a merge) when it is put to you.

What the forge promises two people on one project, and how each kind
of file merges, is described in
[Working together on one project](../about/working-together.md).

## A worked example

You save the project `<slug>`. Someone else has pushed a change to the
same artefact, `10-intent.md`. Before either change, the artefact was
at version 1.2. You both raised it to 1.3, and you both changed the
wording of the same item.

The save makes your commit and stops. It lists two files in conflict:

```
  10-intent.md
  10-intent.history.md
```

In `10-intent.md` git shows two conflicts: the wording of the item,
and the header's `version:` line, which both sides raised.

Claude's first message lays out the item: the remote's wording, your
wording, and a proposition that joins them. It closes with the verdict
line. You answer `a`.

Claude's next message takes the version. Both sides gave 1.3, so the
proposition is that the merged document takes 1.4, with one `changed`
record naming the merge and what was joined. You answer `a`.

`10-intent.history.md` is a record file. Both sides appended their
records after the same last line. Claude proposes keeping both tails.
Both sets of records keep their number 1.3. You answer `a`.

At the round's end you say `write`. Claude writes the joined wording,
the version 1.4 and the `changed` record. The hook then puts
`git add 10-intent.md`, `git add 10-intent.history.md` and
`git rebase --continue` to you, one at a time, and each runs on your
yes. You run `/save <slug>`, and the clean repository is pushed.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the
  one-item-per-message shape the step runs in.
- [Working together on one project](../about/working-together.md):
  what the forge promises two people on one project and how each kind
  of file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken twice
  is settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
