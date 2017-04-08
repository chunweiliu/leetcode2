"""Find the least number of perfect square numbers that form the input.

    << 12
    => 3 (4 + 4 + 4)

    << 13
    => 2 (4 + 9)

    DP[0] = 0
    DP[1] = 1
    DP[2] = 1 + 1
    DP[3] = 1 + 1 + 1
    DP[4] = min(DP[3] + DP[1 * 1] + 1, DP[0] + DP[2 * 2] + 1)

    ...

    DP[n] = min_i(DP[n - i * i] + DP[i * i] + 1)
            0..n

    
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def __init__(self):
        self.DP = {0: 0}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = self.DP

        if len(DP) >= n:
            return DP[n]
        
        for i in range(1, n + 1):
            count = n
            j = 1
            while i - j * j >= 0:
                count = min(count, DP[i - j * j] + 1)
                j += 1
            DP[i] = count

        return DP[n]



        