"""Generate all subsets

    << [1, 2, 3]
    => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2, 3], [1, 3], [1, 2, 3]]


                          []
             []                   [1]                clone and add 1
         []     [2]         [1]       [1, 2]         clone and add 2
      [] [3] [2] [2, 3]  [1] [1, 3][1, 2][1, 2, 3]   clone and add 3    

Time: O(2 ^ n)
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start, attemp):
            for i in range(start, len(nums)):
                # Pick this
                attemp.append(nums[i])

                # In Python, we have to make a copy to save the current attemp.
                # Otherwise, every attemp will be the same [] instance due to
                # the pop() in the end.
                results.append(attemp[:])

                # Recursively do for the rest
                helper(i + 1, attemp)

                # No pick this
                attemp.pop()

        # Initial with the [] element
        results = [[]]
        helper(0, [])
        return results