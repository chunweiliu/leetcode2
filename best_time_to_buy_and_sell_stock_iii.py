"""Find max profit for at most two transactions
        
    - Seperate the stock holding in 4 states and compute the max for each.
        T: O(n); S: O(1)

        Easy to explain with:
        What your best buying prices pair, and what's your best selling prices pair?

    - Seperate the prices into 2 parts and compute the max profit for each.
        T: O(n); S: O(n)

        Not easy to represent with. Hard to generize also.

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        best_one_buy = max(prices)
        best_two_buys = max(prices)
        best_one_sell = 0
        best_two_sells = 0

        # Is the order matter? Yes, beacuse it store the configuration for last price.
        for price in prices:
            best_two_sells = max(best_two_sells, price - best_two_buys)
            best_two_buys = min(best_two_buys, price - best_one_sell)
            best_one_sell = max(best_one_sell, price - best_one_buy)
            best_one_buy = min(best_one_buy, price)

        return best_two_sells

    def maxProfitDivideTwo(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit_before = [0] * len(prices)
        profit_after = [0] * len(prices)

        best_buy = prices[0]
        for i, price in enumerate(prices[1:], 1):  # enumerator starts from 1!
            # Hold or sell
            profit_before[i] = max(profit_before[i - 1], price - best_buy)
            best_buy = min(best_buy, price)

        best_sell = prices[-1]
        for i, price in reversed(list(enumerate(prices[:-1]))):
            # Hold or buy
            profit_after[i] = max(profit_after[i + 1], best_sell - price)
            best_sell = max(best_sell, price)
  
        max_profit = 0
        for first, second in zip(profit_before, profit_after):
            max_profit = max(max_profit, first + second)
        return max_profit
    