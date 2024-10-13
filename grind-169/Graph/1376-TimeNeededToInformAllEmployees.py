import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
            do a search:BFS
            start at headId
            note that it is a tree structure and we just want 
            to find the max time from the times corresponding 
            to the leaf nodes


        '''

        adjList = collections.defaultdict(list)
        for i in range(n):
            adjList[manager[i]].append(i)
        
        #bfs
        # because there are no cycles because it is a tree
        # directed acyclical graph we dont need visited set

        q = collections.deque([(headID, 0)]) # (id, time)
        time = 0
        while q:
            i, timeTaken = q.popleft()
            time = max(time, timeTaken)
            for emp in adjList[i]:
                q.append((emp, timeTaken + informTime[i]))

        return time





        
        