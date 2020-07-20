import argparse
import warnings
from typing import Callable, Optional, Union


def formatter_factory(formatter: argparse.HelpFormatter, /, **kwargs: Optional[int]) -> Union[Callable[[str], argparse.HelpFormatter], argparse.HelpFormatter]:
    try:
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        warnings.warn(
            """
            Only the name of this class is considered a public API.
            All the methods provided by the class are considered an implementation detail.
            """
        )
        return formatter
