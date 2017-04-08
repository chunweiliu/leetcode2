"""Dropbox
"""
from collections import deque

class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.timeout = 300
    
    # vgod: edge case for empty queue
    # Bad readability for tuple
    # Class is better than Dict
    # .append is better than +=
    def log_hit(self):
        now = timestamp()

        queue = self.queue
        if not queue or now - queue[-1].timestamp > 1:
            queue.append(Timestamp(now))
        else:
            queue[-1].frequency += 1

        # vgod: unbounded memory if not prune_queue
        self.prune_queue(now)

    def get_hits(self):
        now = timestamp()
        self.prune_queue(now)
        return len(self.queue)

    def prune_queue(self, timestamp):
        queue = self.queue
        while queue:
            if timestamp - queue[0] < self.timeout:
                break
            queue.popleft
            
"""Design a hit counter which counts the number of hits received in the past 5 minutes.

    - 300 second array
        Time: 
            - hit: O(1)
            - getHit: O(1)
            - update: O(s), must be called either in hit or getHit
        Space: O(s)

        Cons:
            - accuracy

    - queue
        Time:
            - hit: O(1)
            - getHit: O(1)
            - update: O(n), must be called either in hit or getHit
        Space: O(n)

        Cons:
            - When huge request amount, this is slow

    Follow up:
    http://blog.gainlo.co/index.php/2016/09/12/dropbox-interview-design-hit-counter/

        * Concurrent request
            - *race condition*
                lock
         
"""
from collections import deque


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.timeout = 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.queue += timestamp,

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.update(timestamp)
        return len(self.queue)

    def update(self, timestamp):
        queue = self.queue

        while queue:
            if timestamp - queue[0] < self.timeout:
                break
            queue.popleft()

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
import threading
import datetime
import time


class HitCounterMultiThread():
    def __init__(self, lock, queue):
        self.timeout = datetime.timedelta(seconds=4)
        self.lock = lock
        self.queue = queue

    def hit(self, timestamp):
        self.lock.acquire()
        self.queue += (self, timestamp),
        self.lock.release()

    def getHits(self, timestamp):
        self.update(timestamp)
        return len(self.queue)

    def update(self, timestamp):
        queue = self.queue

        self.lock.acquire()

        while queue:
            if timestamp - queue[0][1] < self.timeout:
                break
            queue.popleft()

        self.lock.release()


class MyThread(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        counter = self.counter

        for i in range(8):
            counter.hit(datetime.datetime.now())
            time.sleep(1)

        now = datetime.datetime.now()
        print now
        print counter.getHits(now)

# Each thread ran 8 seconds, only hits within the last 4 seconds are stored in
# queue. The timestamp was provided by two threads.
         
# queue is global and lock is the same one
queue = deque()
lock = threading.Lock()

t1 = MyThread(HitCounterMultiThread(lock, queue))
t2 = MyThread(HitCounterMultiThread(lock, queue))
t1.start()
t2.start()
t1.join()
t2.join()

print
print queue
