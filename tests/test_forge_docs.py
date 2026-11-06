"""
The reading cores of scripts/forge_docs.py: the front-matter of a
document, the values and lists in it, the tail of a history record
and the records of a history companion. Text in, values out; no git,
no tool.
"""
import forge_docs as fd

FRONT = """---
project: forge
version: 0.9    # a comment after the value
status: "draft"
languages:
  - en
  - cs
---
# Body

Text.
"""


def test_split_front_divides_header_and_body():
    front, body = fd.split_front(FRONT)
    assert front[0] == "project: forge"
    assert front[-1] == "  - cs"
    assert body.startswith("# Body")


def test_split_front_without_header_returns_text_whole():
    assert fd.split_front("# No header\n") == (None, "# No header\n")
    assert fd.split_front("---\nnever closed\n") == (None, "---\nnever closed\n")


def test_front_value_strips_comment_and_quotes():
    front, _ = fd.split_front(FRONT)
    assert fd.front_value(front, "version") == "0.9"
    assert fd.front_value(front, "status") == "draft"
    assert fd.front_value(front, "absent") is None
    assert fd.front_value(None, "project") is None


def test_front_list_reads_block_and_inline():
    front, _ = fd.split_front(FRONT)
    assert fd.front_list(front, "languages") == ["en", "cs"]
    assert fd.front_list(front, "project") == ["forge"]
    assert fd.front_list(front, "absent") == []


def test_split_tail_reason_action_was():
    assert fd.split_tail("the reason") == ("the reason", None, None)
    assert fd.split_tail("the reason | Action: do this | Was: old text") == ("the reason", "do this", "old text")
    assert fd.split_tail("the reason | Was: old text") == ("the reason", None, "old text")
    assert fd.split_tail("Was: old text") == ("", None, "old text")
    assert fd.split_tail("Action: do this") == ("", "do this", None)
    assert fd.split_tail(None) == ("", None, None)


HISTORY = """---
project: forge
document: 10-intent.md
---

# History - 10-intent.md

- 2026-10-01 | 0.1 | PCHe | 10-intent.md | created
- 2026-10-02 | 0.2 | PCHe | POS.0010, POS.0020 | changed | sharpened | Was: the old wording
- 2026-10-03 | 0.2 | PCHe | FND.0010 | closed | fixed in 0.2
- 2026-10-04 | not a record | but shaped like one
"""


def test_records_of_a_history(tmp_path):
    path = tmp_path / "10-intent.history.md"
    path.write_text(HISTORY, encoding="utf-8")
    fd.problems.clear()
    out = fd.records(path)
    assert [r["kind"] for r in out] == ["created", "changed", "closed"]
    assert out[1]["subject"] == "POS.0010, POS.0020"
    assert out[1]["reason"] == "sharpened"
    assert out[1]["was"] == "the old wording"
    assert out[1]["line"] == 9
    assert fd.subject_ids(out[1]["subject"]) == ["POS.0010", "POS.0020"]
    assert out[2]["action"] is None
    assert [p[1:] for p in fd.problems] == [(11, "record not in the shape of templates/history.md")]


def test_records_of_a_missing_history_are_none(tmp_path):
    assert fd.records(tmp_path / "absent.history.md") == []


def test_id_regex_takes_four_or_five_digits():
    assert fd.ID_RE.findall("POS.0010 THR.10000 pos.0010 POS.001 X.POS.0020") == ["POS.0010", "THR.10000", "POS.0020"]
