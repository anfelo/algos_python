import pytest
from vowels import vowels


def test_vowels_1():
    assert vowels('aeiou') == 5


def test_vowels_2():
    assert vowels('AEIOU') == 5


def test_vowels_3():
    assert vowels('abcdefghijklmnopqrstuvwxyz') == 5


def test_vowels_4():
    assert vowels('bcdfghjkl') == 0
