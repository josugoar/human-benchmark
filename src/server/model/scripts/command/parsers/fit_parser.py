from .. import subparsers
from . import load_mixin, save_mixin, verbose_mixin, weights_mixin
from .utils import OptionStringHelpFormatter, formatter_factory

fit_parser = subparsers.add_parser(
    "fit",
    description="train the model for a fixed number of epochs",
    formatter_class=formatter_factory(
        OptionStringHelpFormatter,
        max_help_position=30
    )
)
fit_parser.add_argument(
    "data",
    nargs="+",
    help="training data",
    metavar="<filename.npz>"
)

fit_mixins = {
    verbose_mixin: {
        "choices": range(1, 3)
    },
    weights_mixin: {},
    load_mixin: {},
    save_mixin: {
        "required": True
    }
}
for mixin, kwargs in fit_mixins.items():
    mixin(fit_parser, **kwargs)

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
    nargs="+",
    help="data on which to evaluate the loss and any model metrics at the end of each epoch",
    metavar="<filename.npz>"
)
validation_group.add_argument(
    "--validation-split",
    default=0.,
    type=float,
    help="fraction of the training data to be used as validation data",
    metavar="<float>"
)
