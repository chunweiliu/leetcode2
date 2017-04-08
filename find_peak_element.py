class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Questions:
            * What if we have multiple peak?
            * Do we have flat area?
            * Any time complexity requirement?

        Example:
            [1, 2, 3, 1, 2, 4, 3]

        Bug:
            [1, 2, 3, 1]

        Binary search. The peak must be on the larger side.
        """
        if not nums:
            return nums

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                first = mid
            else:
                last = mid

        if nums[first] < nums[last]:
            return last
        return first



        