import argparse

import numpy as np

from .. import subparsers
from . import parent_parser
from .utils import BoundedCountAction, formatter_factory

fit_parser = subparsers.add_parser(
    "fit",
    description="train the model for a fixed number of epochs",
    parents=(parent_parser,),
    formatter_class=formatter_factory(
        argparse.HelpFormatter,
        max_help_position=50
    )
)
fit_parser.add_argument(
    "data",
    nargs="+",
    # type=np.load,
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
    "training parameters"
)
fit_group.add_argument(
    "--batch-size",
    default=32,
    type=int,
    help="number of samples per gradient update",
    metavar="<int>"
)
fit_group.add_argument(
    "--epochs",
    default=1,
    type=int,
    help="number of epochs to train the model",
    metavar="<int>"
)

validation_group = fit_group.add_mutually_exclusive_group()
validation_group.add_argument(
    "--validation-data",
    type=np.load,
    help="data on which to evaluate the loss and any model metrics at the end of each epoch",
    metavar="<filename.npz>"
)
validation_group.add_argument(
    "--validation-split",
    default=0,
    type=float,
    help="fraction of the training data to be used as validation data",
    metavar="<float>"
)
