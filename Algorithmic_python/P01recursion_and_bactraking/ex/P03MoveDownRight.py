def find_path(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 or col == cols - 1:
        return 1

    result = 0
    result += find_path(row, col + 1, rows, cols)
    result += find_path(row + 1, col, rows, cols)
    return result

rows = int(input())
cols = int(input())

print(find_path(0, 0, rows, cols))
