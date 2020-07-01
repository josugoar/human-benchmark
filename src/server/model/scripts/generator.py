from typing import Iterator, Tuple, Union

import chess
import numpy as np
from chess import engine, pgn

from .utils import bitboard, score


def generator(file: Union[str, bytes, int], command: str) -> Tuple[str, int]:
    simple_engine = engine.SimpleEngine.popen_uci(command)
    with open(file) as f:
        while True:
            game = pgn.read_game(f)
            if not game:
                break
            mainline = game.mainline()
            if mainline:
                board = np.random.choice(list(mainline)).board()
                yield bitboard(board.board_fen()), score(simple_engine.analyse(board, engine.Limit()))
