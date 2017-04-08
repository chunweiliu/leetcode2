"""Find the max profit for buying and selling stocks at most k times
    
    Generization of best time to buy and sell stock iii.

    * best_buy = price '-' previous best_sell
    
Time: O(nk)
Space: O(k)
"""
class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0

        if k == 0:
            return 0

        if k >= len(prices) / 2:
            profit = 0
            buy_in = prices[0]
            for price in prices[1:]:
                profit += max(0, price - buy_in)
                buy_in = price
            return profit

        best_buys = [max(prices)] * (k + 1)
        max_profits = [0] * (k + 1)
        for price in prices:
            # For each price, we test all k transactions
            for i in range(1, k + 1):
                max_profits[i] = max(max_profits[i], price - best_buys[i])
                best_buys[i] = min(best_buys[i], price - max_profits[i - 1])

        return max_profits[k]