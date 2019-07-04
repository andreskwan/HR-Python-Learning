import random

# def sort(array: [int]) -> [int]:
#     sorted_list = []
#     size = len(array)
#     if size == 1:
#         return array
#     else:
#     lowest = None
#     middle = array[0]
#     heights = None
#
#     for value in array:
#         if value > middle:
#             heights = value
#         if value < middle:
#             lowest = value
#
#     if lowest is not None:  sorted_list.append(lowest)
#     sorted_list.append(middle)
#     if heights is not None:  sorted_list.append(heights)
#
#     return sorted_list


# def sort(array):
#     size = len(array)
#     while size > 0:
#         index = 0
#         while size > index + 1:
#             if is_out_of_order(array, index):
#                 swap(array, index)
#             index += 1
#         size -= 1
#     return array


def is_out_of_order(args, index):
    return args[index] > args[index + 1]


def swap(args, index):
    temp = args[index]
    args[index] = args[index + 1]
    args[index + 1] = temp


def sort(array):
    sorted_list = []
    size = len(array)

    if size == 0:
        return array
    else:
        middle = array[0]
        lower = []
        higher = []
        for value in array:
            if value > middle:
                higher.append(value)
            elif value < middle:
                lower.append(value)

        sorted_list.extend(sort(lower))
        sorted_list.append(middle)
        sorted_list.extend(sort(higher))
    return sorted_list


def swap_computed(array, middle):
    lower = None
    higher = None
    for value in array:
        if value > middle:
            higher = value
        elif value < middle:
            lower = value
    return higher, lower
# def swap_computed(array, index):
#     if array[index] > array[index + 1]:
#         lower = array[index + 1]
#         higher = array[index]
#     else:
#         lower = array[index]
#         higher = array[index + 1]
#     return higher, lower


def test_sort():
    print("--------------------------")
    print("-------test_prime_factors-------")
    unsorted_list = [random.randint(1, 100000) for x in range(100)]
    sorted_list = sorted(unsorted_list)
    # sorted_list = [*range(10000)]
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),   # 6 permutations
        ([1, 3, 2], [1, 2, 3]),
        ([2, 1, 3], [1, 2, 3]),  # pivot point is array[0]
        ([2, 3, 1], [1, 2, 3]),
        ([3, 1, 2], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        # (sorted_list, sorted_list)]
        (unsorted_list, sorted_list)]

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
