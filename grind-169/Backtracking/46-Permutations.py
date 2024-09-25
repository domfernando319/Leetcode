class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = list(permutations(nums))
        res= []
        for p in perm:
            p = list(p)
            res.append(p)
        return res
    #Time: permutations for n length is n!, for loop is O(n) 
    #Space complexity: O(n! * n) n! for the permutations and n for the
    # length of the permutations which are at most n
class Solution2:
    def permute2(self, nums: List[int]) -> List[List[int]]:
        # dfs approach
        # Time: O(n!)
        # Spcace: O(n)
        n = len(nums)
        res, sol = [], []

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res

