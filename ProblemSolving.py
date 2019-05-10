###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day+1<=30:
        return (year,month,day+1)
    day = (day+1)%30
    if month+1<=12:
        return (year,month+1,day)
    month = (month+1)%12
    year = year+1
    return (year,month,day)

print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30) #=> (2013, 2, 1)
print(nextDay(2012, 12, 30)) #=> (2013, 1, 1)  (even though December really has 31 days)
# Nice job! Test case nextDay(2012, 1, 1) is correct!
# Nice job! Test case nextDay(2012, 4, 30) is correct!
# Nice job! Test case nextDay(2012, 12, 1) is correct!
# Nice job! Test case nextDay(1999, 12, 30) is correct!
# Nice job! Test case nextDay(2012, 12, 30) is correct!