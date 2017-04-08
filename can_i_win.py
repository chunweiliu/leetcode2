"""Pick a range and a disired number for two players, each one can pick a
   number within the range without replacement. Is the first player always win?

    maxChoosableInteger = 10
    desiredTotal = 11

    => False

    * Is there any benefit for not choosing the max?
    - Yes

Time: O(2^n) with memo, O(n!) without memo
Space: O(2^n) for memo witch number has been used
"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        nums = range(1, maxChoosableInteger + 1)

        if sum(nums) < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True

        def helper(nums, goal):
            # Any string can be a key! Even string like '[1, 2, 3]'
            key = str(nums)
            if key in memo:
                return memo[key]

            if nums[-1] >= goal:
                win = True
            else:
                win = False
                for i, num in enumerate(nums):
                    # We did not pick each number, becaues the recursion call
                    # in take care it for us.
                    
                    # Because each player use the best strategy, you win only if
                    # pick the right number so next one won't win.
                    if not helper(nums[:i] + nums[i + 1:], goal - num):
                        win = True
                        break

            memo[key] = win
            return memo[key]

        memo = {}
        return helper(nums, desiredTotal)