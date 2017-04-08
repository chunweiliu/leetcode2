"""Count and say
    
    1, 11, 21, 1211, 111221, ...
    
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        digits = self.countAndSay(n - 1)
        
        count, say = 1, ''
        
        prev_digit = digits[0]
        for digit in digits[1:]:
            if prev_digit == digit:
                count += 1
            else:
                say += str(count) + prev_digit
                count = 1
            prev_digit = digit
    
        # The last character, no mater it is equal or not equal to 
        # its previous one, won't be added via the above if-else block.
        # Because the above only add prev_digit.
        say += str(count) + digits[-1]
    
        return say