"""Remove k digits so the remain number is the samllest

    Input: num = "1432219", k = 3
    Output: "1219"

    Input: num = "10200", k = 1
    Output: "200"

    - DFS + memo

        Time: O(C(n, k))

    - Greedy

        * d0 d1 start from left, if d1 is smaller than d0, d0 can be remove

        4321
        ^^ remove 4

        3421
         ^^ remove 4

Time: O(n)
Space: O(n)
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        # Preserve digits in accending order
        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Keep removing if k left
        while k:
            stack.pop()
            k -= 1

        if not stack:
            return '0'
            
        # Edge case for '0'
        return ''.join(stack).lstrip('0') or '0'