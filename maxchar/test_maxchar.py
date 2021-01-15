import pytest
from maxchar import maxchar


def test_maxchar_1():
    assert maxchar('abcdefghijklmnaaaaa') == 'a'


def test_maxchar_2():
    assert maxchar('ab1c1d1e1f1g1') == '1'
