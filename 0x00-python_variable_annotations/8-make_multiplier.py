#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates and returns a function that multiplies a float
    by the given multiplier."""
    return lambda x: x * multiplier

