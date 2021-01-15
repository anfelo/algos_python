import pytest
from reversestr import reversestr


def test_reversestr():
    assert reversestr('abcd') == 'dcba'


def test_reversestr_spaces():
    assert reversestr('  abcd') == 'dcba  '
