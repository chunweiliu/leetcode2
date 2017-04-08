"""If a string can be a palindrome after permutations

    "code" -> False, "aab" -> True, "carerac" -> True

    * palindrome has two kinds:
        - odd
        - even

        doen't matter actually...

Time: O(n)
Space: O(n)
"""
from collections import Counter


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = Counter(s)
        odds = sum(1 for c in counts.values() if c % 2 == 1)

        if odds <= 1:
            return True
        return False
