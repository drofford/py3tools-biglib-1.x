import logging
import re
import sys

from biglib.utils.list_utils import ListUtils


def _fhelper(initial, expected, length):
    actual = ListUtils.flatten(initial)
    assert actual == expected
    assert len(actual) == length
    assert id(actual) != id(initial)


def test_flatten_empty():
    _fhelper([], [], 0)


def test_flatten_one_element():
    _fhelper([42], [42], 1)


def test_flatten_one_deep():
    _fhelper([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5)


def test_flatten_two_deep():
    _fhelper([1, [2, 3], 4, 5], [1, 2, 3, 4, 5], 5)


def test_flatten_two_deep_twice():
    _fhelper([1, [2, 3], [4], 5], [1, 2, 3, 4, 5], 5)


def test_flatten_muliple_deep():
    _fhelper(
        [1, [2, [3]], [[4], 5], [6, [7, [8, [9]]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9
    )


def _jhelper(initial, expected, length, *, add_and=False, oxford=False, quoting=False):
    actual = ListUtils.join(initial, add_and=add_and, oxford=oxford, quoting=quoting)
    assert isinstance(actual, str)
    assert len(actual) == length


def test_join_none():
    _jhelper(None, "", 0)


def test_join_empty():
    _jhelper([], "", 0)


def test_join_one():
    _jhelper([1], "1", 1)


def test_join_two():
    _jhelper([1, 2], "1,2", 3)


def test_join_three():
    _jhelper([1, 2, 56], "1,2,56", 6)


def test_join_add_and_one():
    _jhelper([1], "1", 1, add_and=True)


def test_join_and_add_two():
    _jhelper([1, 2], "1 and 2", 7, add_and=True)


def test_join_and_add_three():
    _jhelper([1, 2, 56], "1,2 and 56", 10, add_and=True)


def test_join_oxford_add_and_one():
    _jhelper([1], "1", 1, add_and=True, oxford=True)


def test_join_oxford_and_add_two():
    _jhelper([1, 2], "1 and 2", 7, add_and=True, oxford=True)


def test_join_oxford_and_add_three():
    _jhelper([1, 2, 56], "1,2, and 56", 11, add_and=True, oxford=True)


def test_quoted_none():
    _jhelper(None, "", 0, quoting=True)


def test_quoted_empty():
    _jhelper([], "", 0, quoting=True)


def test_join_quoted_one():
    _jhelper([1], '"1"', 3, quoting=True)


def test_join_quoted_two():
    _jhelper([1, 2], '"1","2"', 7, quoting=True)


def test_join_quoted_three():
    _jhelper([1, 2, 56], '"1","2","56"', 12, quoting=True)
