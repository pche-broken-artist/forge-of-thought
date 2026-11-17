---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 200f8cf91631b8b0
inputs:
  - projects/forge/10-intent.md#POS.1920
  - CLAUDE.md#Repository layout
---

# The security policy and the code of conduct

The security policy and the code of conduct are the two fixed files in
the root of the engine (the repository that holds the forge itself):
`SECURITY.md` and `CODE_OF_CONDUCT.md`. This page says what each file
is, what the security policy promises and why neither file is
generated. It is for anyone who runs the forge, adds to it or weighs
it.

## What it is

The root of the engine holds renders. A render is an output that the
forge generates from a recipe (the file that says how the render is
made). What a render is in full is said in
[Renders and recipes](renders-and-recipes.md).

Beside the renders stand two files that are no render and derive from
nothing in the chain. The chain is the numbered documents of a
project, from its brief and its intent downward (see the
[Glossary](../reference/glossary.md)).

- `SECURITY.md`: the security policy. It is the own text of the
  principal (the person whose thinking is forged and who has the final
  word on all content).
- `CODE_OF_CONDUCT.md`: the code of conduct. It is the Contributor
  Covenant 3.0, word for word.

The [Repository layout](../reference/repository-layout.md) names both
among the files of the root, each as no render.

## How it works

### How a problem is reported

A security problem is reported through GitHub's private vulnerability
reporting. This is a setting of the repository. It is switched on
before the file points at it.

The fallback is the private way that the contributing file names. The
contributing file is described in
[Make a change to the forge](../extend/how-a-change-is-made.md).

A security problem is never reported as a public issue.

### What the forge promises

The policy promises three things:

- an acknowledgement within seven days
- a fix or a decision at the principal's pace, told to the reporter
  first
- credit in the advisory (the notice published about the problem)

A reporter who declines the credit is not named.

The policy promises nothing else:

- no bounty
- no safe harbour
- no form

### What is supported

Only the latest release on `main` (a branch of the repository) is
supported. A fix comes as the next release. What a release is stands
in the [Glossary](../reference/glossary.md).

### What the forge does on the machine

The policy says what the forge does on a machine by kind, not in
detail. "The user" below is whoever runs the forge on that machine.

- The forge is instruction files.
- It runs no server.
- It works with the user's permissions.
- It runs programs from PATH (the folders in which the system looks
  for a program).
- It sends nothing but what the user sends.
- Its data may carry instructions.
- Permissions are a guard and not a sandbox.

The specifics are left to the documentation pages. A release
regenerates those pages. This keeps the file true without a recipe.

### What is in scope

In scope is whatever makes the forge write, run, send or publish what
its rules do not say. The cause is one of four kinds:

- a script
- a hook (see the [Glossary](../reference/glossary.md))
- a file of the engine
- a piece of data

Out of scope are three things:

- Claude Code (the agent the forge runs in) and the tools that the
  scripts call
- the user's permission mode
- the content of the user's projects

### The code of conduct

The code of conduct is a standard, taken over unchanged. Three things
hold for it:

- It stands under its own licence (CC BY-SA 4.0). The README names
  that licence beside the engine's licence (CC BY 4.0).
- Its reporting sentence points at the private way that the
  contributing file names.
- Its suggested remedies are kept.

### What neither file has

Neither file is a render. Neither file has any of these three:

- a companion (a file beside it that keeps a record of it)
- a row (a line for it in a table of the forge)
- a check (a test that reads it; see the
  [Glossary](../reference/glossary.md))

The same holds for the principal's own files. Those are the files that
the principal makes by hand from the files of the forge. They are
described in [Renders and recipes](renders-and-recipes.md).

A change to either file is made on the principal's word.

## Why

One reason is recorded for each file.

The security policy is no render. A policy whose threat model is
derived from the design stays true only when it is re-rendered. A
release re-renders the documentation, not a policy. The policy
therefore speaks by kind, in the principal's own words, and leaves the
specifics to the pages that a release does regenerate.

The code of conduct is no render either. A standard that is adopted is
worth exactly its unchanged text.

The reason for the exact promises of the policy, the seven days among
them, is not recorded. The reason for the private channel is not
recorded.

## A worked example

Suppose a visitor finds a fault in the latest release on `main`. A
document that a project holds as data carries a line written as an
instruction. When the forge reads the document, it sends the content
of another file out of the machine. No rule of the forge says that it
sends that file.

The visitor opens no public issue. The visitor reports the fault
through the private vulnerability reporting of the repository. The
policy offers no form. The report is in the visitor's own words and
says three things:

- what carries the fault: a piece of data, here a document in the
  project `my-project`
- what the forge does that its rules do not say: it sends the content
  of a file
- where the fault was seen: the latest release on `main`

Each of the three places the report inside the policy. A piece of data
is one of the four kinds in scope. Sending is one of the four acts the
scope names. The latest release on `main` is the supported one.

The policy then says what the visitor may expect. An acknowledgement
arrives within seven days. The principal makes a fix or a decision at
the principal's own pace, and the visitor is told first. A fix comes
as the next release. The advisory credits the visitor. A visitor who
declines the credit is not named. The visitor receives no bounty and
no safe harbour.

The policy would not cover the same visitor for a fault in Claude Code
itself, in a tool that a script calls, in the user's permission mode
or in the content of a project. Those are out of scope.

## See also

- [Make a change to the forge](../extend/how-a-change-is-made.md): the
  contributing file a visitor reads, which points at both.
- [Renders and recipes](renders-and-recipes.md): what a render is and
  what the principal's own files beside the forge's are.
- [Repository layout](../reference/repository-layout.md): where the
  two files stand among the root's files.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
