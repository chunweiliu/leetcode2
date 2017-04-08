"""Rearrange a string so similar char has distance k

    str = "aabbcc", k = 3

    Result: "abcabc"

    The same letters are at least distance 3 from each other.

    - Greedy
    * Build a max heap with frequency of each chars.
    * When the heap is not empty
        * Pop the first element in heap, use it.
        * Put the element in the wait queue.
        * If wait queue >= k, means the first element in queue can be used again if its count is not 0

    * Tuple and list cannot compare with each other in heap, pick one!

Similar to task cooldown

Time: O(n)
Space: O(n)
"""
from heapq import *
from collections import Counter
from collections import deque


class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        max_heap = []
        counts = Counter(str)
        for word, count in counts.iteritems():
            max_heap.append((-count, word))

        heapify(max_heap)

        ret = []
        queue = deque()
        while max_heap:
            count, word = heappop(max_heap)

            ret.append(word)

            # +1 for max heap in Python
            queue.append((count + 1, word))
            if len(queue) < k:
                continue

            # See if any word in the wait queue can be placed into max_heap
            c, w = queue.popleft()
            if c < 0:
                # Has to 
                heappush(max_heap, (c, w))

        if len(ret) == len(str):
            return ''.join(ret)
        return ''
