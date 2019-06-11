###
### Define a simple next_day procedure, that assumes
### every month has 30 days.
###
### For example:
###    next_day(1999, 12, 30) => (2000, 1, 1)
###    next_day(2013, 1, 30) => (2013, 2, 1)
###    next_day(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###


def next_day(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day + 1 <= 30:
        return year, month, day + 1
    day = (day + 1) % 30
    if month + 1 <= 12:
        return year, month + 1, day
    month = (month + 1) % 12
    year = year + 1
    return year, month, day


print(next_day(2012, 12, 30))  # => (2013, 1, 1)  (even though December really has 31 days)

# print next_day(1999, 12, 30)
# print next_day(2013, 1, 30) #=> (2013, 2, 1)
# Nice job! Test case next_day(2012, 1, 1) is correct!
# Nice job! Test case next_day(2012, 4, 30) is correct!
# Nice job! Test case next_day(2012, 12, 1) is correct!
# Nice job! Test case next_day(1999, 12, 30) is correct!
# Nice job! Test case next_day(2012, 12, 30) is correct!
