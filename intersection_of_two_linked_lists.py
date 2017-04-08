"""Find the node at the intersection of two linked list

    A:          a1 → a2                   5
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3                   6

                ^
                start here


    Compute the offset of the number of node for a1 and b1, advance the longest
    list by the offset. Then advance both node to see if they meet.

Time: O(n)
Space: O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def linked_list_length(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count

        def advance(node, offset):
            while node and offset:
                node = node.next
                offset -= 1
            return node

        length_a = linked_list_length(headA)
        length_b = linked_list_length(headB)
        offset = abs(length_a - length_b)

        if length_a < length_b:
            headB = advance(headB, offset)
        else:
            headA = advance(headA, offset)

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
