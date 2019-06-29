from typing import NamedTuple
from dataclasses import dataclass


# class Mark(NamedTuple):
@dataclass
class Mark:
    # def __init__(self, origin=0, end=0, total=0):
    # self.origin = origin
    # self.end = end
    # self.total = total
    origin: int
    end: int
    total: int


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    end = 0
    origin = None
    marks = []
    total = None
    last_mark = None

    for index, value in enumerate(arr):
        if value >= 0:
            if total is None:
                total = 0
            total += value
            if origin is None:
                origin = index
            last_mark = Mark(origin=origin, end=index, total=total)
            continue
        else:
            if total is not None:
                end = index - 1
                marks.append(Mark(origin=origin, end=end, total=total))
                if (value + total) >= 0:
                    total += value
                else:
                    total = None
                    origin = None
    if last_mark is not None:
        marks.append(last_mark)

    final_index = 0
    final_total = 0
    final_mark = None

    for mark in marks:
        if final_total < mark.total:
            final_total = mark.total
    # print(arr[mark.origin:mark.end + 1])
    return final_total


def test_max_sum_subarray():
    test_cases = [
        # ([], None),
        #               ([0], 0),
        #               ([0, 0], 0),
        #               ([0, 1], None),
        ([1, 2, 3, -4, 6], 8),
        ([1, 2, -5, -4, 1, 6], 7),
        ([-12, 15, -13, 14, -1, 2, 1, -5, 4], 18)]

    for (args, answer) in test_cases:
        print("---------------------")
        result = max_sum_subarray(args)
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


test_max_sum_subarray()
