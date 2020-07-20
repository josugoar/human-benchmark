#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# pylint: disable=import-error

import argparse
from typing import Any, MutableMapping

from command import parser

Namespace = MutableMapping[str, Any]


def compile(model: "keras.Model", argv: Namespace) -> None:
    save = argv.pop("save")
    weights = argv.pop("weights")
    model.compile(**argv)
    if weights:
        model.save_weights(weights)
    else:
        model.save(save)


def fit(model: "keras.Model", argv: Namespace) -> None:
    save = argv.pop("save")
    weights = argv.pop("weights")
    model.fit(verbose=argv.pop("verbose"), **argv)
    if weights:
        model.save_weights(weights)
    else:
        model.save(save)


def predict(model: "keras.Model", argv: Namespace) -> None:
    ph, vh = model.predict(verbose=argv.pop("verbose"), **argv)
    print(ph, vh)


def main(argv: Namespace) -> None:
    from tensorflow import keras
    from tensorflow.keras import models
    load = argv.pop("load")
    if argv["weights"]:
        model = get_model()
        model.load_weights(load)
    else:
        model = models.load_model(load)
    if argv.pop("summary"):
        model.summary()
    globals()[argv.pop("command")](model, argv)


if __name__ == "__main__":
    main(vars(parser.parse_args()))
