class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        Given a sorted array, find two none-zero base index.

        Questions:
            * Do we have one and only solution?

        Thought:
        1. Two pointers O(n)
            * Shrink one element at a time
        2. Binary search O(nlogn)
        """
        indice = []

        left, right = 0, len(numbers) - 1
        while left < right:

            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                indice = [left, right]
                break

            if two_sum > target:
                right -= 1
            else:
                left += 1

        return [i + 1 for i in indice]


        