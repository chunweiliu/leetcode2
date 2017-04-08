"""Given a sorted domain x, return f(x) = ax^2 + bx + c in sorted

    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

    Result: [3, 9, 15, 33]

    - Math:

         --------
        /        \          \             /
       /          \          \___________/ 
    ->             <-             <-|->
    i=0            j=n-1          i=j=-b/2a


    * For a > 0:
        No need to start from the middle, just insert the answer backward

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a * x ** 2 + b * x + c

        ret = [0] * len(nums)
        
        i, j = 0, len(nums) - 1
        insert = i if a < 0 else j
        di = 1 if a < 0 else -1
        while i <= j:
            # Change sign using di
            if di * f(nums[i]) < di * f(nums[j]):
                ret[insert] = f(nums[i])
                i += 1
            else:
                ret[insert] = f(nums[j])
                j -= 1
            insert += di
        return ret