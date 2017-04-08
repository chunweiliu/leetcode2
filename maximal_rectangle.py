"""Find the maximum rectangle area in a matrix

DP using height, left, and right rows.
    - heigth: Accumlated 1s from top 
    - left: left boundary of the current heigth
    - right: right boundary of the currenth height

    [left, right)
    
    area = heigth * (right - left)

Example:
    matrix
    0 0 0 1 0 0 0
    0 0 1 1 1 0 0
    0 1 1 1 1 1 0

    height
    0 0 0 1 0 0 0
    0 0 1 2 1 0 0
    0 1 2 3 2 1 0

    left
    0 0 0 3 0 0 0
    0 0 2 3 2 0 0
    0 1 2 3 2 1 0

    right
    7 7 7 4 7 7 7
    7 7 5 4 5 7 7
    7 6 5 4 5 4 7

    area
    0 0 0 1 0 0 0
    0 0 3 2 3 0 0
    0 5 6 3 6 5 0
    
Time: O(mn)
Space: O(n)
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
    
        m, n = len(matrix), len(matrix[0])        
        h = [0] * n

        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0

            max_area = max(max_area, self.largestRectangleArea(h))
        return max_area

    def maximalRectangleComplex(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
            
        max_area = 0
        
        m, n = len(matrix), len(matrix[0])
        
        h = [0] * n
        l = [0] * n
        r = [n] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
                    
            l1 = 0  # left boundary of height 1
            for j in range(n):
                if matrix[i][j] == '1':
                    l[j] = max(l[j], l1)
                else:
                    l[j] = 0
                    l1 = j + 1
                    
            r1 = n  # right boundary of height 1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], r1)
                else:
                    r[j] = n
                    r1 = j
                    
            for j in range(n):
                max_area = max(max_area, h[j] * (r[j] - l[j]))
                
        return max_area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        heights.append(0)

        i = 0
        stack = []
        while i < len(heights):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1  # not count current i
                area = heights[top] * width
                max_area = max(max_area, area)


        return max_area

        