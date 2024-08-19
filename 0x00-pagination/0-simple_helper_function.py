#!/usr/bin/env python3
"""range of index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
    start_point = (page - 1) * page_size
    end_point = start_point + page_size
    return (start_point, end_point)
