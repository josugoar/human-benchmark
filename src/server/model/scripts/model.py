#!/usr/bin/env python

# pylint: disable=import-error

import argparse

from command import parser


def main(argv: argparse.Namespace):
    print(argv)


if __name__ == "__main__":
    main(parser.parse_args())
