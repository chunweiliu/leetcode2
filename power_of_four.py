class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return num > 0 and math.log(num, 4) % 1 == 0