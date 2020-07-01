import asyncio
import random
from os import path
from typing import Tuple

import aiofiles
import chess
from chess import engine, pgn


async def main() -> None:

    # Move to file
    def evaluate(info: dict) -> int:
        """Transform game analisis parameters to filtered evaluation.

        Args:
            info (dict): Game analisis parameters

        Returns:
            int: Filtered evaluation
        """
        return info["score"]

    dir_path = path.join(path.dirname(path.realpath(__file__)))

    pgn_path = path.join(dir_path, "../data/2019.pgn")
    fen_path = path.join(dir_path, "../data/2019.fen")

    _, stockfish = await engine.popen_uci(
        path.join(dir_path, "../lib/stockfish-11-win/Windows/stockfish_20011801_x64_modern.exe"))

    async with aiofiles.open(fen_path, "w") as fen_file:
        with open(pgn_path) as pgn_file:
            while True:
                game = pgn.read_game(pgn_file)
                if game:
                    mainline = game.mainline()
                    if mainline:
                        board = random.choice(list(mainline)).board()
                        fen, info = board.fen(), await stockfish.analyse(board, engine.Limit())
                        await fen_file.write(f"{fen}, {evaluate(info)}\n")
                else:
                    break

    await stockfish.quit()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(engine.EventLoopPolicy())
    asyncio.run(main())
