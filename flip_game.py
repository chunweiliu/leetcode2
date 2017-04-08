"""Genearte all possible moves for the next player in flip game

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []

        prev = None
        for i, c in enumerate(s):
            if prev == c == '+':
                ret.append(s[:i-1] + '--' + s[i+1:])
            prev = c

        return ret
        