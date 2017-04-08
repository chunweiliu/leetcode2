"""Compute the volume of water after rain in a 3D grid

    - BFS + Heap (priority queue)

    Visit the cells from outside, put their height into the queue.
    BFS from the lowest grid, if there is a grid near by and it is not visited,
    drop rain from the current height.
                ____
       __       |  |
    __|xx|______|  |___
    xx ^^ ^^^^^^
          not visit
       current (drop to the nearby not visit)       
       
    * When adding a new height in BFS, add the larger one (think we are filling the whole)
    * The heap size is O(m + n), so heappush would be O(log(m + n))

Tag: Google

Time: O(mn log (m + n))
Space: O(mn)
"""
from heapq import *


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        
        visited = [[False] * n for _ in range(m)]

        # Initialize first level and push the heights into heap
        heap = []

        for i in range(m):
            # Constructor of a tuple is the last comma
            if not visited[i][0]:
                heap += (heightMap[i][0], i, 0),
                visited[i][0] = True
                
            if not visited[i][n - 1]:
                heap += (heightMap[i][n - 1], i, n - 1),
                visited[i][n - 1] = True

        for j in range(n):
            if not visited[0][j]:
                heap += (heightMap[0][j], 0, j),
                visited[0][j] = True
                
            if not visited[m - 1][j]:
                heap += (heightMap[m - 1][j], m - 1, j),
                visited[m - 1][j] = True

        # O(m + n)
        heapify(heap)

        # BFS
        trap_rain = 0
        while heap:
            h, i, j = heappop(heap)

            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    
                    # Think we are filling the hole, so adding the larger from h and h[ni][nj]
                    heappush(heap, (max(h, heightMap[ni][nj]), ni, nj))

                    # Since we visited from low to high, we can image there is
                    # a sea level increase from lower to topper. We must sit on
                    # the lowest plane to visit a visit, but even lower place.
                    trap_rain += max(0, h - heightMap[ni][nj])

        return trap_rain
