"""
Similar to sliding window approach but don't need to maintain the window.

Questions:
    - This is not hamming distance, right?
    - What if two words are identical?
    - Do you count circularly?
    - Can I assume the answer always exist?

Examples:
    - ["practice", "makes", "perfect", "coding", "makes"]
    => d('coding', 'practice') = 3
    => d('makes', 'coding') = 1

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = len(words)

        index1 = index2 = -1

        for j, word in enumerate(words):
            if word == word1:
                index1 = j
            elif word == word2:
                index2 = j
            
            if index1 >= 0 and index2 >=0:
                distance = min(distance, abs(index1 - index2))

        return distance
