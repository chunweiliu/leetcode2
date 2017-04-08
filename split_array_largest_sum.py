"""Write an algorithm to "minimize" the largest sum among these m subarrays.

   Binary search a target on the solution space [max(nums), sum(nums)].
   The maximum sum among a valid_split split array has to be smaller than the target.

Time: O(nlog s)
Space: O(1)
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Every split sum should smaller than or equal to target.
        # If the split is fewer than m, it's fine. We can split the current
        # one finer and get another valid split.
        def valid_split(nums, m, target):
            split_sum = 0
            split = 1
            for num in nums:
                split_sum += num                
                
                if split_sum > target:
                    split_sum = num
                    split += 1
                
                    if split > m:
                        return False
            return True

        first, last = max(nums), sum(nums)

        while first + 1 < last:
            mid = (first + last) / 2

            # To minimize the sum, a valid split mean we can find a finer split
            # for a smaller value
            if valid_split(nums, m, mid):
                last = mid
            else:
                first = mid

        if valid_split(nums, m, first):
            return first
        return last
