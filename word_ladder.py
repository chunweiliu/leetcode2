"""Find the shortest path length for a transition of words

    << words = ["hot","dot","dog","lot","log"]
       begin = 'hit'
       end = 'cog'

    >> "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    => 5

Use bidirectional BFS

"The idea behind bidirectional search is to run two simultaneous searches—one forward from
the initial state and the other backward from the goal—hoping that the two searches meet in
the middle. The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch factor, d is depth. "

----- section 3.4.6 in Artificial Intelligence - A modern approach by Stuart Russel and Peter Norvig
"""
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_list = set(wordList)
        
        if endWord not in word_list:
            return 0

        # If not using [], set treats each char as a different element.
        small, large = set([beginWord]), set([endWord])
        
        length = 2
        while small:
            next = set()
            
            for word in small:
                # For each position, try every possible chars, if the combination
                # happend to be on the other side, we found the answer. 
                # Otherwise, if the word is in the dictionary, we add this word
                # to next level.
                for i in range(len(word)):
                    for char in string.lowercase:
                        next_word = word[:i] + char + word[i + 1:]
                        
                        if next_word in large:
                            return length
                        
                        if next_word in word_list:
                            next.add(next_word)

                            # Each word can only use once
                            word_list.remove(next_word)
                            
            small = next
            length += 1
            
            # Bidirectional BFS: Always explore the smaller side
            if len(small) > len(large):
                small, large = large, small    
            
        return 0