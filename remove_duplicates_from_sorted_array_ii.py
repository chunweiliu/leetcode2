"""Remove the duplicates, but duplicates are allowed at most twice

    << [1, 1, 1, 2, 2, 3]
              n
              l
       l-2

    => l will stay, and n will advance
       
       [1, 1, 1, 2, 2, 3]
              2  2  3  n
                    l

    >> [1, 1, 2, 2, 3]
    => 5

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ALLOWED_DUPLICATE = 2

        length = 0
        for num in nums:
            print num, length
            if length < ALLOWED_DUPLICATE or num != nums[length - ALLOWED_DUPLICATE]:
                nums[length] = num
                length += 1

        return length

nums = [1, 1, 1, 2, 2, 3]
print Solution().removeDuplicates(nums)
print nums