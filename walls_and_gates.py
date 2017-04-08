"""Run BFS for each door. Update each values for minimun.

    << INF  -1  0  INF
       INF INF INF  -1
       INF  -1 INF  -1
         0  -1 INF INF
         
    => 3  -1   0   1
       2   2   1  -1
       1  -1   2  -1
       0  -1   3   4

Time: O(|size of map|)
Space: O(|size of map|)
"""
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        queue = deque([(i, j) for i, row in enumerate(rooms)
                       for j, element in enumerate(row) if element == 0])
        
        while queue:
            i, j = queue.popleft()
            for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ni < len(rooms) and 0 <= nj < len(rooms[0]) and rooms[ni][nj] > 2 ** 30:
                    rooms[ni][nj] = rooms[i][j] + 1
                    queue.append((ni, nj))
        