"""Implement Least Recently Use Cache. If the number of key reaches the cache's
   capacity, delete the LRU element and insert the new one.

   old <--------------> new

   pop(key, last=False) will give us an FIFO OrderedDict pop

Time: O(1)
Space: O(n)
"""

from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        cache = self.cache

        if key not in cache:
            return -1

        value = cache.pop(key)
        cache[key] = value

        return value
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        cache = self.cache

        # Update the key order if the key existed
        if key in cache:
            cache.pop(key)
        else:
            if len(cache) == self.capacity:
                # FIFO
                cache.popitem(last=False)

        cache[key] = value
