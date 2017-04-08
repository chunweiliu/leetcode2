class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Question:
            * Do we have duplicates?
            * Empty nums?

        Example:
            [4, 5, 6, 7, 0, 1, 2]
            [7, 0, 1, 2, 3, 4, 5]
        """
        if not nums:
            return nums

        first, last = 0, len(nums) - 1
        while first + 1 < last:
            mid = (first + last) / 2

            #            9
            #          8   <--- top middle
            #        7         
            #      6
            #    5
            #  4
            # -0-1-2-3-4-5-6-7-8-9- [index] in array  
            #                    3
            #                  2
            #                1   <--- bottom middle
            #              0
            # The following statement is sufficient 
            # due to the array is ascending.
            # if nums[mid] > nums[last]:
            if nums[first] < nums[mid] > nums[last]:
                first = mid
            else:
                last = mid

        return min(nums[first], nums[last])

nums = [4, 5, 6, 7, 0, 1, 2]
print Solution().findMin(nums)