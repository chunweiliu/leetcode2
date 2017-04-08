"""Find how many way we can evaluate a list to a target

    - without memo
        Time: O(2^n)
        Space: O(1)

    - with memo
        Time: O(ns)
        Space: O(ns)
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def helper(i, attemp):
            # Add these for memo
            key = str(i) + '#' + str(attemp)
            if key in memo:
                return memo[key]

            # No need to add these in memo, otherwise the memory usage is huge.
            if i == len(nums):
                return 0

            ret = 0
            if attemp == S and i == len(nums) - 1:
                ret += 1
            else:
                ret += helper(i + 1, attemp + nums[i]) + helper(i + 1, attemp - nums[i])

            # Add these for memo
            memo[key] = ret
            return memo[key]
            
        if not nums:
            return 0

        memo = {}
        return helper(-1, 0)
        