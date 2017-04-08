"""Find the maximum xor between numbers

    Input: [3, 10, 5, 25, 2, 8]

    Output: 28

    Explanation: The maximum result is 5 ^ 25 = 28.

    * Start from MSB 
    * Math induction
        If we have prefix 7 bits set, how to set the 8th bit?
        ooooooox
        ^^^^^^^
        => This mush from some candidates

Time: O(32n)
Space: O(1)
"""

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        prefix_mask = 0
        for i in range(32)[::-1]:
            prefixs = set()
            prefix_mask |= (1 << i)
            for num in nums:
                prefixs.add(num & prefix_mask)

            # Find if any two prefix with different ith bit
            # candidate set the ith bit to 1 first, if we can find a anb b, st
            # a ^ b = candidate, then we have a ^ candidate = b or b ^ candidate = a
            # check if a or b in set.
            candidate = ret | (1 << i)
            for prefix in prefixs:
                if candidate ^ prefix in prefixs:
                    ret = candidate
                    break

        return ret
