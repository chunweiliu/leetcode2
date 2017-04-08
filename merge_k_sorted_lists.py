"""
Merge k sorted lists

    A  1 -> 2 -> 9
    B  3 -> 4
    C  5 -> 8
    
Use a list to maintain the heads
Time: O(k * n)
Space: O(k)

Use a min heap to maintain the heads
Time: O(k + logk * n)
Space: O(k)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head_ptr = node_ptr = ListNode(-1)
        
        heap = [(node.val, node) for node in lists if node]
        heapq.heapify(heap)
        
        while heap:
            _, node = heapq.heappop(heap)        
            
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
            node_ptr.next = node
            node_ptr = node_prt.next
        
        return head_ptr.next
