import chess
import numpy as np

# tf.keras.layers.experimental.preprocessing.PreprocessingLayer(
#     trainable=True, name=None, dtype=None, dynamic=False, **kwargs
# )


def fenToBitmap(fen: str) -> np.ndarray:
    board = chess.BaseBoard(fen)
    bitmap = np.zeros((len(chess.FILE_NAMES), len(chess.RANK_NAMES), len(chess.PIECE_TYPES)))
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        for file_idx in range(len(chess.FILE_NAMES)):
            for rank_idx in range(len(chess.RANK_NAMES)):
                piece = board.piece_at(file_idx * len(chess.RANK_NAMES) + rank_idx)
                if piece and piece.piece_type is piece_type:
                    bitmap[file_idx, rank_idx, piece_idx] = 1 if piece.color is chess.WHITE else -1
    return bitmap


if __name__ == "__main__":

    def print_bitmap(bitmap: np.ndarray) -> str:
        out = ""
        for piece, idx in zip(chess.PIECE_NAMES[1:], range(bitmap.shape[-1])):
            out += f"{piece}:\n{bitmap[:, :, idx]}\n\n"
        return out

    print(print_bitmap(fenToBitmap(chess.STARTING_BOARD_FEN)))
