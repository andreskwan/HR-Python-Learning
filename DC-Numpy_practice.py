import numpy as np

a = np.array([[4, 0, 1], [2, 2, 2], [5, 5, 5]])

b = a[1, 1]

a[b, :]

c = np.sum(a[b, :])

print(c)

a = np.array([[3, 1, 3], [1, 4, 2]])

b = a[:, 1][0]

print(b)
