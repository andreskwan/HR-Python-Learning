# Open a file: file
file = open('moby_dick.txt', 'r')

# Print it
print(file.read())

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)


# txt = open(file, 'r')
# print(txt.read())