"""Merge two sorted array, from nums2 to nums1

    << [], [1]
    => [1]

Bugs:
    - start from m - 1 and n - 1
    - the last index is m + n + 1
    - empty nums1 case

Time: O(m + n)
Space: O(1)
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        
        while n >= 0:
            if m < 0 or nums1[m] < nums2[n]:
                nums1[m + n + 1] = nums2[n]
                n -= 1
            else:
                nums1[m + n + 1] = nums1[m]
                m -= 1
        