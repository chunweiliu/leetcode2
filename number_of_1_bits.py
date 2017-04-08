class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        Count how many time we can remove the last non-zero bit
        """
        hamming_weight = 0
        while n:
            hamming_weight += 1
            n &= (n - 1)  
        return hamming_weight