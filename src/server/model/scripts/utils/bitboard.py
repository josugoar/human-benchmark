import chess
import numpy as np


def bitboard(board: chess.Board = chess.Board(), /) -> np.ndarray:
    bitboard = np.zeros(
        (len(chess.FILE_NAMES), len(chess.RANK_NAMES), len(chess.PIECE_TYPES)), dtype=int
    )
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type is piece_type:
                bitboard[
                    chess.square_rank(square),
                    chess.square_file(square),
                    piece_idx
                ] = 1 if piece.color else -1
    return bitboard if board.turn else -np.flip(bitboard, axis=range(2))
