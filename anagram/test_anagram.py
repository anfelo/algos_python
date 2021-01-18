import pytest
from anagram import anagram


def test_anagram_1():
    assert anagram('hello', 'llohe') == True


def test_anagram_2():
    assert anagram('Whoa! Hi!', 'Hi! Whoa!') == True


def test_anagram_3():
    assert anagram('One One', 'Two two two') == False


def test_anagram_4():
    assert anagram('One one', 'One one c') == False


def test_anagram_5():
    assert anagram('A tree, a life, a bench',
                   'A tree, a fence, a yard') == False


def test_anagram_6():
    assert anagram('Whoa Hi', 'Hi! Whoa!') == True
