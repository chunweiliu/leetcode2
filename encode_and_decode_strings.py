"""Design an algorithm to encode a list of string to a string, and decode it reversely

    ['a', 'b', 'c']
    => '1#a1#b1#c'

        ^ number
         ^ break point #
          ^ chars

    * str(len(chars)) when concatenating it

Time: O(n)
Space: O(1)
"""

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string = ''
        
        for chars in strs:
            string += str(len(chars)) + '#' + chars
            
        return string        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strings = []
        
        i = 0
        while i < len(s):
            # load digits
            digits = ''
            while s[i].isdigit():
                digits += s[i]
                i += 1

            # Skip #
            i += 1

            # Add chars
            chars_length = int(digits)
            strings.append(s[i:i+chars_length])

            # Advance pointer
            i += chars_length
            
        return strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))