---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: d658d7f6ebd4ed8f
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

The step of a conflict is how a repository left in conflict by git
is brought back to a clean state and saved. This page is for you
when `/save` stops because your commits clash with the remote, or
when a merge of a branch leaves files in conflict. It shows what you
see, how Claude and you settle each conflict, which commands finish
the step and how the save then goes through.

## When to use it

- A save takes your new commit onto the remote's changes by a rebase
  (git replays your commits on top of the remote's), and that rebase
  conflicts.
- A merge of a branch stops with files that git cannot join on its
  own.

In both cases git leaves the rebase or the merge standing. Nothing is
lost: your commit is made.

## The command

Nothing new is typed to start the step. You meet it when you save:

```
/save <slug>
```

The step then runs in the conversation. When it is finished, you
type the same `/save <slug>` again.

## What happens

1. **The save stops and tells you so.** The save script
   (`scripts/forge-save.py`) has made your commit, tried to take it
   onto the remote, and left the rebase standing where it stopped. It
   prints "Remote changes in <slug> conflict with yours. The rebase
   stands where it stopped, the commit is made and nothing was lost."
   Below that it lists the files in conflict and the step that
   follows: settle each file, then `git add <file>`, then
   `git rebase --continue` (again after each conflict, until it ends;
   `--abort` gives it up), then the save script again.
   You should now see the list of files in conflict and those lines.

2. **You can check the state at any time.** The status script reads
   every repository and changes nothing:

   ```
   python scripts/forge-status.py
   ```

   For the repository in question it says "rebase in progress" (or
   "merge in progress") with the number of files in conflict, and
   names the step of a conflict and then the save.
   You should now see that line in yellow under the repository's
   name.

3. **A further save is refused until the step is finished.** While a
   rebase or a merge stands, the save script refuses the repository
   before it stages anything. It says "A rebase is in progress in
   <slug> - nothing was staged or committed. Finish the step of a
   conflict first, then save again", and lists the files and the
   finishing commands once more. This is so that conflict markers
   (the lines git writes into a file to show both sides) are never
   committed.
   You should now see that nothing was staged or committed.

4. **Claude lays out the conflicts as a walkthrough.** A walkthrough
   is the forge's way of working a list: one item per message, each
   closed by your verdict (see
   [Walk through a list](walk-through-a-list.md)). Claude
   reads both sides of each file through the reading commands of git,
   which are open to it. It puts one conflict per message in front of
   you (the principal, the person whose thinking is being forged): what
   each side says, what would change, and its recommendation with the
   exact wording the file would receive. The message closes with the
   line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, and
   you answer with your verdict.
   You should now see one conflict at a time, never a table asking
   for every verdict at once.

5. **Claude writes the chosen wording at the round's end.** On your
   `write`, Claude reflects the round back and, on your yes, writes
   what you decided:
   - In an artefact (a document of the chain, such as the intent),
     the chosen wording goes into the file, and a `changed` record
     goes into the artefact's history, as for any change.
   - In a history, in `decisions.md` or in a resource index, the
     conflict is two tails: each side appended its records after the
     same last line. It is settled by keeping both.

   You should now see the files free of conflict markers.

6. **The finishing commands run on your yes.** Claude sends the
   commands that end the step, and a hook (a small script Claude
   Code runs before each shell command Claude sends,
   `scripts/hook-git.py`) puts each one to you before it runs. The
   harness (Claude Code, the program Claude runs in) shows you the
   command and runs it only on your yes. After a rebase these are:
   - `git add <file>` for each settled file;
   - `git rebase --continue`, again after each conflict until the
     rebase ends;
   - `git rebase --abort`, if you would rather give the rebase up.

   After a merge, `git add <file>` and then `git merge --continue`,
   or `git merge --abort` to give it up.
   You should now see each command offered to you for a yes, and the
   rebase or the merge ended.

7. **You save again.** Type `/save <slug>`. The save script finds a
   clean repository that is ahead of the remote and pushes it.
   You should now see the repository saved and pushed.

## What you have afterwards

- The repository is clean and in step with its remote.
- Every artefact that conflicted carries the wording you chose, and
  its history carries a `changed` record for it.
- Every history, `decisions.md` and resource index that conflicted
  keeps the records of both sides.

## If something goes wrong

- **The save says the pull with rebase failed and left no rebase to
  finish.** The commit is made and nothing was lost. The script asks
  you to check the network and the access to the remote, and to save
  again.
- **The save refuses because a rebase or a merge is in progress.**
  The step is not finished. Settle the files still listed, let the
  finishing commands run, then save again.
- **The save reports "Push failed".** Check the network and the
  access to the remote, and try again.
- **Both sides raised one document to the same version.** Git shows
  it as a conflict at the end of the document's history, because both
  sides appended their records there. The header's `version:` line
  conflicts only where the two numbers differ; where they are the
  same it merges silently. The merged document takes the next
  number, with one `changed` record that names the merge and what was
  joined. The records of both sides keep their numbers.
- **Both sides gave an item the same number.** The younger item is
  renumbered with a record, as
  [Stable IDs](../about/stable-ids.md) describes.

What the forge promises two people working on one project, and how
each kind of file merges, is set out in
[Working together on one project](../about/working-together.md).

## A worked example

You save `<slug>`. Someone else has pushed a change to the same item
of the intent, and the save stops with two files in conflict:

```
  10-intent.md
  10-intent.history.md
```

In `10-intent.md` git has written both sides of the item:

```
<<<<<<< ...
- <ID> <the item as the remote has it>
=======
- <ID> <the item as you wrote it>
>>>>>>> ...
```

In `10-intent.history.md` both sides appended records after the same
last line:

```
<<<<<<< ...
<the record the remote appended>
=======
<the record you appended>
>>>>>>> ...
```

Claude opens the walkthrough with the item. It shows both wordings,
says what each would mean, recommends one (or a joined wording) and
shows the exact text, closing with the verdict line. You answer `a`.
For the history Claude proposes to keep both records, one after the
other, and you answer `a` again. On `write` and your yes, Claude
writes the chosen wording into the intent, its `changed` record into
the intent's history, and both tails into the history. The hook then
offers you `git add 10-intent.md`, `git add 10-intent.history.md` and
`git rebase --continue`, each run on your yes. You type
`/save <slug>`, and the clean repository is pushed.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
