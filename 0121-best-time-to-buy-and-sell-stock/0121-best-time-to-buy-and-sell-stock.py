class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_p = prices[0]
        max_p = 0

        for price in prices:
            profit = price - min_p

            if profit > max_p:
                max_p = profit

            if price < min_p:
                min_p = price

        return max_p
