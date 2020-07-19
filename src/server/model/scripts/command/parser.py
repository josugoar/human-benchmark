import argparse
from typing import Callable

from .utils import BoundedCountAction

FormatterFactory = Callable[[str], argparse.HelpFormatter]

formatter: FormatterFactory = lambda prog: argparse.HelpFormatter(
    prog,
    max_help_position=50
)

parser = argparse.ArgumentParser(
    prog="model",
    description=None,
    epilog=None
)  # TODO: argparse.FileType
parser.add_argument(
    "--version",
    action="version",
    help="show program version and exit",
    version="%(prog)s 1.0.0"
)  # TODO: version

subparsers = parser.add_subparsers(
    description=None,
    help=None,
    dest="command",
    required=True
)

parent_parser = argparse.ArgumentParser(
    add_help=False
)
parent_parser.add_argument(
    "-i", "--input",
    help="load model from path",
    metavar="<path>"
)  # TODO: exclusive group (load/load_weights)
parent_parser.add_argument(
    "-o", "--output",
    required=True,
    help="save model to path",
    metavar="<path>"
)  # TODO: exclusive group (save/save_weights)

compile_parser = subparsers.add_parser(
    "compile",
    description="configure the model for training",
    parents=(parent_parser,),
    formatter_class=formatter
)

compile_group = compile_parser.add_argument_group(
    "compile parameters"
)
compile_group.add_argument(
    "--optimizer",
    help="name of optimizer",
    metavar="<optimizer>",
),
compile_group.add_argument(
    "--loss",
    help="name of objective function",
    metavar="<loss>",
),
compile_group.add_argument(
    "--metric",
    action="append",
    help="metric to be evaluated by the model during training and testing",
    metavar="<metric>",
)

fit_parser = subparsers.add_parser(
    "fit",
    description="train the model for a fixed number of epochs",
    parents=(parent_parser,),
    formatter_class=formatter
)
fit_parser.add_argument(
    "data",
    nargs="+",
    help="training data",
    metavar="<filename.npz>"
)
fit_parser.add_argument(
    "-v", "--verbose",
    action=BoundedCountAction,
    default=0,
    choices=range(1, 3),
    help="increase output verbosity"
)

fit_group = fit_parser.add_argument_group(
    "fit parameters"
)
fit_group.add_argument(
    "--batch-size",
    default=32,
    type=int,
    help="number of samples per gradient update",
    metavar="<int>",
    dest="batch_size"
)
fit_group.add_argument(
    "--epochs",
    default=1,
    type=int,
    help="number of epochs to train the model",
    metavar="<int>"
)
fit_group.add_argument(
    "--validation-split",
    default=0,
    type=float,
    help="fraction of the training data to be used as validation data",
    metavar="<float>",
    dest="validation_split"
)  # TODO: Pass validation data separately
fit_group.add_argument(
    "--shuffle",
    action="store_true",
    help="whether to shuffle the training data before each epoch"
)

predict_parser = subparsers.add_parser(
    "predict",
    description="generates output predictions for the input samples",
    formatter_class=formatter
)
predict_parser.add_argument(
    "x",
    help="input samples",
    metavar="<fen>"
),
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
    metavar="<int>",
    dest="batch_size"
)  # TODO: exclusive group (predict/predict_on_batch)
