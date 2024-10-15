#!/usr/bin/env python3
"""This module imports "wait_random" from 0-basic_async_syntax.py and contains
a function called "task_wait_random" that takes an integer max_delay and
returns a 'asyncio.Task' object."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a 'asyncio.Task' object."""
    task = asyncio.create_task(wait_random(max_delay=max_delay))

    return task
