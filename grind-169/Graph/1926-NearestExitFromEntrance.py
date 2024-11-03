import collections
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def perimeter_coordinates(m, n):
            perimeter = []

            # Top row
            for j in range(n):
                perimeter.append((0, j))

            # Bottom row
            if m > 1:  # Avoid adding the same row if m == 1
                for j in range(n):
                    perimeter.append((m - 1, j))

            # Left column (excluding corners if m > 2)
            for i in range(1, m - 1):
                perimeter.append((i, 0))

            # Right column (excluding corners if m > 2)
            if n > 1:  # Avoid adding the same column if n == 1
                for i in range(1, m - 1):
                    perimeter.append((i, n - 1))

            return perimeter
        
        def isExit(r, c, perimeter):
            return (r,c) in perimeter and maze[r][c] == '.' and (r,c ) != (entrance[0], entrance[1])

        m = len(maze)
        n = len(maze[0])
        perimeter = perimeter_coordinates(m,n)
        
        q = collections.deque()
        q.append((entrance[0], entrance[1], 0))

        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, steps = q.popleft()
            for dy, dx in directions:
                newR, newC = r + dy, c + dx
                #check within bounds
                if 0 <= newR < m and 0 <= newC < n and (newR, newC) not in visited and maze[newR][newC] == '.':
                    if isExit(newR, newC, perimeter):
                        diffY = abs(entrance[0] - r + dy) 
                        diffX = abs(entrance[1] - c + dx)
                        return steps + 1
                    q.append((newR, newC, steps + 1))
                    visited.add((newR, newC))
        return -1
    
    '''
    Time Complexity: 
        Perimeter calculation -> 2 * O(M+N) -> O(m+n)
        isExit : O(1)
        BFS Traversal : O(V * E) 
    Space Complexity: 
        Queue: O(M*N) worst case -> contains all cells in maze = m*n
        Visited set: same O (M*N)
        Perimeter: O(2(m+n)) -> O(m+n)

        Overall: O(M*N)
    
    '''