---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 8d4849216f9baf66
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command, or ask how to do something

`/man` is the forge's manual: it prints what a command or a working method is, and it answers a need you say in your own words. It is for the principal (the person whose thinking is forged) who wants to know what a command does before running it, or does not know which command to use.

## When to use it

- You want the list of commands and working methods.
- You want to know what one command is for, what arguments it takes and what a check, lens, persona or genre it dispatches over looks for.
- You want one working method (a named way a conversation runs) in full.
- You know what you want to do, but not how the forge does it.

## The command

```
/man [command | method | question]
```

`/manual` is an alias and does the same with the same arguments. The word `help` is not used because it is Claude Code's own command, hence the Unix name.

`/man` runs nothing, writes nothing and decides nothing. It reads the files that own the forge's rules at the moment of the call and shortens them to a line, so what it prints is never older than those files.

## What happens

1. **Bare `/man`.** Claude prints each command with its arguments and its purpose cut to one line, `/man` and `/manual` included. Then it prints each working method by name with the first sentence of its paragraph. It closes with a line pointing to `/man <command>` and `/man <method>`.

   You should now see the list of commands, the list of methods and the closing line.

2. **`/man <command>`.** Claude prints the command's purpose, its arguments and the purpose from the command table in full. Where the command dispatches over a roster, it prints each entry with its description and what it looks for, so you know what a check, a lens, a persona or a genre goes after before you run it. It closes with the path of the command's skill file, which holds the whole procedure. If no such command exists, it says so and lists the commands.

   You should now see the purpose, the arguments, the roster where there is one, and the path of the skill file.

3. **`/man <method>`.** Claude matches your word against the names of the working methods, ignoring case and treating hyphens and spaces alike. It prints the method's paragraph in full and, where the method has a skill that holds its shape, the path of that skill. If the word is neither a method nor a question, it says so and lists the methods.

   You should now see the method's paragraph and, where there is one, its skill path.

4. **`/man <question>`.** Any words that are neither a command nor a method are taken as a need. Claude reads the documentation's index, where every page carries the one question it answers, and chooses the pages whose question meets your need. If the need can be read two ways that lead to different pages, it asks once, in one sentence, and waits for you. It then reads the chosen pages, and the skill or definition they name where the detail matters. Nothing is answered from memory.

   The answer comes in plain sentences, in this order:

   - the way the forge has, with what you type
   - what matters to know on that way
   - where several ways fit, one recommended, with its reason
   - plainly, where the way leaves the forge, such as a repository to initialise or a program to install, because the forge does not do that for you

   The pages read are named by path once, at the end.

   You should now see an answer that names the way first and ends with the paths of the pages it was read from.

## What you have afterwards

You have an answer in the conversation and nothing else: no file is written, no command is run and nothing is decided. The output is in the conversation language. The notation stays English: command names, file paths and front-matter keys.

## If something goes wrong

- **The command is unknown.** Claude says so and lists the commands.
- **The method is unknown and the words are not a question.** Claude says so and lists the methods.
- **The forge has nothing for your need.** Claude says so. It names an open thread of the forge's own project if one carries the need. Whatever Claude would do without a mechanism of the forge it marks as its own, so you can tell it from what the forge defines.

## A worked example

A command page:

```
/man <command>
```

Claude prints the purpose of the command and its arguments. If the command is a check, a lens or a persona roster, it lists each member with what it looks for. The last line names the command's skill file.

A question:

```
/man how do I keep a copy of my project on a server?
```

The words match no command and no method, so Claude takes them as a need. It reads the documentation's index and chooses the pages whose question meets the need. It answers with the way the forge has and what you type. It then says what matters on that way. If part of the way is a step the forge does not do, such as creating a repository, it says so plainly. It ends by naming the pages it read.

## See also

- [Commands](../reference/commands.md): the same table of commands, as a page.
- [Generate the documentation](generate-the-documentation.md): the run that makes the index the manual reads to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
