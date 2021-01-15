import pytest
from chunk import chunk


def test_chunk_1():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert chunk(ls, 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


def test_chunk_2():
    ls = [1, 2, 3]
    assert chunk(ls, 1) == [[1], [2], [3]]


def test_chunk_3():
    ls = [1, 2, 3, 4, 5]
    assert chunk(ls, 3) == [[1, 2, 3], [4, 5]]


def test_chunk_4():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert chunk(ls, 5) == [[1, 2, 3, 4, 5], [
        6, 7, 8, 9, 10], [11, 12, 13]]
