#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page of data starting from `index`.

        Returns a dict containing:
          - index: starting index requested
          - next_index: index to use for the next page request
          - page_size: number of items actually returned
          - data: list of rows
        """
        assert (
            isinstance(index, int) and index >= 0
        ), "index must be a non-negative integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be a positive integer"

        total_len = len(self.dataset())
        assert index < total_len, "index out of range"

        indexed = self.indexed_dataset()

        data: List[List] = []
        i = index
        while len(data) < page_size and i < total_len:
            if i in indexed:
                data.append(indexed[i])
            i += 1

        next_index = i
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
