class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool

        You go first. Remove 1-3 stones each time.
        Can you win by removing the last stone?

        n = 1, 2, 3, 4, 5, 6, 7, 8, ...
        w = 1, 1, 1, 0, 1, 1, 1, 1, ...

        Edge case:
        * n == 0
        """
        return n % 4 != 0 or not n

        