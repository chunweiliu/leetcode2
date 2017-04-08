"""Topological sort using DFS

Time: O(|V| + |E|)
Space: O(|V| + |E|)
"""
from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def DFS_visit(u, visit, finish, Adj):
            visit.add(u)
            for v in Adj[u]:
                if v in visit:
                    return True
                
                if v not in finish:
                    if DFS_visit(v, visit, finish, Adj):
                        return True
                    
            visit.remove(u)
            finish.add(u)
            return False
            
            
        Adj = defaultdict(list)
        for v, u in prerequisites:
            Adj[u].append(v)
        
        visit = set()
        finish = set()
        
        for s in range(numCourses):
            if s not in finish:
                if DFS_visit(s, visit, finish, Adj):
                    return False
        
        return True
