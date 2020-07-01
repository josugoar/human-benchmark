from os import path

import tensorflow as tf
from tensorflow import data, keras
from tensorflow.keras import layers

from scripts import generator  # pylint: disable=import-error

# SERIALIZE DATA IN NUMPY ARRAYS

model = keras.Sequential(layers=[
    layers.Flatten(input_shape=(8, 8, 6))
], name="Model")

print(model.summary())


if __name__ == "__main__":

    dir_path = path.dirname(path.realpath(__file__))

    dataset = data.Dataset.from_generator(
        lambda file: generator(
            file, path.join(dir_path, "lib/stockfish-11-win/Windows/stockfish_20011801_x64_modern.exe")),
        (tf.float32, tf.float32),
        output_shapes=((8, 8, 6), ()),
        args=(path.join(dir_path, "data/2019.pgn"),)
    )

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(dataset.batch(32))
