from typing import Callable, Union

import numpy as np
from matplotlib import pyplot as plt

Numeric = Union[np.number, np.ndarray]
Activation = Callable[[Numeric, Numeric], Numeric]

sigmoid: Activation = lambda X, /, *, k=.01: 1 / (1 + np.exp(-X * k))

tanh: Activation = lambda X, /, *, k=.01: np.tanh(X * k)


if __name__ == "__main__":
    X = np.linspace(-1000, 1000, num=1000)
    plt.plot(X, sigmoid(X), X, tanh(X))
    plt.legend(("sigmoid", "tanh"))
    plt.show()
