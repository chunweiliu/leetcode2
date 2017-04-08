"""Return all strobogrammatic numbers for a cerntain length

    Like palindrome check, start from either middle or both side of middle.
    Append all possible configurations.
     
    * Aware '0' is a number with length 1.
    * Aware '00' is not a number with length 2.

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rotate = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        def helper(left, attemp, result):
            if left == 0:
                if attemp[0] != '0' or len(attemp) == 1:
                    result += attemp,
            else:
                for d in rotate.keys():
                    helper(left - 1, d + attemp + rotate[d], result)

        result = []
        if n % 2 == 0:
            helper(n / 2, '', result)
        else:
            helper(n / 2, '0', result)
            helper(n / 2, '1', result)
            helper(n / 2, '8', result)
        return result

        