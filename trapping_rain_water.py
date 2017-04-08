"""Find the height for the trapped rain water

    - Water level algorithm

    BFS from both sides of heights, test if the lower side and trap water and advance.

    * Need to update the height for filling water

      2 1 0 2

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
            
        water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                fill = height[l] - height[l + 1]
                if fill > 0:
                    water += fill
                    height[l + 1] += fill
                l += 1
            else:
                fill = height[r] - height[r - 1]
                if fill > 0:
                    water += fill
                    height[r - 1] += fill
                r -= 1
        return water
