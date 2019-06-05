import numpy as np

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:

def check_sudoku(sodoku):
    matrix = np.array(sodoku)
    length = matrix.shape[0]

    for i in range(length):
        row = matrix[i, :]
        # print("row: "+str(i) + " values "+str(row))
        row = sorted(row)
        # print("sorted row: " + str(i) + " values " + str(row))
        for index, value in enumerate(row):
            if index + 1 != value:
                return False
                # print("row: "+str(i) + " index:"+str(index + 1)+" value: "+ str(value))
        # print(" \n ")

    for i in range(length):
        column = matrix[:, i]
        # print("column: "+str(i) + " values "+str(column))
        column = sorted(column)
        # print("sorted column: " + str(i) + " values " + str(column))
        for index, value in enumerate(column):
            if index + 1 != value:
                return False
                # print("column: "+str(i) + " index:"+str(index + 1)+" value: "+ str(value))
        # print(" \n ")
    return True

print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False


# An example solution for the check_sudoku() function

def check_sudoku_udacity(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        print("row: "+str(row))
        check_list = list(range(1, len(square[0]) + 1))
        print("check_list: "+str(check_list))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True
