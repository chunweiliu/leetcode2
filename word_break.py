"""Find all piece of the word in the string and match them in the dict by DP

    << 'facebook', {'face', 'book'}
    => True

    for j in range(len(constructeds)):
        for i in range(j):
            # s[i:j] is all possible word segments

    break[j] is true if break[i] is true and s[i:j] in word_dict.

    Example: 
        d = {'face', 'book'}
        s =  'facebook'
        si    01234567
        b    TFFFTFFFT
        bi   012345678

        j = 4, i = 0
        break[4] = break[0] and s[0:4] in d

        j = 8, i = 4
        break[8] = break[4] and s[4:8] in d

        Question:
            - Is the word in dictionary reuseable?


        d = {'d'}
        s =  'd'
        si    0
        b    TF
        bi   01

        j = 1, i = 0
        break[1] = break[0] and s[0:1] in d

Time: O(n^2)
Space: O(n)
"""

class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: bool
        """
        constructeds = [False] * (len(s) + 1)
        constructeds[0] = True

        for length in range(len(constructeds)):
            for start in range(length):
                # If the current one is True, we don't want to modify it.
                if constructeds[length]:
                    break

                constructeds[length] = constructeds[start] and s[start:length] in word_dict

        return constructeds[-1]

s = 'facebook'
d = {'face', 'book'}
print Solution().wordBreak(s, d)
        