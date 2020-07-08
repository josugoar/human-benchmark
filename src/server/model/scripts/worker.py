# pylint: disable=import-error

import asyncio
import glob
import pathlib
import threading
from os import path
from typing import Callable, Mapping

import aiofiles
import numpy as np
from chess import engine, pgn
from utils import bitboard, tanh

dir_path: Callable[[str], str] = lambda p: path.join(
    path.dirname(path.realpath(__file__)), p
)


async def worker(
    path: pathlib.PurePath, semaphore: asyncio.Semaphore, *, checkpoint: int = 10000
) -> Mapping[str, list]:
    async with semaphore:
        kwds = {"X": [], "y": []}
        _, simple_engine = await engine.popen_uci(
            dir_path("../lib/stockfish/stockfish")
        )
        async with aiofiles.open(path) as f:
            i = 0
            save_checkpoint = lambda: np.savez(
                dir_path(f"../data/npz/{path.stem}"), **kwds
            )
            while True:
                game = pgn.read_game(f._file)
                if not game:
                    break
                mainline = game.mainline()
                if mainline:
                    board = np.random.choice(list(mainline)).board()
                    kwds["X"].append(
                        bitboard(board)
                    ),
                    kwds["y"].append(
                        tanh(
                            (await simple_engine.analyse(
                                board,
                                engine.Limit(time=0.1)
                            ))["score"].relative.score(mate_score=32768), k=0.0025)
                    )
                    i += 1
                    if i % checkpoint == 0:
                        save_checkpoint()
        await simple_engine.quit()
        save_checkpoint()
        return kwds


async def main() -> None:
    semaphore = asyncio.Semaphore(3)
    await asyncio.gather(*(
        asyncio.ensure_future(
            worker(pathlib.PurePath(file), semaphore)
        ) for file in glob.glob(
            dir_path("../data/*.pgn")
        )
    ))


if __name__ == "__main__":
    asyncio.set_event_loop_policy(
        engine.EventLoopPolicy()
    )
    asyncio.run(
        main()
    )
