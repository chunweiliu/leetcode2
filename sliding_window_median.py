"""Find medium in a sliding window in fly.

    - Min-Max queues approach for finding medium for data stream

        min heap has a larger half
        max heap has a smaller half

        * How to remove an element from heap, if it is not in sliding window?

    - Keep the sliding window sorted

        Time: O(nk + klogk) not O(nklogk) because the rest opperation is inserting
              an element to a sorted array

Time: O(nk)
Space: O(1)
"""
from bisect import insort

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        k = min(k, len(nums))
        nums = map(float, nums)

        window = sorted(nums[:k])

        m = k / 2
        def median(window):
            if k % 2 == 1:
                return window[m]
            return 0.5 * (window[m - 1] + window[m])

        ret = []
        for i, tail in enumerate(nums[k:]):
            ret.append(median(window))

            window.remove(nums[i])
            insort(window, tail)

        # Include the last tail, which just be added into the window
        ret.append(median(window))

        return ret
