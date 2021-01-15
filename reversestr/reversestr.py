import sys
from functools import reduce


def reversestr(string):
    """Given a string returns a string with the reversed order of characters (slices)"""
    return string[::-1]


def reversestr_optional_1(string):
    """Given a string returns a string with the reversed order of characters (for loop)"""
    chars = [char for char in string]
    reversed_str = ''
    for char in chars:
        reversed_str = char + reversed_str
    return reversed_str


def reversestr_optional_2(string):
    """Given a string returns a string with the reversed order of characters (join + reversed)"""
    return "".join(list(reversed(string)))


def reversestr_optional_3(string):
    """Given a string returns a string with the reversed order of characters (functional)"""
    return reduce(lambda acc, curr: curr + acc, string, '')
