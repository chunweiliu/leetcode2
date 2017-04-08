class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        Find if a string can be composed by magazine.
        """

        from collections import Counter
        # Words and counts that appear in ransom note but not in the magazine.
        return not(Counter(ransomNote) - Counter(magazine))
