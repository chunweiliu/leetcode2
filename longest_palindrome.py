class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int

        Given a character list, find the length of the longest palindrome that
        can be built with the list.

        Example:
        'dccaccd' => 7

        "abccccdd"
        a: 1
        b: 1
        c: 4
        d: 2
        """
        from collections import Counter
        odds = sum(1 for value in Counter(s).values() if value % 2 != 0)
        return len(s) - odds + 1 if odds else len(s)

    def longestPalindrome_defaultdict(self, s):
        from collections import defaultdict
        # buggy code
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        length = 0
        signle_used = False
        for key, value in counts.iteritems():
            if value % 2 == 0:
                length += value
            elif value > 1:
                if not signle_used:
                    length += value
                    signle_used = True
                else:
                    length += value - 1
            elif not signle_used:
                length += 1
                signle_used = True

        return length
