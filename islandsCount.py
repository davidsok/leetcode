def islandCount(matrix) -> int:
    x = len(matrix)
    y = len(matrix[0])
    visited = list(list(False for _ in range(y)) for _ in range(x))
    islands = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_node = matrix[i][j]
            visited[i][j] = True
            if matrix[i][j] == 1:
                islands.append(matrix[i][j])
            elif matrix[i][j] == 0:
                islands = islands
    print(islands)
    print(visited)
    return islands

def traverse(i, j, matrix, visited):
    pass

def unvistedAdjacenyList(i, j, matrix, visited):
    current_node = matrix[i][j]
    adjacency_list = []
    if i > 0 and j < len(matrix[i])-1: adjacency_list.append(matrix[i-1][j])
        
    pass


matrix = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]
islandCount(matrix)
            