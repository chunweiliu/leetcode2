"""Match a string and a pattern

      p a b *
    s 1 0 0 0
    a 0 1 0 1
    b 0 0 1 1
    b 0 0 0 ?

    0) Match or '.'

    1) Horizontal look up [j - 2]
       Not use the character before *.

    2) Vertical lookup
       Use at least one character before *.

Time: O(n^2)
Space: O(n^2)
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s) + 1, len(p) + 1
        match = [[False] * n  for _ in range(m)]

        # Match empty string with empty pattern
        match[0][0] = True

        # Match empty string with .*
        for col, pattern in enumerate(p[1:], 2):
            if pattern == '*':
                match[0][col] = match[0][col - 2]

        for row, char in enumerate(s, 1):
            for col, pattern in enumerate(p, 1):
                if pattern != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    if char == pattern or pattern == '.':
                        match[row][col] = match[row - 1][col - 1]
                else:
                    # Horizontal look up [j - 2].
                    # Not use the character before *.
                    match[row][col] |= match[row][col - 2]

                    # Vertical look up [i - 1].
                    # Use at least one character before *.
                    #   p a b *
                    # s 1 0 0 0
                    # a 0 1 0 1
                    # b 0 0 1 1
                    # b 0 0 0 ?
                    # index for pattern need to be minus 1 more
                    if char == p[col - 2] or p[col - 2] == '.':
                        match[row][col] |= match[row - 1][col]

        for row in match:
            print row
        return match[-1][-1]

chars = 'abb'
patterns = 'a*b*'
print Solution().isMatch(chars, patterns)