import pytest
from steps import steps


def test_steps_1():
    assert steps(1) == ['#']


def test_steps_2():
    assert steps(2) == ['# ', '##']


def test_steps_3():
    assert steps(3) == ['#  ', '## ', '###']
