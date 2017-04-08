"""Factor combination for positive integer

    input: 12
    
    output:
    [
      [2, 6],
      [2, 2, 3],
      [3, 4]
    ]

    Use a factor until we cannot use it anymore.
    Iterate through factors from 2 to n ** 0.5.

Time: O(n * d)
Space: O(n)
"""
class Solution(object):
    def getFactors(self, n):
        combinations = []

        stack = [(n, 2, [])]
        while stack:
            target, factor, combination = stack.pop()
            while factor * factor <= target:
                if target % factor == 0:
                    combinations.append(combination + [factor, target / factor])
                    stack.append((target / factor, factor, combination + [factor]))
                factor += 1
        return combinations

    def getFactorsRecursive(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(n, i, comb, combs):
            while i * i <= n:
                if n % i == 0:
                    combs += comb + [i, n / i],
                    helper(n / i, i, comb + [i], combs)

                i += 1
            return combs

        return helper(n, 2, [], [])

n = 12
print Solution().getFactors(n)