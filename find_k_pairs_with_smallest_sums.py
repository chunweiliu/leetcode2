"""Find smallest sum for k pairs

    Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

    Return: [1,2],[1,4],[1,6]

    The first 3 pairs are returned from the sequence:
    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

    * Two pointers not work, because you can go back and use a previous number
        nums1 1 7 11 16
        nums2 2 9 10 15
        => (1, 2), (7, 2), (1, 9)

      0 1 2 3 ...
    0 
    1
    2
    3

Time: O(klogk)
Space: O(k)
"""
from heapq import *


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []

        n = min(len(nums1), k)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(n)]
        heapify(heap)

        ret = []
        while k and heap:
            _, i, j = heappop(heap)
            ret.append([nums1[i], nums2[j]])

            j += 1
            if j < len(nums2):
                heappush(heap, (nums1[i] + nums2[j], i, j))
            k -= 1

        return ret
