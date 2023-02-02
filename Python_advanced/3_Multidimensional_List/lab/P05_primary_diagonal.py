rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

print(len(matrix))

primary_diagonal = 0
secondary_diagonal = 0

for row_idx in range(len(matrix)):
    row = row_idx
    primary_diagonal += matrix[row_idx][row_idx]
    secondary_diagonal += matrix[len(row_idx) - 1 ][row_idx - 1]

print(primary_diagonal)