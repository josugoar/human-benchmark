from .. import subparsers
from . import parent_parser

compile_parser = subparsers.add_parser(
    "compile",
    description="configure the model for training",
    parents=(parent_parser,)
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
