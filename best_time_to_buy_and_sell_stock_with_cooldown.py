"""Find the max profit

    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]


    DP:
        Buy with the balance left two days ago, 
        or don't buy and keep the balance as yesterday
        buy[i]  = max(sell[i-2] - price, buy[i-1])

        Sell with the balance after buying one day ago,
        or don't sell and keep the balacne as yesterday
        sell[i] = max(buy[i-1] + price, sell[i-1])

Time: O(n)
Space: O(1)
"""
class Solution(object):    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        # balance for a sequnce ending with buy or sell
        buy = -prices[0]
        sell = 0
        
        prev_buy = 0
        prev_sell = 0

        for price in prices:
            # This won't work. We use different prev_sell for updating buy and sell
            # Check the DP equations.
            # buy, sell = max(sell - price, buy), max(buy + price, sell)

            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)

            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)

        return sell