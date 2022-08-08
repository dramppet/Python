rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list([int(x) for x in input().split()]))

print(matrix)