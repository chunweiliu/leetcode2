"""Return a number array that is digits plus one

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        ans = []
        carry = 1
        for d in reversed(digits):
            s = d + carry
            ans.append(s % 10)
            carry = s / 10
            
        if carry:
            ans.append(carry)
        
        return ans[::-1]
        
    def plusOneInplace(self, digits):
        carry = 1
        for i in range(1, 1 + len(digits)):
            digits[-i] += carry
            carry = digits[-i] / 10
            digits[-i] %= 10

        if carry:
            digits.insert(0, carry)
        return digits
