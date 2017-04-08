"""Given equations, evaluate functions

     Given a / b = 2.0, b / c = 3.0.
     Evalutate a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
     => [6.0, 0.5, -1.0, 1.0, -1.0 ].

    - Build a graph then traversal using DFS:

       2     3
    a -<- b -<- c
          |
       4  |
    d -<--      

    Why DFS?
    A. Compute products easier
    
    * Check if the equation was not provided
    * Deal with path with empty result

    - Another way is Floyd–Warshall

Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):    
    def calcEquation(self, equations, values, queries):
        # Build the directicted graph with adjacency list and weight matrix.
        Adj = defaultdict(list)
        weights = {}  # Sparse matrix representation
        for (t, s), v in zip(equations, values):
            Adj[s] += t,
            Adj[t] += s,

            weights[(s, t)] = v
            weights[(t, s)] = 1. / v

        def DFS_visit(u, t, product=1., visited=set()):
            # u in Adj is insufficient, since Adj is a defualtdict.
            if u == t and Adj[u]:
                return product
                
            visited.add(u)

            p = None

            for v in Adj[u]:
                if v not in visited:
                    p = DFS_visit(v, t, product * weights[(u, v)], visited)
                
                # If any search reaches t, then we are done. Otherwise, try others.
                if p:
                    break

            visited.remove(u)

            return p


        # DFS
        result = []
        for t, s in queries:
            # Put -1 outside DFS, otherwise you cannot tell if the result
            # is -1 or there is no result
            result += DFS_visit(s, t) or -1,
                
        return result        

# equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
# values = [3.0,4.0,5.0,6.0]
# operations = [["x2","x9"],["x9","x9"]]
# print Solution().calcEquation(equations, values, operations)
