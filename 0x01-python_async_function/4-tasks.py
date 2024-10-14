#!/usr/bin/env python3
"""
"""


import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns
    list of completed delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
