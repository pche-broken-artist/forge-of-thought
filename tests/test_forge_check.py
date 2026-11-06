"""
The text cores of scripts/forge_check.py: versions, IDs and their
ranges, the keys of a front-matter, the line of a match. Text in,
values out; no project read.
"""
import forge_check as fc


def test_version_tuple_reads_major_and_minor():
    assert fc.version_tuple("0.9") == (0, 9)
    assert fc.version_tuple("6.12") == (6, 12)
    assert fc.version_tuple("1.0.1") is None
    assert fc.version_tuple("draft") is None
    assert fc.version_tuple(None) is None


def test_ids_in_finds_every_id_once():
    assert fc.ids_in("POS.0010 and POS.0010, THR.10000; dec.0010") == {"POS.0010", "THR.10000"}


def test_expand_ranges_in_tens():
    assert fc.expand_ranges("POS.0010 to POS.0030") == {"POS.0010", "POS.0020", "POS.0030"}
    assert fc.expand_ranges("FND.3030-FND.3050") == {"FND.3030", "FND.3040", "FND.3050"}
    assert fc.expand_ranges("REQ.0100 to 0120") == {"REQ.0100", "REQ.0110", "REQ.0120"}
    assert fc.expand_ranges("POS.9990 to POS.10010") == {"POS.9990", "POS.10000", "POS.10010"}
    assert fc.expand_ranges("POS.0010, REJ.0020") == {"POS.0010", "REJ.0020"}


def test_front_keys_in_order():
    assert fc.front_keys(["project: forge", "kind: thought  # a comment", "  - item", "version: 0.1"]) == ["project", "kind", "version"]
    assert fc.front_keys(None) == []


def test_line_of_first_match():
    text = "one\ntwo\nthree two\n"
    assert fc.line_of(text, r"two") == 2
    assert fc.line_of(text, r"^three", fc.re.M) == 3
    assert fc.line_of(text, r"four") == 0


def test_norm_collapses_whitespace():
    assert fc.norm("  a \n  b\t c ") == "a b c"
