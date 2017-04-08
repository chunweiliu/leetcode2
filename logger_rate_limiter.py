"""Print the message if it isn't showing up in the last 10 seconds

Time: O(1)
Space: O(n)
"""

class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.log:
            return self.update(timestamp, message)

        if timestamp - self.log[message] >= 10:
            return self.update(timestamp, message)

        return False

    def update(self, timestamp, message):
        self.log[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)