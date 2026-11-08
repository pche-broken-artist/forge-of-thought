---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 9987f937475f11d4
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

A conflict is what git leaves standing when two sides changed the
same lines of one file and git cannot join them by itself. This page
is for you, working on a project under git, when `/save` stops on a
conflict with the remote or when a merge of a branch leaves one. It
says what you see first, what Claude does, what you decide and which
few git commands finish the step. The forge merges nothing on its
own: the conflict is left standing, you settle it with Claude, and
the next save pushes the result.

## When to use it

Two situations bring you here.

- A save whose rebase conflicts. You saved, the remote's branch had
  moved on as well, `/save` integrated the remote changes by rebase,
  and the rebase stopped on a file that both sides changed. The
  save that stops and the save that follows the step are described
  in [Save your work](save-your-work.md).
- A merge of a branch that git leaves in conflict. The merge itself
  is git's. You make it by hand on your own clone, outside the
  forge's scripts, or by a merge request where it needs no hand.
  What git leaves standing after such a merge is settled the same
  way as a conflict of a save.

What the forge promises two people on one project, and how each kind
of file merges, is explained in
[Working together on one project](../about/working-together.md).

## What you do

To see where the repository stands, type:

```
python scripts/forge-status.py <slug>
```

`<slug>` is the name of the project's directory under `projects/`.
The step itself runs in the conversation with Claude. The commands
that finish it are put to you by Claude Code and run on your yes.
Afterwards you save again:

```
/save <slug>
```

## What happens

1. **The save stops and tells you.** The save script has already
   made your commit. It leaves the rebase standing where it stopped.
   So nothing is lost. It prints the files in conflict and the step
   that follows: settle each file, `git add <file>`,
   `git rebase --continue`, then the save again. A merge you made by
   hand runs outside the scripts; what it leaves standing is what
   the status script reports in the next step.
   You should now see a message that begins "Remote changes in
   `<slug>` conflict with yours. The rebase stands where it stopped,
   the commit is made and nothing was lost." followed by the list of
   files.

2. **You look at where you stand.** Run the status script named
   above. It changes nothing. Beside the branch, the last commit and
   the origin it says that a rebase or a merge is in progress and how
   many files are in conflict.
   You should now see a line such as "rebase in progress - 2 file(s)
   in conflict; the step of a conflict, then forge-save".

3. **Claude lays out each conflict as a walkthrough.** A
   walkthrough is the forge's way of working a list of decisions:
   one item per message, each closing with a verdict line; its shape
   is described in [Walk through a list](walk-through-a-list.md).
   Claude reads both sides of every file in conflict. Reading git is
   open to it; writing git is not. Then it puts one conflict in
   front of you per message: what each side says and where it comes
   from, what would change and for whom, and its recommendation with
   the exact wording the file would receive. You give the verdict as
   the principal, the person whose thinking is forged. The message
   closes with `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
   A question keeps the item open; it is never read as a yes.
   You should now see one conflict per message, the recommended
   wording spelled out, and the verdict line at the end.

4. **Claude writes the chosen wording.** The verdicts are carried in
   the conversation and written once, at the round's end, on your
   word `write`. Claude writes the chosen wording into each file. For
   an artefact (a document of the chain, such as the intent) it also
   appends a `changed` record to the artefact's history companion, as
   for any change. A conflict in a history or in `decisions.md`
   looks different: both sides appended their lines after one last
   common line, so the file ends in two tails. Such a conflict is
   settled by keeping both tails. Nothing of either side is dropped.
   You should now see every settled file without git's conflict
   markers, and for each settled artefact a new record at the end of
   its history.

   ### A version given twice

   Where both sides raised one document to the same version, git
   finds it for you. Both sides appended their records to the end of
   the document's history, so the history conflicts as text whenever
   both raised it. The header's `version:` line conflicts only where
   the two numbers differ. Where both wrote the same number, that
   line merges silently, and the clash shows at the end of the
   history alone. The settlement is yours as the one who merges: the
   merged document takes the next number, and one `changed` record
   names the merge and what was joined. The records of both sides
   keep their numbers. An item number taken twice is renumbered as
   [Stable IDs](../about/stable-ids.md) says.

5. **The finishing commands run on your yes.** Claude does not write
   git on its own. A hook, a rule Claude Code runs before every shell
   command Claude sends, denies every writing command of git and
   names the forge's script to use instead. The few commands that
   finish the step of a conflict are the exception: the hook puts
   each to you, and Claude Code runs it on your yes. They are:

   - `git add <file>`, without `--force` and without the interactive
     flags, for each settled file;
   - `git rebase --continue`, again after each conflict until the
     rebase ends; `git rebase --abort` gives it up;
   - `git merge --continue` or `git merge --abort` after a merge you
     made by hand;
   - `git merge <branch>`, with one name and no flag, where you ask
     Claude to start a merge;
   - `git checkout --ours <file>` or `git checkout --theirs <file>`,
     where one side is to be taken whole.

   You should now see each command put to you before it runs, and
   the rebase or the merge ending once the last file is added.

6. **You save again.** Run `/save <slug>`. The repository is clean
   and ahead of its remote: the rebase replayed your commit, or the
   merge commit stands. A branch that is merely ahead is pushed as
   it stands. So a merge made by hand keeps its merge commit, and
   nothing of the other side is replayed.
   You should now see "nothing to commit - N commit(s) ahead of
   origin, pushing" and then "saved and pushed to" the origin.

## What you have afterwards

- A clean repository, pushed, with no commit holding a conflict
  marker.
- Every settled file in the wording you decided on.
- For every settled artefact a `changed` record at the end of its
  history; for a record file both tails, in the order they stood.
- Where a version was given twice, the document on the next number
  and one record naming the merge.
- Where the merge was made by hand, its merge commit kept.

## If something goes wrong

- **The save refuses to run.** "A rebase is in progress in `<slug>` -
  nothing was staged or committed. Finish the step of a conflict
  first, then save again:" and the files still in conflict. The
  save refuses a repository with a rebase or a merge already
  standing before it stages anything. So conflict markers are never
  committed. Finish the step, then save.
- **The save refuses, but lists "(none left in conflict)".** Every
  file is settled and added; the rebase or the merge still stands.
  `git rebase --continue` or `git merge --continue`, on your yes,
  ends it. Then save.
- **The rebase failed without a conflict.** "The pull with rebase
  failed in `<slug>` and left no rebase to finish; the commit is
  made and nothing was lost. Check network / remote access and save
  again." Nothing is to settle here.
- **The push failed after the step.** "Push failed in `<slug>`.
  Check network / remote access and try again." The commits stand;
  save again when the remote can be reached.
- **You want to give the rebase or the merge up.** `git rebase
  --abort` or `git merge --abort`, put to you by the hook and run on
  your yes. The commit the save made stays in your repository.
- **Claude's git command is denied.** The hook has refused a writing
  command and named the script of the forge that does the same
  thing. Only the finishing commands listed above are asked; every
  other write of git goes through the scripts.

## A worked example

You and a colleague each work on a clone of the project `<slug>`.
Both of you changed the intent, `10-intent.md`, which stood at
version 3.3, and both raised it to 3.4 with a record in
`10-intent.history.md`. Your colleague saved first. Now you run
`/save <slug>`.

The save makes your commit, finds the remote's branch moved on,
integrates it by rebase, and stops:

```
Remote changes in <slug> conflict with yours. The rebase stands where it stopped, the commit is made and nothing was lost. The step of a conflict follows, one file at a time:
  10-intent.md
  10-intent.history.md
  settle each file (both sides laid out, the principal deciding), then: git -C '<path>' add <file>
  git -C '<path>' rebase --continue   (again after each conflict, until it ends; --abort gives it up)
  python scripts/forge-save.py <slug>   (pushes the clean repository that is ahead)
```

`python scripts/forge-status.py <slug>` confirms it: "rebase in
progress - 2 file(s) in conflict; the step of a conflict, then
forge-save".

Claude reads both sides. There are two conflicts, and it puts them
to you one by one.

The first is in the body of the intent: one item, which your
colleague reworded and you reworded differently. Claude shows both
wordings, says what each would change, and recommends one wording
that carries both changes, spelled out as the line would stand. You
answer `a`.

The second is at the end of the history. The header's
`version: 3.4` did not conflict: both of you wrote the same number,
and git merged the line silently. The history, though, ends in two
tails after the last common record: your colleague's record of 3.4
and yours. Claude's proposition: keep both tails in the order they
stood, raise the intent to 3.5, and append one `changed` record
naming the merge and the two changes joined, the records of both
sides keeping their numbers. You answer `a`.

On `write`, Claude reflects the round back and writes: the merged
item into `10-intent.md`, the header to `version: 3.5`, both tails
and the new record into `10-intent.history.md`.

Then the finishing commands. Claude Code puts
`git add 10-intent.md 10-intent.history.md` to you; you say yes. It
puts `git rebase --continue` to you; you say yes. The rebase ends.

`/save <slug>` once more: "nothing to commit - 1 commit(s) ahead of
origin, pushing", then "saved and pushed to" the origin. Your
colleague's next `/pull` brings the settled intent to his clone.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the
  one-item-per-message shape the step runs in.
- [Working together on one project](../about/working-together.md):
  what the forge promises two people on one project and how each
  kind of file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken
  twice is settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
