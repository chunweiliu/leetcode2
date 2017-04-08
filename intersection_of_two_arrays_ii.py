class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Follow up:

        1) What if the given array is already sorted? 
        A. O(n + m) two pointer.

        [1, 2, 3, 3, 4]
        [2, 4, 6, 8]

        2) What if nums1's size is small compared to nums2's size?
        num1: [1]
        num2: [2, 1, 1, ...]


        3) What if elements of nums2 are stored on disk, 
           and the memory is limited such that you cannot load all elements 
           into the memory at once?

        A. Binary search for each element in nums1

        buggy
        """
        result = []

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

