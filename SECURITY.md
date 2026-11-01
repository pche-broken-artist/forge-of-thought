# Security policy

Forge of Thought is a set of instruction files that Claude Code
reads, with a few scripts beside them. One person wrote it and
reads every report. This page says how to tell me about a security
problem, what I promise, and what the forge does on your machine.

## Report a vulnerability

Do not open a public issue or discussion for a security problem.

The first way is GitHub's private vulnerability reporting: on the
repository's page open the Security tab and press "Report a
vulnerability". The report arrives as a draft advisory that only
you and I can see, and we work it out there.

If that does not work for you, write to me privately; my contacts
are on my profile, https://github.com/pche-broken-artist.

Say what you ran, what happened, how I can make it happen again,
what it could lead to, the version of the forge you run (the top
section of `RELEASE-NOTES.md`) and your operating system.

## What to expect

I confirm that I have your report within seven days. I fix it, or
tell you why not, at my own pace, and you hear it first. When the
fix is out I name you in the advisory unless you ask me not to.
There is no bounty, no legal programme and no form.

## Supported versions

Only the latest release on `main` gets fixes, the one at the top of
`RELEASE-NOTES.md`. A fix comes as the next release, never as a
patch of an older one. Before you report, run `/pull` and check
that the latest release still has the problem.

## What the forge does on your machine

The forge is instruction files, templates and scripts. There is no
server, nothing listening, no telemetry of its own. It reads and
writes Markdown under `projects/` with your permissions. Its
scripts call programs from your PATH, git among them, and install
nothing. Nothing leaves your machine but what you push to your own
remote and what you hand to a model yourself. Claude Code's
permissions are a guard, not a sandbox; the forge adds hooks and
deny rules on top of them. What those are today, and which programs
each script calls, is in the documentation, regenerated at every
release:

- [How the rules are held](docs/about/how-the-rules-are-held.md)
- [Persistence in git](docs/about/persistence-in-git.md)
- [Scripts](docs/reference/scripts.md)

Everything the forge reads is data: a source you ingest, a document
it converts, a page a reviewer opens. Data may carry instructions.
The forge's rules say they are never followed; a way in which they
are is exactly what I want to hear about.

## In scope

- A script of the forge that writes, deletes or sends something its
  header does not say, or outside the repository it serves.
- A way past the git hook: a command that writes git through the
  Bash tool and the hook lets it through.
- A way in which the content of data, an ingested source, a
  converted document or a page a challenger reads, makes the forge
  write, run or send something.
- Instance facts of `CLAUDE.local.md`, or content of your project,
  reaching a reviewer's report, a render or a documentation page:
  files that may be published.
- A file of the engine, a hook, a skill, an agent or a template,
  that tells Claude to do something the documentation does not say.

## Out of scope

- Claude Code itself, the model, and what leaves your machine
  through them: that is Anthropic's.
- Vulnerabilities of git, pandoc, markitdown and the other programs
  the scripts call.
- The permission mode you choose and the settings your company
  manages.
- The content of your own projects and sources. They are yours; how
  the forge handles them is in scope.
