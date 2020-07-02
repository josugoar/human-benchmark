from tensorflow import keras

model = keras.Sequential(layers=(
    keras.layers.Flatten(input_shape=(8, 8, 6))
), name="Model")


if __name__ == "__main__":
    print(model.summary())
