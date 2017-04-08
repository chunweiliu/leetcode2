"""Find the max profits with unlimit trascations

    Aggregate the profits from every valid sales.

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
        yesterday_price = prices[0]

        for price in prices[1:]:
            
            max_profit += max(0, price - yesterday_price)
            yesterday_price = price

        return max_profit
