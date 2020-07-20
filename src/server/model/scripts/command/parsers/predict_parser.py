import argparse

from .. import subparsers
from .utils import BoundedCountAction, formatter_factory

predict_parser = subparsers.add_parser(
    "predict",
    description="generates output predictions for the input samples",
    formatter_class=formatter_factory(
        argparse.HelpFormatter,
        max_help_position=50
    )
)
predict_parser.add_argument(
    "x",
    nargs="+",
    # type=lambda string: bitboard(chess.Board(string)),
    help="input samples",
    metavar="<fen>"
)
predict_parser.add_argument(
    "-v", "--verbose",
    action=BoundedCountAction,
    default=0,
    choices=range(1, 2),
    help="increase output verbosity"
)

predict_group = predict_parser.add_argument_group(
    "predict parameters"
)
predict_group.add_argument(
    "--batch-size",
    default=32,
    type=int,
    help="number of samples per batch",
    metavar="<int>"
)
