"""Valid if a input can form a perfect word square

    [
      "abcd",
      "bnrt",
      "crmy",
      "dtye"
    ]

    => True

    ["ball",
     "asee",
     "let",
     "lep"]

    => False

    ["abcd",
     "bnrt",
     "crm",
     "dt"]

    * zip function only report the intersections
    
Time: O(n^2)
Space: O(1)
"""
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i, word in enumerate(words):
            words[i] = word.ljust(len(words[0]))

        for word, vertical_word in zip(words, zip(*words)):
            if word != ''.join(vertical_word):
                return False

        return True


words = ["abcd","bnrt","crm","dt"]
print Solution().validWordSquare(words)
