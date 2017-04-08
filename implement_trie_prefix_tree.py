"""
Each Trie node has a dict and a flag.
For inserting a word, insert each character to the Trie if the character is not
there yet. For distiguish a word and a prefix, use the '#' symbol.

      Trie
    (f)  (b)
   (o)    (a)
  (o)T     (r)T

"""
from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root

        # If the key is missing in the dict, __missing__ is called and a default
        # value will be generated for the missing key, according to the the dict's
        # default_factory argument (for example, Trie here).
        for char in word:
            node = node.chars[char]

        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.traverse(word)

        return node and node.is_word
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.traverse(prefix)

        return bool(node)

    def traverse(self, word):
        node = self.root

        for char in word:
            if char not in node.chars:
                return False

            node = node.chars[char]

        return node

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")