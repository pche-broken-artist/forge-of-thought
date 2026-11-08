---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 24442bcb684e6d51
inputs:
  - projects/forge/10-intent.md#POS.1920
  - CLAUDE.md#Repository layout
---

# The security policy and the code of conduct

The security policy and the code of conduct are the two fixed files
of the engine's root: `SECURITY.md` and `CODE_OF_CONDUCT.md`, the
only files among the root's documents that are no render and derive
from nothing in the chain. This page says what the two files are,
what the policy promises and holds, and why neither is generated. It
is for the user who wants to report a problem, for the extender who
wonders why these two files are not made like the README, and for
the evaluator who wants to understand how the forge handles security
and conduct.

## What it is

The root of the engine holds a README, release notes and a
contributing file, each a render: a file generated from a recipe
and never edited by hand (what a render is and what a recipe is:
[Renders and recipes](renders-and-recipes.md)). Beside them stand
two files that are not renders. Where they stand among the root's
files is shown in [Repository layout](../reference/repository-layout.md).

`SECURITY.md` is the security policy. It is the principal's own text.
The principal is the person whose thinking is forged, the one who
supplies ideas, answers and decisions and holds final authority over
all content.

`CODE_OF_CONDUCT.md` is the code of conduct. It is the Contributor
Covenant 3.0 word for word. The Covenant comes under its own licence,
CC BY-SA 4.0, which the README names beside the engine's own licence,
CC BY 4.0. Two things of the text are adjusted to the forge: its
reporting sentence points at the private way that the contributing
file names, and its suggested remedies are kept as they stand in the
Covenant. The contributing file is the page a visitor reads first
([Make a change to the forge](../extend/how-a-change-is-made.md)).

Neither file is a render. Neither has a history companion, a row in
the ledger or a check. The ledger is the project's single source of
truth for state, made at read time from the documents. The same
holds for the principal's own files beside the forge's renders: a
file the forge did not make is kept in git with the rest, and the
forge reads it as no document. A change to either file is the
principal's word, never Claude's.

## How it works

The policy is described here by kind, in the person's terms. Its
exact wording is the file's own.

### How a problem is reported

A problem is reported through GitHub's private vulnerability
reporting. That is a setting of the repository. The setting is
switched on before the file points at it. The fallback is the
private way the contributing file names. A problem is never reported
as a public issue.

### What the forge promises

The forge promises four things to a reporter:

- an acknowledgement within seven days
- a fix or a decision, at the principal's pace, told to the reporter
  first
- credit in the advisory, unless the reporter declines it
- nothing else: no bounty, no safe harbour, no form

### What is supported

Supported is the latest release on `main` only. A fix lands in the
next release.

### What the forge does on the machine

The policy says what the forge does on the machine by kind, not by
listing files:

- the forge is a set of instruction files
- there is no server
- it runs under the user's permissions
- it calls programs found on PATH
- it sends nothing but what the user sends
- the data it reads may carry instructions
- the permissions are a guard, not a sandbox

The specifics, which script does what and which hook denies what,
are left to the documentation pages. A release regenerates those
pages. So the policy stays true without a recipe of its own.

### What is in scope and what is not

In scope is a script, a hook, a file of the engine or a piece of
data that makes the forge write, run, send or publish what its rules
do not say.

Out of scope are:

- Claude Code itself, Anthropic's agent for the command line that
  runs the forge
- the tools the scripts call
- the user's permission mode
- the content of the user's projects

## Why

The policy carries a threat model. That model is derived from the
design of the forge. A text derived from the design stays true only
when it is re-rendered after the design changes. A release
re-renders the documentation, not a policy. So the policy is kept
short and by kind, the specifics are left to the pages a release
regenerates, and the file is the principal's own text rather than a
render.

The code of conduct is an adopted standard. A standard adopted is
worth exactly its unchanged text. So the Covenant stands word for
word, and the file is no render.

Why the policy promises exactly what it promises, seven days, credit,
no bounty and no safe harbour, is not recorded.

## A worked example

A visitor finds that a script of the engine, run as the forge says
to run it, pushes to a remote the user never named. This is in scope:
a script making the forge send what its rules do not say. The visitor
does not open a public issue. He opens a private vulnerability report
on the repository, or, where that is not available, uses the private
way the contributing file names.

The report says, in words:

- what he did: the command he ran and the state of the repository
  when he ran it
- what he saw: where the script pushed and what it printed
- what he expected: what the forge's own rules say the script does
- which release he ran: the latest release on `main`, since only
  that one is supported
- whether he wants credit in the advisory, or declines it

He can then expect an acknowledgement within seven days, and a fix
or a decision told to him before anyone else.

## See also

- [Make a change to the forge](../extend/how-a-change-is-made.md):
  the contributing file a visitor reads, which points at both.
- [Renders and recipes](renders-and-recipes.md): what a render is and
  what the principal's own files beside the forge's are.
- [Repository layout](../reference/repository-layout.md): where the
  two files stand among the root's files.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
