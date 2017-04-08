"""Evaluate Reverse Polish Notation

    Use a stack to store 

    * Divided by 0
    * Float problem

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0

        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                second = stack.pop()
                first = stack.pop()
                
                if token == '+':
                    v = first + second
                elif token == '-':
                    v = first - second
                elif token == '*':
                    v = first * second
                else:
                    # Python do 6 / (-132) = -1, instead of 0
                    v = int(float(first) / second)

                stack.append(v)

        return stack[-1]

