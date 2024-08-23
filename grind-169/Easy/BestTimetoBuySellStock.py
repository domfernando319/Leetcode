class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheapestPriceSoFar = 10000
        maxProfit = 0

        for (day, price) in enumerate(prices):
            profit = price - cheapestPriceSoFar
            maxProfit = max(profit, maxProfit)
            cheapestPriceSoFar = min(cheapestPriceSoFar, price)
            print(maxProfit, cheapestPriceSoFar)
            

        return maxProfit
    