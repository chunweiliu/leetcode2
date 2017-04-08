"""Given a word list, find all distinct (i, j) such that words[i] + words[j] is palindrome

    - Search each position

      1. Seperate prefix and surfix for a word
      2. check reversed surfix if prefix is a palindrome,
      3. check reversed prefix if surfix is a palindrome.

        prefix surfix
        sss    xo     => find ox, append in front
        xo     sss    => find ox, append in end

        Time: O(nk^2)

    - Trie (too complicate)

        Build a trie for every reversed words.
        Search the trie with the original word.
        Search beyond the original word if other words include the current word as surfix

        words = ["ba", "a", "aaa"]

        TrieNode has (index of the word, index of the word that has current word as surfix)

                 root (-1,[1,2])
                    | 'a'
                  n1 (1,[0,1,2]) => ('ba', 'a', 'aaa') all have surfix 'a'
            ---------------------
        'b' |                   | 'a'
          n2 (0,[0])     n3 (-1,[2])
                                | 'a'
                          n4 (2,[2])

            
    
Time: O(nk * k)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word):
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True

        if not words:
            return []

        index = defaultdict(int)
        for i, word in enumerate(words):
            index[word] = i

        pairs = set()
        for i, word in enumerate(words):
            # If we have '' in the words, such as ['a', ''],
            # We want to include both (0, 1) and (1, 0) in the pairs.
            # If we don't check j == len(word), we will not find (1, 0)
            for j in range(len(word) + 1):                
                prefix, surfix = word[:j], word[j:]

                if is_palindrome(prefix):
                    reversed_surfix = surfix[::-1]
                    if reversed_surfix in index and index[reversed_surfix] != i:
                        # (ox) sss xo
                        #      ^^^^^^
                        pairs.add((index[reversed_surfix], i))

                if is_palindrome(surfix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in index and index[reversed_prefix] != i:
                        # xo sss (ox)
                        # ^^^^^^
                        pairs.add((i, index[reversed_prefix]))

        return list(pairs)
