class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int

        Hint:
        * Apply bit operations to integers instead of bit strings.
        * Negative numbers.
        * Python implements integer using big number.
        # Take care Overflow.
        """
        MASK_LAST_EIGHT_BYTES = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF  # 2 ** 31 - 1

        while b:
            # Have carry if both bits are 1.
            carry = a & b

            # Save the addition result for each bit (not included carry).
            # The value of a and b will be stored in the variable a.
            # b will served as carry only in the rest of iteration.
            a ^= b

            # Carry always work in the next position.
            b = carry << 1

            # Treat a and b as 32 bits integers.
            a &= MASK_LAST_EIGHT_BYTES
            b &= MASK_LAST_EIGHT_BYTES

        # Take care overflow using 2's complement
        return a if a <= MAX_INT else ~(a ^ MASK_LAST_EIGHT_BYTES)  

print Solution().getSum(20, 30)