from .. import subparsers
from . import load_mixin, weights_mixin, verbose_mixin
from .utils import OptionStringHelpFormatter, formatter_factory

predict_parser = subparsers.add_parser(
    "predict",
    description="generate output predictions for the input samples",
    formatter_class=formatter_factory(
        OptionStringHelpFormatter,
        max_help_position=30
    )
)
predict_parser.add_argument(
    "x",
    nargs="+",
    help="input samples",
    metavar="<fen>"
)

predict_mixins = {
    verbose_mixin: {
        "choices": range(1, 2)
    },
    weights_mixin: {},
    load_mixin: {
        "required": True
    }
}
for mixin, kwargs in predict_mixins.items():
    mixin(predict_parser, **kwargs)

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
