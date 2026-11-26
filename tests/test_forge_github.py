"""
forge-github with GitHub stood in for: the one request the script
makes through gh (forge_repos.gh_graphql) is replaced by a function of
the test, so no test touches the network or needs gh. What is tested
is what the header promises: the shape of what is read, every page of
the comments, a refusal instead of a cut text, a file never
overwritten, and one comment posted, or none on a dry run. The
refusal on an origin that is not GitHub is run as the forge runs the
script, on the fixture's throwaway repository.
"""
import datetime

import pytest

from conftest import git

TODAY = datetime.date.today().isoformat()
ACME = ("acme", "widgets", "https://github.com/acme/widgets.git")


def found(item):
    return {"data": {"viewer": {"login": "owner"}, "repository": {"item": item}}}, None


def not_found(kind):
    said = f"gh: Could not resolve to {kind} with the number of 7."
    return ({"data": {"viewer": {"login": "owner"}, "repository": {"item": None}},
             "errors": [{"type": "NOT_FOUND", "path": ["repository", "item"], "message": said[4:]}]},
            said)


def comment(body, login="owner", at="2026-11-26T09:05:00Z", replies=None, total=None):
    node = {"body": body, "createdAt": at, "author": {"login": login} if login else None}
    if replies is not None:
        node["replies"] = {"totalCount": len(replies) if total is None else total, "nodes": replies}
    return node


def discussion(comments, more=None, **over):
    item = {"id": "D_19", "number": 19, "title": "A way to see the whole list",
            "url": "https://github.com/acme/widgets/discussions/19",
            "body": "First line.\r\n\r\nSecond line.\r\n", "createdAt": "2026-11-25T14:15:22Z",
            "closed": False, "stateReason": None, "author": {"login": "visitor"},
            "category": {"name": "Ideas"},
            "comments": {"pageInfo": {"hasNextPage": bool(more), "endCursor": more}, "nodes": comments}}
    item.update(over)
    return item


def issue(comments):
    return {"id": "I_14", "number": 14, "title": "The origin cannot be reached",
            "url": "https://github.com/acme/widgets/issues/14", "body": "It fails.",
            "createdAt": "2026-11-16T08:00:00Z", "closed": True, "stateReason": "NOT_PLANNED",
            "author": {"login": "visitor"},
            "comments": {"pageInfo": {"hasNextPage": False, "endCursor": None}, "nodes": comments}}


class GitHub:
    """What stands in for gh: `answers` maps a word of the request,
    `discussion`, `issue` or `mutation`, to the answer, or to a list of
    answers given one per call; every call is kept."""

    def __init__(self, **answers):
        self.answers = answers
        self.calls = []

    def __call__(self, query, variables, cwd):
        if "mutation" in query:
            word = "mutation"
        else:
            word = "discussion" if "item: discussion(" in query else "issue"
        self.calls.append((word, dict(variables)))
        answer = self.answers[word]
        return answer.pop(0) if isinstance(answer, list) else answer

    def words(self):
        return [word for word, _ in self.calls]


@pytest.fixture
def script(load_script, monkeypatch):
    """The script as a module, its repository said to be acme/widgets;
    `script.github(...)` puts a GitHub of the test in place of gh."""
    module = load_script("forge-github")
    monkeypatch.setattr(module.fr, "github_origin", lambda path: ACME)

    def github(**answers):
        fake = GitHub(**answers)
        monkeypatch.setattr(module.fr, "gh_graphql", fake)
        return fake

    module.github = github
    return module


def test_a_discussion_is_read_in_the_shape_of_the_bundle(script, capsys):
    script.github(discussion=found(discussion(
        [comment("An answer.", replies=[comment("Thanks.", login=None, at="2026-11-26T10:00:59Z")])],
        closed=True, stateReason="RESOLVED")))
    assert script.main(["read", "19"]) == 0
    two = "  "                                    # the Markdown line break of the bundle's header
    assert capsys.readouterr().out == "\n".join([
        "# GitHub discussion #19: A way to see the whole list",
        "",
        "Source: https://github.com/acme/widgets/discussions/19" + two,
        "Author: visitor" + two,
        "Opened: 2026-11-25" + two,
        "Category: Ideas" + two,
        f"State at download: closed as resolved, 1 comment and 1 reply, downloaded {TODAY}",
        "",
        "First line.",
        "",
        "Second line.",
        "",
        "---",
        "",
        "## Comment by owner, 2026-11-26 09:05 UTC",
        "",
        "An answer.",
        "",
        "### Reply by ghost, 2026-11-26 10:00 UTC",
        "",
        "Thanks.",
        "",
    ])


def test_an_issue_is_found_after_the_discussion_and_has_no_category(script, capsys):
    gh = script.github(discussion=not_found("a Discussion"), issue=found(issue([])))
    assert script.main(["read", "14"]) == 0
    out = capsys.readouterr().out
    assert gh.words() == ["discussion", "issue"]
    assert out.startswith("# GitHub issue #14: The origin cannot be reached\n")
    assert "Category:" not in out
    assert f"State at download: closed as not planned, 0 comments, downloaded {TODAY}" in out


def test_every_page_of_the_comments_is_read(script, capsys):
    gh = script.github(discussion=[found(discussion([comment("one")], more="cursor-1")),
                                   found(discussion([comment("two")]))])
    assert script.main(["read", "19"]) == 0
    out = capsys.readouterr().out
    assert [v.get("after") for _, v in gh.calls] == [None, "cursor-1"]
    assert out.index("\none\n") < out.index("\ntwo\n")
    assert "2 comments, downloaded" in out


def test_replies_that_would_be_cut_refuse_and_nothing_is_written(script, tmp_path, capsys):
    script.github(discussion=found(discussion([comment("one", replies=[comment("a reply")], total=2)])))
    target = tmp_path / "discussion-19.md"
    assert script.main(["read", "19", "-o", str(target)]) == 1
    assert "would be cut" in capsys.readouterr().out
    assert not target.exists()


def test_read_writes_a_new_file_and_never_over_one_that_exists(script, tmp_path, capsys):
    gh = script.github(discussion=found(discussion([])))
    target = tmp_path / "discussion-19.md"
    assert script.main(["read", "19", "-o", str(target)]) == 0
    written = target.read_bytes()
    assert written.startswith(b"# GitHub discussion #19: ") and b"\r" not in written
    assert script.main(["read", "19", "-o", str(target)]) == 1
    assert "nothing is overwritten" in capsys.readouterr().out
    assert target.read_bytes() == written
    assert len(gh.calls) == 1                     # the second run asked GitHub nothing


def test_a_number_that_is_neither_is_refused(script, capsys):
    script.github(discussion=not_found("a Discussion"), issue=not_found("an Issue"))
    assert script.main(["read", "7"]) == 1
    assert "neither an issue nor a discussion of acme/widgets" in capsys.readouterr().out


def test_what_gh_could_not_do_is_said_in_its_words(script, capsys):
    script.github(discussion=(None, "gh: To get started with GitHub CLI, please run:  gh auth login"))
    assert script.main(["read", "19"]) == 1
    assert "gh auth login" in capsys.readouterr().out


def test_a_dry_run_posts_nothing(script, tmp_path, capsys):
    gh = script.github(discussion=found(discussion([])))
    text = tmp_path / "reply.md"
    text.write_text("Thank you.\n\nWe opened a thread.\n", encoding="utf-8")
    assert script.main(["reply", "19", "-F", str(text), "--dry-run"]) == 0
    out = capsys.readouterr().out
    assert gh.words() == ["discussion"]           # looked up, never posted
    assert 'would post to discussion #19 of acme/widgets, "A way to see the whole list", as owner' in out
    assert out.rstrip().endswith("Thank you.\n\nWe opened a thread.")


@pytest.mark.parametrize("kind", ["discussion", "issue"])
def test_a_reply_is_one_comment_with_the_text_of_the_file(script, tmp_path, capsys, kind):
    url = "https://github.com/acme/widgets/x#comment-1"
    if kind == "discussion":
        posted = {"data": {"addDiscussionComment": {"comment": {"url": url}}}}
        gh = script.github(discussion=found(discussion([])), mutation=(posted, None))
        number, node = "19", "D_19"
    else:
        posted = {"data": {"addComment": {"commentEdge": {"node": {"url": url}}}}}
        gh = script.github(discussion=not_found("a Discussion"), issue=found(issue([])),
                           mutation=(posted, None))
        number, node = "14", "I_14"
    text = tmp_path / "reply.md"
    text.write_bytes("﻿Thank you.\r\nIt is fixed.\r\n".encode("utf-8"))
    assert script.main(["reply", number, "-F", str(text)]) == 0
    assert gh.words().count("mutation") == 1
    assert gh.calls[-1] == ("mutation", {"id": node, "body": "Thank you.\nIt is fixed."})
    assert capsys.readouterr().out.rstrip().endswith(url)


def test_a_reply_that_did_not_land_is_said_as_not_posted(script, tmp_path, capsys):
    script.github(discussion=found(discussion([])), mutation=(None, "gh: HTTP 502"))
    text = tmp_path / "reply.md"
    text.write_text("Thank you.", encoding="utf-8")
    assert script.main(["reply", "19", "-F", str(text)]) == 1
    assert "the reply was not posted: gh: HTTP 502" in capsys.readouterr().out


def test_an_empty_or_a_missing_file_is_refused_before_github_is_asked(script, tmp_path, capsys):
    gh = script.github()
    empty = tmp_path / "empty.md"
    empty.write_text(" \n\n", encoding="utf-8")
    assert script.main(["reply", "19", "-F", str(empty)]) == 1
    assert script.main(["reply", "19", "-F", str(tmp_path / "none.md")]) == 1
    out = capsys.readouterr().out
    assert "is empty: nothing to post" in out and "no file" in out
    assert gh.calls == []


def test_an_origin_that_is_not_github_is_refused(repo, git_env, run_script):
    # The fixture's origin is a local bare repository: refused before gh
    # is looked for, so the same on a machine with gh and without one.
    r = run_script("forge-github", "read", "1", "--project", repo, env=git_env)
    assert r.returncode == 1
    assert "is not on GitHub" in r.stdout


def test_the_address_of_github_is_read_from_the_origin(repo, git_env, monkeypatch):
    import forge_repos as fr
    for name, value in git_env.items():
        monkeypatch.setenv(name, value)
    assert fr.github_origin(repo)[:2] == (None, None)
    for address in ("https://github.com/acme/widgets.git", "git@github.com:acme/widgets.git",
                    "https://github.com/acme/widgets"):
        git(["remote", "set-url", "origin", address], repo, git_env)
        assert fr.github_origin(repo) == ("acme", "widgets", address)
