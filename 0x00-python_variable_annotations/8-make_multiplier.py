#!/usr/bin/env python3
"""Task 8: Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates and returns a multiplier function."""
    return lambda x: x * multiplier
