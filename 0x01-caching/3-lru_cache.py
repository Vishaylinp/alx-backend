#!/usr/bin/env python3
"""Least Recently used caching method
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class for Least recently used
    """

    def __init__(self):
        """initialisation
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add items
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
