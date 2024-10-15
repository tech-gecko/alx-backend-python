#!/usr/bin/env python3
"""This module imports "wait_n" from 1-concurrent_coroutines.py and contains a
function called "measure_time" that takes in 2 int arguments, n and max_delay.
measure_time will measure the total execution time for wait_n(n, max_delay) and
would return the total time divided by n (the average delay)."""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n."""
    start_time = time.perf_counter()
    await wait_n(n=n, max_delay=max_delay)
    total_time = time.perf_counter() - start_time

    return total_time / n  # Returns average delay.
