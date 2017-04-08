"""Decode string given char frequency

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

    Use a stack
    * alphas needs to be reset after pushing into stack
    * digits might be larger than 9, so we need to concatenate them as well

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        alphas, digits = '', ''

        for c in s:
            if c.isdigit():
                digits += c
            elif c == '[':
                stack.append((alphas, int(digits)))
                alphas, digits = '', ''
            elif c == ']':
                prev_alphas, num = stack.pop()
                alphas = prev_alphas + alphas * num
            elif c.isalpha():
                alphas += c

        return alphas
