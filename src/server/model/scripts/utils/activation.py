from numbers import Number
from typing import Callable, Union

import numpy as np
from matplotlib import pyplot as plt

f: Callable[
    [Union[Number, np.ndarray], Number],
    Union[complex, float, np.ndarray]
] = lambda X, k=0.1: np.tanh(X * k)

g: Callable[
    [Union[Number, np.ndarray], Number],
    Union[complex, float, np.ndarray]
] = lambda X, k=0.1: 1 / (1 + np.exp(-X * k))


if __name__ == "__main__":
    X = np.linspace(-100, 100, num=100)
    plt.plot(X, f(X), X, g(X))
    plt.legend(("tanh", "sigmoid"))
    plt.show()
