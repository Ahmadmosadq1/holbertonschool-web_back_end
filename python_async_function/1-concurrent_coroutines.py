#!/usr/bin/env python3
import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    Return the list of delays in ascending order without using sort().
    """  
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Execute all tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays