import random


def sort(array: [int]) -> [int]:
    sorted_list = array
    size = len(array)
    while size > 0:
        index = 0
        while size > index + 1:  # then swap
            if is_out_of_order(array, index):
                swap(array, index)
            index += 1
        size -= 1
    return sorted_list


def is_out_of_order(args, index):
    return args[index] > args[index + 1]


def swap(args, index):
    temp = args[index]
    args[index] = args[index + 1]
    args[index + 1] = temp


def test_sort():
    print("--------------------------")
    print("-------test_prime_factors-------")
    unsorted_list = [random.randint(1, 100000) for x in range(1000)]
    sorted_list = sorted(unsorted_list)
    test_cases = [
        # ([], []),
        # ([1], [1]),
        # ([2, 1], [1, 2]),
        # # ([1, 2, 3], [1, 2, 3]),
        # # ([2, 1, 3], [1, 2, 3]),
        # ([1, 3, 2], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        (unsorted_list, sorted_list)]

    for (args, answer) in test_cases:
        print("---------------------")
        result = sort(args)

        if result is not None and answer is not None:
            print("input: " + str(args) + " | expected answer: " + str(answer) + " | result: " + str(
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
                print("Test with input data:", args, "failed")


test_sort()


