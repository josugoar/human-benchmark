# pylint: disable=import-error

import glob
import pathlib
from os import path

from typing import Callable

import numpy as np
from chess import pgn

from utils import bitboard

dir_path: Callable[[str], str] = lambda p: path.join(
    path.dirname(path.realpath(__file__)), p
)


def worker(path: pathlib.PurePath, *, checkpoint: int = 10000) -> None:
    kwds = {"X": [], "y": []}
    with open(path) as f:
        i = 0
        save_checkpoint = lambda: np.savez(
            dir_path(f"../data/test/{path.stem}"), **kwds
        )
        while True:
            game = pgn.read_game(f)
            if not game:
                break
            mainline = game.mainline()
            result = game.headers["Result"]
            if mainline:
                board = np.random.choice(list(mainline)).board()
                kwds["X"].append(
                    bitboard(board)
                ),
                kwds["y"].append(
                    1 if result == "1-0" else -1 if result == "0-1" else 0
                )
                i += 1
                if i % checkpoint == 0:
                    save_checkpoint()
    save_checkpoint()


def main() -> None:
    for file in glob.glob(dir_path("../data/*.pgn")):
        worker(pathlib.PurePath(file))


if __name__ == "__main__":
    main()
