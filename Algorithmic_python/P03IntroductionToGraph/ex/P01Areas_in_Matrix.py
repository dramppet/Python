def dfs(parrent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parrent:
        return

    visited[row][col] = True
    dfs(parrent, row - 1, col, matrix, visited)
    dfs(parrent, row + 1, col, matrix, visited)
    dfs(parrent, row, col - 1, matrix, visited)
    dfs(parrent, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        total_areas += 1
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
