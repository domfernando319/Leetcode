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
'''
### Time Complexity

The time complexity is recursive in nature.

For n, there are at most n+1 levels to reach base case leaf nodes.

And each node can branch at most 2 times: (n-1) (n-2)

Therefore,
Time without memo:  O(2^n)

Time With Memo: O(n) because each base case return in constant time, each calculation is computed once before memoized which is O(1) for subsequent calculation. There are n - 2 calculations to compute exactly once.

Space: O(n) memo will have at most m mappings

'''