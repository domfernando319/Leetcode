class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        The time complexity is O(n^2) in the worst case 
        where n is the number of and each city is isolated.

        Space complexity is O(N),
        because the visited set will contain at most N cities    

        '''
        visited = set()
        count = 0

        # starting node represented by 0-len(isConnected)
        def dfs(city):
            visited.add(city)

            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    # neighbor is the new starting point for a dfs search
                    dfs(neighbor)

        
        for startCity in range(len(isConnected)):
            if startCity in visited:
                continue
            count += 1
            dfs(startCity)

        return count




        