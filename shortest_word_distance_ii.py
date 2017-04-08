"""
Questions:
    - Optimize in terms of time or space?
        => It has to be O(log n) or O(1) time in query
        - The prepare time could be O(n)

Time: 
    - O(n) init, O(i1 + i2) look up
Space: O(n)
"""
from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.index = defaultdict(list)

        for i, word in enumerate(words):
            self.index[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = self.index[word1], self.index[word2]

        # O(i1 + i2) You don't need to compute a1 with [b2, c2, ...]
        # since they lead to a larger difference
        # i1: [a1, b1, c1, ...]
        # i2: [a2, b2, c2, ...]
        min_distance = abs(index1[0] - index2[0])

        i = j = 0
        while i < len(index1) and j < len(index2):            
            min_distance = min(min_distance, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1

        return min_distance


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")