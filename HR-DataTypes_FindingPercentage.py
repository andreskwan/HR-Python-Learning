#  imperative way
from functools import reduce

# if __name__ == '__main__':
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()


def add(x, y):
    return x + y


def media(student_name):
    value = reduce(add, student_marks[student_name])
    return value / len(student_marks[student_name])


print("{:0.2f}".format(media(query_name)))
