rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


for row in matrix:
    for col in matrix[row]: