#!/usr/bin/env python3
"""
module that houses a function that takes no arguments.

It will collect 10 random numbers using
an async comprehensing over async_generator,
then return the 10 random numbers.
"""


import asyncio
import importlib as imp


async_genr_mod = imp.import_module('0-async_generator')
async_generator = async_genr_mod.async_generator


async def async_comprehension():
    """
    function that takes no arguments.
    then uses async comprehensing over
    async_generator,then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
