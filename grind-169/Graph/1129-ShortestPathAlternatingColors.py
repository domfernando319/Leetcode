from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        '''
        shortest path -> bfs
        start bfs on node 0
        keep track of length, trust that bfs will traverse shortest path for each node
        keep track of prev edge color. branch accordingly
        starting length os 0, starting color is None, node is 0
        bfs  -> use q (deque), create adj lists for red and blue edges
        ''' 
        answer = [-1] * n
        answer[0] = 0
        redMap, blueMap = defaultdict(list), defaultdict(list)

        for src, nei in redEdges:
            redMap[src].append(nei)
        for src, nei in blueEdges:
            blueMap[src].append(nei)

        visited, q = set(), deque() 
        q.append([0, 0, None]) #node, len, prevColor
        visited.add((0, None))

        while q:
            node, length, prevColor = q.popleft()
            if answer[node] == -1:
                answer[node] = length
                
            if prevColor != 'red':
                for nei in redMap[node]:
                    if (nei, 'red') not in visited:
                        visited.add((nei, 'red'))
                        q.append([nei, length + 1, 'red'])
            if prevColor != 'blue':
                for nei in blueMap[node]:
                    if (nei, 'blue') not in visited:
                        visited.add((nei, 'blue'))
                        q.append([nei, length + 1, 'blue'])
    
        return answer

        