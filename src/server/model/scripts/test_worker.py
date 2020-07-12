# pylint: disable=import-error

import asyncio
import glob
import pathlib
import random
from os import path
from typing import Callable, Mapping

import chess
import numpy as np
from chess import engine, pgn

from utils import bitboard, moves, tanh, to_categorical

dir_path: Callable[[str], str] = lambda p: path.join(
    path.dirname(path.realpath(__file__)), p
)


async def worker(path: pathlib.PurePath, /, semaphore: asyncio.Semaphore, *, checkpoint: int = 10000) -> Mapping[str, list]:
    async with semaphore:
        kwds = dict(X=[], y_1=[], y_2=[])
        # _, simple_engine = await engine.popen_uci(
        #     dir_path("../lib/stockfish/stockfish")
        # )
        with open(path) as f:
            i = 0
            save_checkpoint = lambda: np.savez(
                dir_path(f"../data/npz/test/{path.stem}"),
                **kwds
            )
            while True:
                if not (game := pgn.read_game(f)):
                    break
                try:
                    game_node = random.choice(list(game.mainline()))
                    X = bitboard(
                        game_node.parent.board(),
                        dtype=int
                    )
                    y_1 = moves.index(
                        (chess.Move(
                            len(chess.SQUARES) - game_node.move.from_square - 1,
                            len(chess.SQUARES) - game_node.move.to_square - 1,
                            promotion=game_node.move.promotion,
                            drop=game_node.move.drop
                        ) if game_node.board().turn else game_node).uci()
                    )
                    # y_2 = tanh(
                    #     (await simple_engine.analyse(
                    #         game_node.board(),
                    #         engine.Limit(time=0.1)
                    #     ))["score"].relative.score(mate_score=7625),
                    #     k=0.0025
                    # )
                except (AttributeError, IndexError, ValueError):
                    pass
                else:
                    kwds["X"].append(X)
                    kwds["y_1"].append(y_1)
                    # kwds["y_2"].append(y_2)
                    i += 1
                    if i % checkpoint == 0:
                        save_checkpoint()
        # await simple_engine.quit()
        save_checkpoint()
        return kwds


async def main() -> None:
    semaphore = asyncio.Semaphore(3)
    await asyncio.gather(*(
        asyncio.ensure_future(
            worker(
                pathlib.PurePath(file),
                semaphore
            )
        ) for file in glob.glob(
            dir_path("../data/*.pgn")
        )
    ))


if __name__ == "__main__":
    # asyncio.set_event_loop_policy(
    #     engine.EventLoopPolicy()
    # )
    asyncio.run(
        main()
    )
