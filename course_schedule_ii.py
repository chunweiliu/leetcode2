"""Topological sort using DFS

Time: O(|V| + |E|)
Space: O(|V| + |E|)
"""
from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def has_cycle(u, visit, finish, edges):
            visit.add(u)
            for v in edges[u]:
                if v in visit:
                    return True
                
                if v not in finish:
                    if has_cycle(v, visit, finish, edges):
                        return True
                    
            visit.remove(u)
            finish.add(u)
            order.append(u)
            return False
            
            
        edges = defaultdict(list)
        for v, u in prerequisites:
            edges[u].append(v)
        
        order = []
        visit = set()
        finish = set()
        
        for s in range(numCourses):
            if s not in finish:
                if has_cycle(s, visit, finish, edges):
                    return []
        
        return order[::-1]
    
numCourses = 2
prerequisites = [[0, 1]]
print Solution().findOrder(numCourses, prerequisites)