import argparse

from .. import subparsers
from . import parent_parser
from .utils import formatter_factory

compile_parser = subparsers.add_parser(
    "compile",
    description="configure the model for training",
    parents=(parent_parser,),
    formatter_class=formatter_factory(
        argparse.HelpFormatter,
        max_help_position=50
    )
)

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
