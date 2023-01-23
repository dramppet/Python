count_rows, count_cols = [int(x) for x in input().split(", ")]

matrix = []

sum_matrix = 0

for _ in range(count_rows):
    row = [int(x) for x in input().split(", ")]
    sum_matrix += sum(row)
    matrix.append(row)

print(sum_matrix)
print(matrix)