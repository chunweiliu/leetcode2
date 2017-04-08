class Solution(object):
    def minDistance(self, word1, word2):
        """DP

        f(i, j) = min()

        :type word1: str
        :type word2: str
        :rtype: int

        Example:
              0 a
            0 0 1
            b 1 1
        """

        m, n = len(word1), len(word2)

        if not m:
            return n
        if not n:
            return m

        DP = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            DP[i][0] = i
        for j in range(n + 1):
            DP[0][j] = j

        # Skip the initial row and column.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                DP[i][j] = min(
                    [DP[i - 1][j] + 1, 
                     DP[i][j - 1] + 1,
                     DP[i - 1][j - 1] + (word1[i - 1] != word2[j - 1])])

        return DP[-1][-1]

print Solution().minDistance('a', 'b')
        