"""Longest increasing substring

    << [5, 4, 1, 2, 3]
    => 3
    
    << ''
    => 0
    
    << [1, 3, 6, 7, 9, 4, 10, 5, 6]
    => 6
    
- DP
    
    LIS[i] = 1 + max(LIS[j] for j < i and nums[j] < nums[i])

Time: O(n^2)
Space: O(n)

- Binary Search

    Maintain an array to store the last element of 
    the LIS with the smallest last element.
    
    Use binary search to update the array, for example, when we meet 6 in the following
    
    [1, 3, 5, 2, 8, 4, 6]
    
    We have
    
    1 = [1]
    2 = [1, 2]
    3 = [1, 3, 4]
    4 = [1, 3, 5, 6]
    
    (a) We can either add a number, for 9
    
    1 = [1]              
    2 = [1, 2]
    3 = [1, 3, 4]
    4 = [1, 3, 5, 6]      
    5 = [1, 3, 5, 6, 9*]
    
    (b) Update an exist number, for 0
    
    1 = [0*]              
    2 = [1, 2]
    3 = [1, 3, 4]
    4 = [1, 3, 5, 6]
    
    (c) Update an exist number in the middle, for 3
    
    1 = [0]
    2 = [1, 2]
    3 = [1, 3, 3*]
    4 = [1, 3, 5, 6]    
    
Time: O(nlogn)
Space: O(n)
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0

        tails = [0] * len(nums)
        
        for num in nums:
            i, j = 0, length
            while i < j:
                m = (i + j) / 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            
            # (1) if x is larger than all tails, append it, increase the size by 1
            # (2) if tails[i-1] < x <= tails[i], update tails[i]
            tails[i] = num
            length = max(i + 1, length) # Change index to length
            
        return length
            
    def lengthOfLIS_square(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        LIS = [1] * len(nums)
        
        for i, num in enumerate(nums):
            candidates = [1 + LIS[j] for j in range(i) if nums[j] < num]
            if candidates:
                LIS[i] = max(candidates)
                   
        return LIS[-1]

nums = [2, 2]
print Solution().lengthOfLIS(nums)