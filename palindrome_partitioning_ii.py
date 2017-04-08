class Solution(object):
    def minCut(self, s):
        """DP O(n^2)

        Let f(i) is the min cut for the first i character.

        1) odd palindrome
        .......aba
        |--x--| 1
        |----y---|

        2) even palindrome
        .......abba
        |--x--|
        |----y----|

        :type s: str
        :rtype: int
        """
        n = len(s)

        def update_cuts(left, right):
            while 0 <= left <= right < n and s[left] == s[right]:
                cuts[1 + right] = min(cuts[1 + right], 1 + cuts[left])
                left -= 1
                right += 1
        
        # cuts[0] = -1, so 1 + cuts[0] means no cut need.
        cuts = [i - 1 for i in range(n + 1)]

        for i in range(n):
            left, right = i, i
            update_cuts(left, right)
            
            left, right = i, i + 1
            update_cuts(left, right)

        return cuts[-1]

s = 'cabababcbc'
print Solution().minCut(s)
