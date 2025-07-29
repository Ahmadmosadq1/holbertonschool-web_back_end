#!/usr/bin/env python3
"""Task#7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    return (k, (v ** 2))
