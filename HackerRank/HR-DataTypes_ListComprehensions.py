# 2D - list comprehension version
x = int(input())
y = int(input())
n = int(input())

print([[i, j] for i in range(x + 1) for j in range(y + 1) if ((i + j) != n)])

# 3D - list comprehension version
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# leason learned - python 2 allows me to use z inside [i,j,z] for z range(z+1) this is not valid on python3
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])

# Sample Input 0
#
# 1
# 1
# 1
# 2

# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

##################################################################
# Study
##################################################################
# Data camp
# https://www.datacamp.com/community/tutorials/python-list-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=332602034364&utm_targetid=aud-438999696719:dsa-486527602543&utm_loc_interest_ms=&utm_loc_physical_ms=1003659&gclid=EAIaIQobChMItoOO586h4gIVEkYNCh1cRgVrEAAYASAAEgL4mvD_BwE
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

# Flatten `list_of_list`
print([y for list in list_of_list for y in list])

# elegant way to build a list without having to use different for loops to append values one by one.
# [ expression-involving-loop-variable for loop-variable in sequence ]

ListOfNumbers = [x for x in range(10)]  # List of integers from 0 to 9
print(ListOfNumbers)

# nested
# [ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]
# results = []
# for outer_loop_variable in outer_sequence:
#     for inner_loop_variable in inner_sequence:
#         results.append( expression_involving_loop_variables )


# filtering
# [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
#
# it evaluates boolean-expression-involving-loop-variable for every item. It also only keeps those members for which the
# boolean expression is True.

# ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
# print ListOfThreeMultiples


# x = int (input())
# y = int (input())
# n = int (input())
# ar = []
# p = 0
#
# # print range(x + 1)
# # print range(y )
#
# # for 0 <= i <= x or [0,x]
# for i in range ( x + 1 ) :
#     for j in range(y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
# print ar
