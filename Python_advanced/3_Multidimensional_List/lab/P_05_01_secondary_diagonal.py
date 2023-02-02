rows = int(input())

matrix = [[int(el) for el in input().split()]for _ in range(rows)]


sum_secondary_diagonal = 0

for i in range(len(matrix) - 1, -1, -1):
    sum_secondary_diagonal += matrix[i][(len(matrix) - 1) - i]

print(sum_secondary_diagonal)