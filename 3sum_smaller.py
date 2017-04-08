"""Find the number of index triplets (i, j, k), i < j < k, such that
   nums[i] + nums[j] + nums[k] < target

    << [-2, 0, 1, 3], target = 2

    >> [-2, 0, 1], [-2, 0, 3]
    => 2

    * If nums[i] + nums[j] + nums[k] < target, either j += 1 or k -= 1 are answers.
    * The i < j < k condition is useless and also a distraction.

Time: O(n^2)
Space: O(n)
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        
        for i, n in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if n + nums[j] + nums[k] < target:
                    # It is that simple
                    count += (k - j)
                    j += 1
                else:
                    k -= 1

        return count
