# elegant way to build a list without having to use different for loops to append values one by one.

# [ expression-involving-loop-variable for loop-variable in sequence ]

ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
# print ListOfNumbers

# nested
# [ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]
# results = []
# for outer_loop_variable in outer_sequence:
#     for inner_loop_variable in inner_sequence:
#         results.append( expression_involving_loop_variables )


# filtering
# [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
#
#it evaluates boolean-expression-involving-loop-variable for every item. It also only keeps those members for which the
# boolean expression is True.

ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
# print ListOfThreeMultiples


# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
# ar = []
# p = 0
#
# # print range( x + 1)
# # print range( y )
#
# # for 0 <= i <= x or [0,x]
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
# print ar


# 2D - list comprehension version
# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
#
# print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]

# 3D - list comprehension version
x = int ( raw_input())
y = int ( raw_input())
z = int ( raw_input())
n = int ( raw_input())

print [ [ i, j, z] for i in range( x + 1) for j in range( y + 1) for z in range( z + 1) if ( ( i + j + z ) != n )]
