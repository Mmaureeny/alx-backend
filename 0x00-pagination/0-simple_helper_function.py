#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple

def index_range(page, page_size):
    """Fetches the index range from a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
