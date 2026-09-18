---
description: First run after cloning the engine — create and fill CLAUDE.local.md by interview, set the session model (Fable), offer the git identity per host and the global guard in ~/.gitconfig; never overwrites, runs no git operation
disable-model-invocation: true
---

Prepare this instance of the forge (POS.1050). Run after cloning the
engine, before any other work. Two files in the engine — plus, on the
user's word, the git identity configuration outside it, which is
git's own (CLAUDE.md, Persistence); the command runs no git
operation.

The conversation language is not configured yet on a true first run:
speak whatever language the user speaks to you.

1. **`CLAUDE.local.md`** at the engine root.
   - If it already exists: report briefly what it holds and do not
     touch it.
   - Otherwise copy `templates/CLAUDE.local.md` to the root and fill
     it by elicitation interview, one question at a time, the
     language first so that every later question arrives in it:
     - **Conversation language** — the language the working
       conversation runs in (the template says what follows it);
     - **Principal** — the role, whose thinking is being forged (the
       template's placeholder).
   - Keep the template's format; the file is gitignored and never
     committed.
   - Close with the **git identity**, which is git's, per host
     (CLAUDE.md, Persistence): ask for the git hosts the user will
     push to (e.g. github.com, a company host) with a name and an
     e-mail for each — may be left for later; say so. Then offer to
     write, on the user's word, into the global git configuration
     file git actually reads (`git config --global --list
     --show-origin` names it; read it first, never overwrite existing
     content, report an existing stanza or guard and leave it):
     - per host, one stanza
       `[includeIf "hasconfig:remote.*.url:https://<host>/**"]` and
       one `[includeIf "hasconfig:remote.*.url:git@<host>:*/**"]`,
       both with `path = <absolute path>/.gitconfig-<host>` — the
       path absolute, beside that global file, since `~` in git's
       hands and in the shell's may differ — and the file
       `.gitconfig-<host>` created with `[user]` `name` and `email`
       when missing;
     - the global guard `user.useConfigOnly = true` under `[user]`.
       Where the global file carries a `user.name` or `user.email`,
       say the guard only bites once that identity is removed, and
       offer the removal — again only on the user's word.
     Declined: print the stanzas and the lines for the user to apply
     by hand. These are the only edits outside the engine; they are
     configuration text files, not a git operation.
2. **`.claude/settings.local.json`**.
   - If it already exists: report the model it names and do not touch
     it.
   - Otherwise create it with `{ "model": "fable" }` and tell the
     user in one sentence: the session is set to Fable — the
     strongest available model, which the whole forge including the
     blind reviewers runs on — and it can be changed at any time with
     `/model` or by editing this file. A notice, not a question.
3. Finish by pointing at the next step from the Quickstart: start a
   new project with `/new-project <slug>`, or bring an existing one
   with `/import-project <git-url>`.
