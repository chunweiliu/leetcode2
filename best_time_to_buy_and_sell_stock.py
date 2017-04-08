"""Find the maximum profit with only one transaction

    Input: [7, 1, 5, 3, 6, 4]
    Output: 5

    max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

    - Compute profit every time and keep the max profit
    - Update best buy price with the process

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        best_buy = prices[0]

        for price in prices[1:]:

            max_profit = max(max_profit, price - best_buy)
            best_buy = min(best_buy, price)

        return max_profit
