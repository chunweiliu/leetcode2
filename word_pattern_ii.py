"""Given a pattern and a string, find if string follows the same pattern.

    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.

    Try every possible mapping

Time: O()
Space: O(n)
"""
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def helper(pattern, string, forward={}, backward={}):
            if not pattern and string:
                return False

            if not pattern and not string:
                return True

            # Try a length from 1 to m. The rest of string should have at least
            # number of pattern char. The last +1 for range function.
            # abcde redblue
            # ^xxxx ^^^xxxx
            #   5       7
            for length in range(1, len(string) - len(pattern) + 1 + 1):
                p, s = pattern[0], string[:length]
                
                # First match. Note that if p is in backward, 
                # someone took it already, p -> s is not a one to one mapping.
                if p not in forward and s not in backward:
                    forward[p] = s
                    backward[s] = p

                    if helper(pattern[1:], string[length:], forward, backward):
                        return True

                    del forward[p]
                    del backward[s]
                    
                # Match afterward.
                elif p in forward and forward[p] == s:
                    if helper(pattern[1:], string[length:], forward, backward):
                        return True

                # Invalid. But we want to check other posisition.
                else:
                    pass
            return False

        return helper(pattern, str)

