"""

    Given the following 5x5 matrix:

      Pacific ~   ~   ~   ~   ~ 
           ~  1   2   2   3  (5) *
           ~  3   2   3  (4) (4) *
           ~  2   4  (5)  3   1  *
           ~ (6) (7)  1   4   5  *
           ~ (5)  1   1   2   4  *
              *   *   *   *   * Atlantic

    Return:

    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] 
    (positions with parentheses in above matrix).

BFS:
    - Mark all points reachable from Pacific
    - Mark all points reachable from Atlantic
    - Find the intersection of these points

    Why not start from the middle?
    A. Because you don't know going up or down

Semi Bidirectional BFS (X)
    - Mark all points reachable from Pacific
    - Start from those points, do BFS to see if they can reach Atlantic
    - Not sure if this is worthy since the map structure is clear.
      The total running time is O(mn) guarantee. Also, you might need to change
      the algorithm (going up & going down)

Bidirectional BFS (X)
    - Have two queues, alternative run BFS on the smaller one
    - When to stop? => When you cannot climb up
    - Not sure if this is worthy since the map structure is clear.
      The total running time is O(mn) guarantee

Tag: Google

Time: O(mn)
Space: O(mn)

"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def BFS(starts, reachable):
            level = {start: 0 for start in starts}

            l = 1
            frontier = list(level)
            while frontier:
                next = []
                for i, j in frontier:
                    j[i][j] = True
                            
                    for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if 0 <= ni < m and 0 <= nj < n and \
                           matrix[ni][nj] >= matrix[i][j] and \
                           (ni, nj) not in level:
                            level[(ni, nj)] = l
                            next.append((ni, nj))
                frontier = next
                l += 1

        BFS([(0, j) for j in range(n)] + [(i, 0) for i in range(m)], pacific)
        BFS([(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)], atlantic)

        both = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    both.append([i, j])
        return both
