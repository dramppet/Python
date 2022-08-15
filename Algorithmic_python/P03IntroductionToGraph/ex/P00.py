def dfs(parent, row, col, matrix, visited):
    if visited[row][col]:
        return

    if matrix[row][col] != parent:
        return



rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)





for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)