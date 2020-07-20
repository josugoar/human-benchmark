import argparse
from typing import Any, Callable

from .utils import BoundedCountAction

ParserMixin = Callable[[argparse.ArgumentParser, Any], None]

load_mixin: ParserMixin = lambda parser, /, **kwargs: parser.add_argument(
    "-l", "--load",
    help="load model from path",
    metavar="<path>",
    **kwargs
)

save_mixin: ParserMixin = lambda parser, /, **kwargs: parser.add_argument(
    "-s", "--save",
    help="save model to path",
    metavar="<path>",
    **kwargs
)

verbose_mixin: ParserMixin = lambda parser, /, **kwargs: parser.add_argument(
    "-v", "--verbose",
    action=BoundedCountAction,
    default=0,
    help="increase output verbosity",
    **kwargs
)

weights_mixin: ParserMixin = lambda parser, /, **kwargs: parser.add_argument(
    "-w", "--weights",
    action="store_true",
    help="load/save model weights",
    **kwargs
)

from .compile_parser import *
from .fit_parser import *
from .predict_parser import *
