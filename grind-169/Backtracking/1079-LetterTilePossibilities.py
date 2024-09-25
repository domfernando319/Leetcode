#Backtracking for smaller length strings (max is 7)
# can use permutations library as well
# uppercase letters only
# The 3 backtracking patterns:
# 1) Select or Not
# 2) Enumerate or cut
# 3) Game specific (sudoku, n queens, etc)


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(i, res):
            # i is the current index in the substring we are processing
            # res is the string being formed
            if i == n:
                # when i is n , the current string being formed is added to count set
                count.add(res)
                return
            # backtrack(i + 1, res) explores the possibility of not using the current tile at index i.
            backtrack(i + 1, res)
            # backtrack(i + 1, res + substring[i]) explores the possibility of including the tile at index i in the current combination.
            backtrack(i + 1, res + substring[i])
            
        count = set()
        for perm in permutations(tiles):
            substring = ''.join(perm)
            n = len(substring)
            backtrack(0, '')
            

        return len(count) - 1