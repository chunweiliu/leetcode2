"""Find if an array has duplicate in index i and j, such that abs(i - j) is at most k

    Use a set to save k elements

Time: O(n)
Space: O(k)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        exist = set()
        for num in nums[:k + 1]:
            if num in exist:
                return True

            exist.add(num)

        for i, num in enumerate(nums[k + 1:]):
            exist.remove(nums[i])

            if num in exist:
                return True

            exist.add(num)

        return False

nums = [-1, 2, -1]
k = 0
print Solution().containsNearbyDuplicate(nums, k)
        