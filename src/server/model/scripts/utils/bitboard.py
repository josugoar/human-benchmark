import chess
import numpy as np


def bitboard(board: chess.Board) -> np.ndarray:
    bitmap = np.zeros(
        (len(chess.FILE_NAMES), len(chess.RANK_NAMES), len(chess.PIECE_TYPES)), dtype=int
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
    return bitmap


def absolute_bitboard(board: chess.Board) -> np.ndarray:
    bitmap = bitboard(board)
    return np.dstack((bitmap, np.full(bitmap.shape[:-1], 1 if board.turn else -1)))


def relative_bitboard(board: chess.Board) -> np.ndarray:
    bitmap = bitboard(board)
    return bitmap if board.turn else np.flip(bitmap, axis=range(bitmap.ndim - 1)) * -1


def print_bitboard(bitmap: np.ndarray) -> str:
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        print(bitmap[:, :, piece_idx], chess.piece_name(piece_type), end="\n\n")


if __name__ == "__main__":
    print_bitboard(bitboard(chess.Board(chess.STARTING_FEN)))
