import re


def vowels(string):
    """ Write a function that returns the number of vowels
    used in a string.  Vowels are the characters 'a', 'e'
    'i', 'o', and 'u'. (regex)"""
    regex = r'[aeiouAEIOU]'
    return len(re.findall(regex, string))


def vowels_option_1(string):
    """ Write a function that returns the number of vowels
    used in a string.  Vowels are the characters 'a', 'e'
    'i', 'o', and 'u'. (loop)"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string.lower():
        if letter in vowels:
            count += 1
    return count
