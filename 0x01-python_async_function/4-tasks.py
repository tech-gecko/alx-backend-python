#!/usr/bin/env python3
""" The code is nearly identical to wait_n
except task_wait_random is being called."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ The code is nearly identical to wait_n
    except task_wait_random is being called."""
    # Create a list of awaitable coroutines
    coroutines = [task_wait_random(max_delay=max_delay) for _ in range(n)]

    # Gather the results concurrently.
    delays = await asyncio.gather(*coroutines)

    # Sort the delays list after all delays are gathered
    return sorted(delays)
