"""Find the max product of two words that not sharing any letter

    << ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    >> "ab" x "cd"
    => 4

    1) Using set to represent each word:
        - Each O(n) => O(n^3) in total

    2) Using bits to represent each word:
        - Each O(1) => O(n^2) in total

Time: O(n^2)
Space: O()
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Use 26 bits to represent each word
        # 000...000
        # zyx...cba
        bits = [0] * len(words)

        for i, word in enumerate(words):
            for char in word:
                bits[i] |= 1 << ord(char) - ord('a')

        product = 0
        
        for i, s in enumerate(bits):
            for j, t in enumerate(bits):
                if s & t == 0:
                    product = max(product, len(words[i]) * len(words[j]))
        
        return product
        
    def max_product_tle(self, words):
        max_product = 0

        word_sets = map(set, words)

        for word, word_set in zip(words, word_sets):
            for j in range(len(words)):
                if not(word_set & word_sets[j]):
                    max_product = max(max_product, 
                                      len(word) * len(words[j]))

        return max_product
