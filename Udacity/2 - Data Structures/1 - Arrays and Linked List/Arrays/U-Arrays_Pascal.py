def nth_row_pascal(n):
    n -= 1
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row

# def nth_row_pascal(n):
#     """
#     :param - arr - input array
#     return - number - largest sum in contiguous subarry within arr
#     """
#     n += 1
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#
#     array = [1]
#
#     p_r = nth_row_pascal(n-1)
#     print(p_r)
#     for i in range(n-2):
#         value = p_r[i] + p_r[i+1]
#         array.append(value)
#     array.append(1)
#     return array




def test_nth_row_pascal():
    test_cases = [
        (1, [1]),
        (2, [1, 1]),
        (3, [1, 2, 1]),
        (4, [1, 3, 3, 1]),
        (7, [1, 6, 15, 20, 15, 6, 1]),
        (9, [1, 8, 28, 56, 70, 56, 28, 8, 1])]

    for (args, answer) in test_cases:
        print("---------------------")
        result = nth_row_pascal(args)
        if result is not None and answer is not None:
            print("input: " + str(args) + " | expected answer: " + str(answer) + " | result: " + str(
                result))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")
        else:
            print("result: " + str(result) + " and answer: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")


test_nth_row_pascal()
