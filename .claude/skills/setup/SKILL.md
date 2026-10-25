---
description: First run after cloning the engine — create and fill CLAUDE.local.md by interview, set the session model to the forge's default, offer the git identity per host, the global guard and the registration of the merge driver `ours`, written through `scripts/forge-config.py`; never overwrites
disable-model-invocation: true
---

Prepare this instance of the forge (POS.1050). Run after cloning the
engine, before any other work. Two files in the engine — plus, on the
user's word, the global git configuration outside it, which is git's
own (CLAUDE.md, Persistence), written only through
`scripts/forge-config.py`; what each of its calls writes and what it
leaves is its header's.

The conversation language is not configured yet on a true first run:
speak whatever language the user speaks to you.

1. **`CLAUDE.local.md`** at the engine root.
   - If it already exists: report briefly what it holds, touch
     nothing it has, and offer the lines the template has and the
     file lacks (an `Author` line on an instance made before it
     existed), asked for one by one and written on the user's word.
   - Otherwise copy `templates/CLAUDE.local.md` to the root and fill
     it by elicitation interview, one question at a time, the
     language first so that every later question arrives in it:
     - **Conversation language** — the language the working
       conversation runs in (the template says what follows it);
     - **Principal** — the role, whose thinking is being forged (the
       template's placeholder);
     - **Author** — the principal's handle, short, as it stands in
       the author column of every history record he decides
       (templates/history.md).
   - Keep the template's format; the file is gitignored and never
     committed.
   - Close with the **git identity**, which is git's, per host
     (CLAUDE.md, Persistence). First show what is there:
     `python scripts/forge-config.py` names the file git reads, the
     registration, the guard, a global identity and the per-host
     stanzas. Ask for the git hosts the user will push to (e.g.
     github.com, a company host) with a name and an e-mail for each —
     may be left for later; say so. Then offer, on the user's word,
     one call per host,
     `python scripts/forge-config.py --identity <host> <name> <email>`.
     A stanza or an identity file the script reports and leaves
     (another path, an absolute one among them, another name or
     e-mail) is shown, and `--replace` offered for it apart, again on
     the user's word. Then the global guard, `--guard`; where the
     script reports a global `user.name` or `user.email`, say the
     guard only bites once that identity is removed and offer
     `--guard --unset-identity`, again only on the user's word. Where
     git reads another global file in each place, as the script's
     header says, say so: `/setup` runs once in each. Declined:
     print the commands for the user to run by hand.
     The identity is verified by git itself at the first
     `/import-project`: `scripts/forge-clone.py` reports the identity
     git resolves for the clone, and `/import-project` says what to do
     when it resolves none.
   - Then the **registration of the merge driver** `ours`, once per machine
     and once in each place where git reads another global file, on
     the user's word (SOL.0740): the bare run above says whether it is
     there; offer `python scripts/forge-config.py --register`, and
     `--zdiff3` apart. Say in one sentence that these hold for every
     repository on the machine; what each key does is the script's
     header.
     Declined: print the command for the user to run by hand.
     `forge-status` reports the registration afterwards, ok or the
     keys missing.
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
