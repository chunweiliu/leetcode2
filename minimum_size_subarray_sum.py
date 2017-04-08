"""
Questions:
    - Does the array have negative integers?
    - Does the array sorted?

Examples:
    [2, 3, 1, 4, 3], s = 7

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Sliding window data structure
        left = right = sum_up = 0

        i = 0
        for j, num in enumerate(nums, 1):
            sum_up += num

            # If the current window is valid,
            while i < j and sum_up >= s:
                # Try to preserve it.
                if not right or j - i < right - left:
                    left, right = i, j
                    
                # And shrink the window.
                sum_up -= nums[i]
                i += 1

        return right - left

s = 4
nums = [1, 4, 4]
print Solution().minSubArrayLen(s, nums)