def find_path(row, col, lab):
    if row < 0 or col < 0 or row > len(matrix) or col > len(matrix[row]):
        return

    if lab[row][col] == 'v':
        return

    path = 0

    if lab[row][col] == len(matrix[row][col]):
        path += 1
        return

    lab[row][col] = 'v'
    find_path(row - 1, col, matrix)
    find_path(row, col + 1 ,matrix)
    lab[row][col] = '-'

rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(input().split())

find_path(0, 0, matrix)
