import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# from scripts.vectorizer import fenToBitmap

# CNN


class Model(keras.Model):

    def __init__(self):
        super(Model, self).__init__()
        self.a = layers.Lambda(lambda x: fenToBitmap(x))
        self.dense_1 = layers.Dense(100, activation="relu")
        self.dense_2 = layers.Dense(50, activation="relu")
        self.dense_3 = layers.Dense(2, activation="tanh")

    def call(self, inputs):
        x = self.dense_1(inputs)
        x = self.dense_2(x)
        x = self.dense_3(x)
        return x


# x = [fenToBitmap(fen) for fen in ["5k1r/1p3p2/pnn1b3/4PpNp/7P/2N5/PP4P1/3R1R1K",
#                                   "r1bqr1k1/2p2pbp/p1np1np1/1p6/1PB1P3/2N1QN1P/P1P2PP1/1RB2RK1"]]
x = [np.array([1], ndmin=2), np.array([2], ndmin=2)]
y = [np.array([1], ndmin=2), np.array([2], ndmin=2)]


def generator(path="", batch_size=64):
    for _ in range(10000):
        inputs = [[1, 2]]
        targets = [[1, 2]]
        X = np.array(inputs)
        y = np.array(targets)
        # print(X.shape, y.shape)
        # for i, j in zip(x, y):
        yield X, y


a = generator()

model = Model()
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(a, epochs=1, verbose=2)
