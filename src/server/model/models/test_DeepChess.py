from os import path

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import utils
from tensorflow.keras.layers import (Activation, Add, Conv2D, Dense, Flatten,
                                     GlobalAveragePooling2D, Input, Lambda,
                                     Multiply, ReLU, Reshape)


def DeepChess() -> keras.Model:
    inputs = Input(shape=(8, 8, 7))
    FILTERS = 128
    y_1 = Conv2D(FILTERS, (3, 3), padding="same", activation="relu")(inputs)
    BLOCKS = 10
    for _ in range(BLOCKS):
        x = Conv2D(FILTERS, (3, 3), padding="same", activation="relu")(y_1)
        y_2 = Conv2D(FILTERS, (3, 3), padding="same", activation="relu")(x)
        x = GlobalAveragePooling2D()(y_2)
        SE_CHANNELS = 32
        x = Dense(SE_CHANNELS, activation="relu")(x)
        x = Dense(2 * FILTERS)(x)
        x = Reshape((2, FILTERS))(x)
        W, B = Lambda(tf.unstack, arguments=dict(axis=1))(x)
        # THIS IS FIXED, CHANGE IN ORIGINAL
        z = Activation("sigmoid")(W)
        z = Multiply()((z, y_2))
        x = Add()((z, B))
        x = Add()((x, y_1))
        y_1 = ReLU()(x)
    VALUE_CONV_SIZE = 32
    x = Conv2D(VALUE_CONV_SIZE, (3, 3), padding="same", activation="relu")(y_1)
    x = Conv2D(128, (3, 3), activation="relu")(x)
    x = Flatten()(x)
    outputs = Dense(1, activation="tanh")(x)
    return keras.Model(inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    print(DeepChess().summary())
