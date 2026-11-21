class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        profit = 0

        for price in prices: 
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit


        


        









































        maxProfit = 0
        left=0
        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                left = right
            else:
                profit = prices[right]-prices[left]
                maxProfit = max(profit, maxProfit)
        return maxProfit

        