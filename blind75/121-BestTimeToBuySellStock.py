class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            keep track of maxProfit to update iteratively
            profit = currPrice - cheapestPrice
            take max(profit, maxProfit)
            10 1 5 6 7 0
            cheapestPriceSeen = 0
            currPrice = 0
            profit = 0
            max(profit, maxProfit) = 6
        '''

        












        # cheapestPriceSoFar = 10000
        # maxProfit = 0

        # for (day, price) in enumerate(prices):
        #     profit = price - cheapestPriceSoFar
        #     maxProfit = max(profit, maxProfit)
        #     cheapestPriceSoFar = min(cheapestPriceSoFar, price)
        #     print(maxProfit, cheapestPriceSoFar)
            

        # return maxProfit
    