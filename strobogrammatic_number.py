"""Is an input a Strobogrammatic number? 
   Such number looks the same when rotated 180 degrees (looked at upside down)

    1 -> 1
    2 -> 5  (not here)
    3 -> x
    4 -> x
    5 -> 2  (not here)
    6 -> 9
    7 -> x
    8 -> 8
    9 -> 6
    0 -> 0

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rotate = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        rotated = ''
        for d in num:
            if d not in rotate:
                return False

            rotated += rotate[d]

        if num == rotated[::-1]:
            return True

        return False

        