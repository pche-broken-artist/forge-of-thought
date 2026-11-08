---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 710633a850276c81
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
same lines of one file and git cannot join them by itself. In the
forge it arises in two places: a save of yours whose rebase onto the
remote stops, and a merge of a branch that you made by hand and that
git left unfinished. This page is for you, the principal (the person
whose thinking is forged) or anyone who saves a project of the
forge. It says what you do from the moment the save stops until the
repository is pushed clean. The forge merges nothing itself: the
merge is git's, and what git leaves standing is settled by you, one
conflict at a time, with Claude laying the sides out.

## When to use it

- `/save` stopped. The remote's branch had moved on as well, the
  histories diverged, the save script integrated the remote's
  changes by rebase, and the rebase met a conflict. The commit is
  made and nothing is lost: the rebase stands where it stopped.
- A merge you made yourself left files in conflict. A merge is
  git's, made by hand on your own clone outside the forge's scripts,
  or by a merge request on the server where it needs no hand. A merge
  request that merges without conflict needs nothing of this page.
- `python scripts/forge-status.py <slug>` says that a rebase or a
  merge is in progress and how many files are in conflict.

The page is not for a push that failed because of the network: that
save is run again as it stands (see [Save your
work](save-your-work.md)).

## The command

The two lines you type are the save that stops and the save that
follows the step:

```
python scripts/forge-save.py <slug>
```

Between the two, the state of the repository is read with

```
python scripts/forge-status.py <slug>
```

`<slug>` is the project's slug; `forge` names the engine. Nothing
else is typed by you: the commands that finish the step are sent by
Claude and put to you for a yes.

## What happens

1. **The save stops.** The script has staged and committed your
   changes, found the remote's branch moved on and tried to rebase
   your commits onto it. Where the rebase conflicts it is left
   standing, not aborted. The script prints the files in conflict and
   the step that follows. You should now see a message that the
   remote changes conflict with yours, that the rebase stands where
   it stopped, that the commit is made and nothing was lost, and
   under it the files in conflict, one per line.

   After a merge you made by hand, git itself leaves the files in
   conflict and the merge in progress. The step from here is the same.

2. **The state is read.** `python scripts/forge-status.py <slug>`
   reports the repository without changing anything. You should now
   see a line saying that a rebase (or a merge) is in progress with
   the number of files in conflict, and that the step of a conflict
   comes first, then the save.

   A further save is refused at this point before anything is
   staged. So that conflict markers are never committed, the script
   stops and names the files still in conflict and the commands that
   finish the step.

3. **Claude lays both sides out.** Claude reads both sides of each
   conflict through the reading commands of git, which it may run
   freely. The step then runs as a walkthrough: a working method in
   which a list needing your decision is worked one item per message,
   each closing with a verdict line (see [Walk through a
   list](walk-through-a-list.md)). One conflict is one item. The
   message carries what the two sides say and what each would change,
   and ends in one proposition with Claude's recommendation and, for
   `accept`, the concrete text the file would receive. The message
   closes with the line `(a)ccept / (m)odify / (q)uestion / (r)eject
   / (p)ark`. You answer with a verdict, a single letter if that is
   your whole message. The next message acknowledges your verdict in
   one line and carries the next conflict. You should now see one
   conflict per message and nothing written yet: your verdicts are
   carried in the conversation until the round's end.

   Which wording is right is yours to say. Claude proposes and never
   decides, and a proposition never fills a gap with an assumption.

4. **The round is written.** When the conflicts are all answered,
   `write` is added to the verdict line. On your word Claude
   reflects the whole round back and writes it as one round:
   - For an artefact, the chosen wording goes into the file, and a
     `changed` record goes into the artefact's history, as for any
     change.
   - For a record file (a history, `decisions.md`, a resource index)
     the conflict is two tails appended after one last line, both
     sides having added records at the end. It is settled by keeping
     both tails, one after the other.
   - Where both sides raised one document to the same version, git
     merges the header's `version:` line silently, since both wrote
     the same number, and shows the clash at the end of the history,
     where both sides appended their records. The merged document
     takes the next number, with one `changed` record naming the
     merge and what was joined. The records of both sides keep their
     numbers. An item number taken twice is renumbered as [Stable
     IDs](../about/stable-ids.md) says, the younger with a record.

   You should now see each file without conflict markers and, for an
   artefact, the new record at the end of its history.

5. **The finishing commands run on your yes.** A hook of the forge
   stands between Claude and a write of git: Claude Code, the harness
   the forge runs in (the program that runs Claude and its tools),
   judges every git command Claude sends before it runs. A write of
   git is denied and the script to use is named instead. The few
   commands that finish the step of a conflict are the one exception:
   they are put to you and run on your yes. They are, one file and
   one command at a time:
   - `git add <file>` for each settled file (without `--force`, and
     without the interactive flags);
   - `git rebase --continue`, again after each conflict, until the
     rebase ends; `git rebase --abort` gives the rebase up;
   - `git merge --continue` or `git merge --abort` after a merge you
     made by hand;
   - `git merge <branch>` with one branch name and no flag, where you
     ask Claude to start a merge;
   - `git checkout --ours <file>` or `git checkout --theirs <file>`,
     where one side is taken whole for a file.

   The hook judges only what Claude sends. Your own git from your
   shell is yours. You should now see each command put to you before
   it runs, and after the last `--continue` a rebase (or merge) that
   has ended.

6. **The save runs again.** `python scripts/forge-save.py <slug>`
   finds nothing to commit, counts the commits the clean repository is
   ahead of its origin and pushes them. You should now see "nothing
   to commit - N commit(s) ahead of origin, pushing" and then "saved
   and pushed to <origin>".

## What you have afterwards

- A clean repository, pushed, with your commits on top of the
  remote's.
- Each conflicting artefact with one wording, yours by verdict, and a
  `changed` record in its history for the change.
- Each conflicting record file with both tails kept.
- A document that both sides had raised to the same version now at
  the next number, with one record naming the merge and what was
  joined.

## If something goes wrong

- **The save says a rebase or a merge is in progress and refuses.**
  Nothing was staged or committed. The step of a conflict is not
  finished: the message lists the files still in conflict, or says
  "(none left in conflict)", and prints the `add` and the
  `--continue` that end it. Finish the step, then save again.
- **The message says the pull with rebase failed and left no rebase
  to finish.** The commit is made and nothing was lost; there is no
  conflict to settle. Check network and remote access and save again.
- **The push fails after the step.** "Push failed" names the
  network or remote access. Nothing is lost; try the save again. A
  clean repository that is ahead is pushed by a plain save.
- **Claude's git command is denied.** The hook denied a command that
  is not one of the finishing commands: a rebase other than
  `--continue` or `--abort`, a merge with flags or with several
  names, an `add` with `--force` or an interactive flag, or any other
  write of git. The reason names the rule and the script of the
  forge to use instead. A denied command did not run; the files are
  untouched by it.
- **You want to give the rebase up.** `git rebase --abort` (after a
  merge, `git merge --abort`) is put to you like the others and runs
  on your yes. The commit of your changes is made and is not lost by
  it.
- **The registration of the merge driver is missing.** The first
  lines of `python scripts/forge-status.py` say whether the merge
  driver `ours` and the settings it needs are registered in your
  global git configuration, or which keys are missing and that
  `/setup` writes them. Without the registration a clone silently
  falls back to a conflict on the derived files, which then turn up
  in the step.

## A worked example

A thought project `<slug>` with one colleague on the same
repository. Its assignment, `20-assignment.md`, stands at version
0.3 on the remote and on your clone. The colleague saved a round that
raised it to 0.4, rewording the requirement `REQ.0120` to "The
service shall answer a request within two seconds." In the same
hours you raised it to 0.4 on your clone, rewording the same item to
"The service shall answer a request within one second." Both of you
wrote `version: 0.4` into the header and appended a record to
`20-assignment.history.md`.

You save:

```
python scripts/forge-save.py <slug>
```

The script commits your round, reports the branch as diverged,
integrates the remote's changes by rebase and stops. It prints that
the remote changes conflict with yours, that the rebase stands where
it stopped, that the commit is made and nothing was lost, and lists
two files:

```
  20-assignment.md
  20-assignment.history.md
```

followed by the `add`, the `rebase --continue` and the save that
finish the step. `python scripts/forge-status.py <slug>` now says
"rebase in progress - 2 file(s) in conflict; the step of a conflict,
then forge-save".

Claude reads both sides and opens the walkthrough. The first item is
the artefact: `REQ.0120` says "within two seconds" on the remote and
"within one second" on your side; the header's `version:` line is
not in conflict, since both sides wrote 0.4. Claude says what each
wording would change and for whom, recommends one with its reason
and shows the text the item would receive, then closes with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. You answer
`m`, give the wording you want ("within one second at the median"),
and accept the reworked proposition.

The second item is the history: after its last common line two
tails stand, the colleague's record for 0.4 and yours for 0.4. The
proposition is to keep both tails, one after the other, and, since
both sides raised the document to 0.4, to give the merged document
version 0.5 with one `changed` record naming the merge and what was
joined. You answer `a`.

Claude adds `write` to the verdict line; on your word it writes the
round: `20-assignment.md` with the agreed wording of `REQ.0120` and
`version: 0.5` in its header, and `20-assignment.history.md` with the
colleague's 0.4 record, your 0.4 record and one 0.5 record for the
merge. Neither file carries a conflict marker any more.

Claude then sends `git add 20-assignment.md`, which Claude Code puts
to you; you say yes. The same for `git add
20-assignment.history.md`, then `git rebase --continue`. The rebase
ends: your commit now sits on top of the colleague's.

You save again:

```
python scripts/forge-save.py <slug>
```

The script prints "nothing to commit - 1 commit(s) ahead of origin,
pushing" and then "saved and pushed to <origin>". The colleague's
next `/pull` brings the merged assignment at 0.5.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
