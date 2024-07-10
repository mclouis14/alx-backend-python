#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Asynchronous generator that loops 10 times, waits for 1 second in each
    iteration, and yields a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
