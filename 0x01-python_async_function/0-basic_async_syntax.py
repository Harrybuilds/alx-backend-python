#!/usr/bin/env python3
"""
module that houses a python asynchorous function
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asychronous function that
    generates and returns a
    random number
    """
    # Generate a random delay between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
