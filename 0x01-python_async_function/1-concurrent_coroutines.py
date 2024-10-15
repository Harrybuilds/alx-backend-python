#!/usr/bin/env python3
"""
module that house a function that
returns a list of all the delays
(float values)
"""

import asyncio
import heapq
from typing import List
import importlib


basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    # Use a min-heap to store delays
    heap = []

    # Spawn n tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    for delay in await asyncio.gather(*tasks):
        heapq.heappush(heap, delay)

    # Extract all delays from the heap in sorted order
    while heap:
        delays.append(heapq.heappop(heap))

    return delays
