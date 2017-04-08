"""Compute hamming distance for each bit (#1 * #0)

    1 * 2
    v
    0100
    1110
    0010
    ----
      ^
      2 * 1

    The total hamming distance = number of 1 * number 0

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0, 0] for _ in range(32)]

        for num in nums:
            # Count how many ones and zeros in each bit position for each number
            for i in range(32):
                bits[i][num % 2] += 1
                num >>= 1
                
        return sum(ones * zeros for ones, zeros in bits)
