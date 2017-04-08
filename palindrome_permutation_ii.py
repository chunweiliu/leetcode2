"""Generate all palindromes

    Given s = "aabb", return ["abba", "baab"].

    Given s = "abc", return [].

Time: O(kn)
Space: O(k)
"""
from collections import Counter


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = Counter(s)
        odds = sum(1 for c in counts.values() if c % 2 == 1)

        def helper(attemp, counts, ret):
            # {'a': 2, 'b': 2}
            if not counts:
                ret.append(attemp)
                return

            for char in counts.keys():
                counts[char] -= 2
                if counts[char] == 0:
                    del counts[char]
                    
                helper(char + attemp + char, counts, ret)
                
                if char not in counts:
                    counts[char] = 2
                else:
                    counts[char] += 2

        if odds <= 1:
            attemp = ''.join([char for char, count in counts.iteritems() if count % 2 == 1])
            if attemp:
                counts[attemp] -= 1
                if counts[attemp] == 0:
                    del counts[attemp]
                    
            ret = []
            helper(attemp, counts, ret)
            return ret
        return []

        