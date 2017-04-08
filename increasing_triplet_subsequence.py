"""Return True if existed a triplet (a, b, c) with a < b < c.

    << [1, 2, 3, 4, 5]
    => True
    
    << [5, 4, 3, 2, 1]
    => False
    
    << [1, 4, 3, 2, 5]
    => True
    
    << []
    => False
    
    Similar to Longest Increasing Subsequence (LIS)
    Waterflow check
    
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        smallest = second_smallest = max(nums)

        for num in nums:
            if num <= smallest:
                smallest = num
                
            # num > smallest
            elif num <= second_smallest:
                second_smallest = num
                
            # num > second_smallest > smallest
            else:
                return True

        return False