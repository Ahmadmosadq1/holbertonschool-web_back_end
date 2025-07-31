#!/usr/bin/env python3
import asyncio

# import wait_random from "0-basic_async_syntax.py"
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that will run wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
