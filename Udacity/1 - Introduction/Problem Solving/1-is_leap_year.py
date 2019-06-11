def is_leap_year(year):
    """
    :type year: int
    """
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            leap = ((year % 400) == 0)
        else:
            leap = True
    return leap


def test_is_leap_year():
    test_cases = [(1800, False),
                  (1900, False),
                  (1996, True),
                  (2000, True),
                  (2100, False),
                  (2300, False),
                  (2500, False)]

    for (args, answer) in test_cases:
        try:
            result = is_leap_year(args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test_is_leap_year()