import argparse

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

from .compile_parser import *
from .fit_parser import *
from .predict_parser import *
