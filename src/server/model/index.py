import numpy as np
import requests
import tensorflow as tf
from tensorflow import keras


class MyModel(keras.Model):

    def __init__(self):
        super(MyModel, self).__init__()
        self.input = keras.layers.Dense(768, activation="relu")
        self.hidden = keras.layers.Dense(384, activation="relu")
        self.output = keras.layers.Dense(64, activation="softmax")

    def call(self, inputs):
        x = self.input(inputs)
        x = self.hidden(x)
        x = self.output(x)
        return x


model = MyModel()
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(x=[], y=[], epochs=5, verbose=2, validation_split=0.25)
