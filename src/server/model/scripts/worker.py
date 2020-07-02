# pylint: disable=import-error

import asyncio
from os import path

import aiofiles
import numpy as np
from chess import engine, pgn

from utils import bitboard


async def main():
    kwds = {"X": [], "y": []}
    _, simple_engine = await engine.popen_uci(
        dir_path("../lib/stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64_modern")
    )
    async with aiofiles.open(
        dir_path("../data/ficsgamesdb_2019_standard2000_nomovetimes.pgn")
    ) as f:
        while True:
            game = pgn.read_game(f._file)
            if not game:
                break
            mainline = game.mainline()
            if mainline:
                board = np.random.choice(list(mainline)).board()
                kwds["X"].append(
                    bitboard(board.board_fen())
                ),
                kwds["y"].append(
                    (await simple_engine.analyse(
                        board,
                        engine.Limit()
                    ))["score"].relative.score(mate_score=256)
                )
    await simple_engine.quit()
    np.savez(dir_path("../data/raw/data"), **kwds)


dir_path = lambda p: path.join(
    path.dirname(path.realpath(__file__)),
    p
)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(engine.EventLoopPolicy())
    asyncio.run(main())
