import pytest
from reverseint import reverseint


def test_reverseint_cero():
    assert reverseint(0) == 0


def test_reverseint_positive_1():
    assert reverseint(5) == 5


def test_reverseint_positive_2():
    assert reverseint(15) == 51


def test_reverseint_positive_3():
    assert reverseint(90) == 9


def test_reverseint_positive_4():
    assert reverseint(2359) == 9532


def test_reverseint_negative_1():
    assert reverseint(-5) == -5


def test_reverseint_negative_2():
    assert reverseint(-15) == -51


def test_reverseint_negative_3():
    assert reverseint(-90) == -9


def test_reverseint_negative_4():
    assert reverseint(-2359) == -9532
