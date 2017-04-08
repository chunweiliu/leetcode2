"""Binary search for bad version

    << [0, 1, 2, 3, 4, 5, 6]
        g  g  b  b  b  b  b

    => 2

    - Is all bad versions grouping together?
    - What if we don't have bad version?

Time: O(log n)
Space: O(1)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n
        while first + 1 < last:
            mid = (first + last) / 2

            if isBadVersion(mid):
                last = mid
            else:
                first = mid
        
        if isBadVersion(first):
            return first
        if isBadVersion(last):
            return last