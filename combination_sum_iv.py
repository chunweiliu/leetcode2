"""
Ways of combination to a target
    
    If we have nums = [1, 2, 3], target = 4
    comb[4] = comb[3] (if 1 existed) + comb[2] (if 2 existed) comb[1] (if 3 existed)
    
Time: O(nt)
Space: O(t) for input target
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ways = [0] * (1 + target)
        
        # serve as the base, so every remain 0 is a way
        ways[0] = 1
        
        for t in range(1, len(ways)):
            for num in nums:
                remain = t - num

                # Note that we just check ways[remain], it is not guarantee to
                # find a ways to reach the remain.
                if remain >= 0:
                    ways[t] += ways[remain]

        return ways[target]                    
                
                