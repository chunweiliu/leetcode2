"""Given 10 elements, median is the averge of 5th and 6th elements.
    
    We compare nums1[2] and num2[3], and eleminate the smaller part. 
    That is, we will remove either 2 elments or 3 elements.
    In the next iteration, we look for either the 3rd or 2nd larger element.

        nums1 = [1, 3, 5, 7, 9]
        nums2 = [0, 2, 4, 6, 8]

    * Find kth element. Don't implement find element[k].
      You dont' want to deal with off-by-one error.

Time: O(log m+n)
Space: O(1)
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        def find(M, N, k):
            # Assert |M| > |N|
            if len(M) < len(N):
                return find(N, M, k)

            if not N:
                return M[k - 1]

            if k == 1:
                return min(M[0], N[0])

            # Off-by-one error if we try to find m = 0. 
            # Unless we deal with it by minus one to all belows.
            m = k / 2
            n = min(k - m, len(N))
            if M[m - 1] < N[n - 1]:
                return find(M[m:], N, k - m)
            return find(M, N[n:], k - n)

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return find(nums1, nums2, total / 2 + 1)
        return 0.5 * (find(nums1, nums2, total / 2) + find(nums1, nums2, total / 2 + 1))


nums1 = [1,2,8]
nums2 = [3,4,5,6,7]
print Solution().findMedianSortedArrays(nums1, nums2)
        