def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def isBeforeDate((yearBefore, monthBefore, dayBefore), (yearafter, monthAfter, dayAfter)):
    if yearBefore > yearafter:
        return False
    if yearBefore == yearafter:
        if monthBefore > monthAfter:
            return False
        if monthBefore == monthAfter:
            return dayBefore < dayAfter
            #if dayBefore >= dayAfter:
            #    return False
    return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    # date1 = (year1,month1,day1)
    while isBeforeDate((year1,month1,day1),(year2,month2,day2)):
        year1,month1,day1 = nextDay(year1,month1,day1)
        days += 1
    # YOUR CODE HERE!
    return days

def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()

# Nice job! Test case nextDay(2012, 1, 1) is correct!
# Nice job! Test case nextDay(2012, 4, 30) is correct!
# Nice job! Test case nextDay(2012, 12, 1) is correct!
# Nice job! Test case nextDay(1999, 12, 31) is correct!
# Nice job! Test case nextDay(2012, 12, 31) is correct!
# Nice job! Test case daysBetweenDates(2012, 9, 30, 2012, 10, 30) is correct!
# Nice job! Test case daysBetweenDates(2012, 5, 15, 2012, 5, 17) is correct!
# Nice job! Test case daysBetweenDates(2012, 1, 1, 2013, 1, 1) is correct!