from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential(
    layers=(),
    name="Model"
)


if __name__ == "__main__":
    print(model.summary())
