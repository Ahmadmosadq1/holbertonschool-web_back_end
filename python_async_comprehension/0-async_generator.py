#!/usr/bin/env python3
''' Description: Writing a coroutine called async_generator that takes no
'''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generator that yields a random value between 0 and 10 every second,
        10 times. '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()