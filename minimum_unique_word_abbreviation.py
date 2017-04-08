"""Find the minimum abbreviation that avoid every possible abbr. from the dict.

    Example:
        - "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

    Rules:
        - Number only count 1 length, e.g. "a32bc" has length = 4.

        - Assume length of target string = m, and dictionary size = n. 
          You may assume that m <= 21, n <=  1000, and log2(n) + m <=  20.

        - If a word has different length, it won't affect our result.
    
    For each word in the dict has the same length as target, find the different
    bits between the word and target. These bits are "must have" in the final abbr.

    For example, 

    "abcde", ["abxdx", "xbcdx"]
               00101    10001

    * The implementations of bit encoding and abbr are in opsitive order.

Time: O(n 2^m)
Space: O(n) for dictionary
"""
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def abbr(target, num):
            word, count = '', 0
            for w in target:
                if num & 1 == 1:
                    if count:
                        word += str(count)
                        count = 0
                    word += w
                else:
                    count += 1

                num >>= 1
            if count:
                word += str(count)
            return word

        m = len(target)

        # Figure out the different bits for a same length word in the dictionary
        diffs = []
        for word in dictionary:
            if len(word) != m:
                continue

            # The encoding is opposite
            bits = 0
            for i, char in enumerate(word):
                if char != target[i]:
                    bits += 2 ** i
            diffs += bits,

        # No word in dictionary has same length, return the shortest
        if not diffs:
            return str(m)        
        
        abbrs = []
        for i in range(2 ** m):
            # This abbreviation at least has one word different to every words in the dictionary
            if all(d & i for d in diffs):
                abbrs += abbr(target, i),

        return min(abbrs, key=lambda x: len(x))
