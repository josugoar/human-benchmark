import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def policy_head(inputs: tf.Tensor, /) -> tf.Tensor:
    x = layers.Conv2D(POLICY_CONV_SIZE := 32, (3, 3), padding="same")(inputs)
    x = layers.Flatten()(x)
    return layers.Dense(1858)(x)


def value_head(inputs: tf.Tensor, /) -> tf.Tensor:
    x = layers.Conv2D(VALUE_CONV_SIZE := 32, (3, 3), padding="same", activation="relu")(inputs)
    x = layers.Conv2D(128, (3, 3), activation="relu")(x)
    x = layers.Flatten()(x)
    return layers.Dense(1, activation="tanh")(x)


def squeeze_and_exite(inputs: tf.Tensor, /, *, filters: int = 32) -> tf.Tensor:
    x = layers.GlobalAveragePooling2D()(inputs)
    x = layers.Dense(SE_CHANNELS := 32, activation="relu")(x)
    x = layers.Dense(2 * filters)(x)
    x = layers.Reshape((2, filters))(x)
    W, B = layers.Lambda(tf.unstack, arguments={"axis": 1})(x)
    Z = layers.Activation("sigmoid")(W)
    return layers.add((layers.multiply((Z, inputs)), B))


def residual_block(inputs: tf.Tensor, /, *, filters: int = 32) -> tf.Tensor:
    x = layers.Conv2D(filters, (3, 3), padding="same", activation="relu")(inputs)
    x = layers.Conv2D(filters, (3, 3), padding="same")(x)
    x = squeeze_and_exite(x, filters=filters)
    x = layers.add((x, inputs))
    return layers.ReLU()(x)


def get_model() -> keras.Model:
    inputs = layers.Input(shape=(8, 8, 6))
    x = layers.Conv2D(FILTERS := 128, (3, 3), padding="same", activation="relu")(inputs)
    for _ in range(BLOCKS := 10):
        x = residual_block(x, filters=FILTERS)
    outputs = value_head(x)
    return keras.Model(inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    model = get_model()
    print(model.summary())
