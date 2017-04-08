"""Find nth digits of the integer sequence

    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

    12345678910
    1234567891

    - Enumeration
      Time: O(n)
      Space: O(n)

    * nth digit means n - 1 in the string

    - Math
      Number is running for nth digit,

      1. Compute how many digits for the number
          
        [0, 9] provides 9 digits
        [10, 99] provides 90 digits

      2. Compute the number
      3. Compute the digit location

      Time: O(log n)
      Space: O(1)
    
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, length = 1, 9
        start = 1
        while n - digit * length > 0:
            n -= digit * length
            
            digit += 1
            length *= 10
            start *= 10

        # start of each digit group: 1, 10, 100, ...
        start += (n - 1) / digit
        
        return int(str(start)[(n - 1) % digit])


    def findNthDigitTLE(self, n):
        digits, num = '', 1

        while len(digits) < n:
            digits += str(num)
            num += 1

        # nth digit means index n - 1 in the string
        return int(digits[n - 1])

n = 3
print Solution().findNthDigit(n)