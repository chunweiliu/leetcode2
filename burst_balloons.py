class Solution(object):
    def maxCoins(self, nums):
        """
        Assume the last ballon is C. Then coin gain of the last step is 1 * C * 1.
        The max gains for the previous step would be the max gain for [A B] and [D E F G]

            (1 A B C D E F G 1)
        i - 1  i   k       j  j + 1           

        max_coins[i][j]: max coins for bursting all ballons in (i, j).
        max_coins[i][j] = max(
            max_coins[i][j],
            nums[i - 1] * nums[k] * nums[j + 1] + max_coins[i][k - 1] + max_coins[k + 1][j]

        Update order:
          0 1 2 3
        0 a e h j
        1   b f i
        2     c g
        3       d

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = [1] + nums + [1]
        max_coins = [[0] * len(nums) for _ in range(len(nums))]

        for size in range(2, len(nums)):
            # (left, right)
            for left in range(len(nums) - size):
                right = left + size
                for last in range(left + 1, right):
                    max_coins[left][right] = max(
                        max_coins[left][right],
                        nums[left] * nums[last] * nums[right] + max_coins[left][last] + max_coins[last][right])

        return max_coins[0][len(nums) - 1]

    def maxCoins_fail(self, nums):
        """
        This fail because the order we updated the DP table is wrong.
        max_coins[1][n] has to be the last one to update.
        https://www.youtube.com/watch?v=IFNibRVgFBo
        """
        if not nums:
            return 0

        num_length = len(nums)

        nums = [1] + nums + [1]
        max_coins = [[0] * len(nums) for _ in range(len(nums))]

        for left, _ in enumerate(nums[1:-1], 1):
            for right, _ in enumerate(nums[1:-1], 1):
                for last in range(left, right + 1):
                    max_coins[left][right] = max(
                        max_coins[left][right],
                        nums[left - 1] * nums[last] * nums[right + 1] + max_coins[left][last - 1] + max_coins[last + 1][right])                

        for row in max_coins:
            print row

        return max_coins[1][num_length]

nums = [3, 1, 5, 8]
print Solution().maxCoins(nums)