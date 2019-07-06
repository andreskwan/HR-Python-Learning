import random

def test_sort():
    print("--------------------------")
    print("-------test_prime_factors-------")
    repeated_values = [random.randint(1, 5) for x in range(10)]
    repeated_sorted = sorted(repeated_values)
    large = [random.randint(1, 1000000000) for x in range(1000)]
    large_sorted = sorted(large)
    # sorted_list = [*range(10000)]
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),  # middle
        ([3, 2, 1], [1, 2, 3]),  # middle    - pivot at array[1]
        ([2, 1, 3], [1, 2, 3]),  # beginning - pivot at array[0]
        ([2, 3, 1], [1, 2, 3]),  # beginning
        ([1, 3, 2], [1, 2, 3]),  # end       - pivot at array[2]
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
            print("input: " + str(unmodified) + " | expected answer: " + str(answer) + " | result: " + str(
                result))
        else:
            print("result: " + str(result) + " | expected answer: " + str(answer))
        if result == answer:
            print("Test case passed!")
        else:
            print("Test with input data:", unmodified, "failed")


# TODO - fix sort sorted array recursion problem.
def sort(array):
    sorted_list = []
    lower = []
    higher = []
    pivot = None

    if len(array) <= 1:
        return array
    if len(array) > 1:
        pivot = array[0]
        for index, value in enumerate(array):
            if value == pivot and 0 != index:
                higher.append(value)
            if value < pivot:
                lower.append(value)
            elif value > pivot:
                higher.append(value)

    sorted_list.extend(sort(lower))
    sorted_list.append(pivot)
    sorted_list.extend(sort(higher))
    return sorted_list

test_sort()