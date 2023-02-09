rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(el) for el in input().split(", ")]
    matrix.append(row)

primary_diagonal = []

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        diag = matrix[row_idx][col_idx]
        primary_diagonal.append(diag)