#!/usr/bin/env python3
""" Coroutine at the same time witha sync """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waiting for run delay until max_delay, returns list of actual delays """
    spawn = []
    delay = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay.append(x.result()))
        spawn.append(delayed_task)

    for spawn in spawn:
        await spawn

    return delay