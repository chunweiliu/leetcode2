"""Figure out if two string has edit distance exactly one.

     ababb
     ab bb

     => True
    
     abbabb
     abbabc

     => True

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False

        if abs(len(s) - len(t)) > 1:
            return False

        # Make sure s > t.
        if len(s) < len(t):
            s, t = t, s

        # Find the indices that different to each other.
        i = 0
        while i < len(s) and i < len(t) and s[i] == t[i]:
            i += 1

        # Replacement of t
        if len(s) == len(t):
            return s[i + 1:] == t[i + 1:]
        # Insertion of t
        else:
            return s[i + 1:] == t[i:]

