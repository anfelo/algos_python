import pytest
from capitalize import capitalize, capitalize_option_1


def test_capitalize_1():
    assert capitalize_option_1(
        'hi there, how is it going?') == 'Hi There, How Is It Going?'


def test_capitalize_2():
    assert capitalize_option_1(
        'i love breakfast at bill miller bbq') == 'I Love Breakfast At Bill Miller Bbq'
