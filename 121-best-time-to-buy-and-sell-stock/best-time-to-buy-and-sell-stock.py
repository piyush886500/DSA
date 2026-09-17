class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            if buy < prices[i]:
                store = prices[i]-buy
                if max_profit<store:
                    max_profit=store
                
        return max_profit