"""Clone undirected graph
    
        0
       / \
      1---2--
          |_|

    DFS

Time: O(n)
Space: O(n)
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x, n=[]):
#         self.label = x
#         self.neighbors = n        
    
    
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def helper(node, clone)
            if not node:
                return
            
            if node in clone:
                return clone[node]
            
            clone_node = UndirectedGraphNode(node.label)
            
            clone[node] = clone_node
            
            for neighbor in node.neighbors:
                clone_node.neighbors.append(helper(neighbor))
            
            return clone_node

        clone = {}
        return helper(node, clone)
                    
        