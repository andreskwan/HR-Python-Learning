import random


def sort(array):
    sorted_list = []
    lower = []
    higher = []
    pivot = None

    if len(array) <= 1:
        return array
    elif len(array) > 1:
        pivot = array[0]
        for index, value in enumerate(array):
            if pivot == value and 0 != index:
                lower.append(value)
            if pivot > value:
                lower.append(value)
            if pivot < value:
                higher.append(value)

    sorted_list.extend(sort(lower))
    if pivot is not None: sorted_list.append(pivot)
    sorted_list.extend(sort(higher))
    return sorted_list


def test_sort():
    print("--------------------------")
    print("-------test_prime_factors-------")
    unsorted_list = [random.randint(1, 10) for x in range(100)]
    sorted_list = sorted(unsorted_list)
    # sorted_list = [*range(10000)]
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),  # 6 permutations
        ([1, 3, 2], [1, 2, 3]),
        ([2, 1, 3], [1, 2, 3]),  # pivot point is array[0]
        ([2, 3, 1], [1, 2, 3]),
        ([3, 1, 2], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([3, 2, 2, 1], [1, 2, 2, 3]),
        # (sorted_list, sorted_list)]  # to test sorting a sorted array
        (unsorted_list, sorted_list)]  # to test sorting an array with many repeated values

    for (args, answer) in test_cases:
        print("---------------------")
        unmodified = args[:]
        result = sort(args)

        if result is not None and answer is not None:
            print("input: " + str(unmodified) + " | expected answer: " + str(answer) + " | result: " + str(
                result))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " | expected answer: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", unmodified, "failed")


test_sort()
