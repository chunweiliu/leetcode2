"""Return a list of missing range given lower and upper bound

    For example, given [0, 1, 3, 50, 75],                        
    lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

    * Add lower - 1 and upper + 1 to the given number!
    [-1, 0, 1, 3, 50, 75, 100]

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.append(upper + 1)
        # We never include prev in the answer, we use prev + 1.
        # So this will cover lower, if lower not in the range.
        prev = lower - 1

        missing = []
        
        for num in nums:
            if num - prev == 1:
                pass
            elif num - prev == 2:
                missing.append(str(num - 1))
            elif num - prev > 2:
                missing.append('->'.join([str(prev + 1), str(num - 1)]))
            prev = num

        return missing

# nums = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print Solution().findMissingRanges(nums, lower, upper)