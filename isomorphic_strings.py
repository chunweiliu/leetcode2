"""One to one mapping for two string

    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    - alpha mapping

        * ab -> aa
            One mapping function is not good enough

    - index mapping (check if the last index is in the same possition)

        * ab -> aa
        * ab -> ca



Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        seen_s, seen_t = defaultdict(int), defaultdict(int)
        # In order to distinguish not seen, which return 0 in lookup, start indexing from 1
        for i, (ss, tt) in enumerate(zip(s, t), 1):
            if seen_s[ss] != seen_t[tt]:
                return False

            seen_s[ss] = i
            seen_t[tt] = i

        return True

    def isIsomorphicDict(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        forward, backward = {}, {}
        for ss, tt in zip(s, t):
            if ss not in forward and tt not in backward:
                forward[ss] = tt
                backward[tt] = ss
            elif ss in forward and tt in backward:
                if forward[ss] != tt or backward[tt] != ss:
                    return False
            else:
                return False

        return True

