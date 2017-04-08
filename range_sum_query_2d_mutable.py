"""Given a mutable matrix, find range sums

    - Binary indexed tree with integral image

        If we update the tree often, we want to use binary indexed tree.

          0          <- dummy
        / |  \
       1  2   4
          |   | \
          3   5  6   Set the right most bit to 0 and you got the parent
                 |
                 7

        * Update: from the index to n (i += i & (-i))
        * sum_path: from the index to 0, take LSB off each time (i -= i & (-i))
        * Integral image: has a padding index + 1

    Time
        init: O(nm)
        update: O(log nm) *
        sumRegion: O(log nm)

    Space: O(nm)

    - Integral image

    Time
        init: O(nm)
        update: O(nm)
        sumRegion: O(1) *

    Space: O(nm)

"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return 

        m, n = len(matrix), len(matrix[0])

        # Use all zeros M for the first initialization
        self.M = [[0] * n for _ in range(m)]
        self.BIT = [[0] * (1 + n) for _ in range(1 + m)]

        BIT = self.BIT
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        M = self.M
        BIT = self.BIT

        diff = val - M[row][col]
        M[row][col] = val

        # Only update the ancestors utill n is smaller than equal to n
        # To do it in 2D, we need two loops instead of one like while row and col.
        i = row + 1
        while i <= len(M):
            # Since we don't have C style for loop, we need to initialize the index.
            j = col + 1
            while j <= len(M[0]):
                BIT[i][j] += diff

                j += j & (-j)
            i += i & (-i)
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        BIT = self.BIT

        # Aware the index shift for integral image here!
        return (self.sum_path(row2+1, col2+1) + 
                self.sum_path(row1, col1) -
                self.sum_path(row2+1, col1) -
                self.sum_path(row1, col2+1))

    def sum_path(self, row, col):
        BIT = self.BIT

        # Why the index not add 1 here?
        # Because we pad the index in integral image already
        val = 0
        
        i = row
        while i > 0:
            j = col
            while j > 0:
                val += BIT[i][j]
                j -= j & (-j)
            i -= i & (-i)
    
        return val

# matrix = [[3,0,1,4,2],
#           [5,6,3,2,1],
#           [1,2,0,1,5],
#           [4,1,0,1,7],
#           [1,0,3,0,5]]
# numMatrix = NumMatrix(matrix)
# print numMatrix.sumRegion(2, 1, 4, 3)

# In an interview this one might be good enougth
class NumMatrix1(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """        
        if not matrix:
            return 
        
        # Copy the matrix
        self.matrix = matrix
        
        self.integral_image = [[0] + row[:] for row in matrix]
        self.integral_image.insert(0, [0] * (len(row) + 1))

        I = self.integral_image
        for i, row in enumerate(I[1:], 1):
            for j, _ in enumerate(row[1:], 1):
                # Aware matrix's index
                I[i][j] = matrix[i-1][j-1] + I[i-1][j] + I[i][j-1] - I[i-1][j-1]

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        # M = self.matrix
        # I = self.integral_image

        # diff = val - M[row][col]
        # M[row][col] = val

        # for i, r in enumerate(I[row:], row):
        #     for j, _ in enumerate(r[col:], col):
        #         if i > 0 and j > 0:
        #             I[i][j] += diff
        matrix = self.matrix
        matrix[row][col] = val

        I = self.integral_image
        for i, row in enumerate(I[1:], 1):
            for j, _ in enumerate(row[1:], 1):
                # Aware matrix's index
                I[i][j] = matrix[i-1][j-1] + I[i-1][j] + I[i][j-1] - I[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        I = self.integral_image

        # Aware the index shift here!
        return I[row2+1][col2+1] + I[row1][col1] - I[row1][col2+1] - I[row2+1][col1]