def capitalize(string):
    """Write a function that accepts a string. The function should
    capitalize the first letter of each word in the string then
    return the capitalized string."""
    words = string.split(sep=" ")
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:]
    return " ".join(words)


def capitalize_option_1(string):
    return string.title()
