class Solution(object):
    def uniquePathsWithObstacles(self, obstacle_grid):
        """
        For i > 0 and j > 0:
            paths[i][j] = 0 if obstacles[i][j] else paths[i - 1][j] + paths[i][j - 1]

        :type obstacle_grid: List[List[int]]
        :rtype: int

        Bug:
            [[0], 
             [1]]
        """
        if not obstacle_grid or not obstacle_grid[0]:
            return 0

        row, column = len(obstacle_grid), len(obstacle_grid[0])

        # Initalize the first row paths
        paths = [0] * column
        for j in range(column):
            if obstacle_grid[0][j] == 1:
                break
            paths[j] = 1


        for i in range(1, row):
            for j in range(column):
                if obstacle_grid[i][j] == 1:
                    paths[j] = 0
                # Aware the first column
                elif j > 0:
                    paths[j] += paths[j - 1]

        return paths[-1]
