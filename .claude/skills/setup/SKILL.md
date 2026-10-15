---
description: First run after cloning the engine — create and fill CLAUDE.local.md by interview, set the session model to the forge's default, offer the git identity per host and the global guard in the global git configuration git reads; never overwrites, runs no git operation
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
     file git actually reads (`scripts/forge-status.py` names it;
     read it first, never overwrite existing content, report an
     existing stanza or guard and leave it):
     - per host, one stanza
       `[includeIf "hasconfig:remote.*.url:https://<host>/**"]` and
       one `[includeIf "hasconfig:remote.*.url:git@<host>:*/**"]`,
       both with `path = <absolute path>/.gitconfig-<host>` — the
       path absolute and the file in the user's local profile (on
       Windows `C:/Users/<user>`), not necessarily beside the global
       file: the global file follows HOME, and HOME may differ by
       place — a network home at work, the local profile at home —
       so a `~` path, or a file beside a global file that moves, is
       found from one place and not from the other (found
       2026-10-15); the file `.gitconfig-<host>` created with
       `[user]` `name` and `email` when missing. Where the global
       file already carries such a stanza with a `~` path, report it
       and offer to make the path absolute;
     - the global guard `user.useConfigOnly = true` under `[user]`.
       Where the global file carries a `user.name` or `user.email`,
       say the guard only bites once that identity is removed, and
       offer the removal — again only on the user's word.
     Declined: print the stanzas and the lines for the user to apply
     by hand. These are the only edits outside the engine; they are
     configuration text files, not a git operation.
     The identity is verified by git itself at the first
     `/import-project`: `scripts/forge-clone.py` reports the identity
     git resolves for the clone, and `/import-project` says what to do
     when it resolves none.
2. **`.claude/settings.local.json`**.
   - If it already exists: report the model it names and do not touch
     it.
   - Otherwise create it with `{ "model": "fable" }`, the strongest
     model, and tell the user in one sentence: the session is set to
     Fable, which the whole forge including the blind reviewers runs
     on, and it can be changed at any time with `/model` or by
     editing this file. Where the account does not offer Fable
     (`/model` does not list it), write the strongest model it lists
     and say which. A notice, not a question.
3. Finish by pointing at the next step from the Quickstart: start a
   new project with `/new-project <slug>`, or bring an existing one
   with `/import-project <git-url>`.
