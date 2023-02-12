rows = int(input())

matrix = [ [int(el) for el in input().split(" ")] for _ in range(rows)]

sum_primary, sum_secondary = 0, 0

for r in range(rows):
    sum_primary += matrix[r][r]
    sum_secondary += matrix[rows - r - 1][r]

print(abs(sum_primary - sum_secondary))