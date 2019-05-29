from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print ("Title: " + self.title)
        print ("Author: " + self.author)
        print ("Price: " + str(self.price))



def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

# year = int(input())
# print(is_leap(year))

print(is_leap(1996))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2300))
print(is_leap(2500))

# myBook = MyBook("Cosmos","Carl Sagan","50.000")
# myBook.display()
#
# numeroDouble = 10.5
#
# print("Hello python world")
#
# print(numeroDouble)


# # The current volume of a water reservoir (in cubic metres)
# reservoir_volume = 4.445e8
# # The amount of rainfall from a storm (in cubic metres)
# rainfall = 5e6
#
# # decrease the rainfall variable by 10% to account for runoff
# rainfall -= rainfall * 0.1
# # add the rainfall variable to the reservoir_volume variable
# reservoir_volume += rainfall
# # increase reservoir_volume by 5% to account for stormwater that flows
# # into the reservoir in the days following the storm
# reservoir_volume += reservoir_volume * 0.05
# # decrease reservoir_volume by 5% to account for evaporation
# reservoir_volume -= reservoir_volume * 0.05
# # subtract 2.5e5 cubic metres from reservoir_volume to account for water
# # that's piped to arid regions.
# reservoir_volume -= 2.5e5
# # print the new value of the reservoir_volume variable
# print(reservoir_volume)