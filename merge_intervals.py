"""Merge intervals

    << [1, 3], [2, 6], [8, 10], [15, 18]    
    => [1, 6], [8, 10], [15, 18]
    
    << [1, 2]
    => [1, 2]    
    
Time: O(n log n)
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
    
        results = []
    
        # Interval is not tuples. Need to define the key.
        intervals.sort(key=lambda interval: interval.start)
    
        to_be_merged = intervals[0]
    
        for interval in intervals[1:]:
            if to_be_merged.start <= interval.start <= to_be_merged.end:
                to_be_merged.end = max(to_be_merged.end, interval.end)
            else:
                results.append(to_be_merged)

                # The candidate interval need to be updated.
                to_be_merged = interval
        
        # This line need to be added for
        # 1) One interval,
        # 2) The last interval was merged.
        results.append(to_be_merged)
    
        return results
