"""Find the min cost of painting house that any neighbors pait different colors

Use tuple (R, B, G) to represent min cost so far
min_cost = (r + min(previous g, previous b),
            b + min(previous r, previous g),
            g + min(previous r, previous b))

Examples:
    - House nearby should be painted different color

      h 0 1 2 3 4
    r   5 2 4 9 1
    b   3 9 2 3 5
    g   4 9 8 8 1

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        min_r = min_b = min_g = 0

        for r, b, g in costs:
            min_r, min_b, min_g = r + min(min_b, min_g), b + min(min_r, min_g), g + min(min_r, min_b)

        return min([min_r, min_b, min_g])
