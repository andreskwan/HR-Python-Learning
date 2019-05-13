n = int(raw_input())
arr = map(int, raw_input().split())

if 2 <= n and n <= 10:
    arr = list(dict.fromkeys(arr))
    arr = sorted(arr)

# print arr
print arr[len(arr)-2]


