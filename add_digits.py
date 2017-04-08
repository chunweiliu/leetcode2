class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        Time: O(1)

        Example:
        38 => 2 (3 + 8 = 11, 1 + 1 = 2)

        0  => 0
        1  => 1
        2  => 2
        3  => 3
        4  => 4
        5  => 5
        6  => 6
        7  => 7
        8  => 8
        9  => 9
        10 => 1
        11 => 2
        12 => 3
        13 => 4
        14 => 5
        15 => 6
        16 => 7
        17 => 8
        18 => 9  
        19 => 1
        20 => 2
        21 => 3
        22 => 4
        23 => 5
        24 => 6
        25 => 7
        26 => 8
        27 => 9
        28 => 1
        29 => 2
        30 => 3
        31 => 4
        32 => 5
        33 => 6
        34 => 7
        35 => 8
        36 => 9
        37 => 1
        38 => 2
        """
        if num == 0:
            return num

        digital_root = num % 9
        if digital_root == 0:
            return 9
        else:
            return digital_root

        