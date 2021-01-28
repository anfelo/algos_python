def fib(n):
    """Print out the n-th entry in the fibonacci series.
    The fibonacci series is an ordering of numbers where
    each number is the sum of the preceeding two. (for loop O(n))"""
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]


def fib_recursive(n):
    """Print out the n-th entry in the fibonacci series.
    The fibonacci series is an ordering of numbers where
    each number is the sum of the preceeding two. (recursive O(2^n))"""
    # Base Case
    if n < 2:
        return n

    return fast_fib(n - 1) + fast_fib(n - 2)


def memoized(fn):
    """Print out the n-th entry in the fibonacci series.
    The fibonacci series is an ordering of numbers where
    each number is the sum of the preceeding two. (recursive with memoization)"""
    # Base Case
    cache = {}

    def inner(n):
        nonlocal cache
        if n in cache:
            return cache[n]

        result = fn(n)
        cache[n] = result

        return result

    return inner


fast_fib = memoized(fib_recursive)
