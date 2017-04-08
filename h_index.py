"""Compute h-index (max h, such that at least h papers have been sited h times)

    << [3, 0, 6, 1, 5]
    
    => 3

Time: O(n log n)
Space: O(1)
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        
        citations.sort()
        
        for c in reversed(citations):
            if c > h:
                h += 1
                
        return h
        