"""Reverse all vowels in a string

    << "hello"
    => "holle"


    ----vv---v-----v---
    0123456789012345678

    * aeiouAEIOU
    * string is immutable

Time: O(n)
Space: O(n)
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        vowels = 'aeiou'
        front, back = 0, len(s) - 1

        while front < back:
            if s[front] in vowels and s[back] in vowels:
                s[front], s[back] = s[back], s[front]
                front += 1
                back -= 1
            elif s[front] in vowels:
                back -= 1
            elif s[back] in vowels:
                front += 1
            else:
                front += 1
                back -= 1

        return ''.join(s)

s = 'hello'
print Solution().reverseVowels(s)