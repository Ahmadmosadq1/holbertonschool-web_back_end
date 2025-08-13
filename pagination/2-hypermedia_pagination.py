#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        A function that takes page number and page size and return the
        start and end indexes

        Args:
            page (int): Page number.
            page_size (int): Page size

        Returns:
            tuple: size two tuple of start and end indexes.

        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        finding a page
        """
        assert isinstance(page, int) and page > 0, "Page is greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "size < 0"
        try:
            data = self.dataset()
            start_index, end_index = self.index_range(page, page_size)
            return data[start_index:end_index]
        except Exception as e:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        A function for hypermedia pagination.

        Args:
            page (int): Page number.
            page_size (int): Page size

        Returns:
            tuple: size two tuple of start and end indexes.
        """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
