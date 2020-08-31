

def test_recursion():
    print("--------------------------")
    print("-------test_sort-------")
    repeated_values = [random.randint(1, 5) for x in range(10)]
    repeated_sorted = sorted(repeated_values)
    large = [random.randint(1, 1000000000) for x in range(2000)]
    large_sorted = sorted(large)
    # sorted_list = [*range(10000)]
    test_cases = [
        # (None, []),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),  # middle
        ([3, 2, 1], [1, 2, 3]),  # middle    - pivot at array[1] - TPP - constant to array - lower = []
        ([2, 1, 3], [1, 2, 3]),  # beginning - pivot at array[0]
        ([2, 3, 1], [1, 2, 3]),  # beginning
        ([1, 3, 2], [1, 2, 3]),  # end       - pivot at array[2] - TPP - constant to array - higher = []
        ([3, 1, 2], [1, 2, 3]),  # end
        (repeated_values, repeated_sorted),
        ([3, 2, 2, 1], [1, 2, 2, 3]),
        (large, large_sorted),
        # (large_sorted, large_sorted),  # works up to 1000 values - recursive stack size
    ]

    for (args, answer) in test_cases:
        print("---------------------")
        result = sort(args)

        print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(result) + " |")
        if result == answer:
            print("Test case passed!")
        else:
            print("**********************Test with input data:", args, "failed")