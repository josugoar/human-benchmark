from numbers import Number
from typing import Callable

import numpy as np
from matplotlib import pyplot as plt

sigmoid: Callable[[np.ndarray, Number], np.ndarray] = lambda X, k=.01: 1 / (1 + np.exp(-X * k))

tanh: Callable[[np.ndarray, Number], np.ndarray] = lambda X, k=.01: np.tanh(X * k)


if __name__ == "__main__":
    X = np.linspace(-1000, 1000, num=1000)
    plt.plot(X, sigmoid(X), X, tanh(X))
    plt.legend(("sigmoid", "tanh"))
    plt.show()
