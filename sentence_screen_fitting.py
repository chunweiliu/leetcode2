"""Count how many time we fit a sentence into a screen

    << rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
    => 2

    a-bcd- 
    e-a---
    bcd-e-
    012345
    
    Greedy on a repeated word string:

        a bcd e a bcd e a
        01234567890123456
        ^     ^   ^     X  
start   0    5   9     16

16 is the last try, so the length of total vaild chars is 16

        hello world
        012345678901


Time: O(n)
Space: O(1)
"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sentence = ' '.join(sentence) + ' '

        # Use start position with the module factor to create repeated string
        start, length = 0, len(sentence)
        for i in range(rows):
            # Put as much as you can in each line, then addjust later
            start += cols

            # If we are in a middle of some word, rollback
            while sentence[start % length] != ' ':
                start -= 1

            # If we are in a space we are good for next word
            start += 1
            
        # vaild char / length of the sentence (with spaces)
        return start / length


    def wordsTyping_bugs(self, sentence, rows, cols):
        count = 0
        w, s = 0, len(sentence)
        
        i = j = 0
        while i < rows and j < cols:
            end = j + len(sentence[w % s]) - 1

            print i, j, sentence[w % s], end
            # Can't fit
            if end > cols - 1:
                i += 1
                j = 0
            else:
                # Fit into the last word
                if end == cols - 1:
                    w += 1
                    i += 1
                    j = 0
                # Fit with space
                else:
                    w += 1
                    j = end + 1
            
                if w != 0 and w % s == 0:
                    count += 1
        return count

sentence = ["hello", "world"]
rows = 2
cols = 8
print Solution().wordsTyping(sentence, rows, cols)