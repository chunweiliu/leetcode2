"""
The inorder traversal of a BST is the nodes in ascending order. To find a
successor is equal to finding the smallest value which is larger than p.

Example:
           5
      3         7
    2  4      6   8
  1                 9
Questions:
    - How many time you are going to apply this method?
    - How would you determine the node is equal?
    - What's the value stored in the BST?

Fail attemp:
    - Parse the tree to a string and find the node there. (Google)

Time: O(h), h is the height of the tree.
Space: O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None

        while root:
            # Successor's value is larger or equal to p's.
            # Going left means searching smaller value.
            if root.val > p.val:
                successor = root
                root = root.left
            # Going right means searching larger value.
            else:
                root = root.right

        return successor


    def inorder_successor_recursion(self, root, p):
        if not root:
            return None

        if root.val > p.val:
            return self.inorder_successor_recursion(root.left, p) or root
        return self.inorder_successor_recursion(root.right, p)


    def inorder_successor_fail(self, root, p):
        stack, current = [], root
        while stack or current:
            if id(current) == id(p):
                return_next = True

            if current.left:
                stack.append(current)
                current = current.left
                if return_next:
                    return current
            else:
                current = stack.pop()
                if return_next:
                    return current
                current = current.right

        return None
