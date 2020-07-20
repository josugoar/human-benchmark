import argparse
import warnings
from typing import Callable, Optional, Union


class OptionStringHelpFormatter(argparse.HelpFormatter):

    def _format_action_invocation(self, action: argparse.Action):
        if action.nargs and action.option_strings:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return f"{', '.join(action.option_strings)} {args_string}"


def formatter_factory(formatter: argparse.HelpFormatter, /, **kwargs: Optional[int]) -> Union[
    Callable[[str], argparse.HelpFormatter], argparse.HelpFormatter
]:
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
