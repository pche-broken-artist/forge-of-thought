"""
forge-engine.py - run one packet on a model of another family and bring
its answer back as a note. The CLI adapter of the forge: one script, one
table of engines, the login the user's (made once outside the forge, in
the engine's own tool), the forge carrying no key, account or
configuration (POS.0800, research of 2026-10-23).

    python scripts/forge-engine.py <engine> --packet <dir> --out <file>
        [--model <word>] [--effort low|medium|high|xhigh|max]
        [--timeout <seconds>] [--schema <file.json>] [--allow-all]
        [--sandbox] [--prompt <text>]

WHAT IT DOES
    1. Finds the engine's CLI on PATH and checks its version against
       the floor where a bug is known (antigravity: 1.1.1, the Windows
       pipe bug of `agy -p`); refuses below it.
    2. Reads the packet folder: it must hold `packet.md`, the whole
       context of the run (the card, the agent's brief, the note's
       shape, the attached notes), composed by the command from the
       forge's own definition (.claude/skills/research/SKILL.md). The
       engine is given THAT folder as its workspace and runs in it,
       under the project's tmp/ so that the run stays traceable; never
       the forge root, whose hooks and instance file an engine must
       not see or execute.
    2a. The lock. The place alone locks nothing: with every tool
       allowed (--allow-all, the only way a headless run reads at all
       in an untrusted folder) the engine reads any path on the disk
       (the probe of 2026-10-24: CLAUDE.md four levels up and a sibling
       packet, read without a question; the sandbox restrains the
       terminal, not the reading), and the engine reads permission
       rules from its user-level settings file alone, which the forge
       never writes. So the script gives the engine a PROFILE OF ITS
       OWN for the run: <run>/.home/.gemini/antigravity-cli/
       settings.json, a copy of the user's settings with `permissions`
       added - allow `read_url(*)`; deny `command(*)`, `write_file(*)`
       and `read_file(<path>)` for every entry of the engine root but
       tmp/ and for <run>/hold/ (where the first engine's notes wait),
       the paths computed from where this script lies - and starts
       the engine with HOME and USERPROFILE pointing at that profile.
       Verified 2026-10-24: a deny rule holds under --allow-all
       ("Matches user-configured deny rule"), the shell is refused,
       the engine's own web tools work, and the login is found. The
       profile stays in the run folder as its record; the user's
       global settings are not touched. Independence of the engines
       is still shown at the synthesis (forge-cite --independence).
       --no-profile runs without it, for a trial of the engine alone.
    3. Records a fingerprint of every file in the packet folder, the
       envelopes and logs of earlier runs left out, runs the engine
       once, non-interactively, stdin closed, with its JSON envelope
       asked for and a time limit set, and compares the folder
       afterwards: a run that changed or added anything in it is
       refused and nothing is filed - read-only is verified, never
       trusted.
    4. Reads the envelope: `status` must say success and `response`
       must be non-empty; exit 0 with an empty answer is a failure.
       The envelope is saved beside the packet as `envelope.json` for
       inspection; the run folder is kept, never cleaned.
    5. Writes the answer to --out as a note: the engine's text with
       `engine`, `model` (as the envelope or the --model word says,
       else "engine default"), `usage`, `run` and `status: immutable`
       put into its front-matter, or a front-matter made when the
       answer has none. The caller files, indexes and remakes the
       ledger (the command's steps).

ENGINES (one row each; a new engine is a row and its pair in COMMANDS)
    antigravity   `agy -p <prompt> --add-dir <packet> --output-format json
                   --print-timeout <s>s --disable-slash-commands
                   [--model] [--effort] [--json-schema] [--sandbox]
                   [--dangerously-skip-permissions]`
                  envelope: status (SUCCESS | ERROR | ...), response,
                  usage, duration_seconds, num_turns; the model is not
                  in the envelope, the --model word is recorded.
    (codex, claude, copilot: rows to add when wanted; the shape every
    one-shot CLI shares is the research note's table.)

FLAGS
    --prompt      the one sentence the engine is started with; default:
                  read packet.md in the workspace and do exactly what it
                  says, the final message the whole note it asks for.
    --allow-all   passes the engine's "approve every tool call" flag;
                  needed when the engine's web tools would otherwise wait
                  for a permission nobody can give in a headless run.
                  What a headless run does without it is untested
                  (brief research, Later).
    --sandbox     passes the engine's sandbox flag where it has one.
    --no-profile  runs the engine under the user's own settings, no
                  per-run profile (step 2a): a trial, never a research.
    --schema      a JSON schema file the engine must shape its final
                  answer by; off by default, the note's shape being in
                  the packet.
    --timeout     seconds for the run; default 1800. Passed to the engine
                  where it has a flag, and enforced here a minute later.

EXIT CODES
    0 the note written; 1 a refusal with the reason on stderr (tool
    missing, version below the floor, packet without packet.md, the
    folder changed by the run, the envelope unreadable or the answer
    empty); the engine's own non-zero exit is reported with its stderr.

EXAMPLES
    python scripts/forge-engine.py antigravity --packet tmp/research/2026-10-24-topic/card-1 --out projects/forge/research/2026-10-24-topic/card-1.antigravity.md
    python scripts/forge-engine.py antigravity --packet tmp/research/2026-10-24-topic/plan-review --out tmp/research/2026-10-24-topic/plan-review/antigravity.md --allow-all
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from forge_tools import fail, say, tool, utf8_console  # noqa: E402

DEFAULT_PROMPT = (
    "Read the file packet.md in your workspace directory and do exactly "
    "what it says. Your final message is the whole note it asks for, in "
    "the shape it gives, and nothing else: no preface, no summary after "
    "it. Write no file."
)

ENGINES = {
    "antigravity": {
        "exe": "agy",
        "floor": (1, 1, 1),
        "version": ["--version"],
        "allow_all": "--dangerously-skip-permissions",
        "sandbox": "--sandbox",
    },
}


def version_of(exe, args):
    out = subprocess.run([exe] + args, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", (out.stdout or "") + (out.stderr or ""))
    return tuple(int(x) for x in m.groups()) if m else None


def fingerprint(folder):
    """{relative path: sha256} of every file under the folder, the
    envelopes and logs of earlier runs left out (they are the caller's
    record beside the packet, not the packet)."""
    fp = {}
    for f in sorted(p for p in folder.rglob("*") if p.is_file()):
        if f.name.startswith(("envelope", "run")) and f.suffix in (".json", ".log"):
            continue
        if ".home" in f.parts:
            continue
        fp[str(f.relative_to(folder))] = hashlib.sha256(f.read_bytes()).hexdigest()
    return fp


def command_antigravity(exe, a, packet):
    cmd = [exe, "-p", a.prompt, "--add-dir", str(packet), "--output-format", "json",
           "--print-timeout", f"{a.timeout}s", "--disable-slash-commands"]
    if a.model:
        cmd += ["--model", a.model]
    if a.effort:
        cmd += ["--effort", a.effort]
    if a.schema:
        cmd += ["--json-schema", str(Path(a.schema).resolve())]
    if a.sandbox:
        cmd.append(ENGINES["antigravity"]["sandbox"])
    if a.allow_all:
        cmd.append(ENGINES["antigravity"]["allow_all"])
    return cmd


def read_envelope_antigravity(text):
    """(ok, response, model, usage, detail) from the agy json envelope."""
    try:
        env = json.loads(text)
    except json.JSONDecodeError:
        # the envelope may follow log lines: take the last JSON object
        m = re.search(r"\{.*\}\s*$", text, re.S)
        if not m:
            return False, "", None, None, "no JSON envelope in the output"
        try:
            env = json.loads(m.group(0))
        except json.JSONDecodeError:
            return False, "", None, None, "the envelope is not valid JSON"
    status = str(env.get("status", "")).upper()
    response = env.get("response") or ""
    if isinstance(env.get("structured_output"), (dict, list)):
        response = response or json.dumps(env["structured_output"], ensure_ascii=False, indent=2)
    usage = env.get("usage")
    if status != "SUCCESS":
        return False, response, env.get("model"), usage, f"status {status or 'missing'}: {env.get('error') or ''}".strip()
    if not str(response).strip():
        denied = ", ".join(d.get("display_name") or d.get("action", "?") for d in env.get("denied_actions") or [])
        hint = f"; denied tool calls: {denied} (a headless run denies what it cannot ask about; --allow-all with --sandbox)" if denied else ""
        return False, response, env.get("model"), usage, f"empty response with status SUCCESS{hint}"
    return True, response, env.get("model"), usage, env


COMMANDS = {"antigravity": (command_antigravity, read_envelope_antigravity)}


def profile_for(packet):
    """The per-run profile (header, step 2a): <run>/.home with the
    engine's settings file carrying the permission rules. Returns the
    environment to start the engine with."""
    engine_root = Path(__file__).resolve().parents[1]
    run = packet.parent
    home = run / ".home"
    cfg_dir = home / ".gemini" / "antigravity-cli"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    user_cfg = Path(os.path.expanduser("~")) / ".gemini" / "antigravity-cli" / "settings.json"
    settings = {}
    if user_cfg.is_file():
        try:
            settings = json.loads(user_cfg.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            settings = {}
    posix = lambda p: str(p).replace("\\", "/")
    deny = [f"read_file({posix(c)})" for c in sorted(engine_root.iterdir()) if c.name != "tmp"]
    deny += [f"read_file({posix(run / 'hold')})", "command(*)", "write_file(*)"]
    settings["permissions"] = {"allow": ["read_url(*)"], "deny": deny}
    (cfg_dir / "settings.json").write_text(json.dumps(settings, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    env = dict(os.environ)
    env["HOME"] = str(home)
    env["USERPROFILE"] = str(home)
    return env, home


def relative_or_absolute(path):
    """The path relative to the working directory where it lies under
    it (as written in a note's `run`), else absolute (Python 3.8 has no
    is_relative_to)."""
    try:
        return str(path.relative_to(Path.cwd())).replace("\\", "/")
    except ValueError:
        return str(path)


def with_front_matter(text, fields):
    """Put the engine's fields into the note's front-matter, or make one."""
    lines = [f"{k}: {v}" for k, v in fields.items()]
    text = text.lstrip("﻿ \n\r\t")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if m:
        body = m.group(1)
        keep = [ln for ln in body.splitlines()
                if not re.match(r"^(engine|model|usage|run|status):", ln)]
        return "---\n" + "\n".join(keep + lines) + "\n---\n" + text[m.end():]
    return "---\n" + "\n".join([f"date: {date.today().isoformat()}"] + lines) + "\n---\n\n" + text


def main():
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], add_help=True)
    ap.add_argument("engine", choices=sorted(ENGINES))
    ap.add_argument("--packet", required=True, help="the packet folder, holding packet.md")
    ap.add_argument("--out", required=True, help="the note to write")
    ap.add_argument("--model", help="a model word the engine understands; recorded, never defaulted by the forge")
    ap.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--timeout", type=int, default=1800, help="seconds; default 1800")
    ap.add_argument("--schema", help="a JSON schema file for the final answer")
    ap.add_argument("--allow-all", action="store_true", help="approve every tool call of the engine")
    ap.add_argument("--sandbox", action="store_true", help="the engine's sandbox, where it has one")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--no-profile", action="store_true", help="no per-run profile: the user's own settings (a trial, never a research)")
    a = ap.parse_args()

    spec = ENGINES[a.engine]
    exe = tool(spec["exe"], f"{spec['exe']} not found on PATH - install the engine's CLI and log in once, outside the forge.")
    v = version_of(exe, spec["version"])
    if v is None:
        fail(f"{spec['exe']} did not report a version.")
    if v < spec["floor"]:
        fail(f"{spec['exe']} {'.'.join(map(str, v))} is below the floor {'.'.join(map(str, spec['floor']))}; update it.")

    packet = Path(a.packet).resolve()
    if not (packet / "packet.md").is_file():
        fail(f"no packet.md in {packet}.")
    out = Path(a.out)
    if out.exists():
        fail(f"{out} exists; a note is immutable, choose another name.")

    # the run in the packet folder itself (header, step 2), under the
    # per-run profile (step 2a)
    env, home = (dict(os.environ), None) if a.no_profile else profile_for(packet)
    before = fingerprint(packet)
    build, read = COMMANDS[a.engine]
    cmd = build(exe, a, packet)
    say(f"{a.engine} {'.'.join(map(str, v))}: running on {packet.name} (timeout {a.timeout}s"
        f"{'; profile ' + relative_or_absolute(home) if home else '; no profile'})", "cyan")
    try:
        proc = subprocess.run(cmd, cwd=str(packet), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", env=env,
                              stdin=subprocess.DEVNULL, timeout=a.timeout + 60)
    except subprocess.TimeoutExpired:
        fail(f"{a.engine} did not finish within {a.timeout + 60}s.")

    after = fingerprint(packet)
    if after != before:
        changed = sorted(set(before) ^ set(after) | {k for k in before if k in after and before[k] != after[k]})
        (packet / "envelope.rejected.json").write_text(proc.stdout or "", encoding="utf-8")
        fail(f"the run changed its workspace ({', '.join(changed)}); nothing filed. Output kept in envelope.rejected.json.")

    ok, response, model, usage, detail = read(proc.stdout or "")
    (packet / "envelope.json").write_text(proc.stdout or "", encoding="utf-8")
    if proc.returncode != 0 and not ok:
        fail(f"{a.engine} exited {proc.returncode}: {(proc.stderr or '').strip()[:800] or detail}")
    if not ok:
        fail(f"{a.engine}: {detail}. Envelope kept in {packet / 'envelope.json'}.")

    fields = {
        "engine": a.engine,
        "model": model or a.model or "engine default",
        "usage": json.dumps(usage, ensure_ascii=False, separators=(",", ":")) if usage else "—",
        "run": relative_or_absolute(packet),
        "status": "immutable",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(with_front_matter(response, fields), encoding="utf-8")
    env = detail if isinstance(detail, dict) else {}
    say(f"note written: {out} ({len(response)} chars; {env.get('num_turns', '?')} turns, "
        f"{env.get('duration_seconds', '?')} s)", "green")


if __name__ == "__main__":
    main()
