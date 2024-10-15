#!/usr/bin/env python3
"""
module that houses a python asynchronous
function that creates an asyncio task for
wait_random with max_delay
"""


import asyncio
import importlib


basic_asyn = importlib.import_module('0-basic_async_syntax')
wait_random = basic_asyn.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.
    Task for wait_random with max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
