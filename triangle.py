class Solution(object):
    def minimumTotal(self, triangle):
        """
        The minimum value of node j of row i can only from either 
        node j or j - 1 of row i - 1.

        For i > 0, j > 0:
            node[i][j] = value[i][j] + min(node[i - 1][j - 1], node[i - 1][j])

        :type triangle: List[List[int]]
        :rtype: int

        Example:
              1
            2   3
          3   4   5
        """
        if not triangle or not triangle[-1]:
            return 0

        for i, row in enumerate(triangle):
            for j, node in enumerate(row):
                if i == 0 and j == 0:
                    continue

                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(row) - 1:
                    triangle[i][j] += triangle[i - 1][-1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
                
        return min(triangle[-1])        