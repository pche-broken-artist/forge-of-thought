---
id: THR.0720
concerns: intent, solution-design
origin: the principal
status: open
---

The global git configuration moves with HOME, and the forge must not
depend on where it lies: no absolute path, for anyone. Opened
2026-10-20.

Found 2026-10-20 at /setup after the pull of release 5.26: on a
domain machine Windows sets HOMEDRIVE=H: and HOMEPATH=\ from the
home folder in Active Directory; HOME is set nowhere (user and
machine both "not set"); Git for Windows takes HOME, else
HOMEDRIVE+HOMEPATH when it exists, else USERPROFILE (the order from
memory, consistent with the output). So git read H:\.gitconfig at
work and would read C:\Users\<user>\.gitconfig off the network. The
fix of 2026-10-15 (commit 5050cc0: identity files in the local
profile, absolute paths in the stanzas) mended only where the
stanzas point; the stanzas themselves, and since 5.26 the merge
drivers (SOL.0740, one registration per machine), stay in a file
that moves. The principal: absolute paths must go, a user may put
his profile anywhere; it must work for everyone, not for him.

Direction accepted 2026-10-20 (to be written into the intent):
the forge reads and writes the global configuration only through
`git config --global`, which lands where git reads, and names no
path; identity stanzas carry `path = .gitconfig-<host>`, relative
to the global file; on a machine whose home moves, /setup runs once
in each place and forge-status says where the registration is
missing. Chosen against: GIT_CONFIG_GLOBAL set by /setup (a new
exception to POS.1050, a change to the user's system); the
registration per repository (reverses SOL.0740, leaves the
identity unsolved); writing both files (drifts). GIT_CONFIG_GLOBAL
stays a user's own choice: the principal set it for himself on
2026-10-20 (%USERPROFILE%\.gitconfig, REG_EXPAND_SZ, H:\.gitconfig
copied there), not something the forge does.

Built 2026-10-20 on the principal's word, ahead of the intent:
scripts/forge-config.py (bare shows; --register [--zdiff3];
--guard [--unset-identity]; --identity <host> <name> <email>
[--replace]); forge_repos.global_config_files, which also unquotes
the path git C-quotes in --show-origin, used by forge-status.
Not yet run beyond the bare read.

State 2026-10-20: open. Next: run --register; the stanzas of
github.com and gitlab.sazka.cz rewritten relative (--replace, the
identity file then named .gitconfig-<host>, the existing
.gitconfig-github and .gitconfig-sazka to be settled); --guard;
then the intent round: POS.1050, POS.0950, SOL.0150, SOL.0740, the
setup skill (step 1, git identity and registration through
forge-config), CLAUDE.md Persistence (~/.gitconfig, "that same
global file") and the Repository layout's scripts line; the open
item of /setup, the Author line PCHe in CLAUDE.local.md, still
waits for a verdict.

Run 2026-10-20 on the principal's word, on his machine: --register
--zdiff3 and --guard written; the stanzas of github.com and
gitlab.sazka.cz rewritten to `.gitconfig-github.com` and
`.gitconfig-gitlab.sazka.cz` by --identity --replace, the names set
by the author of his commits on each host (git log): PCHe
<petr.chlumsky@gmail.com> on github.com, "Petr Chlumsky"
<chlumsky@allwyn.cz> on gitlab.sazka.cz; --replace widened to
rewrite a differing name or e-mail in the identity file. The
relative include path verified by git itself (--show-origin names
the file beside the global one, in the engine and in ai-strategy).
Found on the way: the engine's own `.git/config` carried a local
user.name and user.email, a remnant of the identity once set at
creation, which overrode every stanza (today's commit 08f4ee7 was
signed by it); removed by the principal with `git config --unset`.
Worth considering in the round: forge-config or forge-status
reporting a repository-local identity, since the forge sets none
(POS.0950). The old files .gitconfig-github and .gitconfig-sazka
are used by nothing; the principal may delete them.

State 2026-10-20: open. The machine is done. Left: the intent round
(POS.1050, POS.0950, SOL.0150, SOL.0740, the setup skill, CLAUDE.md
Persistence and the Repository layout's scripts line, the report of
a local identity) and the Author line PCHe in CLAUDE.local.md,
waiting for a verdict.

State 2026-10-21: open. The engine check of 2026-10-21 found the gap
as FND.2260, the setup skill against forge-config; the round above
settles both.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
