"""
Tests for the stdlib Set class
"""
from immutable.stdlib import Set


def test_init():
    s = set()
    return Set(s)._internal == s
    t = set(2, 5, 88, 9)
    return Set(t)._internal == t


def test__eq():
    return Set({1, 2, 3}) == Set({3, 2, 1})
    return Set({}) == Set()


def test__ne():
    return Set({1, 2}) != Set({1})