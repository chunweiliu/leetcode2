"""Maximum length of the subarray that sum to k

    << [-2, -1, 2, 1], k = 1
    => 2    ^^^^^
    
    << [-2, -1, 2, 1], k = 2
    => 3    ^^^^^^^^
        -2  -3 -1  0
            |------|
                   0 - 2 = 2
         
    1. Compute a running 1d sums in a dict {sum: left most index}
    2. Look back the left most target (sum - k) index to find a max size subarray
    
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = 0

        running_sum = 0
        # Integral image, you have to pad an element in the front.
        index = {running_sum: 0}
        
        for i, num in enumerate(nums, 1):
            running_sum += num
                
            target = running_sum - k
            
            if target in index:
                length = max(length, i - index[target])                

            if running_sum not in index:
                index[running_sum] = i
            
                
        return length
        
nums = [-2, -1, 2, 1]
k = 0
print Solution().maxSubArrayLen(nums, k)