---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 82dc3b0dad1323d5
inputs:
  - CLAUDE.md#Persistence (git)
  - scripts/forge-save.py
  - scripts/forge-status.py
  - scripts/hook-git.py
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/40-solution-design.md#SOL.0840
  - projects/forge/10-intent.md#POS.1750
  - projects/forge/10-intent.md#POS.1790
---

# Settle a conflict

The step of a conflict is the way a conflict in git is settled in the
forge: Claude lays both sides out, you decide, Claude writes the
wording you chose, and the commands of git that finish the conflict
run on your yes. This page is for you as the principal (the person
whose thinking is forged) when `/save` stops on a conflict with the
remote, or when a merge leaves one. The remote is the repository your
save pushes to.

## When to use it

- A save stopped on a conflict. `/save` makes a commit of your work
  and pushes it. Where the remote's branch has moved on as well, it
  first integrates the remote's changes by a rebase of your commits
  onto them, and that rebase can conflict. The save itself is told in
  [Save your work](save-your-work.md).
- A merge of a branch left a conflict. The merge itself belongs to
  git: you make it by hand on your own clone, with git itself and
  outside the forge's scripts, or it is made by a merge request. What
  git leaves in conflict is settled in the step told here.

## What you do

You type one line, which shows where the repository stands:

```
python scripts/forge-status.py <slug>
```

`<slug>` is the slug of your project. Without it the script reports
the engine and every project.

The rest is a conversation with Claude:

1. You give a verdict on each conflict that it puts in front of you.
2. You say `write` at the end of the round, and yes to what it
   reflects back.
3. You say yes to each finishing command of git that is put to you.
4. You run `/save` again.

## What happens

### 1. The save stops and prints what follows

The save script (`scripts/forge-save.py`, which `/save` runs) has made
the commit and left the rebase standing where it stopped. Nothing is
lost. It prints the files in conflict and the step that follows:

```
Remote changes in <slug> conflict with yours. The rebase stands where it stopped, the commit is made and nothing was lost. The step of a conflict follows, one file at a time:
  <a file in conflict>
  <another file in conflict>
  settle each file (both sides laid out, the principal deciding), then: git -C '<path>' add <file>
  git -C '<path>' rebase --continue   (again after each conflict, until it ends; --abort gives it up)
  python scripts/forge-save.py <slug>   (pushes the clean repository that is ahead)
```

`<path>` is the directory of the repository. After a merge made by
hand there is no such message: the save script took no part in the
merge, and the conflict is what git left standing.

You should now see the message, with the files in conflict listed
under its first line.

### 2. The status says what is in progress

`python scripts/forge-status.py <slug>` reads the state and changes
nothing. Among the lines of the repository it prints this one:

```
   rebase in progress - <n> file(s) in conflict; the step of a conflict, then forge-save
```

After a merge the line opens with `merge in progress`. Until the step
is finished, a further save is refused before anything is staged. This
keeps conflict markers out of every commit.

You should now see that line, with the number of files in conflict.

### 3. Claude puts one conflict in front of you

The step runs as a walkthrough: a list of items that need your
decision, worked one item per message, as
[Walk through a list](walk-through-a-list.md) tells. Claude reads both
sides of each conflict with the reading commands of git, which are
open to it.

The terms of the forge that this page uses, such as an artefact, a
history or an index, each stand in one line in the
[Glossary](../reference/glossary.md).

A conflict in an artefact is the same item or sentence changed on both
sides. It is settled by you, with Claude's help. Each message carries
one such conflict, in this order:

1. what the two sides say and the situation behind them, in a few
   sentences;
2. what would change and for whom;
3. Claude's recommendation with its reason, and the concrete text the
   file would receive.

The message ends in one proposition, worded so that `accept` has
exactly one meaning. It closes with the line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

A conflict in a history, in `decisions.md` (the file of decisions) or
in an index is of another kind. The history of a document is the file
to whose end the records of its changes are appended. In such a file
both sides appended their own lines after the same last line. The
conflict is the two tails, and it is settled by keeping both.
[Working together on one project](../about/working-together.md) tells
how each kind of file merges.

You should now see one conflict, one proposition and the verdict line,
and no second conflict in the same message.

### 4. You give the verdict

One letter is enough when it is your whole message. The words mean
what they mean in every walkthrough. Three of them:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the conflict, and the solution found
  is put forward to be accepted.
- `question`: you ask about the open conflict. Nothing changes and
  nothing is written. Claude answers and closes with the verdict line
  again.

Your verdicts are carried in the conversation and written once, at the
round's end. Until that write, what is agreed is nowhere yet.

You should now see the next message open with one line that
acknowledges your verdict, followed by the next conflict and nothing
else.

### 5. Claude writes at the round's end

When the round looks finished, `write` is added to the verdict line.
On `write` Claude reflects the whole round back. On your yes it writes
everything carried as one round:

- the chosen wording into each file that was in conflict;
- both tails into each history, `decisions.md` or index that was in
  conflict;
- for an artefact, a `changed` record into its history.

You should now see the chosen wording in each file and, for an
artefact, a `changed` record at the end of its history.

### 6. The finishing commands run on your yes

The hook (`scripts/hook-git.py`) is a script that Claude Code runs
before every Bash command Claude sends. It denies every write of git
that Claude sends and names the script of the forge to use instead.
The few commands that finish this step are the exception: each is put
to you as a question and runs on your yes. The question comes in the
automatic permission mode as well.

| Command | What it does |
|---|---|
| `git add <file>` | stages a settled file for the commit that follows |
| `git rebase --continue` | goes on with the rebase; it comes again after each conflict, until the rebase ends |
| `git rebase --abort` | gives the rebase up |
| `git merge --continue` | ends a merge in progress, once its files are settled and staged |
| `git merge --abort` | gives the merge up |
| `git merge <branch>` | merges one branch into the current branch, where you ask Claude to start a merge; one name and no flag |
| `git checkout --ours <file>` or `git checkout --theirs <file>` | takes one side for a file in conflict |

A command may carry `-C '<path>'` before its verb, as the save script
printed it. Claude starts no merge on its own judgement.

You should now see each command as a question before it runs. After
the last one, `python scripts/forge-status.py <slug>` prints no
`in progress` line.

### 7. You save again

Run `/save` again. The save pushes the clean repository that is ahead
of the remote. Where nothing is left to commit, it says
`nothing to commit - <n> commit(s) ahead of origin, pushing`.

You should now see `saved and pushed to <origin>`.

### A version given twice, an item number taken twice

Both sides may have raised one document to the same version. Git shows
this clash itself. Both sides appended their records to the end of the
document's history, and that end conflicts as text whenever both
raised the document. The `version:` line of the document's header
conflicts only where the two numbers differ. Where both sides wrote
the same number, git merges that line silently and the clash shows at
the end of the history alone.

Whoever merges settles it in the same step:

- the merged document takes the next number;
- one `changed` record names the merge and what was joined;
- the records of both sides keep their numbers.

An item number that both sides took is settled as
[Stable IDs](../about/stable-ids.md) tells: the younger item is
renumbered with a record, in a walkthrough, never by Claude alone.

## What you have afterwards

- A repository with no rebase and no merge in progress, clean and
  pushed to the remote.
- Your commit, which the save made before the rebase began. Nothing
  was lost on the way.
- The wording you chose in each artefact that was in conflict, and a
  `changed` record in its history.
- Both tails kept in each history, `decisions.md` or index that was in
  conflict.
- After a merge made by hand, its merge commit. A branch that is
  merely ahead of the remote is pushed as it stands.

## If something goes wrong

**A save is refused while the step stands.** The save script prints:

```
A rebase is in progress in <slug> - nothing was staged or committed. Finish the step of a conflict first, then save again:
  <a file still in conflict>
  settle each file, then: git -C '<path>' add <file>
  git -C '<path>' rebase --continue   (or --abort to give it up)
```

After a merge the message says `A merge is in progress` and names
`merge --continue`. Nothing was staged or committed. Finish the step,
then save again. Where the list reads `(none left in conflict)`, no
file is in conflict any more and only the last printed command is
left.

**The rebase stops again.** `git rebase --continue` can meet a further
conflict. The step repeats for it, until the rebase ends.

**The save reports no rebase to finish.** The save script prints:

```
The pull with rebase failed in <slug> and left no rebase to finish; the commit is made and nothing was lost. Check network / remote access and save again.
```

This is not a conflict. Do what the message says.

**The push fails after the step.** The save script prints:

```
Push failed in <slug>. Check network / remote access and try again.
```

Save again: a clean repository that is ahead of the remote is pushed
by the next save.

**The hook denies a command Claude sent.** The hook asks you only for
the commands of the table above. It denies a merge with a flag or with
several names, a rebase that starts or skips, and `git add` with a
forcing or an interactive flag. A merge of that kind is made by your
own hand or by a merge request. The hook judges Claude's commands
alone: what you type into git yourself from the shell is not judged by
it.

**You want to give the conflict up.** `git rebase --abort`, or
`git merge --abort` after a merge, is put to you by the hook and runs
on your yes.

## A worked example

One run of the job in a project `<slug>`. You and a second person both
changed the same item of one artefact, and both raised the artefact to
the same version. Each side appended its record to the artefact's
history.

1. `/save` stops. It prints the message of step 1 above with two files
   listed: the artefact and its history.

2. `python scripts/forge-status.py <slug>` prints:

   ```
      rebase in progress - 2 file(s) in conflict; the step of a conflict, then forge-save
   ```

3. Claude's first message carries the conflict in the artefact:

   ```
   Both sides changed the same item.
     Your side:      The report is sent every week.
     The other side: The report is sent every month, to the team lead.
   What would change: how often the report is sent, and to whom.
   I recommend your interval with the other side's recipient: the two
   changes do not exclude each other.
     The report is sent every week, to the team lead.
   Proposition: the item reads as the last line shows. The artefact
   takes the next version, and one `changed` record in its history
   names the merge and what was joined.
   (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
   ```

   You answer `a`.

4. The next message opens with one line that acknowledges your
   `accept`, and then carries the conflict in the history. Both sides
   wrote the same number, and git merged the `version:` line of the
   artefact silently. The clash shows here, where both sides appended
   one record after the same last record:

   ```
   on both sides     <the last record both sides have>
   your tail         <the record of your change>
   the other tail    <the record of the other side's change>
   ```

   The proposition is to keep both tails. You answer `a`.

5. You say `write`. Claude reflects the round back, and on your yes it
   writes the item into the artefact and the records into the history.
   The history now ends like this:

   ```
   <the last record both sides have>
   <the two records of the two sides, both kept, each with its number>
   <one `changed` record that names the merge and what was joined>
   ```

6. The hook puts three commands to you, one after another. You say yes
   to each:

   ```
   git -C '<path>' add <the artefact>
   git -C '<path>' add <its history>
   git -C '<path>' rebase --continue
   ```

   The rebase ends, and the status prints no `in progress` line.

7. You run `/save` again and see `saved and pushed to <origin>`.

## See also

- [Save your work](save-your-work.md): the save that stops on the
  conflict and the save that follows it.
- [Walk through a list](walk-through-a-list.md): the one-item-per-message
  shape the step runs in.
- [Working together on one project](../about/working-together.md): what
  the forge promises two people on one project and how each kind of
  file merges.
- [Stable IDs](../about/stable-ids.md): how an item number taken twice
  is settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
