import numpy as np
import matplotlib.pylab as plt


def step_fun(x):
    y = x > 0
    y = y.astype(np.int64)
    return y


x = np.arange(-5.0, 5.0, 0.1)
y = step_fun(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
