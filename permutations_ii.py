"""Permute a list of numbers with duplicated numbers

    [1,1,2] have the following unique permutations:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

    - Use a set
    - Sort and not repeat permutation

Time: O(n!)
Space: O(n!)
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums):
            if not nums:
                return [[]]

            prev = None
            ret = []
            for i, num in enumerate(nums):
                if prev != num:
                    for permutation in helper(nums[:i] + nums[i + 1:]):
                        ret.append([num] + permutation)
                prev = num
            return ret

        return helper(sorted(nums))
