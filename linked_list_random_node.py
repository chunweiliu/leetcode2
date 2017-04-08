"""Ramdon return one value uniformly in a linked list

    Reservoir samping

Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head

        keep = None
        count = 1
        while node:
            r = random.randrange(count)
            if r == 0:
                keep = node

            node = node.next
            count += 1

        return keep.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()