import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Every element appears twice except for one. Find that one.
        Time: O(n)
        Space: O(1)
        """
        return reduce(operator.xor, nums)

print Solution().singleNumber([1, 1, 2])
