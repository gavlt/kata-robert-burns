import io
import pytest 

import ttr


def test_parse_file_simple():
    file = io.StringIO("Hello world here are some words")
    words = ttr.parse_file(file)

    assert words == ["hello", "world", "here", "are", "some", "words"]


def test_parse_file_multiline():
    file = io.StringIO("Hello world \n And some more words\n And new lines")
    words = ttr.parse_file(file)

    assert words == ["hello", "world", "and", "some", "more", "words", "and", "new", "lines"]


def test_parse_file_punctuation():
    file = io.StringIO("Hello world,\nand some more words. And here's some more!")
    words = ttr.parse_file(file)

    assert words == ["hello", "world", "and", "some", "more", "words", "and", "here's", "some", "more"]


def test_parse_file_empty():
    file = io.StringIO("")
    words = ttr.parse_file(file)

    assert words == []
    assert isinstance(words, list)

def test_parse_file_newline_only():
    file = io.StringIO("\n")
    words = ttr.parse_file(file)

    assert words == []


@pytest.mark.parametrize("words, expected", (
    (["hello", "world", "here", "are", "some", "words"], 1.0),
    (["badger", "badger", "badger", "badger", "badger"], 0.2),
    (["badger", "badger", "badger", "badger", "mushroom", "mushroom"], 2/6),
))
def test_calculate_ttr(words, expected):
    assert ttr.calculate_ttr(words) == expected

def test_calculate_ttr_empty_wordlist():
    with pytest.raises(ttr.EmptyFileError):
        ttr.calculate_ttr([])
