"""Find the longest increasing path in a matrix
    nums = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    => [1, 2, 6, 9]

    DFS with cache

    * cache served as visited set, and also prevented duplicated search

    Why not BFS?
        - BFS search an area, not a path.
        - You cannot use level set to represent a path

Time: O(mn)
Space: O(mn)
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]

        # Closure in python reference to matrix, m, n, cache
        def visit(i, j):
            if cache[i][j]:
                return cache[i][j]

            length = 1
            for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = max(length, 1 + visit(ni, nj))

            cache[i][j] = length
            return cache[i][j]

        length = 1
        for i in range(m):
            for j in range(n):
                length = max(length, visit(i, j))
        return length

matrix = [
          [9,9,4],
          [6,6,8],
          [2,1,1]
         ]
print Solution().longestIncreasingPath(matrix)
