"""Return the length of the longest consecutive sequence
    
    << [100, 4, 200, 1, 3, 2]
    => 4
    
    for [1, 2, 3, 4]
    
    Only check the start of the consecutive sequence. 
    For above example, we only check the set for 100, 200, and 1.
    
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 1
        
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                next_consecutive_num = num + 1
                while next_consecutive_num in nums:
                    next_consecutive_num += 1
                    
                # Not include current since it is not in nums
                length = max(length, next_consecutive_num - num)
                
        return length
        
        