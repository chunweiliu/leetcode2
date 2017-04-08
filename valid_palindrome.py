"""Valid palindrome sentence

    << 'A man, a plan, a canal: Panama'
    => True

    << '0A'
    => False

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rs = ''.join([c for c in s if c.isalnum()])
                        
        return rs.lower() == rs[::-1].lower()
        