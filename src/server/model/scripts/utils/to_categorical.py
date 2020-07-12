import numpy as np


def to_categorical(y, /, *, num_classes: int, dtype: np.dtype = np.float32):
    try:
        classes = []
        for idx in y:
            clazz = np.zeros(num_classes)
            clazz[idx] = 1
            classes.append(clazz)
        return np.array(classes, dtype=dtype)
    except TypeError:
        clazz = np.zeros(num_classes, dtype=dtype)
        clazz[y] = 1
        return clazz


if __name__ == "__main__":
    print(to_categorical(range(5), num_classes=5))
