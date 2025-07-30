#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """choosing random numbers and async them"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep
    return delay
