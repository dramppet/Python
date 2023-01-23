count_row = int(input())

matrix = []

for _ in range(count_row):
    row = [int(x) for x in input().split(', ')]
    matrix.append([el for el in row if el % 2 == 0])

print(matrix)