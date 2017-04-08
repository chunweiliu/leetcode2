class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices and not prices[1]:
            return 0

        lowest_price = prices[0]
        max_profit = max(0, prices[1] - lowest_price)

        for price in prices[1:]:
            max_profit = max(max_profit, price - lowest_price)
            lowest_price = min(price, lowest_price)

        return max(0, max_profit)

prices = [1, 10, 9]
print Solution().maxProfit(prices)
