---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 88ed088ca9a374e3
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command, or ask how to do something

This page is for you when you want to know what a command does, what a
working method is, or how to get something done with the forge. `/man`
is the forge's manual: it prints what you ask for, in the conversation
language, and does nothing else. The forge has no second help command.
The word `help` belongs to Claude Code itself, which is why the manual
has the Unix name.

## When to use it

- You want the list of commands and working methods.
- You want to know what one command is for, which arguments it takes
  and what its roster looks for before you run it.
- You want the paragraph of one working method.
- You have a need in your own words and do not know which command
  meets it.

## The command

```
/man [command | method | question]
```

`/manual` is an alias and takes the same arguments. The manual runs
nothing, writes nothing and decides nothing. It reads the files that
own each fact at the moment you call it, so what it prints is never
older than the forge itself. The principal (whoever's thinking is
being forged) is the one who reads the answer and chooses what to do
with it.

## What happens

1. Bare `/man` prints the overview. The commands come as a list, each
   with its arguments and its purpose cut to one line, `/man` and
   `/manual` included. The working methods follow, each with the first
   sentence of its paragraph. A last line tells you to type
   `/man <command>` for a command and `/man <method>` for a method.
   You should now see the two lists and that closing line.
2. `/man <command>` prints the page of one command. It gives the
   purpose, the arguments and the purpose of the command's row in full.
   Where the command dispatches over a roster (checks, lenses,
   personas or genres), it prints each entry with its description and
   what the entry looks for, so that you know it before you run
   anything. A last line names the skill file, for the reader who wants
   the whole procedure. If no such command exists, the manual says so
   and lists the commands. You should now see the command's purpose,
   its arguments, its roster where it has one, and the skill file.
3. `/man <method>` prints the paragraph of one working method in full
   and, where a skill holds the shape of the method, the path of that
   skill. The name matches without regard to case, and hyphens and
   spaces count alike. If the name is unknown and is not a question,
   the manual says so and lists the methods. You should now see the
   method's paragraph and, where there is one, its skill.
4. `/man <question>` takes anything that is neither a command nor a
   method as a need in your own words. Claude reads the index of the
   documentation, where every page carries the one question it
   answers, and chooses the pages that meet your need. Where your
   words can be read two ways that lead to different pages, it asks
   once, in one sentence, and waits. It then reads the chosen pages,
   and the skill they name where the detail matters. You should now
   see the answer, built in this order:
   - the way the forge has, with what you type;
   - what matters to know on that way;
   - where several ways fit, one recommended, with its reason;
   - plainly, where the way leaves the forge (a repository to
     initialise, a program to install), because the forge does not do
     that part for you.

   The pages read are named by path at the end of the answer.
5. Where the forge has nothing for your need, the manual says so. It
   names an open thread of the forge's own project if one carries the
   need. What Claude would do without a mechanism is marked as its own
   suggestion.

## What you have afterwards

You have an answer on the screen and nothing else: no file is written,
no command has run and no decision is taken. The language is the
conversation language, with command names, paths and front-matter keys
staying in English.

## If something goes wrong

- A command name that does not exist: the manual says so and lists the
  commands.
- A method name that does not exist and does not read as a question:
  the manual says so and lists the methods.
- A question answered "nothing for this": the forge has no mechanism
  for the need. The manual says so instead of inventing one.
- A question answered from pages that look stale: the answer is only as
  current as the documentation index. See [Generate the
  documentation](generate-the-documentation.md) for the run that makes
  it.

## A worked example

A command page. You type a command name, here `<command>` stands for
any command of the overview:

```
/man <command>
```

The manual prints the command's purpose, its arguments and the full
purpose of its row. If the command has a roster, each entry follows
with its description and what it looks for. The last line names the
skill file, `.claude/skills/<command>/SKILL.md`.

A question. You type your need in your own words:

```
/man how do I <something I want done>?
```

The manual finds no command and no method by that name, so it reads
the documentation index and the pages whose question meets your need.
It answers in plain sentences: first the way the forge has, with the
line you type; then what matters on that way; then, if two ways fit,
the one it recommends and why. If part of the way happens outside the
forge, it says so. The answer closes with the paths of the pages it
read.

## See also

- [Commands](../reference/commands.md): the same table of commands, as
  a page.
- [Generate the documentation](generate-the-documentation.md): the run
  that makes the index the manual reads to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
