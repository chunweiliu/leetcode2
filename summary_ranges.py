"""Summary ranges

    << [0, 1, 2, 4, 5, 7]
    => ["0->2","4->5","7"]

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        def format(left, right):
            if left != right:
                return str(left)
            return '->'.join(map(str, [left, right]))

        summary = []

        left = right = nums[1]
        for num in nums[1:]:
            if num - right == 1:
                right = num
            else:
                summary += format(left, right),
                left = right = num

        summary += format(left, right),

        return summary
