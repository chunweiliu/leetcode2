"""Given nodes from 0 to n - 1 and edges, determine if this graph is a tree

DFS with visit and finish set:
    - visit: During a traversal, we don't want to look back.
             Since this is a bidirectional graph, a back edge might be just your parent.
             
    - finish: After all of a node's neighbors have been visit, this node is finish.
              If a finish node has been visited again, we know there is a backedge.

Time: O(|v| + |e|)
Space: O(|v| + |e|)
"""
from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Preprocess edges to adjacency lists
        Adj = defaultdict(list)
        for u, v in edges:
            Adj[u].append(v)
            Adj[v].append(u)

        # DFS_visit
        def is_cyclic(s, visit, finish):
            visit.add(s)
            
            for v in Adj[s]:
                if v not in visit:
                    if v in finish:
                        return True

                    if is_cyclic(v, visit, finish):
                        return True
                    
            visit.remove(s)
            finish.add(s)

        # DFS from a single node
        visit = set()
        finish = set()
        if is_cyclic(0, visit, finish):
            return False
            
        # Check from a single node, if DFS can visit entire graph.
        return len(finish) == n
        