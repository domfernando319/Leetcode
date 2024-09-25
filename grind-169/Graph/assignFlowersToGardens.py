def gardenNoAdj(n, paths):
    # Step 1: Create an adjacency list for the gardens
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    for x, y in paths:
        graph[x].append(y)
        graph[y].append(x)
    
    # Step 2: Prepare the result array and initialize it
    answer = [0] * n
    
    # Step 3: Assign flower types
    for garden in range(1, n + 1):
        # Create a set to keep track of flower types used by adjacent gardens
        used_flowers = {answer[neighbor - 1] for neighbor in graph[garden] if answer[neighbor - 1] != 0}
        
        # Find the first flower type that is not used
        for flower in range(1, 5):
            if flower not in used_flowers:
                answer[garden - 1] = flower
                break
                
    return answer

