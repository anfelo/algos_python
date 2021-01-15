from collections import Counter


def maxchar(string):
    """Given a string, return the character that is most
    commonly used in the string. (dict + max)"""
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return max(char_dict, key=lambda k: char_dict[k])


def maxchar_option_1(string):
    """Given a string, return the character that is most
    commonly used in the string. (Counter)"""
    return Counter(string).most_common()[0][0]


def maxchar_option_2(string):
    """Given a string, return the character that is most
    commonly used in the string. (dict + for loop)"""
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    max_char = (None, 0)
    for key, value in char_dict.items():
        if value > max_char[1]:
            max_char = (key, value)

    return max_char[0]
