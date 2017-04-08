class Solution(object):
    def canJump(self, nums):
        """DP: O(n^2)
        f(i): if the neighbor i can be reached.

        f(0) = True
        f(1) = True if f(0) is True and f(0) + n(i) >= i else False
        f(2) = True if f(0) is True and f(0) + n(i) >= i ...
                       f(1) is True and f(1) + n(i) >= i else False

        Greedy: O(n) Update the farest element we can reach

        :type nums: List[int]
        :rtype: bool

        Example
            * [0]
            * [0, 1] => Bug

        """
        farest = 0 

        for i, num in enumerate(nums):
            if i > farest:
                break
                
            farest = max(farest, i + num)

        return farest >= len(nums) - 1

print Solution().canJump([0, 1])

                    