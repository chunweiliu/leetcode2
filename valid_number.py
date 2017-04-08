"""Valid input is a number

Examples:
    - T '123'
    - T '-123'
    - T '+123'
    
    - T '12.3'
    - T '-1.23'
    - T '+1.0'
    - T '1.'
    - T '.1'
    - F '.-4'
    
    - T '1e10'
    - ? '1e01'
    - T '1e+1'
    
    - ? '0123'
    - F '10 0'
    - T '   13'
    - F '0x12'
    - F '01001'

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip(' ')
        
        sign = num = point = exp = after_exp = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = True
                after_exp = True
            elif c == '.':
                if point or exp:
                    return False
                point = True
            elif c == 'e':
                if exp or not num:
                    return False
                exp = True
                after_exp = False
            elif c in '-+':
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False
                
        return num and after_exp