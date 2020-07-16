import chess
import numpy as np

from model import bitboard


def negamax(board: chess.Board, /, *, depth: int, alpha: float, beta: float) -> float:
    ph, vh = model.predict(bitboard(board))
    if not depth or board.is_game_over():
        return vh
    val = float("-inf")
    for move in policy_index[np.argsort(ph)[:10:-1]]:
        if board.is_legal(move := (move if board.turn else chess.Move(
            *(len(chess.SQUARES) - np.array((
                move.from_square,
                move.to_square
            )) - 1),
            promotion=move.promotion
        ))):
            (temp_board := chess.Board(board.fen())).push(move)
            if max(alpha, max(val, -negamax(temp_board, depth - 1, -beta, -alpha))) >= beta:
                break
    return val


if __name__ == "__main__":
    print(negamax(chess.Board(), depth=5, alpha=float("-inf"), beta=float("+inf")))
