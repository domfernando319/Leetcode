class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Brute force: run a dfs on the entire board from each position
        # 1 dfs is O(4^(m*n)) and you would have to do this for each board position -> O(mn * 4^mn)

        # what data structure can help you organize the words by prefix
        # Prefix Tree (Trie)  
        '''
            trie
            /   \
            a    c exists?
           /  \      / \
          p     c   ... ...
         / \     \ 
        p   e     e
        '''
        root = TrieNode()

        for w in words:
            root.addWord(w)

        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or ROWS == 0 or COLS == 0 or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)
            

            dfs(r - 1, c, node, word)
            dfs(r + 1 , c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)