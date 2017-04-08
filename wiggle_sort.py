"""Sort an array in place, such that

    a0 <= a1 >= a2 <= a3 >= a4 ...
    --------
          --------
                --------
                      --------

    << [3, 5, 2, 1, 6, 4]
    => [1, 6, 2, 5, 3, 4]

    Check neighbor using rules alternatively

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums[1:], 1):
            if i % 2 == 1:
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                if nums[i-1] < nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]   

# nums = [1,3,4,2]
# Solution().wiggleSort(nums)
# print nums