class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Assume:
        1. No empty nums
        2. Always have a solution

        Only two kinds of element: majority and others.
          3, 0, 0, 1, 2, 0
        c 1, 1, 2, 1, 1, 1
        n 3, 0, 0, 0, 2, 0
        """
        count = 1
        majority = nums[0]
        for num in nums[1:]:
            if num == majority:
                count += 1
            else:
                count -= 1

            if count == 0:
                majority = num
                count = 1

        return majority

        