"""Find a point that has minimum distance to all building

    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0

    0: Space
    1: Building
    2: Obstacle

    >> (1, 2) is the point and from there to all building need 3 + 3 + 1 = 7
    => 7

    1) If no obstacle:
        - L1 distance => Find medium for row and col

        Time: O(m + n)
        Space: O(1)

    2) Otherwise:
        - BFS

        In place change the grid. The valid grid has a value 0 at first,
        and -1 if it can be visited from a house, and -2, ...
        
        Time: O(kmn)
        Space: O(mn)

        * Only visit the cell which previous building has visitted
        * Avoid naming (i, j) within the for loop
"""
from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        def is_vaild(position):
            i, j = position
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == target

        def next(i, j):
            return filter(is_vaild, [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

        def zero_grid():
            return [[0] * len(grid[0]) for _ in range(len(grid))]
            
        # Total distance accumlated for all buildings
        # Since we use BFS, this is the minimum value
        total = zero_grid()  

        target = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    min_dist = -1
                    dist = zero_grid()

                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft() 
                        valids = next(r, c)

                        for nr, nc in valids:
                            grid[nr][nc] -= 1
                            dist[nr][nc] = dist[r][c] + 1
                            total[nr][nc] += dist[nr][nc]

                            # min_dist has to be a valid one
                            # so we keep update it inside the valids loop
                            if min_dist == -1 or min_dist > total[nr][nc]:
                                min_dist = total[nr][nc]

                        queue.extend(valids)

                    # End of a visit from a building. Next time we will only visit the following target.
                    print total
                    target -= 1
        return min_dist

grid = [[1,0,0],
        [0,2,0],
        [0,2,1]]
print Solution().shortestDistance(grid)