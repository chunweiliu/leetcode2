"""Seperate the string with dash, join them with following rules
    - first group has least number
    - every other group has to have k number

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = [str.upper(str(c)) for c in S if c != '-']
        
        ret = ''
        for i, c in enumerate(reversed(s)):
            if i and i % K == 0:
                ret += '-'
            ret += c

        return ret[::-1]
