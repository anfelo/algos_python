import pytest
from matrix import matrix


def test_matrix_1():
    assert matrix(2) == [[1, 2], [4, 3]]


def test_matrix_2():
    assert matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


def test_matrix_3():
    assert matrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5],
                         [11, 16, 15, 6], [10, 9, 8, 7]]
