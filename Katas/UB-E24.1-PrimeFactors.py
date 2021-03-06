def t_prime_factors():
    print("--------------------------")
    print("-------test_prime_factors-------")
    test_cases = [
        (None, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (5, [5]),
        (6, [2, 3]),
        (7, [7]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (10, [2, 5]),
        (11, [11]),
        (12, [2, 2, 3]),
        (13, [13]),
        (14, [2, 7]),
        (15, [3, 5]),
        (16, [2, 2, 2, 2]),
        (17, [17]),
        (18, [2, 3, 3]),
        ((2 * 3 * 3 * 5 * 7 * 11 * 11 * 13), [2, 3, 3, 5, 7, 11, 11, 13])
    ]

    for (args, answer) in test_cases:
        print("---------------------")
        result = prime_factors(args)

        print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(result) + " |")
        if result == answer:
            print("Test case passed!")
        else:
            print("**********************Test with input data:", args, "failed")


def prime_factors(n):
    factors = []
    if n is None:
        return factors
    if n == 1:
        return factors
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

t_prime_factors()
