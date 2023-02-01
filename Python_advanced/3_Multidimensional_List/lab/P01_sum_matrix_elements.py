rows, columns = map(int, input().split(", "))

matrix = []

sum_row_matrix = 0

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    sum_row_matrix += sum(row)
    matrix.append(row)

sum_matrix = 0

for row_idx in range(len(matrix)):
    row_matrix = matrix[row_idx]
    sum_matrix += sum(row_matrix)

print(sum_matrix)
print(sum_row_matrix)
print(matrix)