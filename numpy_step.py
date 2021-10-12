import numpy as np


def step_fun(x):
    y = x > 0
    return y.astype(np.int64)


print(step_fun(np.array([1.0, -1.0])))
