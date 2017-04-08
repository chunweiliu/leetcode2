"""Check if a string of parentheses is valid
    
    << '('
    => False

    << ')'
    => False

    << '(]'
    => False

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {')': '(', ']': '[', '}': '{'}
        opens = []

        for c in s:
            if c in '([{':
                opens.append(c)
            else:
                if not opens:
                    return False

                if matches[c] != opens[-1]:
                    return False

                opens.pop()

        if opens:
            return False
        return True
