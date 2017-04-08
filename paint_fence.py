"""Ways of painting a fence with n posts and k colors. 
   No more than two adjacent fence posts have the same color.


   Assume we know the preivous two groups same (oo) and diff (ox).
   What will the two variables update for the third input?   

   1) same
        ooo (invalid)
        oxx (x)

   2) diff
        ook (anything but o)
        oxk  (anything but x)
   
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0

        if n <= 0:
            return 0
            
        if n == 1:
            return k

        same = k
        diff = k * (k - 1)

        for i in range(2, n):
            same, diff = same * 0 + diff * 1, same * (k - 1) + diff * (k - 1)

        return same + diff
