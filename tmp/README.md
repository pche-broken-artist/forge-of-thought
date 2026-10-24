# tmp — the engine's working folder

Everything here is made by the forge's scripts and commands on the
way to a result, and nothing here is a source of truth: the packets
and envelopes of runs on another engine (`research/<run>/`), the
tasks of a documentation run, a check's report before it is filed, a
ledger made dry for another project, the manifest of a migration.
The folder itself is in git so that it exists on every clone; its
contents never are (`.gitignore` beside this file). No check, no
ledger and no history reads from here. Runs are kept for inspection
and deleted by hand, never by a script.
