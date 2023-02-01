rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = 0

for row_idx in range(len(matrix)):
    row = row_idx
    primary_diagonal += matrix[row_idx][row_idx]

print(primary_diagonal)