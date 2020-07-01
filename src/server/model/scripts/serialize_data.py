import asyncio
import random
from glob import glob
from os import path
from pathlib import PurePath
from typing import Iterator, Tuple, Union

import aiofiles
from chess import engine, pgn

# SERIALIZE IN NUMPY ARRAYS!!!!


async def serialize_data(input_path: Union[str, bytes, int], output_path: Union[str, bytes, int], command: str = "stockfish") -> Iterator[Tuple[str, str]]:
    _, stockfish = await engine.popen_uci(command)
    async with aiofiles.open(output_path, "w") as output_file:
        with open(input_path) as input_file:
            while True:
                game = pgn.read_game(input_file)
                if not game:
                    break
                mainline = game.mainline()
                if mainline:
                    board = random.choice(list(mainline)).board()
                    fen, info = board.board_fen(), await stockfish.analyse(board, engine.Limit())
                    await output_file.write(f"{fen},{info['score']}" + "\n")
    await stockfish.quit()


async def main() -> None:
    dir_path = path.dirname(path.realpath(__file__))
    input_suffix, output_suffix = ".pgn", ".txt"
    await asyncio.gather(
        *[serialize_data(input_path,
                         path.join(output_path, PurePath(
                             input_path).with_suffix(output_suffix).name),
                         command=path.join(dir_path, "../lib/stockfish-11-win/Windows/stockfish_20011801_x64_modern.exe"))
          for output_path in glob(path.join(dir_path, "../data/*/"))
          for input_path in glob(path.join(dir_path, f"../data/*{input_suffix}"))])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(engine.EventLoopPolicy())
    asyncio.run(main())
