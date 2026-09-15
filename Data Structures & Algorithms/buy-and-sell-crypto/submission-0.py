class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_sell=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            profit = prices[i] - buy
            max_sell = max(profit, max_sell)
        return max_sell

