"""Find all (a, b, c) such that a + b + c == 0

    << [-2, -1, 0, 1, 1, 2]
    => [(-2, 0, 2), (-2, 1, 1), (-1, 0, 1)]

    - Are these numbers sorted?
    - Does duplicate exist?

Time: O(n^2)
Space: O(1)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i and num == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            
            while j < k:
                t = num, nums[j], nums[k]

                if sum(t) == 0:
                    results.append(t)
                    j += 1
                    k -= 1

                    # Skip the same results. Because the num is the same, if we
                    # keep the same second number, we will get the same third
                    # number which makes the tuple duplicated.
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif sum(t) > 0:
                    k -= 1
                else:
                    j += 1

        return results
