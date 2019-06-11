# https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/9bbb9a6d-d848-4153-a2fc-25065ee8d42d/lessons/2bdc11fe-1acf-4363-8cac-d2a9c1d714a1/concepts/d5d4db5f-e7fc-4005-96b1-cb8b1c770fdc
# http://www.onlineconversion.com/leapyear.htm


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
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    if day < day_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def is_date_before(year_before, month_before, day_before, year_after, month_after, day_after):
    if year_before > year_after:
        return False
    if year_before == year_after:
        if month_before > month_after:
            return False
        if month_before == month_after:
            return day_before < day_after
    return True


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    # date1 = (year1,month1,day1)
    assert not is_date_before(year2, month2, day2, year1, month1, day1)
    while is_date_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1
    # YOUR CODE HERE!
    return days


def test_days_between_dates():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523),
                  ((2013, 1, 1, 1999, 12, 31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = days_between_dates(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test_days_between_dates()

# Nice job! Test case next_day(2012, 1, 1) is correct!
# Nice job! Test case next_day(2012, 4, 30) is correct!
# Nice job! Test case next_day(2012, 12, 1) is correct!
# Nice job! Test case next_day(1999, 12, 31) is correct!
# Nice job! Test case next_day(2012, 12, 31) is correct!
# Nice job! Test case days_between_dates(2012, 9, 30, 2012, 10, 30) is correct!
# Nice job! Test case days_between_dates(2012, 5, 15, 2012, 5, 17) is correct!
# Nice job! Test case days_between_dates(2012, 1, 1, 2013, 1, 1) is correct!

# Nice job! Test case next_day(2012, 1, 1) is correct!
# Nice job! Test case next_day(2012, 4, 30) is correct!
# Nice job! Test case next_day(2012, 12, 1) is correct!
# Nice job! Test case next_day(1999, 12, 31) is correct!
# Nice job! Test case next_day(2012, 12, 31) is correct!
# Nice job! Test case days_between_dates(2012, 9, 30, 2012, 10, 30) is correct!
# Nice job! Test case days_between_dates(2012, 2, 1, 2012, 3, 1) is correct!
# Nice job! Test case days_between_dates(2013, 1, 1, 1999, 12, 31) correctly raises AssertionError!
# Nice job! Test case days_between_dates(1991, 3, 1, 1991, 1, 3) correctly raises AssertionError!
# Nice job! Test case days_between_dates(2012, 1, 1, 2012, 2, 28) is correct!
# Nice job! Test case days_between_dates(2012, 1, 1, 2012, 3, 1) is correct!
# Nice job! Test case days_between_dates(2011, 6, 30, 2012, 6, 30) is correct!
# Nice job! Test case days_between_dates(2011, 1, 1, 2012, 8, 8) is correct!
# Nice job! Test case days_between_dates(1900, 1, 1, 1999, 12, 31) is correct!

# print days_between_dates(2013, 1, 24, 2013, 6, 29)
# print days_between_dates(1912, 12, 12, 2012, 12, 12)
# print days_between_dates(2013, 1, 1, 2012, 12, 20) # returns 0 - but it doesn't make sense so program defensevely

# print not is_date_before(2012, 9, 1, 2012, 9, 1)

# BEI-C_G_-AF-DHJK
# BEI
#
