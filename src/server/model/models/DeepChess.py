from os import path

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import utils
from tensorflow.keras.layers import (Activation, Add, Conv2D, Dense, Flatten,
                                     GlobalAveragePooling2D, Input, Lambda,
                                     ReLU, Reshape)


def PolicyHead(inputs: tf.Tensor) -> tf.Tensor:
    POLICY_CONV_SIZE = 32
    x = Conv2D(POLICY_CONV_SIZE, (3, 3), padding="same")(inputs)
    x = Flatten()(x)
    x = Dense(1858)(x)
    return x


def ValueHead(inputs: tf.Tensor) -> tf.Tensor:
    VALUE_CONV_SIZE = 32
    x = Conv2D(VALUE_CONV_SIZE, (3, 3), padding="same")(inputs)
    x = Conv2D(128, (3, 3), activation="relu")(x)
    x = Flatten()(x)
    x = Dense(1, activation="tanh")(x)
    return x


def SENet(inputs: tf.Tensor, *, filters: int = 32) -> tf.Tensor:
    x = GlobalAveragePooling2D()(inputs)
    SE_CHANNELS = 32
    x = Dense(SE_CHANNELS, activation="relu")(x)
    x = Reshape((2, filters))(x)
    x = Dense(filters)(x)
    W, B = Lambda(tf.unstack, arguments=dict(axis=1))(x)
    Z = Activation("sigmoid")(W)
    x = Lambda(lambda x: Z * x + B)(inputs)
    return x


def ResNet(inputs: tf.Tensor, skip_connection: tf.Tensor, *, filters: int = 32) -> tf.Tensor:
    x = Conv2D(filters, (3, 3), padding="same")(inputs)
    x = Conv2D(filters, (3, 3), padding="same")(x)
    x = SENet(x, filters=filters)
    x = Add()((x, skip_connection))
    x = ReLU()(x)
    return x


def DeepChess() -> keras.Model:
    inputs = Input(shape=(8, 8, 6))
    FILTERS = 128
    x = y = Conv2D(FILTERS, (3, 3), padding="same")(inputs)
    BLOCKS = 10
    for _ in range(BLOCKS):
        x = ResNet(x, y, filters=FILTERS)
    outputs = PolicyHead(x), ValueHead(x)
    return keras.Model(inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    print(DeepChess().summary())
