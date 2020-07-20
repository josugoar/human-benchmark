import argparse

from .version import __version__

parser = argparse.ArgumentParser(
    prog="model",
    description="Powered by TensorFlow",
    epilog="<https://github.com/JoshGoA>"
)
parser.add_argument(
    "--summary",
    action="store_true",
    help="print a string summary of the network"
)
parser.add_argument(
    "--version",
    action="version",
    help="show program version and exit",
    version=f"%(prog)s {__version__}"
)

subparsers = parser.add_subparsers(
    dest="command"
)

from .parsers import *
