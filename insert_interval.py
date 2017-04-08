"""Insert a new interval

    << [[1, 2], [3, 5], [7, 9]], [4, 8]
    => [[1, 2], [3, 9]]
    
    << [[1, 2]], [3, 4]
    => [[1, 2], [3, 4]]
    
    - Insert a number
    [0, 1, 2, 10], 3
    
    Seperate the intervals to left and right half by comparing them with the target interval
    - If not overlap, put them in to left or right
    - Otherwise, update the start and end interval
    
    
Time: O(n)
Space: O(n)
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# 
#     def __repr__(self):
#         return '({}, {})'.format(self.start, self.end)
        
class Solution(object):
    def insert(self, intervals, target):
        """
        :type intervals: List[Interval]
        :type target: Interval
        :rtype: List[Interval]
        """        
        left, right = [], []
        for interval in intervals:
            if interval.end < target.start:
                left.append(interval)
            elif interval.start > target.end:
                right.append(interval)
            else:
                target.start = min(target.start, interval.start)
                target.end = max(target.end, interval.end)
            
        return left + [target] + right