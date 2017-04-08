"""Find the length of the longest substring that contains at most k distinct chars
    
    << 'eceba', k = 2
    >> 'ece'
    => 3   
       
    Sliding window:

    1) Right most position
        Time: O(nk)
    
        Only preserve the rightest index for a character. When you need 
        to give up a character, you only need to know its rightest index.
    
        e: 2
        c: 1
        b: 3
        a: 4

        eceba
        ---
          --

    2) Use a counter and left position to maintain the sliding window
        Time: O(n)
        
        Use a while loop inside the for loop for finding next valid window
        
        eceba
        ---
          --

Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = 0

        counts, left = defaultdict(int), 0
        for right, c in enumerate(s):
            counts[c] += 1

            while len(counts) > k:
                left_most_char = s[left]
                
                counts[left_most_char] -= 1

                # If we don't update the key, len(counts) wont' work.
                if counts[left_most_char] == 0:
                    del counts[left_most_char]
                
                left += 1

            length = max(length, right - left + 1)

        return length

    def lengthOfLongestSubstringKDistinct_nk(self, s, k):
        length = 0

        window, left = {}, 0
        for i, c in enumerate(s):
            window[c] = i

            if len(window) > k:
                left = min(window.values())
                del window[s[left]]
                left += 1

            length = max(length, i - left + 1)

        return length
