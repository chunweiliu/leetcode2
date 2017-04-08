"""Pick the index of the target. Randomly (uniformly) return one if duplicated.

    << [1, 1, 2, 3, 1], target = 1
    => 0|1|4

Reservoir Sampling:

    Pick the ith line with the probability 1/i.
    
    For example, given a stream data [1, 2, 3…]

    Pick 1: 1 * 1/2 * 2/3 = 0.3333 (pick first * not be replaced by 2 * not be replaced by 3)
    Pick 2: 1/2 * 2/3 = 0.3333 (pick second * not be replaced by 3)
    Pick 3: with 1/3 = 0.3333 

Require Space O(1). The intuition behinds this is for stream data.

Time: O(n)
Space: O(1)
"""
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        keep, seen = None, 0

        for i, num in enumerate(self.nums):
            if num == target:
                seen += 1
                if random.randrange(seen) == 0:
                    keep = i

        return keep


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)