"""Find the maximum subsequence in an array, such that adjacent numbers not included

    Either rob ith house or not

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        skip_last = 0
        not_skip_last = 0

        for num in nums:
            value = max(skip_last + num, not_skip_last)
            skip_last, not_skip_last = not_skip_last, value

        return max(skip_last, not_skip_last)
