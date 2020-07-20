import argparse

parent_parser = argparse.ArgumentParser(
    add_help=False
)
parent_parser.add_argument(
    "-l", "--load",
    help="load model from path",
    metavar="<path>"
)
parent_parser.add_argument(
    "-s", "--save",
    required=True,
    help="save model to path",
    metavar="<path>"
)
parent_parser.add_argument(
    "-w", "--weights",
    action="store_true",
    help="load/save model weights"
)

from .compile_parser import *
from .fit_parser import *
from .predict_parser import *
