"""Use a dict to represent heights. For each critical point, pop the heightest.

    << [[1, 10, 5], [3, 8, 7]]
    => [[1, 5], [3, 7], [8, 5], [10, 0]]

A good illustration of the skyline problem
https://briangordon.github.io/2014/08/the-skyline-problem.html

Time: O(nlogn)
Space: O(n)
"""
from heapq import *


class Solution(object):
    def getSkyline(self, LRH):
        """
        :type LRH: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []

        # liveHR is a max heap of (-height, -right). Pairs are kept in the 
        # priority queue and they stay in there as long as there's a larger 
        # height in there, not just until their building is left behind.
        liveHR = [] 
        
        i, n = 0, len(LRH)
        while i < n or liveHR:
            # If the next building has a smaller x, comparing with the largest
            # right point in the heap, add it to the liveHR heap.
            #
            # ------       <- roof (liveHR[0])
            #     -------  <- LRH[i] should be added to the live HR
            # -------      <- liveHR[1] 
            if not liveHR or (i < n and LRH[i][0] <= -liveHR[0][1]):
                x = LRH[i][0]

                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1            

            # Otherwise, we need to update liveHR.
            #
            # ------            <- liveHR that is going to be removed
            #          -------  <- LRH[i]
            # --------          <- liveHR will not be removed at this time, but soon
            else:
                x = -liveHR[0][1]

                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)

            if liveHR:
                height = -liveHR[0][0]
            else:
                height = 0

            if not skyline or height != skyline[-1][1]:
                skyline.append([x, height])

        return skyline