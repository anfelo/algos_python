import pytest
from palindrome import palindrome


def test_is_palindrome_1():
    assert palindrome("aba") == True


def test_is_palindrome_2():
    assert palindrome("pennep") == True


def test_not_palindrome_left_space():
    assert palindrome(" aba") == False


def test_not_palindrome_right_space():
    assert palindrome("aba ") == False


def test_not_palindrome():
    assert palindrome("greetings") == False


def test_is_number_palindrome():
    assert palindrome("1000000001") == True


def test_not_palindrome_case_sensitive():
    assert palindrome("greetings") == False
