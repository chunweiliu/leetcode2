"""Recursively prepend the new letter in exist combination

    - Does the return letter's order matter?
    - How about the mapping for 0 and 1?

Time: O(4^n)
"""

class Solution(object):
    KEYS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        keys = self.KEYS
        
        def helper(digits):
            if not digits:
                return ['']
                
            combinations = helper(digits[1:])
            
            try:
                return [char + comb for char in keys[digits[0]] for comb in combinations]
            except KeyError:
                return combinations
            
        return helper(digits)
