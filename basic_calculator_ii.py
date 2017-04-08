"""Evaluate expressions

    "3+2*2" = 7
    " 3/2 " = 1
    " 3+5 / 2 " = 5

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def operate(stack, operator, digits):
            num = int(digits)
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                # For Python 2.x floor division bug. E.g -3 / 2 = -2
                stack.append(int(float(stack.pop()) / num))
            
        stack = []
        digits = ''
        operator = '+'

        for c in s:
            if c == ' ':
                continue
            
            if c.isdigit():
                digits += c
            else:
                operate(stack, operator, digits)
                operator = c
                digits = ''
                
        operate(stack, operator, digits)
        return sum(stack)
