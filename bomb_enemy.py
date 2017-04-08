"""The `Bomb Man` game 

    0 E 0 0
    E 0 W E
    0 E 0 0

    => 3, by placing the bomb at (1, 1)
        
    - For each empty cell, explore 4 directions

    Time: O(mn(m + n))
    Space: O(1)

    - Store the enemies from top-left to bottom-right
      Think about the case if we don't have wall. This is how we approach.
      Unlike the previous one, this one won't looks back, but only look forward.
         |
         |
      ---v-->
         |
         v
      The previous hit record is stored and therefore we need O(n) space.      

    Time: O(mn)
    Space: O(n)

    * It seems three for loops, but each element was visited at most once.
"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        max_count = 0
        col_e = [0] * len(grid[0])

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                # Not look back until there is a W behind
                if j == 0 or grid[i][j - 1] == 'W':
                    # How many enemy in a row
                    row_e = 0
                    for c in row[j:]:
                        if c == 'W':
                            break

                        if c == 'E':
                            row_e += 1

                if i == 0 or grid[i - 1][j] == 'W':
                    # How many enemy in a column
                    # We need to have an array to store this,
                    # since we won't hit the end until i == m - 1
                    # so this col_e is counting.
                    col_e[j] = 0
                    for k in range(i, len(grid)):
                        if grid[k][j] == 'W':
                            break

                        if grid[k][j] == 'E':
                            col_e[j] += 1

                # You cannot place a bomb if the place is not empty
                if cell == '0':
                    max_count = max(max_count, row_e + col_e[j])

        return max_count

    def maxKilledEnemies_TLE(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def explore(i, j, di, dj):
            count = 0
            while 0 <= i < m and 0 <= j < n:
                if grid[i][j] == 'W':
                    break
                
                if grid[i][j] == 'E':
                    count += 1

                i += di
                j += dj
            return count

        max_count = 0
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element == '0':
                    max_count = max(max_count,
                                    (explore(i, j, 1, 0) + 
                                     explore(i, j, -1, 0) + 
                                     explore(i, j, 0, 1) + 
                                     explore(i, j, 0, -1)))
        return max_count
