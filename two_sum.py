"""Two sum

    * Not include self
        [0, 1, 0], 0 => (0, 2)
        [3, 2, 4], 6 => (1, 2)

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}

        for i, num in enumerate(nums):
            lookup = target - num

            if lookup in index:
                return [index[lookup], i]

            index[num] = i
