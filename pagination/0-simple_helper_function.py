#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that takes page number and page size and return the
    start and end indexes

     Args:
         page (int): Page number.
         page_size (int): Page size

     Returns:
         tuple: size two tuple of start and end indexes.

     Raises:
         ErrorType: Condition under which the error is raised.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
