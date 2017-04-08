"""Reverse linked list in k group

    << 1 -> 2 -> 3 -> 4, k = 2
    => 2 -> 1 -> 4 -> 3
    
    Template for reversing a pair
    
    0---->1---->2----->3
    prev  last  curr



    0---->1     2----->3
          v------------^  
    prev  last  curr



    0---->1<----2      3
          v------------^  
    prev  last  curr



    ^-----------v
    0     1<----2      3
          v------------^
    prev  last  curr
    
    
    
    ^-----------v
    0     1<----2      3
          v------------^
    prev  last         curr
    
    Then,
    
    ^------------------v
    0     1<----2<-----3      4
          v-------------------^
    prev  last         curr
    
    
    
Time: O(n)
Space: O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 2:
            return head
        
        # Check if the length is enough for reversing
        curr, length = head, 0
        while curr and length < k:
            curr = curr.next
            length += 1
            
        if length < k:
            return head        
        
        head_pointer = ListNode(-1)
        head_pointer.next = head
        
        prev = head_pointer
        last = prev.next
        curr = last.next
    
        # Push current further, and
        # keep update prev.next to curr
        # and         last.next to curr.next
        for _ in range(k - 1):
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        
        last.next = self.reverseKGroup(last.next, k)
        
        return head_pointer.next