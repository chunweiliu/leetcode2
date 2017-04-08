class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        num1 = '123'
        num2 = '4'
        """
        add_up = []
        
        num1 = self.string_to_digits(num1)
        num2 = self.string_to_digits(num2)

        carry = 0
        while num1 or num2 or carry:
            d1 = num1.pop() if num1 else 0
            d2 = num2.pop() if num2 else 0

            d = d1 + d2 + carry
            carry = d / 10
            add_up.append(d % 10)

        return ''.join(map(str, add_up[::-1]))

    def string_to_digits(self, s):
        return [ord(c) - ord('0') for c in s]

num1 = '1'
num2 = '1'
print Solution().addStrings(num1, num2)
