#!/usr/bin/env python3
"""
module that houses a function that calculate
the time taken to execute wait_n
"""


import time
import asyncio
import importlib


concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    for wait_n(n, max_delay),
    and returns total_time / n.
    """

    start_time = time.time()  # Record start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # Record end time

    total_time = end_time - start_time  # Calculate the total time
    return total_time / n  # Return average time per task
