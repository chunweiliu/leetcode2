"""Search dictionary words on a board.

    Given words = ["oath","pea","eat","rain"] and board =

    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    Return ["eat","oath"].

    If the current candidate does not exist in all words' prefix, 
    you could stop backtracking immediately. 
    What kind of data structure could answer such query efficiently?

    - Trie + DFS

        * Even with trie, aware not going back for the same char
            In [
                ['a', 'a']
               ]
            find 'aaa'
        * Each dictionary word can only appear once. Trie needs to be updated.
        * Start each search from beginning gets TLE.

Time: O(mn)
Space: O(mn)
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.chars = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.chars[char]
        node.is_word = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])        
        
        def DFS_visit(i, j, node, prefix, result):
            if node.is_word:
                result.append(prefix)

                # Remove the word since each word can only appear once.
                node.is_word = False

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            char = prefix[-1]
            node = node.chars.get(char)

            if not node
                return
            
            # Avoid go back
            board[i][j] = '#'
            for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                DFS_visit(ni, nj, node.chars[char], prefix + board[ni][nj], result)
            board[i][j] = char

        trie = Trie()
        for word in words:
            trie.insert(word)

        result = []
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                # Operate on TrieNode 
                DFS_visit(i, j, trie.root, '', result)
        return result

board = [['a', 'b']]
words = ['ab']
print Solution().findWords(board, words)