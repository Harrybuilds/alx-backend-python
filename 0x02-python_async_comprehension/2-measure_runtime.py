#!/usr/bin/env python3
"""
a module that houses a coroutine that
will execute async_comprehension four times
in parallel using asyncio.gather.

the coroutine should measure the total runtime
and return it.
"""


import asyncio
import time
import importlib as imp


async_comp_mod = imp.import_module('1-async_comprehension')
async_comprehension = async_comp_mod.async_comprehension


async def measure_runtime():
    """
    a coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.

    the coroutine should measure the total runtime and
    return it.
    """
    start_time = time.perf_counter()  # Start measuring time

    # Run 4 instances of async_comprehension in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # Stop measuring time

    return end_time - start_time  # Return the total runtime
