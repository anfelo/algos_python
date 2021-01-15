def fizzbuzz(num):
    """Returns a list containing the fizzbuzz sequence.
    But for multiples of three print “fizz” instead of
    the number and for the multiples of five print “buzz”.
    For numbers which are multiples of both three and five
    print “fizzbuzz”."""
    fizzbuzz_list = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:  # i % 15 (MCM)
            fizzbuzz_list.append('fizzbuzz')
        elif i % 3 == 0:
            fizzbuzz_list.append('fizz')
        elif i % 5 == 0:
            fizzbuzz_list.append('buzz')
        else:
            fizzbuzz_list.append(i)

    return fizzbuzz_list
