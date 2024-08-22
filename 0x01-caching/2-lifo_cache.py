#!/usr/bin/env python3
"""LIFO algo in python"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """last in first out"""

    def __init__(self):
        """initilisation"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add item"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last, _ = self.cache_data.popitem(True)
                print("DISCARD:", last)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """retrieve item"""
        return self.cache_data(key, None)
