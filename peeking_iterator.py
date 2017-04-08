"""Use a given Iterator to implment a peeking iterator

Below is the interface for Iterator, which is already defined for you.

class Iterator(object):
    def __init__(self, nums):
        # Initializes an iterator object to the beginning of a list.
        # :type nums: List[int]

    def hasNext(self):
        # Returns true if the iteration has more elements.
        # :rtype: bool

    def next(self):
        # Returns the next element in the iteration.
        # :rtype: int

    * When element is integer, dont' use element = self.element for operations.
      Because element = new_value is binding to the element label but not to
      the self.element object.


Time: O(1) for all operations
Space: O(1)
"""

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator

        # When element is integer, dont' use element = self.element for operations.
        # Because element = new_value is binding to the element label but not to
        # the self.element object.
        self.element = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.element:
            self.element = self.iterator.next()

        return self.element

    def next(self):
        """
        :rtype: int
        """
        if not self.element:
            return self.iterator.next()

        ret = self.element
        self.element = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.element:
            return self.iterator.hasNext()

        return True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].