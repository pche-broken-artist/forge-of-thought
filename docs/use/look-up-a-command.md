---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 85c82446b2743f92
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command, or ask how to do something

`/man [command | method | question]` is the manual of the forge: it prints what a command or a working method is, or answers a need you say in your own words. This page is for the user of the forge who wants to know what a command does before running it, or who does not know which command fits. The alias `/manual` does the same.

## When to use it

- You want the list of commands and working methods.
- You want to know what one command is for, what arguments it takes and what its roster holds.
- You want the text of one working method.
- You know what you want to get done but not which command does it.

The manual is read at the moment of the call from the files that own it, so it is never out of date with them. It runs nothing, writes nothing and decides nothing. The word `help` is Claude Code's own command, which is why the forge's manual has the Unix name `man`. The forge has no second help command.

## The command

```
/man
```

Replace the empty argument with a command, a method or a question:

```
/man check
/man walkthrough
/man how do I get my project into git
```

The first is a command, the second a working method, the third a need in free words. A name that is neither a command nor a method is read as a question.

## What happens

1. **Bare `/man`.** Claude prints the commands, each with its arguments and its purpose cut to one line, `/man` and `/manual` included. Then it prints each working method with the first sentence of its paragraph. It closes with one line: `/man <command>` for a command's page, `/man <method>` for a method's. You should now see two lists and that closing line.
2. **`/man <command>`.** Claude prints the command's purpose, its arguments and its purpose in full as the table of commands gives it. Where the command dispatches over a roster (checks, critic lenses, challenger personas, genres), it prints every entry with what that entry looks for, so you know before running it. It closes with the path of the command's skill file, for the reader who wants the whole procedure. You should now see the purpose, the arguments, the roster where there is one, and the skill path. A name with no skill file gets a plain statement that none exists, followed by the list of commands.
3. **`/man <method>`.** Claude matches the name against the working methods (case does not matter, hyphens and spaces are alike) and prints the paragraph in full. Where a skill holds the method's shape, it names that skill's path. You should now see the method's paragraph. An unknown name that is not a question gets the list of methods.
4. **`/man <question>`.** Claude takes your words as a need.
   - It reads the documentation's index, where every page carries the one question it answers, and chooses the pages that meet the need.
   - Where the need can be read two ways that lead to different pages, it asks once, in one sentence, and waits.
   - It reads the chosen pages, and the skill or definition a page names where the detail matters. Nothing is answered from memory.
   - It answers in plain sentences. The way the forge has comes first, with what you type. Then comes what matters on that way. Where several ways fit, one is recommended, with its reason, once.
   - Where the way leaves the forge, it says so plainly, because the forge does not do it. Examples are a repository to initialise and a program to install.
   - It names the pages it read by path at the end.

   You should now see an answer that opens with the way and ends with the paths of the pages read.

The index the question reads is made by the documentation run, described in [Generate the documentation](generate-the-documentation.md).

## What you have afterwards

Text in the conversation and nothing else: no file is written and no state changes. The output is in the language of the conversation. Command names, file paths, front-matter keys and the names of the methods stay in English.

## If something goes wrong

- The name is not a command: Claude says so and lists the commands.
- The name is not a method and not a question: Claude says so and lists the methods.
- The forge has nothing for the need: Claude says so. It names an open thread of the forge's own project if one carries the need. What Claude would do without a mechanism it marks as its own.

## A worked example of a command page

```
/man check
```

Claude prints the purpose of `/check`, its arguments `[check] [slug]`, the row's purpose in full, and then each check of the roster with what it looks for. It ends with the path `.claude/skills/check/SKILL.md`.

## A worked example of a question

```
/man how do I keep my project's history on a server
```

Claude reads the documentation's index, chooses the pages whose question meets the need, and reads them. It answers with the way the forge has and the command you type. It then says what matters on that way. It says plainly which step is yours, such as creating the remote repository, since the forge does not do it. It ends with the paths of the pages it read.

## See also

- [Commands](../reference/commands.md): the same table of commands, as a page.
- [Generate the documentation](generate-the-documentation.md): the run that makes the index the manual reads to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
