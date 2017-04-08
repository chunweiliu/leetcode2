"""Find the contiguous subarray that has max sum

    [-2,1,-3,4,-1,2,1,-5,4]
    => 6, for [4,-1,2,1]

    - O(n^3) brute force sum for nums[i:j] for i and j
    - O(n^2) brute force check S[i:j] for i and j, where S[i] is an array of sum(nums[:i])
    - O(n) one pass, just add up and see what's going on

      for each position, either add the num to the previous balance
      or start a new count from that number      

    similar to maximum_product_subarray

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_overall = max_included_last = nums[0]

        for num in nums[1:]:
            max_included_last = max(max_included_last + num, num)
            max_overall = max(max_overall, max_included_last)

        return max_overall
        