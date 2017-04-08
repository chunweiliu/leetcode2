"""Find i, j in nums such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k

    Check near by bucket, the elements are guarantee to have difference <= t

    |    |    |    |
    |____|____|____|
   0t   1t   2t   3t
   ^
   bucket_id

    If t == 0, num / t bombed
    If t == 1, num / t

Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        
        bucket = {}

        for i, num in enumerate(nums):
            bucket_id = num / t if t != 0 else num

            for near_by in (bucket_id - 1, bucket_id, bucket_id + 1):
                if near_by in bucket and abs(bucket[near_by] - num) <= t:
                    return True

            # We don't need to store multiple values in a bucket.
            # Because if that is a case, we should return True above.
            # So we always update the bucket with the latest (right most) value.
            bucket[bucket_id] = num

            if i >= k:
                expired = nums[i - k] / t if t != 0 else nums[i - k]
                del bucket[expired]

        return False
        