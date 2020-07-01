import chess
import numpy as np


def bitboard(fen: str) -> np.ndarray:
    board = chess.BaseBoard(fen)
    bitboard = np.zeros((len(chess.FILE_NAMES), len(chess.RANK_NAMES), len(chess.PIECE_TYPES)))
    for piece_idx, piece_type in enumerate(chess.PIECE_TYPES):
        for file_idx in range(len(chess.FILE_NAMES)):
            for rank_idx in range(len(chess.RANK_NAMES)):
                piece = board.piece_at(file_idx * len(chess.RANK_NAMES) + rank_idx)
                if piece and piece.piece_type is piece_type:
                    bitboard[file_idx, rank_idx, piece_idx] = 1 if piece.color is chess.WHITE else -1
    return bitboard


if __name__ == "__main__":

    def print_bitboard(bitmap: np.ndarray) -> str:
        for piece, idx in zip(chess.PIECE_NAMES[1:], range(bitmap.shape[-1])):
            print(bitmap[:, :, idx], piece, end="\n\n")

    print_bitboard(bitboard(chess.STARTING_BOARD_FEN))
