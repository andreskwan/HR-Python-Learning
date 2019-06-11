def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            leap = ((year % 400) == 0)
        else:
            leap = True
    return leap


def day_in_month(year, month):
    assert 1 <= month <= 12
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return days[month - 1] + 1
    return days[month - 1]


def next_day(year, month, day):
    """It depends on the exactly numbers of days in a month, so it also depends on identifying
    if a year passed is a leap year.
    """
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    """Simple version: assume every month has 30 days"""
    if day < day_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def test_next_day():
    test_cases = [((1999, 12, 31), (2000, 1, 1)),
                  ((1999, 2, 28), (1999, 3, 1)),
                  ((1999, 3, 28), (1999, 3, 29)),
                  ((1999, 0, 31), "AssertionError"),
                  ((1999, -1, 31), "AssertionError"),
                  ((1999, 13, 31), "AssertionError"),
                  ((1999, 12, -1), "AssertionError"),
                  ((1999, 12, 0), "AssertionError"),
                  ((1999, 12, 32), "AssertionError")]
    #           ((0, 12), 31),
    #           ((0, 2), 28),
    #           ((0, 1), 31)]

    for (args, answer) in test_cases:
        try:
            result = next_day(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test_next_day()
