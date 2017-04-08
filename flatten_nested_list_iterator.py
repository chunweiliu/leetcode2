"""
Prase nested interger with an iterator

    << [[1, 2], 3, [4, 5]]
    => [1, 2, 3, 4, 5]

    So the first time by calling next we got 1, and then 2, 3, 4, 5.

This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#       
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
#        Return None if this NestedInteger holds a single integer#
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Cannot use tuple, since you cannot change tuple element with += 1.
        self.stack = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        self.hasNext()

        nested_list, nested_list_index = self.stack[-1]

        self.stack[-1][1] += 1

        return nested_list[nested_list_index].getInteger()
                

    # Keep unpack the nested list and append it to the stack until we find an integer.      
    def hasNext(self):
        """
        :rtype: bool
        """
        stack = self.stack

        while stack:
            nested_list, nested_list_index = stack[-1]

            # If we visit the end of the last nested list, pop it out of the stack.
            if nested_list_index == len(nested_listist):
                stack.pop()
            else:
                # If the current element of the last nexted list is an integer,
                # return True.
                element = nested_list[nested_list_index]
                if element.isInteger():
                    return True

                # Otherwise, advance the index of the current level, and append
                # the list in to the stack, so next time we can start from there.
                stack[-1][1] += 1
                stack.append([element.getList(), 0])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())