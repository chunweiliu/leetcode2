"""Count range sum that within [lower, upper]

    Given nums = [-2, 5, -1], lower = -2, upper = 2,
    Return 3.
    The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

    * In general, this *count something in an array* can be done by merge sort.
        - Count of smaller numbers after self
          (count nums[i] > nums[j], for i < j)
        - Count for range sum within an interval
          (count lower <= S[j] - S[i] < upper, for i < j)

          left_sorted_array  rigth_sorted_array
              1 3 4 9 10      -2 -5 4 9 10 17
                i             j: first index for lower interval
                              k: first index for upper interval

        if i advance, j and k have to advance without look back

Time: O(n log n)
Space: O(1)
"""
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def sort(start, end):
            # Only one element left, no count
            if end - start <= 1:
                return 0

            mid = (start + end) / 2
            count = sort(start, mid) + sort(mid, end)

            j = k = mid
            for left in S[start:mid]:
                while j < end and S[j] - left < lower:
                    j += 1
                while k < end and S[k] - left <= upper:
                    k += 1
                count += k - j  # no off-by-one since k is not included

            S[start:end] = sorted(S[start:end])
            return count
        
        S = [0]
        for num in nums:
            S.append(S[-1] + num)
        return sort(0, len(S))



        