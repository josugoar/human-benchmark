import argparse

parser = argparse.ArgumentParser(
    prog="model",
    description="powered by TensorFlow",
    epilog="<https://github.com/JoshGoA>"
)
parser.add_argument(
    "--version",
    action="version",
    help="show program version and exit",
    version="%(prog)s 1.0.0"
)
parser.add_argument(
    "--summary",
    action="store_true",
    help="print a string summary of the network and exit"
)
parser.add_argument(
    "--plot",
    help="convert the model to dot format and save to a file",
    metavar="<file>"
)

subparsers = parser.add_subparsers(
    dest="command"
)

from .parsers import *
