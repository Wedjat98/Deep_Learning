import numpy as np

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


def sum_squared_error(m, n):
    return 0.5 * np.sum((m - n) ** 2)


y2 = sum_squared_error(np.array(y), np.array(t))
print(y2)
