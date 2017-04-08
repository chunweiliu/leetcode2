"""Use counter as a hash key

Time: O(nm), where n is number of strings, m is the lenght of string
Space: O(m)
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def counter(chars):
            counts = [0] * 26
            for char in chars:
                counts[ord(char) - ord('a')] += 1
            return str(counts)

        group = defaultdict(list)

        for chars in strs:
            group[counter(chars)].append(chars)

        return [anagrams for anagrams in group.values()]        

