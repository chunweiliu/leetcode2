"""Find the area of the maximal square in a matrix

    << 0 1 0
       0 1 1
       0 1 1
       
    => 4
    
    DP:
        M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1]) + 1 if matrix[i][j] == 1

Time: O(n^2)
Space: O(n^2) can improve to O(n)
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        M = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_length = 0
        for i, row in enumerate(matrix, 1):
            for j, element in enumerate(row, 1):
                if element == '1':
                    M[i][j] = min([M[i-1][j], M[i][j-1], M[i-1][j-1]]) + 1
                    max_length = max(max_length, M[i][j])
                    
        return max_length * max_length
        
        