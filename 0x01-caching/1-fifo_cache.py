#!/usr/bin/python3
"""Fifo"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """First in first out"""

    def __init__(self):
        """initilisation"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first, _ = self.cache_data.popitem(False)
            print("DISCARD:", first)

        def get(self, key):
            """retrieve"""
            return self.cache_data.get(key, None)
