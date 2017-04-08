"""Count how many island during evolution.

    Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].

    0 0 0
    0 0 0
    0 0 0
    Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

    1 0 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

    1 1 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

    1 1 0
    0 0 1   Number of islands = 2
    0 0 0
    Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

    1 1 0
    0 0 1   Number of islands = 3
    0 1 0

    => [1, 1, 2, 3]

    * Aware when the bounary, if we want to use linear coordination.
      If using 2D tuple, then we don't need to worry about it.

    * With compression, the complexity of find is roughly constant.

Time: O(k log mn)
Space: O(mn)
"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """        
        evolution = []

        islands = DisjointSet()
        # List is not hashable, use tuple for add in set.
        for position in map(tuple, positions):
            islands.add(position)

            i, j = position
            for next in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if next in islands.parent:
                    islands.union(position, next)

            evolution.append(islands.count)

        return evolution


class DisjointSet():
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.count = 0

    def add(self, n):
        self.parent[n] = n
        self.size[n] = 1
        self.count += 1

    def union(self, a, b):
        i, j = self.find(a), self.find(b)

        if i == j:
            return

        size = self.size
        parent = self.parent

        # Let i always the one has a larger size
        if size[i] < size[j]:
            i, j = j, i

        parent[j] = i
        size[i] += size[j]
        self.count -= 1

    def find(self, n):
        parent = self.parent

        while n != parent[n]:
            parent[n] = parent[parent[n]]
            n = parent[n]

        return n

# m, n = 3, 3
# positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
# print Solution().numIslands2(m, n, positions)
