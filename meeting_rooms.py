"""Determine if a person can attend all meetings

    << [[0, 30],[5, 10],[15, 20]]
    => False
    
        |----------------------|
           |---|
                   |---|
        ------------------------
        0  5  10  15  20  25  30

used    1  1  -1   1  -1      -1
room    1  2   1   2   1       0
    
Time: O(n + k log k)
Space: O(n)
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from collections import defaultdict


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        used = defaultdict(int)
        
        for interval in intervals:
            used[interval.start] += 1
            used[interval.end] -= 1
            
        room = 0
        
        for time in sorted(used.keys()):
            room += used[time]
            
            if room > 1:
                return False
            
        return True
