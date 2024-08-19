#!/usr/bin/env python3
"""hypermedia"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
    start_point = (page - 1) * page_size
    end_point = start_point + page_size
    return (start_point, end_point)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_point, end_point = index_range(page, page_size)
        data = self.__dataset()
        if start_point > len(data):
            return []
        return data[start_point:end_point]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get information"""
        data_on_page = self.get_page(page, page_size)
        start_point, end_point = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_information = {
            "page_size": len(data_on_page),
            "page": page,
            "data": data_on_page
            "next_page": page + 1 if end_point < len(self.__dataset) else None,
            "prev_page": page - 1 if start_point > 0 else None,
            "total_pages": total_pages
        }
        return page_information
