rows, cols = map(int, input().split(", "))

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])


for col_idx in range(cols):
    col = col_idx
    sum_column = 0
    for row_idx in range(rows):
        row = row_idx
        sum_column += matrix[row][col]
    print(sum_column)

