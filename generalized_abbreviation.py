"""Output all ways of abbreviation of a word

    Given word = "word", return the following list (order does not matter):
    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", 
     "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


    - Bit manipulation

        Use i to list total configuration, and then j to actually pick the element.

        i 1 2 3

          0 0 0
          0 0 1
          0 1 0
          0 1 1
          1 0 0
          1 0 1
          1 1 0
          1 1 1

        j 0 0 1 => Pick 3?
          0 1 0 => Pick 2?
          1 0 0 => Pick 1?

          How to?
          1o11 => 1o2
          1o11o11 => 1o2o2

    - Backtracking with recursion

Time: O(2^n)
Space: O(1)
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(i, attemp, count):
            if i == len(word):
                attemp += str(count) if count else ''    
                result.append(attemp)
            else:
                # Include the current position, and none zero count
                helper(i + 1, attemp + (str(count) if count else '') + word[i], 0)

                helper(i + 1, attemp, count + 1)

        result = []
        helper(0, '', 0)
        return result
    
    def generateAbbreviationsBits(self, word):
        result = []

        for config in range(1 << len(word)):
            ones = list(word)
            
            for pick in range(len(word)):
                if config & 1 << pick:
                    ones[pick] = '1'

            abbr, count = '', 0
            for char in ones:
                if char == '1':
                    count += 1
                else:
                    if count:
                        abbr += str(count)
                        count = 0
                    abbr += char
            if count:
                abbr += str(count)
                
            result.append(abbr)

        return result
