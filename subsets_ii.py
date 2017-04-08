"""Return all subsets, avoid duplications

    << [1, 2, 2]
    => [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    
    1) Append the new element to all current subsets.
       If duplicate found, only append the new element to the last created subset.

       []  [1]  [1, 2]    [1, 2, 2]
       ----------------------------
       []  []     []          []
           [1]    [1]         [1]
                  [2]    >    [2]
                  [1, 2] >    [1, 2]
                              ------
                              [2, 2]
                              [1, 2, 2]

                      []
             []                   [1]                clone and add 1
         []     [2]         [1]       [1, 2]         clone and add 2
      [] [3] [2] [2, 3]  [1] [1, 3][1, 2][1, 2, 3]   clone and add 3

    2) Tree

               []
             / | \
          [1] [2] [3]
         / \   |
       [2] [3] [3]
      /
    [3]

Time: O(2^n)
Space: O(n)
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start, attemp):
            # The depth of helper is equal to size of the subset.
            # For example, nums = [1, 2, 3], in the first call,
            # subset [1], [2], [3] will be iterated. And in the second call,
            # we try to append avaiable nubmers of these attemp subset, which are
            # [1, 2], [1, 3], [2, 3], and so on
            for i in range(start, len(nums)):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                
                attemp.append(nums[i])
                subsets.append(attemp[:])
                helper(i + 1, attemp)
                attemp.pop()
        
        nums = sorted(nums)
            
        subsets = [[]]
        helper(0, [])
        return subsets
            