#!/usr/bin/env python3
"""This module imports "wait_random" from 0-basic_async_syntax.py and writes an
async routine called "wait_n" that takes in 2 int arguments (in this order):
n and max_delay. wait_n will spawn wait_random n times with the specified
max_delay. wait_n would return the list of all the delays (float values).
The list of the delays would be in ascending order."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """Spawns "wait_random" n times with the specified max_delay. Returns the
    list of all the delays (float values). The list of the delays would be in
    ascending order."""
    return_list = []

    for i in range(n):
        delay = await wait_random(max_delay=max_delay)

        inserted = False
        for j in range(len(return_list)):
            if delay < return_list[j]:
                return_list.insert(j, delay)
                inserted = True
                break

        if not inserted:
            return_list.append(delay)

    return return_list
