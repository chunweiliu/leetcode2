"""K largest numbers in an array

	<< [3, 1, 2, 5, 4, 9, 4, 2], k = 3
    => 9, 5, 4

- Heap
Time: O(n + klogn)
Space: O(k)

- Quick Select
Time: O(n + n) in average
Space: O(1)
"""
import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, first, last):
            pivot = nums[random.randrange(first, last + 1)]

            bottom, middle, upper = first, first, last
            while middle <= upper:
                if nums[middle] > pivot:
                    nums[bottom], nums[middle] = nums[middle], nums[bottom]
                    bottom += 1
                    middle += 1
                elif nums[middle] == pivot:
                    middle += 1
                else:
                    nums[middle], nums[upper] = nums[upper], nums[middle]
                    upper -= 1

            return bottom

        first, last = 0, len(nums) - 1

        while first + 1 < last:
            pivot_index = partition(nums, first, last)

            if pivot_index < k:
                first = pivot_index + 1
            else:
                last = pivot_index - 1

        if nums[first] < nums[last]:
            nums[first], nums[last] = nums[last], nums[first]

        return nums[k - 1]

nums = [1, 2, 3, 4, 5]
k = 2
print Solution().findKthLargest(nums, k)


