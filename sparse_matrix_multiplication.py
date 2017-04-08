"""Return A x B, for sparse matrix A (m x k) and B (k x n)

For each element in C (m x n), sum up the k elements a_i * b_i

    [[(0), 0, 0, 1]    [[1, 0, 0]         [[a, b, c]
      [1,  2, 0, 0]     [0, 1, 0]          [d, e, f]
      [0,  0, 0, 1]]    [0, 0, 0]          [g, h, i]]
                        [0, 0, 1]]
                         
    How C's first row got constructed?
    - The first elemnt in A's first row contributed to all 
    - The second element in A's first row contributed to all

Time: O(mn k)
Space: O(mn)
"""
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        num_row_A, num_column_B = len(A), len(B[0])

        C = [[0] * num_column_B for _ in range(num_row_A)]

        for i, row in enumerate(A):
            for k, a in enumerate(row):
                if a:
                    for j, b in enumerate(B[k]):                        
                        C[i][j] += a * b

        return C

# 2 x 3, 3 x 4
A = [[1, 3, 5],
     [10, 30, 50]]
B = [[1, 0, 0, 0],
     [0, 1, 0, 1],
     [0, 0, 1, 0]]
# How C's first row got constructed?
#       +3 from [(3), 0, 1]
#       +1 from [3, 0, (1)]
# C=[[1, 3, 5, 3],
#    [10, 30, 50, 30]]
print
print Solution().multiply(A, B)

        