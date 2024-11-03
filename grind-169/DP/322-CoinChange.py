class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount + 1)
        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        if dp[amount] != 10001:
            return dp[amount]
        else:
            return -1


    '''
    Time: O(amount * len(coins)) -> O(M*N)
    Space: O(amount) -> O(n)
    
    '''