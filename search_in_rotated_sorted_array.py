"""Find a target in rotated list with binary search

    Example
       [4, 5, 6, 7, 0, 1, 2], find 3
       [0, 1, 2, 4, 5, 6, 7], find 3
       [6, 7, 0, 1, 2, 4, 5], find 0

    Edge cases
       nums, target = [1, 3], 1
       nums, target = [1, 3], 3
       nums, target = [1, 3, 5], 5

    Our goal is to eliminate half numbers at a time

    * Does the array have duplicates?
    * What if we cannot find the target?

Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int           .
        """
        if not nums:
            return -1

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            # Only assert the target in normal order side
            if nums[first] < nums[mid]:
                if nums[first] <= target <= nums[mid]:
                    last = mid
                else:
                    first = mid
            else:
                if nums[mid] <= target <= nums[last]:
                    first = mid
                else:
                    last = mid

        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1
