"""Find all partitions that each substring is a palindrom
    
    << 'aab'
    => [['aa', 'b'], ['a', 'a', 'b']]
    
    << ''
    => [[]]
    

Complexity

    T(n) = T(n-1) + T(n-2) + ...
    T(n+1) = T(n) + T(n-1) + ...
    ----------------------------
    T(n+1) - T(n) = T(n)
    T(n+1) = 2T(n)
    
    T(n) = O(2^n)
    
Time: O(2^n)
Space: O(1)
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrom(s):
            return s == s[::-1]
        
        def DFS(s, path):
            if not s:
                results.append(path)
                return
            
            # a a b
            # -     add 'a', and check 'ab'
            # ---   add 'aa', and check 'b'
            # ----- not add 'aab'
            for i in range(1, len(s) + 1):
                if is_palindrom(s[:i]):
                    DFS(s[i:], path + [s[:i]])
        
        results = []
        
        DFS(s, [])
        
        return results
                
        