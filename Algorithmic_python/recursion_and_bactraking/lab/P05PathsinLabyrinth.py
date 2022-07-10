def find_path(row, col, matrix):

    if row < 0 or col < 0 or matrix[row] > 0 or matrix[row][col] > 0:
        return

    if matrix[row][col] == 'e':
        pass
    if matrix[row][col] == '*':
        return

    find_path(row, col + 1,matrix)
    find_path(row, col - 1,matrix)
    find_path(row + 1, col,matrix)
    find_path(row - 1, col,matrix)

row = int(input())
col = int(input())

lab = []

for _ in range(row):
    lab.append(input())

find_path(0, 0, lab)
