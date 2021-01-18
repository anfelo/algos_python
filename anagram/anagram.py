import re


def anagram(stringA, stringB):
    """
    Check to see if two provided strings are anagrams of eachother.
    One string is an anagram of another if it uses the same characters
    in the same quantity. Only consider characters, not spaces
    or punctuation.  Consider capital letters to be the same as lower case
    """
    regex = r"[\W]"
    strA = re.sub(regex, "", stringA).lower()
    strB = re.sub(regex, "", stringB).lower()

    if len(strA) != len(strB):
        return False

    char_dictA = {}
    char_dictB = {}
    for index in range(len(strA)):
        if strA[index] in char_dictA:
            char_dictA[strA[index]] += 1
        else:
            char_dictA[strA[index]] = 1

        if strB[index] in char_dictB:
            char_dictB[strB[index]] += 1
        else:
            char_dictB[strB[index]] = 1

    for key, value in char_dictA.items():
        if char_dictA[key] != char_dictB[key]:
            return False

    return True


def anagram_option_1(stringA, stringB):
    regex = r"[\W]"
    strA = sorted(re.sub(regex, "", stringA).lower())
    strB = sorted(re.sub(regex, "", stringB).lower())

    return strA == strB
