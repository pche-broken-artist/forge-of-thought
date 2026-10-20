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
