#!/usr/bin/env python3
"""Fifo Alogo in python"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """First in first out"""

    def __init__(self):
        """initilisation"""

        super().__init__()

    def put(self, key, item):
        """add item"""

        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            first_in = next(iter(self.cache_data))
            del self.cache_data[first_in]
            print("DISCARD: {}".format(first))

        self.cache_data[key] = item

        def get(self, key):
            """retrieve it"""
            if key is None or key not in self.cache_data:
                return None
            return self.cache_data.get(key)
