"""Preorder traversal for serializing all nodes (including None) in a binary tree.
   Use preorder because then the first node is always the root.

            1
        2       3
      4  5    #   #
     # ## # 
  
  => 1,2,4,#,#,5,#,#,3,#,#

  How many # in the serialized data?
  A. n + 1, n is the number of node.

Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, l=None, r=None):
#         self.val = x
#         self.left = l
#         self.right = r
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def build_string(root):
            if not root:
                return ['#']
            
            # Don't add [] arround the function call. This will make nasted list.
            return [str(root.val)] + build_string(root.left) + build_string(root.right)
        
        return ','.join(build_string(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(values):
            # Pop the first element with argument 0,
            # or use Deque's popleft
            value = values.popleft()
            
            if value == '#':
                return None
            
            # value will change during the recursion, since popleft is operated
            # on the same object.
            root = TreeNode(value)
            root.left = build_tree(values)
            root.right = build_tree(values)
            
            return root
            
        return build_tree(deque(data.split(',')))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
