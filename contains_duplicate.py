class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Another 1-liner
        # return len(nums) != len(set(nums))

        from collections import Counter
        return any(value > 1 for value in Counter(nums).values())
        