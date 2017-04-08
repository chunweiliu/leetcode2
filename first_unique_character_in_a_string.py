class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        'leetcode' -> return 0
        """
        from collections import Counter
        char_counts = Counter(s)

        # Iterate through the original string. No need OrderedDict.
        for i, c in enumerate(s):
            if char_counts[c] == 1:
                return i

        return -1
