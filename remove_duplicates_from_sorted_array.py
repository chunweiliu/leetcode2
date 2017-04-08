"""Remove the duplicate elements.

    Similar to move zeros, but using assignment

    << [1, 1, 2, 2]
           j
    >> [1, 2, 2, 2]
              j
    => 2

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        identical = 1        
        for i, num in enumerate(nums[1:], 1):
            if num != nums[identical-1]:
                nums[identical] = nums[i]
                identical += 1
        return identical
