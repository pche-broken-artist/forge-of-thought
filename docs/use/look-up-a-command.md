---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
  - CLAUDE.md
---

# Look up a command

This page is for a user of the forge who wants to know what a command
does, what arguments it takes or how a working method runs, without
leaving the conversation. The forge has its own manual for that:
`/man`, with the alias `/manual`.

## What the manual is

`/man [command | method]` prints the forge's manual. It has no text of
its own: everything it shows is read at the moment you call it from
the files that own it (`CLAUDE.md`, the skills, the agents, the state
and genre files) and shortened to the line. So what you see is always
what those files say now.

It only reads. It runs none of the commands it describes.

`/manual` is the same command under another name: it takes the same
arguments and does exactly what `/man` does.

The name is the Unix one because the word `help` is already Claude
Code's own command.

## See the overview

1. Type `/man` with no argument.
2. You see:
   - every command of the forge with its arguments, each followed by
     its purpose cut to one line, `/man` and `/manual` included;
   - every working method by name, each with the first sentence of
     its paragraph;
   - a closing line telling you that `/man <command>` opens a
     command's page and `/man <method>` a method's.

## Look up one command

1. Type `/man` followed by the command's name, for example
   `/man critique`.
2. You see:
   - the command's purpose and its arguments, and the purpose as the
     forge's command list states it, in full;
   - where the command chooses among several entries (a check, a
     critic lens, a challenger persona, a recipe genre), the list of
     those entries, each with its own description and what it looks
     for, so that you know what an entry does before you run it;
   - a closing line naming the skill file, for when you want the
     whole procedure.

If no command of that name exists, the manual says so and lists the
commands, as in the overview.

## Look up one working method

1. Type `/man` followed by the method's name, for example
   `/man walkthrough`. Case does not matter, and a hyphen and a space
   count alike, so `/man step-by-step` and `/man step by step` both
   work.
2. You see the method's paragraph in full and, where the method's
   shape is held in a skill, that skill's path.

If no method of that name exists, the manual says so and lists the
methods, as in the overview.

## Language

The manual answers in your conversation language, the whole page
included: descriptions and the lists of what each entry looks for are
translated. Only the notation stays in English: command names, file
paths, IDs, front-matter keys and the names of the working methods,
each name followed once by its translation.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
