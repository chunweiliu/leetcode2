"""Plus one on a singly-linked list

    Input:
    1->2->3

    Output:
    1->2->4

    ^-----------v
    0     1<----2      3
          v------------^
    hptr  tail         curr
    
    * reverse tail (not prev.next)
    * the last carry

Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(head):
            if not head and not head.next:
                return

            head_pointer = ListNode(0)
            head_pointer.next = head

            tail = head
            runner = head.next

            while runner:
                tail.next = runner.next
                runner.next = head_pointer.next
                head_pointer.next = runner
                runner = tail.next

            return head_pointer.next

        tail = reverse(head)
        
        prev = None
        curr = tail
        carry = 1
        while curr:
            curr.val += carry
            carry = curr.val / 10
            curr.val %= 10
            
            prev = curr
            curr = curr.next
            

        if carry:
            prev.next = ListNode(carry)

        return reverse(tail)
        