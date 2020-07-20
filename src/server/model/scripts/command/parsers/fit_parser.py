from .. import subparsers
from . import parent_parser
from .utils import BoundedCountAction

fit_parser = subparsers.add_parser(
    "fit",
    description="train the model for a fixed number of epochs",
    parents=(parent_parser,)
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
