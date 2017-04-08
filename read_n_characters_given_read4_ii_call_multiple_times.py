"""Use instance variable to preserve the read chars

Time: O(1)
Space: O(1)
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf4 = [''] * 4

        # Where is the index in the buf4
        self.buf4_index = 0

        # How many chars that read4 read this time
        self.buf4_count = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        actual = 0

        while actual < n:
            # Nothing left in the buf4, read the file
            if self.buf4_index == 0:
                self.buf4_count = read4(self.buf4)
            
            # Reach file end, break
            if self.buf4_count == 0:
                break

            # Move the content 1 by 1 from buf4 to the buf to return
            if self.buf4_index < self.buf4_count:
                buf[actual] = self.buf4[self.buf4_index]

                actual += 1
                self.buf4_index += 1
            # Reset the index if all content in buf4 has been dumped to buf
            else:
                self.buf4_index = 0

        return actual
