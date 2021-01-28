import pytest
from fib import fib, fib_recursive, fast_fib


def test_fib_1():
    assert fast_fib(1) == 1


def test_fib_2():
    assert fast_fib(2) == 1


def test_fib_3():
    assert fast_fib(3) == 2


def test_fib_4():
    assert fast_fib(4) == 3


def test_fib_5():
    assert fast_fib(39) == 63245986
