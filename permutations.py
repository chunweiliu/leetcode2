"""Permute a list of distinct numbers

    [1,2,3] have the following permutations:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

    Treat each digit as a head prepend over the permutations of the rest numbers

T(n) = n * T(n-1)
Time: O(n!)
Space: O(n!)
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        ret = []
        for i, num in enumerate(nums):
            for permutation in self.permute(nums[:i] + nums[i + 1:]):
                ret.append([num] + permutation)

        return ret
