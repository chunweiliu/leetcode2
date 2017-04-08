"""Add two binary string from the back

        i
     '111'
       '1'
        j
    ------
    '1000'

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''

        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0 or carry:
            carry += int(a[i] if i >= 0 else 0)
            carry += int(b[j] if j >= 0 else 0)

            result = str(carry % 2) + result
            carry /= 2

            i -= 1
            j -= 1

        return result

a = '10'
b = '10'
print Solution().addBinary(a, b)