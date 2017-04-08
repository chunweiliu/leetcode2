# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        Questions:
            - What's the return of read4?
                ['a', 'b', 'c', 'd']

        Edge cases:
            - n < 4?
            - file size < n?
        
        Example:
            - abcdefg, 5
              ['abcd', 'e']
              ['abcd', 'efg']

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        actual = 0

        current = -1
        while actual < n and current:
            buf4 = [''] * 4
            current = read4(buf4)

            for c in buf4:
                buf[actual] = c
                actual += 1

        # Given the while loop, here we either have actual > n or actual <= n.
        if actual > n:
            buf = buf[:n]
            return n
        return actual