import random

import chess
from chess import pgn
from stockfish import Stockfish

pgn_path = "src/server/model/data/2019.pgn"
fen_path = "src/server/model/data/2019.fen"

stockfish = Stockfish(
    "src/server/model/utils/stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64_modern.exe")

with open(pgn_path, "r") as pgn_file, open(fen_path, "w") as fen_file:
    i = 0
    while True:
        try:
            i += 1
            for choice in random.sample(list(pgn.read_game(pgn_file).mainline()), 10):
                fen = choice.board().fen()
                stockfish.set_fen_position(fen)
                evaluation = stockfish.get_evaluation()
                if evaluation["type"] == "cp":
                    fen_file.write(f"{fen}, {str(evaluation['value'])}\n")
            if i >= 100:
                break
        except:
            pass
