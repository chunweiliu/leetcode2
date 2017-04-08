class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """DP O(m * n)
        Either choose s1 or s2 each time for s3.

        interleaved[i][j] = if s1[:i] and s2[:j] can form s3[:i + j]
        
        interleaved[i][j] = interleaved[i - 1][j] and s1[i] == s3[i + j] or
                            interleaved[i][j - 1] and s2[j] == s3[i + j]

        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        Example:
              0 a a
            0 T T T
            b T 
            b T

        Bug: 
        - while loop += 1
        - s3 indexing
        """
        if len(s3) != len(s1 + s2):
            return False

        s1 = '0' + s1
        s2 = '0' + s2
        s3 = '0' + s3

        m, n = len(s1), len(s2)

        interleaved = [[False] * n for _ in range(m)]

        interleaved[0][0] = True

        i = 1
        while i < m and interleaved[i - 1][0] and s1[i] == s3[i]:
            interleaved[i][0] = True
            i += 1

        j = 1
        while j < n and interleaved[0][j - 1] and s2[j] == s3[j]:
            interleaved[0][j] = True
            j += 1

        for i in range(1, m):
            for j in range(1, n):
                # For example, when i = 1 and j = 1, you are checkecking s3[2],
                # which is the current character we care about. s3[1] has to be
                # filled by either s1[1] or s2[1] (after padding).
                interleaved[i][j] = interleaved[i - 1][j] and s1[i] == s3[i + j] or \
                                    interleaved[i][j - 1] and s2[j] == s3[i + j]

        return interleaved[-1][-1]

s1, s2, s3 = 'a', 'b', 'ab'
print Solution().isInterleave(s1, s2, s3)
