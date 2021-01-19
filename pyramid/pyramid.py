from math import floor


def pyramid(n):
    """Write a function that accepts a positive number N.
    The function should console log a pyramid shape
    with N levels using the # character.  Make sure the
    pyramid has spaces on both the left *and* right hand sides"""
    step_list = []
    for i in range(1, n + 1):
        step = '#' * i
        spaces = ' ' * (n - i)
        step_str = step + spaces
        step_str_rev = step_str[::-1]
        step_list.append(step_str_rev + step_str[1:])
    return step_list


def pyramid_option_1(n, row=0):
    """Write a function that accepts a positive number N.
    The function should console log a pyramid shape
    with N levels using the # character. Make sure the
    pyramid has spaces on both the left *and* right hand sides (recursive)"""
    if n == row:
        return

    step = '#' * (row + 1)
    spaces = ' ' * (n - (row + 1))
    step_str = step + spaces
    step_str_rev = step_str[::-1]
    print(step_str_rev + step_str[1:])
    pyramid_option_1(n, row + 1)


def pyramid_option_2(n, row=0, level=''):
    """Write a function that accepts a positive number N.
    The function should console log a pyramid shape
    with N levels using the # character. Make sure the
    pyramid has spaces on both the left *and* right hand sides (recursive 2)"""
    if n == row:
        return

    if len(level) == (2 * n - 1):
        print(level)
        pyramid_option_2(n, row + 1)
        return

    mid = floor((2 * n - 1) / 2)
    add = ''
    if (mid - row <= len(level)) & (mid + row >= len(level)):
        add = '#'
    else:
        add = ' '
    pyramid_option_2(n, row, level + add)


pyramid_option_2(4)
