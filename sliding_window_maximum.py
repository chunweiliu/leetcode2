"""Sliding Window Maximum

    - Heap
        Time: O(n logk)
        Space: O(k)

    - deque (Double-end queue)
        Time: O(n)
        Space: O(k)

    - Monotonic queue
        Time: O(n)
        Space: O(k)

        Maintain a desending deque for size smaller than k.
        
        After enqueue four times on number [1, 6, 8], we have the following

        1, 6, 8, 7
             {value: 8, left: 2, value: 7, left: 0}
                        ^^^
                        when we dequeue, we will minus this first


Time: O(n)
Space: O(n)
"""
from collections import deque


# Values in queue are in desending order
class MonoQueue:
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        return ', '.join(map(str, self.queue))

    def enqueue(self, value):
        queue = self.queue

        # When last element in queue is smaller than the value,
        # it is impossible to be a sliding window maximum.
        # Not include it in queue, but count how many elements we skip to maintain
        # the sliding window.
        count = 0
        while queue and queue[-1]['value'] < value:
            count += queue[-1]['left'] + 1
            queue.pop()

        queue.append({'value': value, 'left': count})

    def dequeue(self):
        queue = self.queue

        # If there are numbers on the left side of the current maximum.
        # We cannot remove current maximum from the queue.
        if queue and queue[0]['left'] > 0:
            queue[0]['left'] -= 1
        else:
            queue.popleft()

    def peek(self):
        return self.queue[0]['value']


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = MonoQueue()

        k = min(k, len(nums))
        for num in nums[:k - 1]:
            queue.enqueue(num)

        ret = []
        for num in nums[k - 1:]:
            queue.enqueue(num)
            ret.append(queue.peek())
            queue.dequeue()

        return ret

nums = [1, 6, 8, 2, 3, 7, 8, 9]
k = 3
print Solution().maxSlidingWindow(nums, k)