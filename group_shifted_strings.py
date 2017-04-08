"""Group strings that has the same pattern

    - Permute 26 times for each word, and match the other to the subset

    Time: O(nk)
    Space: O(n)

    - Compute word difference list string as a key

    * mod 26 for key

    Time: O(nk)
    Space: O(n)


"""
from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ret = defaultdict(list)

        for s in strings:
            key = str([(ord(c) - ord(s[0])) % 26 for c in s])
            ret[key].append(s)

        return ret.values()

        