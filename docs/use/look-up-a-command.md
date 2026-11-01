---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 171decbb4e941b5f
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command, or ask how to do something

This page is for anyone who wants to know what a command does before running it, what a working method is, or how to do something in the forge without knowing the command. `/man` is the forge's manual. It is read at the moment of the call from the files that own the commands and methods, so it is never out of date.

## When to use it

- You want the list of commands and working methods.
- You want to know what one command does, what it takes and what it looks for before you run it.
- You want the paragraph of a working method (a named way a conversation runs).
- You have a need and do not know the command. You say it in your own words and Claude finds the way.

`/man` runs nothing, writes nothing and decides nothing. It only shows. The alias `/manual` does the same. The word `help` is not the forge's: it belongs to Claude Code itself, which is why the forge's manual has the Unix name.

## The command

```
/man [command | method | question]
```

The argument is one of three things. Claude takes it as a command if it names one, as a method if it names one, and as a question otherwise.

## What happens

### Bare `/man`

1. Claude prints the commands, each with its arguments and its purpose cut to one line. `/man` and `/manual` are in the list.
2. It prints each working method with the first sentence of its paragraph.
3. It closes with one line: `/man <command>` for the page of a command, `/man <method>` for the page of a method.

You should now see the whole forge on one screen, and the two ways to go deeper.

### `/man <command>`

1. Claude finds the skill file of the command. If there is none, it says so and prints the list from the bare call.
2. It prints the purpose of the command, its arguments and its purpose in full as the table of commands gives it.
3. Where the command dispatches over a roster (the checks, the critic lenses, the challenger personas, the recipe genres), it prints every member with its own description. Where a member has a section on what it looks for, that section is printed in full; for a genre, its list of interview questions. You learn what a member looks for before you run it.
4. It closes with one line naming the skill file, for the reader who wants the whole procedure.

You should now see what the command is for, what it takes and, for a command with a roster, what each member goes after.

### `/man <method>`

1. Claude matches your word against the names of the working methods. Case, hyphens and spaces do not matter.
2. It prints the paragraph of the method in full and, where the method has a skill that holds its shape, the path of that skill.
3. If the word is neither a method nor a question, it says so and lists the methods.

You should now see the paragraph of the method and, where there is one, the path to its shape.

### `/man <question>`

Anything that is neither a command nor a method is taken as a need said in free words.

1. Claude reads the index of the documentation. Every page there carries the one question it answers. Claude chooses the pages whose question meets your need. Where your need can be read two ways that lead to different pages, it asks once, in one sentence, and waits for you.
2. It reads the chosen pages and, where the detail matters, the skill they name. Nothing is answered from memory: every mechanism in the answer was read in this run.
3. It answers in plain sentences:
   - the way the forge has, first, with what you type;
   - then what matters to know on that way;
   - where several ways fit, one recommended, with its reason.
4. Where the way leaves the forge, it says so plainly. A repository to initialise or a program to install is yours to do, because the forge does not do it.
5. It names the pages it read by path, once, at the end.

You should now see an answer that starts with what to type, and a list of the pages it rests on.

Where the forge has nothing for your need, Claude says so. It names an open thread of the forge's own project if one carries the need. What Claude would do without a mechanism, it marks as its own.

The answer is printed in the conversation language. Command names, file paths, front-matter keys and the names of the methods stay English.

## What you have afterwards

Nothing on disk has changed. You have the text in the conversation, and the choice of what to run next is yours.

## If something goes wrong

- An unknown command name is not an error. If it is no method either, Claude takes it as a question, or says so and lists the commands or the methods.
- A question gets a wrong or thin answer if the documentation's index is missing or out of date. The index is made by the documentation run: see [Generate the documentation](generate-the-documentation.md).

## A worked example

A command page, with a placeholder command:

```
/man check
```

Claude prints the purpose and the arguments of `/check`, then every check of its roster with the description of its file and what it looks for, and closes with the path of the skill file of `/check`. You pick a check from the list and run `/check <check> <slug>` yourself.

A question, with a placeholder need:

```
/man how do I keep a copy of my project somewhere else?
```

If the need could mean two things, Claude asks one sentence first, such as whether you mean a copy on a remote or a copy to hand to someone. Then it answers: the command to type first, what matters on that way, and, if the way starts outside the forge, that this step is yours. It ends with the paths of the pages it read.

## See also

- [Commands](../reference/commands.md): the same table of commands, as a page.
- [Generate the documentation](generate-the-documentation.md): the run that makes the index the manual reads to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
