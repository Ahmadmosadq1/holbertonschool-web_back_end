#!/usr/bin/env python3
"""Task#8. Complex types - functions"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """funcion takes multiplyers as a function"""
    def multiply(x: float) -> float:
        """multiplier function"""
        return x * multiplier
    return multiply
