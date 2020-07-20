import argparse

parser = argparse.ArgumentParser(
    prog="model",
    description=None,
    epilog=None
)  # TODO: argparse.FileType
parser.add_argument(
    "--version",
    action="version",
    help="show program version and exit",
    version="%(prog)s 1.0.0"
)  # TODO: version

subparsers = parser.add_subparsers(
    description=None,
    help=None,
    dest="command",
    required=True
)

from .parsers import *
