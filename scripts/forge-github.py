#!/usr/bin/env python3
"""
forge-github.py - read one issue or discussion of a repository on
GitHub with its comments, or post one reply to it; nothing else on
GitHub.

SYNOPSIS
    python scripts/forge-github.py read <number> [--project <slug | path>]
        [-o <file>]
    python scripts/forge-github.py reply <number> -F <file>
        [--project <slug | path>] [--dry-run]

WHAT IT DOES
    No model, no git. The repository is the one the origin of the
    engine names, or with --project the origin of that project, a slug
    or the path of its directory (forge_repos.project_path). The
    script carries no address and takes none, so it reaches no
    repository but one cloned here. GitHub is asked through gh
    (forge_repos.gh_graphql).

    read finds what carries the number, a discussion or an issue, and
    prints it as Markdown in the shape of a file of the bundle
    `sources/github-issues/`: a heading with the kind, the number and
    the title; Source, Author, Opened, for a discussion its Category,
    and the State at download with the count of the comments and the
    day; the text as its author wrote it, the line breaks alone
    brought to one form; every comment under `## Comment by <login>,
    <day> <time> UTC`, a reply to a comment under `### Reply by ...`
    after it. With -o it writes that to a new file and refuses one
    that exists. Every comment is read, page by page; where a comment
    carries more replies than one request returns, the script refuses
    and writes nothing, never a file that is cut.

    reply posts the text of the file -F names, as it stands, as one
    comment on that issue or discussion, under the login gh carries,
    and prints the address of the comment. A reply cannot be taken
    back in silence: the session posts one on the principal's word
    (CLAUDE.md, Working methods, Step by step). --dry-run prints where
    the text would go, under which login, and the text, and posts
    nothing.

    It edits nothing, closes nothing and deletes nothing: a reading
    and one comment are all it can do.

    It refuses, exit 1 with the reason and nothing written or posted:
    a project that does not exist; an origin that is not on GitHub; a
    number that is neither an issue nor a discussion there, a pull
    request among them; whatever kept gh from answering, in gh's own
    words; a file of -o that exists or whose directory does not; a
    file of -F that does not exist, is not UTF-8 or is empty.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH; gh on PATH and logged in.
    `forge_repos.py` and `forge_tools.py` beside it.

EXAMPLES
    python scripts/forge-github.py read 19
    python scripts/forge-github.py read 19 -o projects/forge/sources/github-issues/discussion-19-overview.md
    python scripts/forge-github.py read 4 --project forge-ui
    python scripts/forge-github.py reply 19 -F tmp/reply-19.md --dry-run
    python scripts/forge-github.py reply 19 -F tmp/reply-19.md
"""

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

# One request per kind: the item under the alias `item`, so that a
# number the kind does not have is told from every other failure by
# the path of GitHub's error.
QUERIES = (
    ("discussion", """
query($owner: String!, $name: String!, $number: Int!, $after: String) {
  viewer { login }
  repository(owner: $owner, name: $name) {
    item: discussion(number: $number) {
      id number title url body createdAt closed stateReason
      author { login }
      category { name }
      comments(first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes { body createdAt author { login }
          replies(first: 100) { totalCount nodes { body createdAt author { login } } } }
      }
    }
  }
}
"""),
    ("issue", """
query($owner: String!, $name: String!, $number: Int!, $after: String) {
  viewer { login }
  repository(owner: $owner, name: $name) {
    item: issue(number: $number) {
      id number title url body createdAt closed stateReason
      author { login }
      comments(first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes { body createdAt author { login } }
      }
    }
  }
}
"""),
)

# The one write: a comment, with the way to its address in the answer.
MUTATIONS = {
    "discussion": ("""
mutation($id: ID!, $body: String!) {
  addDiscussionComment(input: {discussionId: $id, body: $body}) { comment { url } }
}
""", ("addDiscussionComment", "comment", "url")),
    "issue": ("""
mutation($id: ID!, $body: String!) {
  addComment(input: {subjectId: $id, body: $body}) { commentEdge { node { url } } }
}
""", ("addComment", "commentEdge", "node", "url")),
}


class Refusal(Exception):
    pass


def page(query, owner, name, number, after, cwd):
    """One request for the item: (item, the login gh carries). The item
    is None where the repository has nothing of that kind under the
    number; whatever else kept gh from answering is a refusal, in its
    own words."""
    variables = {"owner": owner, "name": name, "number": number}
    if after:
        variables["after"] = after
    answer, said = fr.gh_graphql(query, variables, cwd)
    answer = answer if isinstance(answer, dict) else {}
    errors = answer.get("errors") or []
    data = answer.get("data") or {}
    repo = data.get("repository")
    if not said and not errors and isinstance(repo, dict) and "item" in repo:
        return repo["item"], (data.get("viewer") or {}).get("login") or "?"
    if errors and all(e.get("type") == "NOT_FOUND" and e.get("path") == ["repository", "item"]
                      for e in errors):
        return None, None
    raise Refusal(said or (errors[0].get("message") if errors else None)
                  or "gh answered with something that is not the repository")


def find(owner, name, number, cwd):
    """What carries the number: (kind, item, query, login), the item
    with the first page of its comments. A number is one thing in a
    repository; a discussion is asked for first, then an issue."""
    if number < 1:
        raise Refusal(f"#{number} is no number of an issue or a discussion")
    for kind, query in QUERIES:
        item, login = page(query, owner, name, number, None, cwd)
        if item is not None:
            return kind, item, query, login
    raise Refusal(f"#{number} is neither an issue nor a discussion of {owner}/{name}"
                  " (a pull request is not read)")


def whole(item, query, owner, name, cwd):
    """The item with every comment, read page by page, as a plain list
    under `comments`. Refuses where a comment carries more replies
    than came with it: the output would be cut."""
    number = item["number"]
    comments = item["comments"]
    nodes = list(comments["nodes"])
    while comments["pageInfo"]["hasNextPage"]:
        more, _ = page(query, owner, name, number, comments["pageInfo"]["endCursor"], cwd)
        if more is None:
            raise Refusal(f"#{number} was gone before its comments were read")
        comments = more["comments"]
        nodes += comments["nodes"]
    for c in nodes:
        replies = c.get("replies") or {}
        got = len(replies.get("nodes") or [])
        if replies.get("totalCount", got) > got:
            raise Refusal(f"a comment of #{number} carries {replies['totalCount']} replies and one"
                          f" request returned {got}: nothing is written, the text would be cut")
    item["comments"] = nodes
    return item


def login_of(node):
    """The author's login; `ghost` where the account is gone, as GitHub
    shows it."""
    return ((node or {}).get("author") or {}).get("login") or "ghost"


def text_of(body):
    """A text as its author wrote it, the line breaks brought to one
    form and the empty lines around it dropped."""
    return (body or "").replace("\r\n", "\n").replace("\r", "\n").strip("\n")


def stamp(iso):
    """`2026-11-19T18:58:07Z` as `2026-11-19 18:58 UTC`."""
    return f"{iso[:10]} {iso[11:16]} UTC"


def render(kind, item, today):
    """The item as a file of the bundle `sources/github-issues/`; the
    shape is this function's, read from the files the bundle holds."""
    comments = item["comments"]
    replies = sum(len((c.get("replies") or {}).get("nodes") or []) for c in comments)
    state = "open"
    if item.get("closed"):
        reason = (item.get("stateReason") or "").replace("_", " ").lower()
        state = f"closed as {reason}" if reason and reason != "reopened" else "closed"
    count = f"{len(comments)} comment" + ("" if len(comments) == 1 else "s")
    if replies:
        count += f" and {replies} " + ("reply" if replies == 1 else "replies")
    head = [f"# GitHub {kind} #{item['number']}: {item['title']}", "",
            f"Source: {item['url']}  ",
            f"Author: {login_of(item)}  ",
            f"Opened: {item['createdAt'][:10]}  "]
    if kind == "discussion" and item.get("category"):
        head.append(f"Category: {item['category']['name']}  ")
    head.append(f"State at download: {state}, {count}, downloaded {today}")
    parts = ["\n".join(head), text_of(item.get("body"))]
    for c in comments:
        parts += ["---", f"## Comment by {login_of(c)}, {stamp(c['createdAt'])}", text_of(c.get("body"))]
        for r in (c.get("replies") or {}).get("nodes") or []:
            parts += [f"### Reply by {login_of(r)}, {stamp(r['createdAt'])}", text_of(r.get("body"))]
    return "\n\n".join(p for p in parts if p) + "\n"


def read(args, owner, name, root):
    out = args.output
    if out is not None:
        if out.exists():
            raise Refusal(f"{out} exists: nothing is overwritten")
        if not out.parent.is_dir():
            raise Refusal(f"no directory {out.parent}")
    kind, item, query, _ = find(owner, name, args.number, root)
    text = render(kind, whole(item, query, owner, name, root), datetime.date.today().isoformat())
    if out is None:
        return text.rstrip("\n")
    with open(out, "x", encoding="utf-8", newline="\n") as f:
        f.write(text)
    count = len(item["comments"])
    return (f"written to {out}: {kind} #{item['number']} of {owner}/{name}, "
            f"{count} comment" + ("" if count == 1 else "s"))


def reply(args, owner, name, root):
    path = args.file
    if not path.is_file():
        raise Refusal(f"no file {path}")
    try:
        body = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        raise Refusal(f"{path} is not UTF-8")
    body = body.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not body:
        raise Refusal(f"{path} is empty: nothing to post")
    kind, item, _, login = find(owner, name, args.number, root)
    where = f"{kind} #{item['number']} of {owner}/{name}, \"{item['title']}\", as {login}"
    if args.dry_run:
        return f"would post to {where}:\n\n{body}"
    query, keys = MUTATIONS[kind]
    answer, said = fr.gh_graphql(query, {"id": item["id"], "body": body}, root)
    answer = answer if isinstance(answer, dict) else {}
    errors = answer.get("errors") or []
    node = answer.get("data")
    for key in keys:
        node = node.get(key) if isinstance(node, dict) else None
    if not node:
        # no address of a comment came back: said as not posted, in gh's words
        raise Refusal("the reply was not posted: "
                      + (said or (errors[0].get("message") if errors else None)
                         or "gh answered with no address of a comment"))
    return f"posted to {where}:\n{node}"


def main(argv=None):
    ft.utf8_console()
    p = argparse.ArgumentParser(prog="forge-github.py",
                                description=" ".join(__doc__.strip().split("\n\n")[0].split()))
    sub = p.add_subparsers(dest="what", required=True)
    r = sub.add_parser("read", help="print one issue or discussion with its comments")
    r.add_argument("number", type=int)
    r.add_argument("-o", "--output", type=Path, help="write to this new file instead of printing")
    w = sub.add_parser("reply", help="post the text of a file as one comment")
    w.add_argument("number", type=int)
    w.add_argument("-F", "--file", type=Path, required=True, help="the file whose text is posted")
    w.add_argument("--dry-run", action="store_true",
                   help="print where the text would go and the text, post nothing")
    for s in (r, w):
        s.add_argument("--project",
                       help="the project whose repository is meant, a slug or a path (default: the engine)")
    args = p.parse_args(argv)
    try:
        root = fr.project_path(args.project) if args.project else fr.ENGINE_ROOT
        if not root.is_dir():
            raise Refusal(f"no project {fr.project_label(args.project)}")
        owner, name, origin = fr.github_origin(root)
        if not owner:
            raise Refusal(f"the origin of {root} is not on GitHub ({origin or 'no origin'})")
        said = (read if args.what == "read" else reply)(args, owner, name, root)
    except Refusal as e:
        print(f"forge-github: {e}")
        return 1
    print(said)
    return 0


if __name__ == "__main__":
    sys.exit(main())
