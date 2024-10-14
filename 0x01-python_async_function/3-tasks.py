#!/usr/bin/env python3
"""
"""


import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.
    Task for wait_random with max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
