class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, column = len(matrix), len(matrix[0])

        r, c = 0, column - 1
        while r < row and c >= 0:
            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
