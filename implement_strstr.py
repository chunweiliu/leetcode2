"""strStr: Return the first occurrence of needle in haystack

    << 'aaxxbbxx', 'xx'
    => 2
    
    << 'ab', 'x'
    => -1
    
    << '', ''
    => 0
    
Time: O(nm)
Space: O(1)
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i
            
        return -1
            