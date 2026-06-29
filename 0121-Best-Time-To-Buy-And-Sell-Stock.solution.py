class Solution(object):
    def maxProfit(self, prices):

        buy = prices[0]
        max_profit = 0

        for price in prices:

            if price < buy:
                buy = price

            else:
                profit = price - buy
                max_profit = max(max_profit, profit)

        return max_profit