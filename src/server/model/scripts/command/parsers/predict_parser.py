from .. import subparsers
from .utils import BoundedCountAction

predict_parser = subparsers.add_parser(
    "predict",
    description="generates output predictions for the input samples"
)
predict_parser.add_argument(
    "x",
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
    metavar="<int>",
    dest="batch_size"
)  # TODO: exclusive group (predict/predict_on_batch)
