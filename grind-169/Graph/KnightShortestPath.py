from collections import deque

def withinBounds(x,y):
    return 65 <= x <= 72 and 1 <= y <= 8

def KnightShortestPath(start, end):
    '''
    start: 'E4', 'D3' use ascii to convert to number
    for each position there is a dx and dy eg. 2, 1
    '''
    deltaX = [2, 2, 1, 1, -2, -2, -1, -1]
    deltaY = [1, -1, 2, -2, 1, -1, 2, -2]
    
    xCoord, yCoord = ord(start[0]), int(start[1])
    print("Start: ", start[0], start[1])
    
    q = deque([(xCoord, yCoord, [start])])
    visited = set()
    visited.add((xCoord, yCoord))
    
    # q looks like : [(x,y,[]),(x,y, []),(x,y, [])]
    while q:
        x, y, path = q.popleft()
        if (x,y) == (ord(end[0]), int(end[1])):
            return path
            
        for dx, dy in zip(deltaX, deltaY):
            newX, newY = x + dx, y + dy
            
            if (newX, newY) not in visited and withinBounds(newX, newY):
                visited.add((newX, newY))
                newPath = path + [chr(newX) + str(newY)]
                q.append((newX, newY, newPath))
            
    return []
        
if __name__ == "__main__":
 
   # do stuff
   path = KnightShortestPath('D5' , 'F5')
   print("path", path)