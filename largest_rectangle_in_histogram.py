"""Find the max rect area under histogram
     
                 
              |  
           |  |
           |  |  
        |  |  |  |
        ---------------
        0  1  2  3 '4' <- append a fake height, so we can always pop the left height.
                 ^
                 hit a place that has lower height than the stack top
              4 x 1
           3 x 2
        1 x 3

    Maintain a monotonic increasing stack.
    If the current heigth is lower than the stack top,
    We compute the area backward.

Time: O(n)
Space: O(n)
"""

class Solution(object):
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

heights = [1, 3, 4, 1]
print Solution().largestRectangleArea(heights)



        