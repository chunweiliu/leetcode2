"""Find how many connect components for an undirected graph

     0          3
     |          |
     1 --- 2    4

     => 2

Time: O(n), almost linear to #edges since find is almost in const time.
Space: O(n)
"""

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = DisjointSet()
        for i in range(n):
            graph.add(i)
            
        for u, v in edges:
            graph.union(u, v)
            
        return graph.count
            

class DisjointSet():
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.count = 0
        
    def add(self, n):
        if n in self.parent:
            return
        
        self.parent[n] = n
        self.size[n] = 1
        self.count += 1
        
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        
        if ra == rb:
            return
        
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
            
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        
    def find(self, n):
        if n not in self.parent:
            return
        
        parent = self.parent
        while parent[n] != n:
            # Path compression https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
            # Link every other node in the path to their grandparent. Half the path.
            parent[n] = parent[parent[n]]
            n = parent[n]
            
        return n
