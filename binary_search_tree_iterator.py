# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        
        self.visit_the_left_most(root)
                
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            node = self.stack.pop()
            
            if node.right:
                self.visit_the_left_most(node.right)
            
            return node.val
        
    def visit_the_left_most(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())