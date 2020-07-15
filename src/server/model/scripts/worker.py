# pylint: disable=import-error

import asyncio
import glob
import pathlib
import random
from os import path
from typing import Callable, Union

import chess
import numpy as np
from chess import engine, pgn

from utils import bitboard, moves, synchronize, tanh

path_: Callable[[str], str] = lambda p, /: path.join(
    path.dirname(path.realpath(__file__)), p
)


async def worker(file: Union[str, bytes, int], /, *, checkpoint: int = None) -> None:
    kwds = {"X": [], "y_1": [], "y_2": []}
    _, uci_protocol = await engine.popen_uci(path_("../lib/stockfish/stockfish"))
    with open(file) as f:
        savez = lambda: np.savez(path_(f"../data/npz/{pathlib.PurePath(f).stem}"), **kwds)
        while True:
            try:
                play_result = await uci_protocol.play(
                    board := random.choice(tuple(pgn.read_game(f).mainline())).board(),
                    limit=engine.Limit(time=.1),
                    info=engine.INFO_SCORE
                )
            except AttributeError:
                break
            try:
                X, y_1, y_2 = (
                    bitboard(board, dtype=int),
                    moves.index((play_result.move if board.turn else chess.Move(
                        *(len(chess.SQUARES) - np.array((
                            play_result.move.from_square,
                            play_result.move.to_square
                        )) - 1), promotion=play_result.move.promotion
                    )).uci()),
                    tanh(play_result.info["score"].relative.score(mate_score=7625), k=.0025)
                )
            except (AttributeError, IndexError, ValueError):
                pass
            else:
                kwds["X"].append(X), kwds["y_1"].append(y_1), kwds["y_2"].append(y_2)
                if checkpoint and not len(X) % checkpoint:
                    savez()
        savez()
        await uci_protocol.quit()


async def main() -> None:
    semaphore = asyncio.Semaphore(value=3)
    await asyncio.gather(*(
        synchronize(semaphore)(worker)(
            file, checkpoint=10000
        ) for file in glob.glob(path_("../data/*.pgn"))
    ))


if __name__ == "__main__":
    asyncio.set_event_loop_policy(engine.EventLoopPolicy())
    asyncio.run(main())
