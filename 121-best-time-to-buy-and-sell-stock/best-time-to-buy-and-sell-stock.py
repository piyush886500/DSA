class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minn = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if minn > prices[i]:
                minn = prices[i]
            curr_profit = prices[i]-minn
            if curr_profit > profit:
                profit = curr_profit
        return profit
            

