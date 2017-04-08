"""Design two sum class 

    Use a counter to look up 

    - Add quick
        - Add O(1)
        - Find O(n)

    - Find quick
        - Add O(n), add all possible pair for the input
        - Find O(1), just look up if the answer is in the pair

Space: O(n)
"""
from collections import defaultdict


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.counters = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.counters[number] += 1
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        counters = self.counters

        for number in counters:
            lookup = value - number
            # lookup != number or
            # lookup == number and counter[lookup] > 1
            if lookup in counters and (lookup != number or counters[lookup] > 1):
                return True
        return False
        
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)