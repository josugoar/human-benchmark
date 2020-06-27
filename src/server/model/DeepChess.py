from tensorflow import keras


class DeepChess(keras.Model):

    def __init__(self):
        super(DeepChess, self).__init__()
        self.input = keras.layers.Dense(768, activation="relu")  # ranks * files * pieces * players
        self.hidden = keras.layers.Dense(384, activation="relu")  # ranks * files * pieces
        self.output = keras.layers.Dense(64, activation="sigmoid")  # ranks * files

    def call(self, inputs):
        x = self.input(inputs)
        x = self.hidden(x)
        x = self.output(x)
        return x


model = DeepChess()
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(x=[], y=[], epochs=5, verbose=2, validation_split=0.25)

# MCTS/UCT
