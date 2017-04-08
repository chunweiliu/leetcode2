"""Search the index range for a target

    Binary search with different comparison function and differnt ending conditions

Time: O(log n)
Space: O(1)
"""
import operator


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Question:
            * What should we return if target was not found?

        Exaxmple:
            nums, target = [1, 2, 2, 2, 4, 5, 7], 2

            Bug:
            nums, target = [1, 2, 3], 1
            nums, target = [1, 2, 2], 2
        """
        return [self.search_first(nums, target), self.search_last(nums, target)]

    def search_first(self, nums, target):
        if not nums:
            return -1

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            if nums[mid] < target:
                first = mid
            else:
                last = mid

        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1

    def search_last(self, nums, target):
        if not nums:
            return -1

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            if nums[mid] <= target:
                first = mid
            else:
                last = mid

        if nums[last] == target:
            return last
        if nums[first] == target:
            return first
        return -1

nums, target = [1, 2, 2], 2
print Solution().searchRange(nums, target)