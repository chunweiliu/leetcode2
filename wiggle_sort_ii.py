"""Given an unsorted array nums, 
   reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

    Example:
    (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
    (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

    - Sort

      Put the smaller half in even index, and larger index in odd index

      Time: O(nlogn)
      Space: O(n)

    - Partion

    * Assume there must be an answer
    * The equal is not allow, nums[0] < nums[1] > nums[2] < nums[3] ...,
      local pair comparison information is not enough

        index:     0  1  2  3  4    5  6  7  8  9
        number:   18 17 19 16 15   11 14 10 13 12
        new_index: 1  3  5  7  9    0  2  4  6  8

        After partion, we know the first half are going to > median
        But the first half now point to 1, 3, 5, 7, 9

Time: O(n)
Space: O(1)
"""
import random


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        median = self.find_kth(nums, len(nums) / 2)

        # Given a partion array, do a partion again
        # map [0, 1, 2, 3, 4, 5]
        # to  [1, 3, 5, 0, 2, 4]
        #      ^^^^^^^
        #      the first half will satisify "> pivot"
        self.partition(nums, 0, len(nums) - 1, median, lambda i: (1 + 2 * i) % (len(nums) | 1))
        
    def partition(self, nums, first, last, pivot, index):
        bottom, middle, upper = first, first, last
        while middle <= upper:
            if nums[index(middle)] > pivot:
                nums[index(bottom)], nums[index(middle)] = nums[index(middle)], nums[index(bottom)]
                bottom += 1
                middle += 1
            elif nums[index(middle)] == pivot:
                middle += 1
            else:
                nums[index(middle)], nums[index(upper)] = nums[index(upper)], nums[index(middle)]
                upper -= 1
        return bottom

    def find_kth(self, nums, k):
        first, last = 0, len(nums) - 1
        while first + 1 < last:
            pivot = nums[random.randrange(first, last + 1)]
            sorted_element = self.partition(nums, first, last, pivot, lambda x: x)
            if sorted_element < k:
                first = sorted_element + 1
            else:
                last = sorted_element - 1

        if nums[first] < nums[last]:
            nums[first], nums[last] = nums[last], nums[first]

        return nums[k - 1]