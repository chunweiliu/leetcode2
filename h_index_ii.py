"""Compute h-index (max h, such that at least h papers have been sited h times)

    << [0, 1, 3, 5, 6]
    
    => 3

    first last
     n-f  n-l  n-l-1 ... 0

Time: O(log n)
Space: O(1)
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        n = len(citations)
        first, last = 0, n - 1
        
        while first + 1 < last:
            m = (first + last) / 2
            
            if citations[m] > n - m:
                last = m
            else:
                first = m
                
        if citations[first] >= n - first:
            return n - first
        
        if citations[last] >= n - last:
            return n - last
        
        return n - last - 1