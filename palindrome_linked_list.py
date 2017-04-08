"""Check if a linked list is a palindrome

    Reverse the right half and compare two halfs.

Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Find the right half
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Reverse the right half
        tail = None
        while slow:
            slow.next, slow, tail = tail, slow.next, slow
            
        # Compare
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
            
        return True
        