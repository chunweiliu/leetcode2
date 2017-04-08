class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str

        Question:
        - What's the range for the input number?
        => 32 bits

        - How about negative number?
        => Python use 2's complement already
        """
        import string
        hexdigits = string.hexdigits[:16]  # 0123456789abcdef

        hex_string = ''
        for i in range(0, 32, 4):
            hex_string = hexdigits[num & 15] + hex_string
            num >>= 4
        return hex_string.lstrip('0')

    def toHex2(self, num):
        sixteen = 16
        hex_table = {}
        for i in range(sixteen):
            if i > 10:
                hex_table[i] = chr(i - 10 + ord('a'))
            else:
                hex_table[i] = str(i)

        hex_str = ''
        while num:
            hex_str = hex_table[num % sixteen] + hex_str
            num /= sixteen
        return hex_str

    def toHex_dumb_buggy(self, num):
        # Covert number to bits
        negative = True if num < 0 else False
        if negative:
            num *= (-1)
        
        bits = [0] * 32
        i = 0
        while num:
            bits[i] = num & 1
            num >>= 1
            i += 1

        # Convert bits to hex
        hex_str = ''
        for i in range(0, 32, 4):
            digit = 8 * bits[i + 3] + 4 * bits[i + 2] + 2 * bits[i + 1] + 1 * bits[i]

            char = chr(digit - 10 + ord('a')) if digit > 10 else str(digit)
            hex_str = char + hex_str
        return hex_str

print Solution().toHex(26)