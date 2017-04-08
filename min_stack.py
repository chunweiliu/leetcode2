"""Design a stack that can get the min value

Time: O(1) for all operations
Space: O(n)
"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append({'value': x, 'min_below': x})
        else:
            self.stack.append({'value': x, 'min_below': min(x, self.getMin())})        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]['value']
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]['min_below']
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()