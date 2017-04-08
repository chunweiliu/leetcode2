class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Compare the target with the upper right element

        Questions:
            * What's the required complexity?
        
        Complexity:
            O(log n + log m)

        Example:
        [[0, 1, 2, 3],
         [4, 5, 6, 7]]
        """
        row, column = len(matrix), len(matrix[0])

        def row_and_column_of(index):
            return index / column, index % column

        first, last = 0, row * column - 1
        while first + 1 < last:
            mid = (first + last) / 2

            r, c = row_and_column_of(mid)
            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                first = mid
            else:
                last = mid

        r, c = row_and_column_of(first)
        if matrix[r][c] == target:
            return True
        r, c = row_and_column_of(last)
        if matrix[r][c] == target:
            return True
        return False
                