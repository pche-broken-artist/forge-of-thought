---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: d93177f26304d441
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that tells you, before you close the command
line, whether closing it would lose anything. It is for the
principal (whoever's thinking is being forged) at the end of a working
conversation. It only reports and offers: it writes nothing itself.

## When to use it

Use it when you are about to stop working and shut the command line.
A conversation holds things that no file holds yet, and a repository
may hold changes that are not saved. `/end` finds both. Terms of the
forge are explained in the [Glossary](../reference/glossary.md).

## The command

```
/end
```

## What happens

1. Claude says what lives only in this conversation. That is a round
   (one working conversation over the intent or open items) not yet
   written, verdicts carried but not written, and anything Claude
   promised and has not done. It then offers the write.

   You should now see a list of what the conversation alone holds, and
   an offer to write it, or a statement that there is nothing.

2. Claude runs the status script without the remote, so it touches no
   network. It names every repository with unsaved changes, the
   engine and each project, and offers `/save`. The script reports
   for each repository its unsaved changes or "clean - nothing to
   save", the branch, the last commit and the origin. How a save
   works is on [Save your work](save-your-work.md).

   You should now see each repository listed, with its changes or
   the line saying it is clean.

3. Claude remakes the project's ledger (the file that holds the
   state of the project, made from its documents at the moment it is
   read). It then names any stale renders as a fact. It makes no
   offer here: the renders are the release's.

   You should now see the stale renders named, or nothing about
   renders if none is stale.

4. Claude closes with one sentence. Either nothing lives only in this
   conversation and shutting the command line loses nothing, or the
   list of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You know whether shutting the command line is safe. If the closing
sentence is a list, every item on it comes with an offer to write or
to save, and nothing is done until you say so. State is kept in
files and never only in the conversation; the reason is on
[Documents and records](../about/documents-and-records.md).

## If something goes wrong

- The script prints "not under git" for a project that is not a
  repository. That is a property of the project, not a defect, and
  there is nothing to save for it.
- The script prints a line that a merge or a similar step is in
  progress, with the number of files in conflict. The step of the
  conflict comes first, then the save.
- The script prints a line that the merge driver registration is
  missing. Run `/setup`.
- The script prints the identity set in a repository itself. It is
  shown as a warning; the forge never sets one.

## A worked example

The slug `my-project` stands for any project. Claude's closing
sentence may take either form.

Nothing is lost:

```
Nothing lives only in this conversation, and shutting the command
line loses nothing.
```

Something would be lost:

```
Shutting the command line now would lose:
- the round on the intent: three verdicts carried, not written;
- unsaved changes in my-project (two files).
```

After the second form, you can answer the offered write and the
offered `/save`, then run `/end` again.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
