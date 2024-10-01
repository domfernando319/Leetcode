class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dp(n, memo):
            if n == 0:
                return 0
            if n == 1:
                return 1

            return dp(n -1, memo) + dp(n -2, memo)
        
        return dp(n, memo)