#!/usr/bin/env python3
"""
forge-config.py - read and write the global git configuration the
forge needs, through git alone.

SYNOPSIS
    python scripts/forge-config.py
    python scripts/forge-config.py --register [--zdiff3]
    python scripts/forge-config.py --guard [--unset-identity]
    python scripts/forge-config.py --identity <host> <name> <email> [--replace]

WHAT IT DOES
    The one door of the forge to the user's global git configuration
    (CLAUDE.md, Persistence; SOL.0150, SOL.0740 of the forge solution
    design). Every read and every write goes through
    `git config --global`, so it lands in the file git itself reads,
    wherever that lies: the forge names no path to it, because git
    decides it (HOME, HOMEDRIVE and HOMEPATH, GIT_CONFIG_GLOBAL) and
    it may differ from place to place - a network home at work, the
    local profile at home. On such a machine the configuration is made
    once in each place; forge-status says where it is missing.

    A key that already carries the value asked is reported and left;
    a key that carries another value is reported and left as well,
    never overwritten, unless --replace is given for an identity.
    Values are compared as git stores them, so a name differing in a
    diacritic differs.

    Bare: what is there - the file git reads, the registration of the
    merge driver ours, the guard, a global identity and the per-host
    identity stanzas. Changes nothing.

    --register: the merge driver ours and the settings it needs, once per
    place (SOL.0740): merge.ours.driver true, merge.renormalize true,
    rebase.backend merge (the apply backend ignores drivers) and
    rerere.enabled true, a convenience. --zdiff3 adds
    merge.conflictStyle zdiff3. They hold for every repository the
    configuration serves.

    --guard: user.useConfigOnly true (why: CLAUDE.md, Persistence).
    It bites only once no global user.name or user.email is left;
    --unset-identity removes them.

    --identity <host> <name> <email>: the two stanzas of one host,
    includeIf "hasconfig:remote.*.url:https://<host>/**" and
    includeIf "hasconfig:remote.*.url:git@<host>:*/**", each with
    path = .gitconfig-<host>, a path relative to the global file, so
    the identity file always lies beside the file that includes it;
    then that file, with [user] name and email, written by
    `git config --file` where it is missing. A stanza that carries
    another path, an absolute one among them, and an identity file
    that carries another name or e-mail are reported and left;
    --replace rewrites them.

WHAT IT NEEDS
    Python 3.8 or newer; git 2.36 or newer on PATH (hasconfig in
    includeIf). `forge_repos.py` and `forge_tools.py` beside it.

EXAMPLES
    python scripts/forge-config.py
    python scripts/forge-config.py --register --zdiff3
    python scripts/forge-config.py --guard --unset-identity
    python scripts/forge-config.py --identity github.com "Jane Doe" jane@example.com
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

ROOT = fr.ENGINE_ROOT


def get(key, *scope):
    return fr.git_out(["config", *(scope or ("--global",)), "--get", key], ROOT)


def put(key, value, *scope):
    fr.git(["config", *(scope or ("--global",)), key, value], ROOT, check=True)


def ensure(key, value, replace=False, *scope):
    """Write `key` unless it already carries a value; say what was done."""
    current = get(key, *scope)
    if current == value:
        print(f"   {key} = {value} - already there, left")
    elif current and not replace:
        fr.say(f"   {key} = {current} - carries another value than {value}, left", "yellow")
    else:
        put(key, value, *scope)
        word = f"replaced {current} with" if current else "written"
        fr.say(f"   {key} = {value} - {word}", "green")


def stanza_keys(host):
    return (f"includeIf.hasconfig:remote.*.url:https://{host}/**.path",
            f"includeIf.hasconfig:remote.*.url:git@{host}:*/**.path")


def show():
    files = fr.global_config_files()
    print("global git config: " + (files[0] if files
                                   else "none yet - git creates it at its first write"))
    missing = fr.registration_state()
    if not missing:
        fr.say("registration:      ok", "green")
    else:
        fr.say("registration:      missing " + ", ".join(missing) + " - --register", "yellow")
    guard = get("user.useConfigOnly")
    fr.say("guard:             " + ("user.useConfigOnly = true" if guard == "true"
                                    else "missing - --guard"),
           "green" if guard == "true" else "yellow")
    name, email = get("user.name"), get("user.email")
    if name or email:
        fr.say(f"global identity:   {name} <{email}> - the guard does not bite while it stands",
               "yellow")
    listing = fr.git_out(["config", "--global", "--get-regexp", r"^includeif\..*\.path$"], ROOT)
    for line in listing.splitlines():
        key, _, path = line.partition(" ")
        relative = not (Path(path).is_absolute() or path.startswith("~") or ":" in path[:3])
        print(f"identity stanza:   {key} -> {path}"
              + ("" if relative else "  (not relative to the global file)"))
    if not listing:
        print("identity stanza:   none")


def register(zdiff3):
    print("registration of the merge driver ours (SOL.0740):")
    for key, value in fr.REGISTRATION:
        ensure(key, value)
    ensure("rerere.enabled", "true")
    if zdiff3:
        ensure("merge.conflictStyle", "zdiff3")


def guard(unset_identity):
    print("the guard:")
    ensure("user.useConfigOnly", "true")
    for key in ("user.name", "user.email"):
        value = get(key)
        if not value:
            continue
        if unset_identity:
            fr.git(["config", "--global", "--unset-all", key], ROOT, check=True)
            fr.say(f"   {key} = {value} - removed", "green")
        else:
            fr.say(f"   {key} = {value} - the guard does not bite while it stands; "
                   "--unset-identity removes it", "yellow")


def identity(host, name, email, replace):
    print(f"identity for {host}:")
    include = f".gitconfig-{host}"
    for key in stanza_keys(host):
        ensure(key, include, replace)
    files = fr.global_config_files()
    if not files:
        fr.fail("git reports no global configuration file after the write.")
    target = Path(files[0]).parent / include
    scope = ("--file", str(target))
    ensure("user.name", name, replace, *scope)
    ensure("user.email", email, replace, *scope)
    print(f"   identity file: {target}")


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("--register", action="store_true",
                    help="the merge driver ours and the settings it needs")
    ap.add_argument("--zdiff3", action="store_true",
                    help="with --register: merge.conflictStyle zdiff3")
    ap.add_argument("--guard", action="store_true", help="user.useConfigOnly true")
    ap.add_argument("--unset-identity", action="store_true",
                    help="with --guard: remove a global user.name and user.email")
    ap.add_argument("--identity", nargs=3, metavar=("HOST", "NAME", "EMAIL"),
                    help="the two includeIf stanzas of one host and its identity file")
    ap.add_argument("--replace", action="store_true",
                    help="with --identity: rewrite a stanza or an identity that differs")
    a = ap.parse_args(argv)
    fr.need_git()
    if a.zdiff3 and not a.register:
        ap.error("--zdiff3 goes with --register")
    if a.unset_identity and not a.guard:
        ap.error("--unset-identity goes with --guard")
    if a.replace and not a.identity:
        ap.error("--replace goes with --identity")
    if not (a.register or a.guard or a.identity):
        show()
        return 0
    if a.register:
        register(a.zdiff3)
    if a.guard:
        guard(a.unset_identity)
    if a.identity:
        identity(*a.identity, a.replace)
    print()
    show()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
