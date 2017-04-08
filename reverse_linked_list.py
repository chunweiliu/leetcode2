# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseList_template(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Example:
        1 -> 2 -> 3 -> 4 -> 5
        2 -> 1 -> 3 -> 4 -> 5
        3 -> 2 -> 1 -> 4 -> 5
        4 -> 3 -> 2 -> 1 -> 5
        5 -> 4 -> 3 -> 2 -> 1
        """
        # No action need for linked list last than two nodes.
        if not head or not head.next:
            return head

        # The original head will be the tail in the end.
        # Add a dummy node that points to the new head.
        head_pointer = ListNode(0)
        head_pointer.next = head
        tail = head

        current = tail.next
        while current:
            # ... 1 -> 3
            tail.next = current.next

            # ... 2 -> 1
            current.next = head_pointer.next

            # 2
            head_pointer.next = current

            # 3
            current = tail.next
        return head_pointer.next
      
    def print_list(self, head):
        list_values = []
        while head:
            list_values.append(str(head.val))
            head = head.next
        print ' -> '.join(list_values)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print 
Solution().reverseList(head)
