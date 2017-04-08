class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Hint: SINGLE character, digit, symbol => XOR
        """
        import operator
        numerical_string = map(ord, s + t)
        return chr(reduce(operator.xor, numerical_string))

    def findTheDifference_bugs(self, s, t):
        def counter(s):
            from collections import defaultdict
            d = defaultdict(int)
            for char in s:
                d[char] += 1
            return d

        # zip is an intersection and will exclude the uniquic key.
        for (key_s, val_s), (key_t, val_t) in zip(counter(s).iteritems(), 
                                                  counter(t).iteritems()):
            if val_s != val_t:
                break
        return key_t

s = 'abc'
t = s + 't'
print Solution().findTheDifference(s, t)
        