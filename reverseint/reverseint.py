def reverseint(num):
    """Given an integer, return an integer that is the reverse
    ordering of numbers."""
    sign = '-' if num < 0 else ''
    return int(sign + str(abs(num))[::-1])
