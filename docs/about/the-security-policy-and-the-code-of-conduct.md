---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 1447c396d1b9c121
inputs:
  - projects/forge/10-intent.md#POS.1920
  - CLAUDE.md#Repository layout
---

# The security policy and the code of conduct

The security policy and the code of conduct are the two files of the
engine's root that are written by hand and generated from nothing:
`SECURITY.md` says how a security problem is reported and what the
forge promises in return, and `CODE_OF_CONDUCT.md` says how people
treat each other around the project. This page is for the user who
wants to report something, the extender who wonders why these two
files have no recipe, and the evaluator who wants to know what the
policy promises and what it does not. It says what the two files are,
how the policy is built so that it stays true, and why neither file is
a [render](renders-and-recipes.md).

## What it is

Most files of the engine's root are renders: outputs generated from a
recipe, never edited by hand. The README, the release notes and the
contributing file are of that kind. Where they stand among the root's
files is shown on [Repository layout](../reference/repository-layout.md).

Beside them stand two files that are no render and derive from
nothing in the chain, that is, from none of the project's versioned
documents:

- `SECURITY.md`, the security policy: the own text of the principal
  (the person whose thinking the forge serves and who has the final
  word on its content).
- `CODE_OF_CONDUCT.md`, the code of conduct: the Contributor Covenant
  3.0, word for word.

The code of conduct comes under its own licence, CC BY-SA 4.0. That
licence is named in the README beside the engine's own licence, CC BY
4.0. Two things of the adopted text are adjusted to the project: its
reporting sentence points at the private way that the contributing
file names, and its suggested remedies are kept as they stand. The
contributing file is the one a visitor reads first; what it says about
making a change is on [Make a change to the forge](../extend/how-a-change-is-made.md).

Neither file is a render. Neither has a history companion, a row in
the [ledger](../reference/glossary.md) (the file that holds a
project's state) or a check that reads it. The same holds for the
principal's own files beside the forge's renders, which the page
[Renders and recipes](renders-and-recipes.md) describes. A change to
either file is the principal's word.

## How it works

The policy is written by kind, not by specifics. Each of its parts
says what holds in general terms, so that no detail in it goes stale
when the engine changes.

**How a problem is reported.** A security problem is reported through
GitHub's private vulnerability reporting. That is a setting of the
repository, and it is switched on before the file points at it. The
fallback is the private way the contributing file names. A public
issue is never the way.

**What the forge promises.** The forge promises these things and
nothing else:

- an acknowledgement within seven days;
- a fix or a decision, at the principal's pace, told to the reporter
  first;
- credit in the advisory, unless the reporter declines it.

There is no bounty, no safe harbour and no form. Why the promises are
exactly these, and why the channel is a private one, is not recorded.

**What is supported.** The latest release on `main` is supported, and
nothing else. A fix comes with the next release.

**What the forge does on the machine.** The policy says this by kind
and leaves the specifics to the documentation pages, which a release
regenerates:

- the forge is instruction files;
- there is no server;
- it runs with the user's permissions;
- it runs programs found on PATH;
- nothing is sent but what the user sends;
- data it reads may carry instructions;
- its permissions are a guard, not a sandbox.

Because the specifics live in the documentation and not in the policy,
the policy stays true without a recipe.

**What is in scope.** In scope is any script, hook, file of the engine
or piece of data that makes the forge write, run, send or publish what
its rules do not say.

**What is out of scope.** Out of scope are Claude Code itself, the
tools the scripts call, the user's permission mode and the content of
the user's projects.

The code of conduct has no mechanism of its own beyond the two
adjustments named above: its reporting sentence points at the private
way the contributing file names, and the remedies it suggests are
kept.

## Why

A policy whose threat model is derived from the design stays true only
when it is re-rendered. A release re-renders the documentation, not a
policy. So the policy is written in a way that does not depend on the
design's details: it states kinds, and it points at the documentation
for the specifics. That is why it needs no recipe and is no render.

A standard adopted is worth exactly its unchanged text. That is why
the code of conduct is the Contributor Covenant 3.0 word for word
rather than a render composed from the project's own material, and
why only its reporting sentence is pointed at the project's private
way.

Neither file has a companion, a row or a check because the two are
treated as the principal's own files, and the principal's own files
have none of the three. A change to either is the principal's word.

## A worked example

A visitor has cloned the latest release and noticed that one script of
the engine sends something to a remote that the forge's rules do not
say it sends. That is in scope: a script making the forge send what
its rules do not say.

The visitor does not open a public issue. He opens a private
vulnerability report on the repository, or, where that is not open to
him, uses the private way the contributing file names. In the report
he says, in his own words:

- which file it is, by its path in the engine;
- what the file makes the forge do that the rules do not say: here,
  send;
- how he saw it, so that the principal can see the same;
- which release he was on, which is the latest release on `main`;
- whether he wants to be credited in the advisory or declines it.

He then expects an acknowledgement within seven days, and after that a
fix or a decision, told to him before it is told to anyone else. The
fix, where there is one, arrives with the next release. He expects no
bounty and no form to fill in.

## See also

- [Make a change to the forge](../extend/how-a-change-is-made.md): the contributing file a visitor reads, which points at both.
- [Renders and recipes](renders-and-recipes.md): what a render is and what the principal's own files beside the forge's are.
- [Repository layout](../reference/repository-layout.md): where the two files stand among the root's files.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
