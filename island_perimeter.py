"""Find the perimeter for an island surrounded water

    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Answer: 16

    - DFS (bug)
       +4 -2  
        1 - 1 +4
      ? |   | -2
        1 - 1 +4
       +4 -2

       Missing one -2

    - Count island and neighbor
        node * 4 - edge * 2

Time: O(mn)
Space: O(1)
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        node = 0
        edge = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    node += 1

                    # Only count edge in two direction without duplicated
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        edge += 1

                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        edge += 1

        return 4 * node - 2 * edge
