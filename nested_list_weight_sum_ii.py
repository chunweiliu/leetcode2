"""Find the sum of nested integers.

    Given the list [1,[4,[6]]], return 17. 
    (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
    
    BFS
    - if the element is a list, extend it to the next level, 
    - otherwise, add the number to unweighted.
    - unweighted number is added again each time.
    

Time: O(n)
Space: O(1)
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        weighted = 0

        # unweighted never reset, so the number in there would be
        # accumulated by the level of nested list.
        unweighted = 0

        while nestedList:
            next_level = []

            for element in nestedList:
                if element.isInteger():
                    unweighted += element.getInteger()
                else:
                    next_level.extend(element.getList())

            weighted += unweighted
            nestedList = next_level

        return weighted
