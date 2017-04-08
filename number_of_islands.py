"""
Count and clear the adjacency 1s using DFS.

Questions:
    - How to determine a isolated island?
        - surrounded by 4 or 8 0s?
    - What's the format of the input?
        - If it is a list of string, than we need extra space.

Example:
    100
    011
    000

Time: O(n)
Space: O(n)
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def clear_up(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(clear_up, (i - 1, i, i + 1, i), (j, j - 1, j, j + 1))

        grid = [list(row) for row in grid]

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    clear_up(i, j)
        return count
