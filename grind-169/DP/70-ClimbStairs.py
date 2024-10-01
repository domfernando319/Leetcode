class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(n, memo):
            if n in memo:
                return memo[n]
            # base case
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            # sum elements left and right children to bubble of total count
            val = recurse(n - 1, memo) + recurse(n - 2, memo)
            # save to memo
            memo[n] = val
            return val

        count = recurse(n, memo)
        return count
