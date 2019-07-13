# understand set of possible inputs
# input format
# array values from [0, n-2)
# smallest input
# n = 2 -> [0] - is not valid because
# n = 3 -> [0, 0] returns 0

# only one number is repeated
# numbers appear only once


# def duplicate_number(arr):
#     current_sum = 0
#     expected_sum = 0
#
#     for num in arr:
#         current_sum += num
#
#     for i in range(len(arr) - 1):
#         expected_sum += i
#     return current_sum - expected_sum


def duplicate_number(arr):
    """
    :preconditions
    - array first element should be 0
    - array is not necessarily ordered , but conteins elements from (0, n-2)
    - minimum length is 2 [0, 0]
    - [0, 1] is not valid
    - [0, 1, 1] is valid
    - only one element is repeated
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    partial = 0
    expected_total = 0
    if len(arr) == 0 or len(arr) == 1:
        return None

    for value in arr:
        partial += value

    for value in range(len(arr) - 1):
        expected_total += value
    return abs((expected_total - partial))


# ([], None),
#                   ([0], None),
#                   ([0, 0], 0),
#                   ([0, 1], None),
#                   ([0, 0, 1], 0),
#                   ([0, 1, 1], 1),
#                   ([0, 1, 2], None),
#                   ([0, 1, 2, 2], 2),
#                   ([0, 1, 3, 3], 3),
#                   ([0, 2, 3, 1, 4, 5, 3], 3),
#                   ([0, 1, 5, 4, 3, 2, 0], 0)
test_duplicate_number()


def test_duplicate_number():
    test_cases = [([], None),
                  ([0], None),
                  ([0, 0], 0),
                  # ([0, 1], None),
                  ([0, 0, 1], 0),
                  ([0, 1, 1], 1),
                  # ([0, 1, 2], None),
                  ([0, 1, 1, 2], 1),
                  ([0, 1, 2, 2], 2),
                  # ([0, 1, 3, 3], None),
                  ([0, 1, 2, 2, 3], 2),
                  ([0, 1, 3, 3, 2], 3),
                  ([0, 2, 3, 1, 4, 5, 3], 3),
                  ([0, 1, 5, 4, 3, 2, 0], 0)]

    for (args, answer) in test_cases:
        print("---------------------")
        result = duplicate_number(args)
        if result is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(
                result) + " |")
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")
