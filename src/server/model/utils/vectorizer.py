import chess
import numpy as np


def fenToBitmap(fen: str) -> np.array:
    board = chess.BaseBoard(fen)
    bitmap = np.zeros((len(chess.PIECE_NAMES), len(chess.FILE_NAMES), len(chess.RANK_NAMES)))
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        for file_idx in range(len(chess.FILE_NAMES)):
            for rank_idx in range(len(chess.RANK_NAMES)):
                piece = board.piece_at(file_idx * len(chess.RANK_NAMES) + rank_idx)
                if piece and piece.piece_type is piece_type:
                    bitmap[piece_idx, file_idx, rank_idx] = 1 if piece.color is chess.WHITE else -1
    return bitmap


if __name__ == "__main__":
    fenToBitmap(chess.STARTING_BOARD_FEN)
