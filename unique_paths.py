class Solution(object):
    def uniquePaths(self, m, n):
        """
        A robot in cooridnate (x, y) can only come from (x - 1, y) or (x, y - 1)

        For x > 0, y > 0:
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        paths = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                paths[j] += paths[j - 1]
        
        return paths[-1]