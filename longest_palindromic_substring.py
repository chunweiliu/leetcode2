"""Longest palindromic substring

    << 'babad'
    => 'bab'
    
    b a b a d
    
    
Time: O(n^2)
Space: O(1)
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def find(s, first, last):
            while 0 <= first <= last < len(s) and s[first] == s[last]:
                first -= 1
                last += 1
                    
            # Shrink the interval since s[first] != s[last] when the loop break
            return s[first + 1:last]
        
        longest = ''
        
        for i in range(len(s)):
            odd = find(s, i, i)            
            even = find(s, i, i + 1)
            candidate = odd if len(odd) > len(even) else even
            
            if len(candidate) > len(longest):
                longest = candidate
            
        return longest
    