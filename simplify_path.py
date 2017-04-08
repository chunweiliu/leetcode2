"""Simplify path

    << '/a/./b/../../c/'
    => '/c'
    
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
    
        path = path.split('/')
    
        for f in path:
            if f == '' or f == '.':
                pass
            # We go no where up from the root.
            elif f == '..':
                if result:
                    result.pop()
            else:
                result.append(f)
                
        return '/' + '/'.join(result).rstrip('/')
