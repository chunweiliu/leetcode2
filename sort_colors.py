"""Sort 0, 1, 2

    partition, Dutch flag

Time: O(n)
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        small = mid = 0
        large = len(nums) - 1
        
        while mid <= large:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] < 1:
                swap(nums, small, mid)
                small += 1
                mid += 1
            else:
                swap(nums, mid, large)
                large -= 1                


def partition(nums, k):
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    small = 0
    large = k - 1
    lower = mid = 0
    upper = len(nums) - 1
    
    while small <= large:
        while mid <= upper:
            if nums[mid] == small:
                swap(nums, lower, mid)
                lower += 1
                mid += 1
            elif nums[mid] == large:
                swap(nums, mid, upper)
                upper -= 1            
            else:
                mid += 1

        small += 1
        large -= 1
        mid = lower

    return nums

nums = [0, 1, 2, 3, 4, 5, 3, 2, 1, 0]
k = 6
print partition(nums, k)
