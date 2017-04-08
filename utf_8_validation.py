"""Is a given string (multiple chars) a UTF-8 coding?

    1) For 1-byte character, the first bit is a 0, followed by its unicode code.

    2) For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, 
       followed by n-1 bytes with most significant 2 bits being 10.

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    * Count leading ones

    data = [197, 130, 1], which represents the octet sequence: 
    11000101 10000010 00000001 is a 2 byte char follow by a 1 byte char.

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False

        char_pointer = 0
        while char_pointer < len(data):
            header = data[char_pointer]

            if header >> 7 == 0:
                if header > 0x7F:
                    return False
                char_pointer += 1
            else:
                # Count leading ones for header
                leading_ones, bits = 0, bin(header)[2:]
                while leading_ones < len(bits) and bits[leading_ones] == '1':
                    leading_ones += 1

                if leading_ones < 2 or leading_ones == 8:
                    return False
                
                for i in range(leading_ones):
                    if char_pointer + i == len(data):
                        return False
                        
                    if 0b10 & data[char_pointer + i] >> 6 != 0b10:
                        return False
                char_pointer += leading_ones

        return True