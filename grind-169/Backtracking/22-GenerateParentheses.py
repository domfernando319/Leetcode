class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 3  open 
        # we can start with an open bracket only
        # draw a tree
        # next we can pick a closing bracket or open bracket
        # keep track of open brackets and closing brackets at any step
        #close if open > close
        # can only open if open < n

        res, validString = [] , []

        def backtrack(open, close):
            if len(validString) == 2*n:
                res.append(''.join(validString))
                return
            
            if open < n:
                validString.append('(')
                backtrack(open + 1, close)
                # backtrack and undo the open bracket that we used
                validString.pop()
            
            if open > close:
                validString.append(')')
                backtrack(open, close + 1)
                validString.pop()

        backtrack(0,0)

        return res
    
        #Time: O(2^n) each node could go down 2 subtrees
        # Space: res and validString will contain at most 2*n parentheses -> O(n)
