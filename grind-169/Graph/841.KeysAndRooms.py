class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
            We can think of the rooms as nodes and the keys in each room as edges to the other nodes
            Therefor we can run a graph traversal on room 0 using DFS. If each room is 
            able to be visited, we return True, else false.
            We can know this by comparing the visited set size to the total number of rooms 
            at the completion of the dfs.

            Time: O(V + E) where V is number of rooms and E is number of keys           
            Space: O(n) for use of visited set which stores at most n unique elements
        '''
        visited = set()
        def dfs(nodeIndex):
            visited.add(nodeIndex)
            for room in rooms[nodeIndex]:
                if room not in visited:
                    dfs(room)

        dfs(0)

        if len(visited) == len(rooms):
            return True
        else:
            return False
