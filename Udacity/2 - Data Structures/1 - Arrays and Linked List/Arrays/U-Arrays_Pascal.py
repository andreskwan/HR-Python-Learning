def nth_row_pascal_udacity(n):
    """
    first row is n = 0
    :param n:
    :return:
    """
    n -= 1
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):  # start from 1 allows to have (j - 1)
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row


def nth_row_pascal(n):
    """
    first row is n = 1
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    current_row = [1]
    previous_row = nth_row_pascal(n-1)
    for i in range(n-1):
        next_number = previous_row[i] + previous_row[i+1]
        current_row.append(next_number)
    current_row.append(1)
    return current_row


# (1, [1]),
#         (2, [1, 1]),
#         (3, [1, 2, 1]),
#         (4, [1, 3, 3, 1]),
#         (7, [1, 6, 15, 20, 15, 6, 1]),
#         (9, [1, 8, 28, 56, 70, 56, 28, 8, 1])]

def test_nth_row_pascal():
    test_cases = [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
        (8, [1, 8, 28, 56, 70, 56, 28, 8, 1])]

    for (args, answer) in test_cases:
        print("---------------------")
        result = nth_row_pascal(args)
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


test_nth_row_pascal()
