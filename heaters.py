"""Given locations of houses and heaters, find the minimum radius for heaters
   that every houses could be coverred.

   house = [1, 2, 3]; heater = [2]
            ___|___
             1   1

   => 1

    house    0    1    2    3    4    5
    heater   0              3                 6
   
    for house 1             left

    Find the maximum distance of gap

Time: O(nlogn)
Space: O(n)
"""
from bisect import bisect_left

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()

        radius = 0

        for house in houses:
            # Find the left most position 
            left = bisect_left(heaters, house)

            # Find the closest heater to the left and right
            # The left-(left>0) handle when left = 0
            # Don't need to worry about left+1 overflow, since Python handle it.
            need = min(abs(house - heater) for heater in heaters[left-(left>0):left+1])            
            radius = max(radius, need)

        return radius
