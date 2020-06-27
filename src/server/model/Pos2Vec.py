from tensorflow import keras


class Pos2Vec(keras.Model):

    def __init__(self):
        super(Pos2Vec, self).__init__()
        self.dense_1 = keras.layers.Dense(768, activation="relu")
        self.dense_2 = keras.layers.Dense(600, activation="relu")
        self.dense_3 = keras.layers.Dense(400, activation="relu")
        self.dense_4 = keras.layers.Dense(200, activation="relu")
        self.dense_5 = keras.layers.Dense(100, activation="relu")

    def call(self, inputs):
        x = self.dense_1(inputs)
        x = self.dense_2(x)
        x = self.dense_3(x)
        x = self.dense_4(x)
        x = self.dense_5(x)
        return x


autoencoder = Pos2Vec()
autoencoder.compile(optimizer="", loss="", metrics=[])
history = autoencoder.fit(x=None, y=None, epochs=5, verbose=2, validation_split=0.2)
