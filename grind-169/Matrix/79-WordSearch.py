class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find string by character 
        # can move up down left right
        # same character cannot be used twice
        # use backtracking recursively which is basically a DFS

        ROWS, COLS = len(board), len(board[0])
        pathSet = set() # makes sure we dont visit same coordinate twice in path

        def dfs(r, c, currCharInd):
            if currCharInd == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in pathSet):
                return False
        
            pathSet.add((r,c))

            res = (
                dfs(r + 1, c, currCharInd + 1) or
                dfs(r - 1, c, currCharInd + 1) or
                dfs(r, c + 1, currCharInd + 1) or
                dfs(r, c - 1, currCharInd + 1)
            )

            pathSet.remove((r,c))
            return res
          
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True


        return false