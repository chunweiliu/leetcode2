"""Get the first row and backword zip the rest row. You will see the magic

    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    => [1,2,3,6,9,8,7,4,5]

Time: O(mn)
Space: O(mn)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        while matrix:
            nums += matrix[0]
            matrix = zip(*matrix[1:])[::-1]
        return nums

matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
print Solution().spiralOrder(matrix)

        