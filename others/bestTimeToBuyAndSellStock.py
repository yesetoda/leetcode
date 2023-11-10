class Solution:
    def maxProfit( prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    prices = [3,2,6,5,0,3]
    print(maxProfit(prices))