from .. import subparsers
from . import load_mixin, save_mixin, weights_mixin
from .utils import OptionStringHelpFormatter, formatter_factory

compile_parser = subparsers.add_parser(
    "compile",
    description="configure the model for training",
    formatter_class=formatter_factory(
        OptionStringHelpFormatter,
        max_help_position=30
    )
)

compile_mixins = {
    weights_mixin: {},
    load_mixin: {},
    save_mixin: {
        "required": True
    }
}
for mixin, kwargs in compile_mixins.items():
    mixin(compile_parser, **kwargs)

compile_group = compile_parser.add_argument_group(
    "compilation parameters"
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
