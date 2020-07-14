# pylint: disable=import-error

import asyncio
import glob
import pathlib
import random
from os import path
from typing import Callable, List, Tuple

import chess
import numpy as np
from chess import engine, pgn

from utils import bitboard, moves, synchronize, tanh

path_: Callable[[str], str] = lambda p, /: path.join(
    path.dirname(path.realpath(__file__)), p
)


async def worker(file: pathlib.PurePath, /, *, checkpoint: int = None) -> Tuple[
    List[np.ndarray], List[int], List[float]
]:
    X, y_1, y_2 = [], [], []
    _, uci_protocol = await engine.popen_uci(
        path_("../lib/stockfish/stockfish")
    )
    with open(file) as f:
        while True:
            try:
                play_result = await uci_protocol.play(
                    board := random.choice(tuple(pgn.read_game(f).mainline())[:-1]).board(),
                    limit=engine.Limit(time=.1),
                    info=engine.INFO_SCORE
                )
                XX, yy_1, yy_2 = (
                    bitboard(
                        board,
                        dtype=int
                    ),
                    moves.index(
                        (chess.Move(
                            *(len(chess.SQUARES) - np.array((
                                play_result.move.from_square,
                                play_result.move.to_square
                            )) - 1),
                            promotion=play_result.move.promotion
                        ) if board.turn else play_result.move).uci()
                    ),
                    tanh(
                        play_result.info["score"].relative.score(
                            mate_score=7625
                        ),
                        k=.0025
                    )
                )
            except AttributeError:
                break
            except (IndexError, ValueError):
                pass
            else:
                X.append(XX), y_1.append(yy_1), y_2.append(yy_2)
                if checkpoint and not len(X) % checkpoint:
                    np.savez(
                        path_(f"../data/npz/temp/{file.stem}"),
                        X=X, y_1=y_1, y_2=y_2
                    )
        await uci_protocol.quit()
        np.savez(
            path_(f"../data/npz/{file.stem}"),
            X=X, y_1=y_1, y_2=y_2
        )
        return X, y_1, y_2


async def main() -> None:
    semaphore = asyncio.Semaphore(value=3)
    await asyncio.gather(*(
        asyncio.ensure_future(
            synchronize(semaphore)(worker)(
                pathlib.PurePath(file),
                checkpoint=10000
            )
        ) for file in glob.glob(path_("../data/*.pgn"))
    ))


if __name__ == "__main__":
    asyncio.set_event_loop_policy(
        engine.EventLoopPolicy()
    )
    asyncio.run(
        main()
    )
