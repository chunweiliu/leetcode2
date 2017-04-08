"""Wildcard matching

    << isMatch("aab", "c*a*b")
    => False
    
    A wildcard is like a place holder, for example,
    - * matches any sequence including ''
    - ? matches any single character
    
    Regular Expression is more default than wildcard. So RE needs O(n^2).
    
    For this problem, we just need to walk through both string once.
    
         l
    s = abbc
    p = a*c
          s
    
Time: O(mn)
Space: O(1)
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        match = [[False] * (n + 1) for _ in range(m)]

        match[0][0] = True

        for col in range(1, n + 1):
            if p[col - 1] == '*'
                match[0][col] == match[0][col - 1]

        for row, char in enumerate(s, 1):
            for col, pattern in enumerate(p, 1):
                if pattern == '*':
                    match[row][col] = match[row - 1][col] or match[row][col - 1]
                else:
                    if char == pattern or pattern == '?':
                        match[row][col] = match[row - 1][col - 1]

        return match[-1][-1]


    def isMatch(self, s, p):
        i = j = 0
        
        match = star = -1

        # The pattern can be long, but we don't need to move through it all.
        while i < len(s):
            # Advance both
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1    
            # Advance pattern
            elif j < len(p) and p[j] == '*':
                match = i
                star = j
                j += 1            
            # Advance string
            # If the pattern is not match, reset the pattern to the last seen *.
            # And try to advance string as far as possible (by using the last *).
            # If we move out the string, we break the while loop, and we check
            # if the rest pattern are all *s.
            elif star != -1:
                j = star + 1
                match += 1
                i = match               
            else:
                return False
            
        return all(pattern == '*' for pattern in p[j:])
    
