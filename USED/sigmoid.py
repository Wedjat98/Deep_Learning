import numpy as np
import matplotlib.pylab as plt


def sigmoid(x1):
    return 1 / (1 + np.exp(-x1))


x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
