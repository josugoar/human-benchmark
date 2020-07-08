from numbers import Number
from typing import Callable, Union

import numpy as np
from matplotlib import pyplot as plt

sigmoid: Callable[
    [Union[Number, np.ndarray], Number],
    Union[complex, float, np.ndarray]
] = lambda X, k=0.01: 1 / (1 + np.exp(-X * k))

tanh: Callable[
    [Union[Number, np.ndarray], Number],
    Union[complex, float, np.ndarray]
] = lambda X, k=0.01: np.tanh(X * k)


if __name__ == "__main__":
    X = np.linspace(-10000, 10000, num=10000)
    plt.plot(X, sigmoid(X), X, tanh(X))
    plt.legend(("sigmoid", "tanh"))
    plt.show()
