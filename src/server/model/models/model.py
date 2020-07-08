import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def f(z):
    # == BODY == #
    FILTERS = 128
    y = layers.Conv2D(FILTERS, (3, 3), padding="same")(z)

    # == RESIDUAL_TOWER == #
    BLOCKS = 10
    for _ in range(BLOCKS):
        x = layers.Conv2D(FILTERS, (3, 3), padding="same")(y)
        x = layers.Conv2D(FILTERS, (3, 3), padding="same")(x)

        # == SQUEEZE_AND_EXITATION == #
        SE_CHANNELS = 32
        x = layers.GlobalAveragePooling2D()(y)
        x = layers.Dense(SE_CHANNELS, activation="relu")(x)
        x = layers.Reshape((2, FILTERS))(x)
        x = layers.Dense(FILTERS)(x)
        W, B = tf.unstack(x, axis=1)
        Z = layers.Activation("sigmoid")(W)
        # Use lambda here
        x = layers.Add()((layers.Multiply()((Z, y)), B))

        x = layers.Add()((x, y))
        x = layers.ReLU()(x)

    # == POLICY_HEAD == #
    POLICY_CONV_SIZE = 32
    ph = layers.Conv2D(POLICY_CONV_SIZE, (3, 3), padding="same")(x)
    ph = layers.Flatten()(ph)
    ph = layers.Dense(1858)(ph)

    # == VALUE_HEAD == #
    vh = layers.Conv2D(32, (3, 3), padding="same")(x)
    vh = layers.Conv2D(128, (3, 3), activation="relu")(vh)
    vh = layers.Flatten()(vh)
    vh = layers.Dense(1, activation="tanh")(vh)
    return ph, vh


inputs = layers.Input(shape=(8, 8, 6))

model = keras.Model(inputs=inputs, outputs=f(inputs))


if __name__ == "__main__":
    print(model.summary())
