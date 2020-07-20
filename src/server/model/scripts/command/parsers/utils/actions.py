import argparse
from typing import Any, Sequence


class BoundedCountAction(argparse._CountAction):

    def __init__(self, choices: Sequence[int], *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.choices = choices

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Sequence[Any],
        option_string: str = None
    ):
        parser._check_value(self, getattr(namespace, self.dest, self.default) + 1)
        super().__call__(parser, namespace, values, option_string=option_string)
