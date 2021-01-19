def steps(n):
    """Write a function that accepts a positive number N.
    The function should console log a step shape
    with N levels using the # character.  Make sure the
    step has spaces on the right hand side! (str repeat)"""
    step_list = []
    for i in range(1, n + 1):
        step = '#' * i
        spaces = ' ' * (n - i)
        step_list.append(step + spaces)
    return step_list


def steps_option_1(n):
    """Write a function that accepts a positive number N.
    The function should console log a step shape
    with N levels using the # character.  Make sure the
    step has spaces on the right hand side! (List comprenhension)"""
    return [(('#' * i) + (' ' * (n - i))) for i in range(1, n + 1)]


def steps_option_2(n):
    """Write a function that accepts a positive number N.
    The function should console log a step shape
    with N levels using the # character.  Make sure the
    step has spaces on the right hand side! (for loop)"""
    step_list = []
    for row in range(1, n + 1):
        step_str = ''
        for col in range(1, n + 1):
            if col - row <= 0:
                step_str += '#'
            else:
                step_str += ' '
        step_list.append(step_str)
    return step_list


def steps_option_3(n, row=0):
    """Write a function that accepts a positive number N.
    The function should console log a step shape
    with N levels using the # character.  Make sure the
    step has spaces on the right hand side! (recursive)"""
    if n == row:  # Base case
        return

    print(('#' * (row + 1)) + ('*' * (n - row - 1)))
    steps_option_3(n, row + 1)  # Recursive call changing inputs
