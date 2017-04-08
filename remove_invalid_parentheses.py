"""Given an invalid parentheses, return all valid parentheses with minimum steps

    << "()())()" 
    => ["()()()", "(())()"]
    
    << "(a)())()"
    => ["(a)()()", "(a())()"]
    
    << ""
    => [""]
    
    - BFS for minimum
    - How many kind of parentheses?
    - Do we allow duplicated?
    
Time: O(nk), where n is the number of parentheses, k is the search depth.
Space: O(n)
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(s):
            open_parenthes = 0
            
            for c in s:
                if c == '(':
                    open_parenthes += 1
                elif c == ')':
                    open_parenthes -= 1
                    
                if open_parenthes < 0:
                    return False

            return open_parenthes == 0
        
        # Use set to avoid duplicate
        level = {s}
        
        while True:
            valid_parentheses = filter(valid, level)
            
            # Empty set is valid
            if valid_parentheses:
                return valid_parentheses
            
            # s[n + 1:n] == ''
            # For every parentheses, try every position for removing a parenthes.
            level = {p[:i] + p[i + 1:] for p in level for i in range(len(p))}
