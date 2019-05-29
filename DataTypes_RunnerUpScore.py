# n = int(raw_input())
# arr = map(int, raw_input().split())

n = int(input())
arr = map(int, input().split())


if 2 <= n and n <= 10:
    arr = list(dict.fromkeys(arr))
    arr = sorted(arr)

# print arr
print(arr[len(arr)-2])

# input
# 5
# 2 3 6 6 5

# output
# 5