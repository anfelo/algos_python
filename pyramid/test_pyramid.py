import pytest
from pyramid import pyramid


def test_pyramid_1():
    assert pyramid(1) == ['#']


def test_pyramid_2():
    assert pyramid(2) == [' # ', '###']


def test_pyramid_3():
    assert pyramid(3) == ['  #  ', ' ### ', '#####']


def test_pyramid_4():
    assert pyramid(4) == ['   #   ', '  ###  ', ' ##### ', '#######']
