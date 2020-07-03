# pylint: disable=import-error,no-member

import asyncio
import glob
import pathlib
from os import path

import aiofiles
import numpy as np
from chess import engine, pgn
from scipy import special

from utils import bitboard

dir_path = lambda p: path.join(
    path.dirname(path.realpath(__file__)), p
)


async def worker(path: pathlib.PurePath, *, checkpoint: int = 10000):

    def save_checkpoint():
        np.savez(
            dir_path(f"../data/npz/{path.stem}"),
            **kwds
        )

    kwds = {"X": [], "y": []}
    _, simple_engine = await engine.popen_uci(
        dir_path("../lib/stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64_modern")
    )
    async with aiofiles.open(path) as f:
        i = 0
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
                    special.expit(
                        (await simple_engine.analyse(
                            board,
                            engine.Limit(depth=15)
                        ))["score"].relative.score(mate_score=32768) / 100
                    )
                )
                i += 1
                if i % checkpoint == 0:
                    save_checkpoint()
    await simple_engine.quit()
    save_checkpoint()


async def main():
    await asyncio.gather(*[
        worker(pathlib.PurePath(file))
        for file in glob.glob(
            dir_path("../data/*.pgn")
        )
    ])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(
        engine.EventLoopPolicy()
    )
    asyncio.run(
        main(),
    )
