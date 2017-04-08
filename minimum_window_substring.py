"""Find the minimum window in S which will contain all the characters in T

    << S = 'ADOBECODEBANC', T = 'ABC'
    => 'BANC'

Questions:
    - Does the string case sensity?
    - What should we return?

Bugs:
    - window is empty
    - Duplicated characters in T

Template:

def find_substring(s, t):
    # Pick a data structure to represent the sliding window.
    # For example, (need, missing)

    # Incraese the right end of the window until we find a valid solution.

    # Reduce the left end for a smaller window.    

Time: O(n)
Space: O(n)
"""
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        # Sliding window structure
        # need: modify the current state in O(1)
        # missing: validate current window in O(1) by avoiding sum(need.values()) == 0
        need = Counter(t)
        missing = len(t)

        left_most, right_most = 0, 0
        left = 0
        for right, c in enumerate(s, 1):
            # If you need the character, you can reduce the missing counter by 1.
            # Update the sliding window accordingly
            if need[c] > 0:
                missing -= 1
            need[c] -= 1  # No matter you need that or not, it's in your pocket.

            # When a valid window found, reduce the window size as long as it is valid
            if missing == 0:
                # Move one char at a time, since need[s[l]] < 0, no missing added
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if right_most == 0 or right - left < right_most - left_most:
                    left_most, right_most = left, right

        # If we did not update right_most, return s[0:0]
        return s[left_most:right_most]