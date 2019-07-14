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
        return days[month-1] + 1
    return days[month-1]


def test_day_in_month():
    test_cases = [((0, 13), "AssertionError"),
                  ((0, 0), "AssertionError"),
                  ((0, 12), 31),
                  ((0, 2), 29),
                  ((0, 1), 31),
                  ((1800, 2), 28),
                  ((1996, 2), 29)]

    for (args, answer) in test_cases:
        try:
            result = day_in_month(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test_day_in_month()