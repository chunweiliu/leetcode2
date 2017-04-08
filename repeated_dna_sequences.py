"""Find every 10-letter-long string repeated in a DNA sequence.

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

    Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        repeated = set()
        exist = set()

        length = 10
        i = 0
        while i + length <= len(s):
            ten_dna = s[i:i+length]
            if ten_dna in exist:
                repeated.add(ten_dna)
            
            exist.add(ten_dna)
            i += 1

        return list(repeated)
