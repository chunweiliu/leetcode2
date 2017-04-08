"""Find the product of maximum product subarray

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.

    One pass, for each number, consider if we want the current * all preivous or 
    the current only. Store both the max and min products.

            2 * 3 * 0 * -2 * -2 
        min 2   3   0   -2   -2
        max 2   6   0    0    4
    
    Similar to maximum_subarray

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_overall = max_product = min_product = nums[0]

        for num in nums[1:]:
            # Make the comparison eaiser
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            max_overall = max(max_overall, max_product)

        return max_overall



