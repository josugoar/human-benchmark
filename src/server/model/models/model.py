import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import (Activation, Conv2D, Dense, Flatten,
                                     GlobalAveragePooling2D, Input, Lambda,
                                     ReLU, Reshape, add, multiply)


def policy_head(inputs: tf.Tensor, /) -> tf.Tensor:
    x = conv_block(inputs, filters=32)
    x = Flatten()(x)
    return Dense(1858, activation="softmax", name="policy")(x)


def value_head(inputs: tf.Tensor, /) -> tf.Tensor:
    x = conv_block(inputs, filters=32)
    x = Flatten()(x)
    x = Dense(128, activation="relu")(x)
    return Dense(1, activation="tanh", name="value")(x)


def squeeze_and_exite(inputs: tf.Tensor, /, units: int) -> tf.Tensor:
    x = GlobalAveragePooling2D()(inputs)
    x = Dense(32, activation="relu")(x)
    x = Dense(2 * units)(x)
    x = Reshape((2, units))(x)
    W, B = Lambda(tf.unstack, arguments={"axis": 1})(x)
    Z = Activation("sigmoid")(W)
    return add((multiply((Z, inputs)), B))


def conv_block(inputs: tf.Tensor, /, filters: int, *, units: int = None, skip_connection: tf.Tensor = None) -> tf.Tensor:
    x = Conv2D(filters, (3, 3), padding="same")(inputs)
    if units is not None:
        x = squeeze_and_exite(x, units=units)
    if skip_connection is not None:
        x = add((x, skip_connection))
    return ReLU()(x)


def residual_block(inputs: tf.Tensor, /, filters: int) -> tf.Tensor:
    x = conv_block(inputs, filters=filters)
    return conv_block(x, filters=filters, units=128, skip_connection=inputs)


def get_model() -> keras.Model:
    inputs = Input(shape=(8, 8, 6))
    x = conv_block(inputs, filters=128)
    for _ in range(10):
        x = residual_block(x, filters=128)
    outputs = policy_head(x), value_head(x)
    return keras.Model(inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    model = get_model()
    print(model.summary())
