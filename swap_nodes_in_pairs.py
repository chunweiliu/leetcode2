# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Example:
           1 -> 2 -> 3 -> 4
        => 2 -> 1 -> 4 -> 3        

        Gotcha: Python swaping!
        prev -> a -> b -> b.next => prev -> b -> a -> b.next
        ^^^^^^^^^
                ^^^^^^
                     ^^^^^^^^^^^
        Instead of thinking about in what order I change them, I just change all three at once.
        """
        dummy = ListNode(0)
        prev, prev.next = dummy, head

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            prev.next, a.next, b.next = b, b.next, a
            prev = a

        return dummy.next

        