class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Question:
            * Any duplicates?

        Example:
            nums = [1, 3, 5], target = 0
        """
        if not nums:
            return -1

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            if nums[mid] <= target:
                first = mid
            else:
                last = mid

        if nums[first] == target:
            return first
        if nums[last] == target:
            return last

        # [x, first, x, last, x]
        if target < nums[first]:
            return first
        if target < nums[last]:
            return last
        return last + 1
