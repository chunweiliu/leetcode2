"""Encode the string in a shortest format

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".

    DP[i][j] store the shortest encoding for s[i:j]

    daabcaabcd => d2[aabc]d
    0123456789
    _---------

    Try every potition in [0, 9], the partion 1 gave us the right encoding

    * (s + s).find(s, 1) find the start posisiton of the longest repeated substring.
      - Assume s[0] is the first char of the repeated substring
      - Assume s[-1] is the last char of the repeated substring
      - Not work if the repeated substring vailate the above assumption

        Work
            - aabcaabc => 2[aabc]
            - aabcaabcaabc => 3[aabc]

        Not work  
            - xxaabcaabc
            - abaabax
            - aabcxaabc

    * Don't skip character
      t = compress(s[:i]) + self.encode(s[i:])

    * The compress function should cover all cases for s
      - s[:1] ... s[:len(s)+1],
      - s[:0] is OK in compress, because compress will just return ''.
        S[0:] is not OK in encode, because it makes infinite loop.

    * In compress, we insert the compressed form instead of the original form.
      The compress form might not be computed yet so we just call the encode function.

Time: O(n * n^2)
Space: O(n^2)
"""

class Solution(object):
    def encode(self, s, memo={}):
        """
        :type s: str
        :rtype: str
        """ 
        def compress(s):
            n = len(s)
            i = (s + s).find(s, 1)

            if i < n:
                return '%d[%s]' % (n / i, self.encode(s[:i]))
            return s

        if s in memo:
            return memo[s]

        shortest = s
        for i in range(1, len(s) + 1):
            t = compress(s[:i]) + self.encode(s[i:])

            if len(t) < len(shortest):
                shortest = t

        memo[s] = shortest
        return memo[s]

# s = "abbbabbbcabbbabbbc"
# s = "abbbabbbc"
# print Solution().encode(s)