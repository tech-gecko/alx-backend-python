#!/usr/bin/env python3
"""This module imports "wait_random" from 0-basic_async_syntax.py and contains
an async routine called "wait_n" that takes in 2 int arguments (in this order):
n and max_delay. wait_n will spawn wait_random n times with the specified
max_delay. wait_n would return the list of all the delays (float values).
The list of the delays would be in ascending order."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns "wait_random" n times with the specified max_delay. Returns the
    list of all the delays (float values). The list of the delays would be in
    ascending order."""
    # Create a list of awaitable coroutines
    coroutines = [wait_random(max_delay) for _ in range(n)]

    # Gather the results concurrently.
    delays = await asyncio.gather(*coroutines)

    # Sort the delays list after all delays are gathered
    return sorted(delays)
