"""
Questions:

Example:
    ['a', 'b', 'a', 'c', 'd', 'a', 'a']
      0    1    2    3    4    5    6

      a a
    -1 -1
      0 2
      2 5
      5 6

      a c
    -1 -1
      0-1
      0 3
      5 3
      6 3

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = len(words)

        index1 = index2 = -1
        for i, word in enumerate(words):
            if word == word1 == word2:
                index1 = index2
                index2 = i
            elif word == word1:
                index1 = i
            elif word == word2:
                index2 = i

            if index1 >= 0 and index2 >= 0:
                distance = min(distance, abs(index1 - index2))

        return distance
