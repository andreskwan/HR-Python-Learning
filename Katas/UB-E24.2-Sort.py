import random


def test_sort():
    print("--------------------------")
    print("-------test_prime_factors-------")
    repeated_values = [random.randint(1, 5) for x in range(10)]
    repeated_sorted = sorted(repeated_values)
    large = [random.randint(1, 1000000000) for x in range(2000)]
    large_sorted = sorted(large)
    # sorted_list = [*range(10000)]
    test_cases = [
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
        (large_sorted, large_sorted),  # works up to 1000 values - recursive stack size
    ]

    for (args, answer) in test_cases:
        print("---------------------")
        unmodified = args[:]
        result = sort(args)

        if result is not None and answer is not None:
            print("input:    " + str(unmodified) + "\nexpected: " + str(answer) + "\nresult:   " + str(
                result))
        else:
            print("result: " + str(result) + "\nexpected: " + str(answer))
        if result == answer:
            print("Test case passed!")
        else:
            print("Test with input data:", unmodified, "failed")


# TODO - fix sort sorted array recursion problem.
def sort(array):
    sorted_list = []
    pivot = None
    lower = []
    higher = []
    size = len(array)
    if size <= 1:  # <= 1 to have the base case for the recursive version.
        return array
    if size > 1:
        pivot = array[0]
        for index, value in enumerate(array):
            if index != 0 and value == pivot:
                higher.append(value)
            if value > pivot:
                higher.append(value)
            elif value < pivot:
                lower.append(value)

    sorted_list.extend(sort(lower))
    sorted_list.append(pivot)
    sorted_list.extend(sort(higher))
    return sorted_list


test_sort()
