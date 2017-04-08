class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Question:
            * Which index do you want? N/A

        Example:
            [0, 1, 1, 1, 1]
            [1, 1, 1, 0, 1]
        """
        if not nums:
            return nums

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            if nums[mid] == nums[last]:
                last -= 1
            elif nums[mid] < nums[last]:
                last = mid
            else:
                first = mid

        return min(nums[first], nums[last])
        