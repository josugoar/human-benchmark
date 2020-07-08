# pylint: disable=import-error,no-name-in-module

import chess
import numpy as np

from scripts.utils import bitboard


def minimax(board: chess.Board, depth: int, maximize: bool, alpha: float, beta: float) -> float:
    max_depth = 5
    if depth < max_depth and board.legal_moves.count():
        if maximize:
            min_max = max
            alpha_beta = alpha
            best_val = float("-inf")
        else:
            min_max = min
            alpha_beta = beta
            best_val = float("+inf")
        for move in board.legal_moves:
            temp_board = chess.Board(board.fen())
            temp_board.push(move)
            value = minimax(temp_board, depth + 1, not maximize, alpha, beta)
            best_val = min_max(best_val, value)
            if maximize:
                alpha = min_max(alpha_beta, best_val)
            else:
                beta = min_max(alpha_beta, best_val)
            if beta <= alpha:
                break
        return best_val
    return model.predict(bitboard(board))


if __name__ == "__main__":
    value = minimax(chess.Board(chess.STARTING_FEN), 0, True, float('-inf'), float('+inf'))
    print(f"The optimal value is: {value}")
