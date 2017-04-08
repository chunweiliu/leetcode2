# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Example:
        1 -> 2 -> 3 -> 4
                  4 ->   -> 

        Edge case: the node won't be the tail
        """
        node.val = node.next.val
        node.next = node.next.next
        