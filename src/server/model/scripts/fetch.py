# pylint: disable=import-error

import asyncio
import glob
import pathlib
import random
from os import path
from typing import Callable, Optional, Union

import chess
import numpy as np
from chess import engine, pgn

from utils import bitboard, moves, synchronize, tanh

_path: Callable[[str], str] = lambda p, /: path.join(path.dirname(path.realpath(__file__)), p)


async def fetch(file: Union[str, bytes, int], /, *, checkpoint: Optional[int] = None) -> None:
    kwds = {x: [] for x in ("X", "y_1", "y_2")}
    _, uci_protocol = await engine.popen_uci(_path("../lib/stockfish/stockfish"))
    with open(file) as f:
        savez = lambda: np.savez(_path(f"../data/npz/{pathlib.PurePath(f.name).stem}"), **kwds)
        while True:
            try:
                try:
                    play_result = await uci_protocol.play(
                        board := random.choice(tuple(pgn.read_game(f).mainline())).board(),
                        limit=engine.Limit(time=.1),
                        info=engine.INFO_SCORE
                    )
                except AttributeError:
                    break
                for kwd, x in zip(kwds.values(), (
                    bitboard(
                        board,
                        dtype=int
                    ),
                    moves.index(
                        (play_result.move if board.turn else chess.Move(
                            *(len(chess.SQUARES) - np.array((
                                play_result.move.from_square,
                                play_result.move.to_square
                            )) - 1),
                            promotion=play_result.move.promotion
                        )).uci()
                    ),
                    tanh(
                        play_result.info["score"].relative.score(
                            mate_score=7625
                        ),
                        k=.0025
                    )
                )):
                    kwd.append(x)
            except (AttributeError, IndexError, ValueError):
                continue
            if checkpoint and not len(kwds["X"]) % checkpoint:
                savez()
        savez()
        await uci_protocol.quit()


async def main() -> None:
    semaphore = asyncio.Semaphore(value=3)
    await asyncio.gather(*(
        synchronize(semaphore)(fetch)(
            file, checkpoint=10000
        ) for file in glob.glob(_path("../data/*.pgn"))
    ))


if __name__ == "__main__":
    asyncio.set_event_loop_policy(engine.EventLoopPolicy())
    asyncio.run(main())
