"""Move all zeros to the back

    << [3, 0, 1, 0, 2] 
    => [3, 1, 2, 0, 0]

    1) Swap every non-zeros to the front.

        |--------|------------|
         non-zero

         swap^

        - If non-zero elements are in the front, this swaps still and waste time

    2) Skip the front non-zeros and swap

        |--------|------------|
         non-zero

         skip^

         1 2 3 4 9 0 7 0 1
                   j
         1 2 3 4 9 7 0 0 1
                     j
         1 2 3 4 9 7 1 0 0

    3) Skip the front non-zeros then replace and fill zeros (fastest)

        |--------|------------|
         non-zero

         skip^

         1 2 3 4 9 0 7 0 1
                   j
         1 2 3 4 9 7 7 0 1
                     j
         1 2 3 4 9 7 1 0 1

         1 2 3 4 9 7 1 0 0

Tag: Facebook

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        try:
            zero_i = nums.index(0)
        except ValueError:
            return
        
        for num in nums[zero_i:]:
            if num:
                nums[zero_i] = num
                zero_i += 1

        for i in range(zero_i, len(nums)):
            nums[i] = 0

    def moveZeroes_skipswap(self, nums):
        try:
            j = nums.index(0)
        # If not found a zero we do nothing
        except ValueError:
            return
        
        for i, num in enumerate(nums[j:], j):
            if num:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

    
    def moveZeroes_swap(self, nums):
        num_none_zeros = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[num_none_zeros] = nums[num_none_zeros], nums[i]
                num_none_zeros += 1


    def moveZeroes_insert(self, nums):
        insert_position = 0
        for num in nums:
            if num != 0:
                nums[insert_position] = num
                insert_position += 1

        while insert_position < len(nums):
            nums[insert_position] = 0
            insert_position += 1
