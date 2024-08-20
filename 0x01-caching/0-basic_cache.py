#!/usr/bin/python3
"""Basic cache"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic cache"""

    def __init__(self):
        """initialisation"""
        super().__init__()

    def put(self, key, item):
        """add an item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieve item"""
        return self.cache_data.get(key, None)
