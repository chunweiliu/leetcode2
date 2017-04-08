class Solution(object):
    def climbStairs(self, n):
        """
        ways[1] = 1
        ways[2] = 2
        For i > 2:
            ways[i] = ways[i - 1] + ways[i - 2]
                      (2-step-ways) (1-steps-ways)

            <------------------------------------
        :type n: int
        :rtype: int
        """
        one_step_ways, two_step_ways = 1, 2

        for _ in range(3, n):
            two_step_ways, one_step_ways = one_step_ways + two_step_ways, two_step_ways

        if n == 1:
            return one_step_ways
        if n == 2:
            return two_step_ways
        return one_step_ways + two_step_ways
