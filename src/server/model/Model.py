from tensorflow import keras
from tensorflow.keras import layers

# model = keras.Sequential(
#     layers=(
#         layers.Dense(
#             384,
#             activation="relu",
#             input_shape=(8, 8, 6),
#             name="dense_1"
#         ),
#         layers.Dropout(
#             .2,
#             name="dropout_1"
#         ),
#         layers.Dense(
#             192,
#             activation="relu",
#             name="dense_2"
#         ),
#         layers.Dropout(
#             .2,
#             name="dropout_2"
#         ),
#         layers.Flatten(),
#         layers.Dense(
#             1,
#             activation="softmax",
#             name="dense_3"
#         )
#     ),
#     name="Model"
# )

model = keras.Sequential(
    layers=(
        # layers.Conv2D(
        #     5, (5, 5),
        #     padding="same",
        #     activation="relu",
        #     input_shape=(8, 8, 6),
        #     name="conv2d_1"
        # ),
        # layers.SpatialDropout2D(
        #     .2,
        #     name="spatial_dropout2d_1"
        # ),
        # layers.Conv2D(
        #     10, (3, 3),
        #     # padding="same",
        #     activation="relu",
        #     name="conv2d_2"
        # ),
        # layers.SpatialDropout2D(
        #     .2,
        #     name="spatial_dropout2d_2"
        # ),
        layers.Flatten(),
        layers.Dense(
            8*8*6,
            activation="relu"
        ),
        layers.Dense(
            1,
            activation="sigmoid",
            name="dense_4"
        )
    ),
    name="Model"
)


if __name__ == "__main__":
    print(model.summary())
