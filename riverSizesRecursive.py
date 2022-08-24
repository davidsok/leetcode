def riverSizes(matrix):
    results, visited = [], [[False for i in column] for column in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j] and matrix[i][j] == 1:
                length = dfs(i, j, matrix, visited)
                results.append(length)
    print('All Rivers: ', results)
    print('Longest River: ', max(results))    
    print(matrix)    
    return results

def dfs(i, j, matrix, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or visited[i][j]:
        return 0
    visited[i][j] = True
    if matrix[i][j] == 0:
        return 0
    return 1 + dfs(i,j+1,matrix,visited) + dfs(i+1, j, matrix, visited) + dfs(i, j-1, matrix, visited) + dfs(i-1, j, matrix, visited)






matrix = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
]

riverSizes(matrix)