import chess
import numpy as np


def bitboard(board: chess.Board = chess.Board(), /, *, dtype: np.dtype = float) -> np.ndarray:
    bitmap = np.zeros(
        (len(chess.FILE_NAMES), len(chess.RANK_NAMES), len(chess.PIECE_TYPES)), dtype=dtype
    )
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type is piece_type:
                bitmap[
                    chess.square_rank(square),
                    chess.square_file(square),
                    piece_idx
                ] = 1 if piece.color else -1
    return bitmap if board.turn else -np.flip(bitmap, axis=range(2))


def print_bitboard(bitmap: np.ndarray, /) -> None:
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        print(bitmap[:, :, piece_idx], chess.piece_name(piece_type), end="\n" * 2)


if __name__ == "__main__":
    print_bitboard(bitboard(chess.Board()))
