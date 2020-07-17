import chess
import numpy as np
from chess import engine

# uci_protocol = engine.SimpleEngine.popen_uci("model/lib/stockfish/stockfish")


def negamax(board: chess.Board, /, *, depth: int, alpha: float, beta: float) -> chess.Board:
    if depth and not board.is_game_over():
        best_board, best_score = None, float("-inf")
        for move in board.legal_moves:
            (temp_board := board.copy()).push(move)
            child_board = negamax(
                temp_board,
                depth=depth - 1,
                alpha=-beta,
                beta=-alpha
            )
            analysis_result = uci_protocol.analyse(
                child_board,
                engine.Limit(time=.1),
                info=engine.INFO_SCORE
            )
            if best_score < (child_score := -analysis_result["score"].relative.score(mate_score=7625)):
                best_board, best_score = child_board, child_score
            if max(alpha, best_score) >= beta:
                break
        return best_board
    return board


if __name__ == "__main__":
    best_board = negamax(
        board := chess.Board(),
        depth=2,
        alpha=float("-inf"),
        beta=float("+inf")
    )
    move, *ponder = best_board.move_stack[len(board.move_stack):]
    print(f"{board}\nMove:\t{move}\nPonder:\t{ponder}")
