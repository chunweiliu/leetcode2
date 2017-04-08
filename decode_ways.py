"""
DP; similar to climb stairs

For i >= 2:
    ways[i] = Either
        ways[i - 1] + ways[i - 2], if pd < 27, otherwise
        ways[i - 1] if d > 0

Example:
    A -> 1
    B -> 2
    ...
    Z -> 26

    12 -> 'AB' or 'L'

    #  1  2  3  4
w   1  1  2  3  3

Tag: Facebook

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        prev, curr = 0, 1
        p = ''
        for d in s:
            prev, curr = curr, curr * (d > '0') + prev * (10 <= int(p + d) < 27)
            p = d

        return curr
        
    def num_decoding(self, s):
        if not s:
            return 0

        ways = [0] * (len(s) + 1)

        # In Python True is equal to 1 in operation. For example, 2 * True = 2
        # But True * 2 != 2
        ways[0] = 1
        ways[1] = int(s[0] > '0')

        p = s[0]
        for i, d in enumerate(s[1:], 2):
            if 1 <= int(d) <= 9:
                ways[i] += ways[i - 1]
            if 10 <= int(p + d) <= 26:
                ways[i] += ways[i - 2]
            p = d

        return ways[-1]

    def decode(self, s, memo):
        if not s:
            return ['']

        if s in memo:
            return memo[s]

        ret = []
        if 1 <= int(s[0]) <= 9:
            for surfix in self.decode(s[1:], memo):
                ret.append(self.alpha(s[0]) + surfix)

        if 10 <= int(s[0:2]) <= 26:
            for surfix in self.decode(s[2:], memo):
                ret.append(self.alpha(s[0:2]) + surfix)

        memo[s] = ret
        return ret

    def alpha(self, digits):
        if 1 <= int(digits) <= 26:
            return chr(ord('A') + int(digits) - 1)
        return ''

s = '121231'
memo = {}
print Solution().decode(s, memo)