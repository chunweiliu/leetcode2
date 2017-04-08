"""
Search a word in a Trie, if a character is '.' then evaluate all the children.
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.chars = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root

        for char in word:
            node = node.chars[char]

        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(word, node):
            if not word:
                return node.is_word

            char, surfix = word[0], word[1:]

            # If the current char is the skip one, match any subtrie is fine.
            if char == '.':
                return any(find(surfix, child) for child in node.chars.values())

            # Otherwise, match the current node and the trie after it.
            return char in node.chars and find(surfix, node.chars[char])
                
        return find(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")